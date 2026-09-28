#!/usr/bin/env python3
"""Reproducible corpus runner. Semantic and voice judgments remain human reviewed."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / 'evals/cases.jsonl'
FIXTURES = ROOT / 'evals/fixtures/long-form'
SKILL = ROOT / 'skills/no-ai-slop-tr/SKILL.md'
EVAL = ROOT / 'skills/no-ai-slop-tr/eval.md'
HEADING = re.compile(r'^\*\*([^*]+)\.\*\*', re.M)
REPORT_HEADING = re.compile(r'^\s*(?:#{1,5}\s*)?\*\*([^*]+)\*\*\s*$', re.M)


def patterns():
    section = SKILL.read_text().split('## Kaçınılacak kalıplar', 1)[1].split('## Çıktı biçimi', 1)[0]
    names = HEADING.findall(section)[1:]  # first heading describes overlap, not a pattern
    if len(names) != 28 or len(set(names)) != 28:
        raise ValueError('SKILL.md must define exactly 28 distinct patterns')
    return {f'PAT-{i:02}': name for i, name in enumerate(names, 1)}


def fixtures():
    result = []
    for path in sorted(FIXTURES.glob('*.md')):
        content = path.read_text(encoding='utf-8')
        if '## Input\n' not in content or '## Oracle\n' not in content:
            raise ValueError(f'Invalid fixture: {path.name}')
        body = content.split('## Input\n', 1)[1].split('## Oracle\n', 1)[0].strip()
        oracle = content.split('## Oracle\n', 1)[1].strip()
        register = re.search(r'^- Register: (.+)$', content, re.M)
        if not body or not oracle or not register:
            raise ValueError(f'Incomplete fixture: {path.name}')
        result.append({'id': 'LONG-' + path.stem, 'mode': 'edit', 'register': register[1],
                       'input': body, 'expect': {'oracle': oracle}, 'notes': path.name})
    return result


def cases():
    result = [json.loads(line) for line in CORPUS.read_text(encoding='utf-8').splitlines() if line.strip()]
    result.extend(fixtures())
    return result


def validate():
    names = patterns()
    data = cases()
    if len(data) != 148 or len(fixtures()) != 8 or len({v['id'] for v in data}) != len(data):
        raise ValueError('Expected 140 unique atomic cases and 8 unique long-form fixtures')
    for case in data:
        if not all(case.get(k) for k in ('id', 'mode', 'register', 'input')) or not isinstance(case.get('expect'), dict):
            raise ValueError(f'Invalid case: {case.get("id")}')
        if case['mode'] not in ('detect', 'edit', 'scope'):
            raise ValueError(f'Invalid mode: {case["id"]}')
        e = case['expect']
        for key in ('must_find', 'must_not_find'):
            for identifier in e.get(key, []):
                if identifier not in names:
                    raise ValueError(f'Unknown pattern {identifier} in {case["id"]}')
        if case['mode'] == 'scope' and not isinstance(e.get('should_run'), bool):
            raise ValueError(f'Invalid scope oracle: {case["id"]}')
    return data


def prompt(case):
    intro = {'detect': 'Bu metindeki AI slop kalıplarını tespit et. Metni yeniden yazma.',
             'edit': 'Bu metni düzenle. Anlamını ve sesini koru.',
             'scope': 'Bu metni düzenle. Dil kapsamı kuralını uygula.'}[case['mode']]
    return f'{intro}\n\nBağlam/üslup: {case["register"]}\n\nMetin:\n{case["input"]}'


def api_call(model, instructions, user_text):
    payload = json.dumps({'model': model, 'instructions': instructions, 'input': user_text,
                          'store': False}, ensure_ascii=False).encode('utf-8')
    request = urllib.request.Request('https://api.openai.com/v1/responses', data=payload,
                                     headers={'Authorization': 'Bearer ' + os.environ['OPENAI_API_KEY'],
                                              'Content-Type': 'application/json'})
    with urllib.request.urlopen(request, timeout=180) as response:
        value = json.load(response)
    if value.get('status') != 'completed':
        raise RuntimeError(f'Incomplete response {value.get("id")}: {value.get("status")}')
    texts = [part['text'] for item in value.get('output', []) if item.get('type') == 'message'
             for part in item.get('content', []) if part.get('type') == 'output_text']
    if not texts:
        raise RuntimeError(f'No text output in response {value.get("id")}')
    return '\n'.join(texts), value.get('model', model), value.get('id')


def parse_codex_events(output):
    messages = []
    thread_id = None
    completed = False
    for line in output.splitlines():
        event = json.loads(line)
        if event.get('type') == 'thread.started':
            thread_id = event.get('thread_id')
        elif event.get('type') == 'item.completed' and event.get('item', {}).get('type') == 'agent_message':
            messages.append(event['item']['text'])
        elif event.get('type') == 'turn.completed':
            completed = True
    if not completed or not messages or not messages[-1].strip() or not thread_id:
        raise ValueError('Codex did not return a completed text answer')
    return messages[-1], thread_id


def codex_diagnostics(output, stderr):
    details = []
    for line in output.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get('type') in ('error', 'turn.failed'):
            error = event.get('error')
            if isinstance(error, dict):
                error = error.get('message') or str(error)
            details.append(str(error or event.get('message') or event))
    if stderr.strip():
        details.append(stderr.strip())
    if not details and output.strip():
        details.append(output.strip())
    return '\n'.join(details)[-2000:] or 'Codex returned no diagnostic output'


def codex_environment():
    environment = os.environ.copy()
    # Prevent ambient API credentials from silently billing a different account.
    environment.pop('OPENAI_API_KEY', None)
    environment.pop('CODEX_API_KEY', None)
    return environment


def check_chatgpt_login():
    executable = shutil.which('codex')
    if not executable:
        raise ValueError('Codex CLI is required: install it and run `codex login` with ChatGPT')
    result = subprocess.run([executable, 'login', 'status'], text=True, capture_output=True,
                            timeout=30, check=False, env=codex_environment())
    if result.returncode or 'chatgpt' not in (result.stdout + result.stderr).casefold():
        raise ValueError('Codex CLI must be signed in with ChatGPT; run `codex login` and check `codex login status`')


def codex_call(model, instructions, user_text, sandbox_dir):
    executable = shutil.which('codex')
    if not executable:
        raise ValueError('Codex CLI is required: install it and run `codex login` with ChatGPT')
    command = [executable, 'exec', '--json', '--ephemeral', '--sandbox', 'read-only',
               '--ignore-user-config', '--ignore-rules', '--skip-git-repo-check',
               '--model', model, '-']
    prompt_text = (f'{instructions}\n\nBu tek eval vakasını yukarıdaki skill kurallarına göre yanıtla. '
                   'Dosya okuma, araç çağırma veya dış bilgi kullanma. Yalnızca kullanıcıya verilecek son yanıtı üret.\n\n'
                   f'{user_text}')
    # No repository files or auth material are copied into this isolated working directory.
    with tempfile.TemporaryDirectory(dir=sandbox_dir) as directory:
        result = subprocess.run(command, input=prompt_text, text=True, capture_output=True,
                                cwd=directory, timeout=300, check=False, env=codex_environment())
    if result.returncode:
        raise RuntimeError(f'Codex exited {result.returncode}: {codex_diagnostics(result.stdout, result.stderr)}')
    try:
        answer, thread_id = parse_codex_events(result.stdout)
    except (ValueError, json.JSONDecodeError) as exc:
        raise RuntimeError(f'{exc}: {codex_diagnostics(result.stdout, result.stderr)}') from exc
    return answer, model, thread_id


def fingerprint():
    return hashlib.sha256(SKILL.read_bytes() + EVAL.read_bytes() + CORPUS.read_bytes() +
                          b''.join(p.read_bytes() for p in sorted(FIXTURES.glob('*.md')))).hexdigest()


def run(args):
    if args.provider == 'api' and not os.getenv('OPENAI_API_KEY'):
        raise ValueError('OPENAI_API_KEY is required for the API provider')
    if args.provider == 'codex':
        check_chatgpt_login()
    data = validate()
    if not args.model or not args.output:
        raise ValueError('--model and --output are required')
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    current_hash = fingerprint()
    existing = {}
    if destination.exists():
        for line in destination.read_text().splitlines():
            row = json.loads(line)
            if (row['fingerprint'] != current_hash or row['requested_model'] != args.model
                    or row.get('provider', 'api') != args.provider):
                raise ValueError('Output file belongs to another corpus/skill/model/provider; use a new file')
            existing[row['id']] = row
    instructions = SKILL.read_text(encoding='utf-8') + '\n\n' + EVAL.read_text(encoding='utf-8')
    for case in data:
        if case['id'] in existing:
            continue
        if args.provider == 'codex':
            answer, resolved_model, response_id = codex_call(args.model, instructions, prompt(case), destination.parent)
        else:
            answer, resolved_model, response_id = api_call(args.model, instructions, prompt(case))
        record = {'id': case['id'], 'fingerprint': current_hash, 'provider': args.provider,
                  'requested_model': args.model, 'model': resolved_model,
                  'response_id': response_id, 'at': dt.datetime.now(dt.timezone.utc).isoformat(),
                  'output': answer}
        with destination.open('a', encoding='utf-8') as stream:
            stream.write(json.dumps(record, ensure_ascii=False) + '\n')
        print(f'{case["id"]}: recorded', file=sys.stderr)


def grade_case(case, output):
    e = case['expect']
    failures = []
    reviews = []
    if case['mode'] == 'detect':
        names = patterns()
        heading_names = {s.rstrip('.').casefold() for s in REPORT_HEADING.findall(output)}
        found = {pid for pid, name in names.items() if name.casefold() in heading_names}
        # An explicit ID in a heading is also accepted without changing the public skill format.
        found.update(re.findall(r'^\s*(?:#{1,5}\s*)?(?:\*\*)?(PAT-(?:0[1-9]|1\d|2[0-8]))\b', output, re.M))
        failures += [f'missing {pid}' for pid in e.get('must_find', []) if pid not in found]
        failures += [f'false positive {pid}' for pid in e.get('must_not_find', []) if pid in found]
        if e.get('must_not_score') and re.search(r'(?:%\s*AI|AI\s*%|slop\s*(?:skoru|puanı|yüzdesi))', output, re.I):
            failures.append('unsupported score')
        if e.get('must_not_claim_ai_authorship') and re.search(r'(?:AI|yapay zekâ|yapay zeka)\s*(?:tarafından\s*)?yazıl', output, re.I):
            reviews.append('Check whether authorship is claimed or explicitly denied')
        if found or e.get('must_find'):
            reviews.append('Check evidence quote, suggestion and overlap classification')
        else:
            reviews.append('Check unlisted false positives and scope of response')
    elif case['mode'] == 'edit':
        body = re.split(r'(?im)^\s*#{0,3}\s*(?:\*\*)?Neleri değiştirdim\??', output)[0]
        for phrase in e.get('must_change', []):
            if phrase.casefold() in body.casefold():
                failures.append(f'unchanged: {phrase}')
        for phrase in e.get('must_preserve', []):
            if phrase.casefold() not in body.casefold():
                reviews.append(f'Check paraphrased or missing preservation: {phrase}')
        reviews.append('Review meaning, added claims, register and full oracle manually')
    else:
        reviews.append(f'Check language scope: should_run={e["should_run"]}; {e["reason"]}')
    return failures, reviews


def grade(args):
    data = validate()
    output_path = Path(args.output)
    if not output_path.is_file() or output_path.stat().st_size == 0:
        raise ValueError('No model outputs recorded. Run `eval_runner.py run` first; a previous Codex call may have failed.')
    rows = {r['id']: r for r in map(json.loads, output_path.read_text(encoding='utf-8').splitlines())}
    reviews = json.loads(Path(args.review).read_text(encoding='utf-8')) if args.review else {}
    if set(rows) - {c['id'] for c in data}:
        raise ValueError('Unknown IDs in output')
    result = []
    for case in data:
        row = rows.get(case['id'])
        if not row:
            result.append({'id': case['id'], 'status': 'pending', 'findings': ['No model output']})
            continue
        if row['fingerprint'] != fingerprint():
            raise ValueError(f'Stale output for {case["id"]}')
        failures, manual = grade_case(case, row['output'])
        review = reviews.get(case['id'])
        if review is not None and (not isinstance(review, dict) or review.get('verdict') not in ('pass', 'fail') or not review.get('note')):
            raise ValueError(f'Invalid review for {case["id"]}; verdict and note required')
        status = 'fail' if failures or (review and review['verdict'] == 'fail') else 'pass' if review else 'review'
        result.append({'id': case['id'], 'status': status, 'findings': failures + ([] if review else manual),
                       'review': review, 'model': row['model'], 'response_id': row['response_id']})
    counts = {s: sum(r['status'] == s for r in result) for s in ('pass', 'fail', 'review', 'pending')}
    report = {'fingerprint': fingerprint(), 'counts': counts, 'results': result}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.report:
        Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if args.strict and (counts['fail'] or counts['review'] or counts['pending']):
        raise SystemExit(1)


def self_test():
    validate()
    positive = {'id': 'test', 'mode': 'detect', 'expect': {'must_find': ['PAT-06'], 'must_not_find': ['PAT-18']}}
    assert not grade_case(positive, '### Bulunan kalıplar\n**Önem şişirme**\n> "kritik"')[0]
    assert 'false positive PAT-18' in grade_case(positive, '**Önem şişirme**\n**Yapay gözlem dili**')[0]
    assert 'missing PAT-06' in grade_case(positive, 'Hiçbir kalıp yok.')[0]
    edit = {'mode': 'edit', 'expect': {'must_change': ['Boş giriş'], 'must_preserve': ['42']}}
    assert grade_case(edit, 'Boş giriş ve 42')[0] == ['unchanged: Boş giriş']
    events = ('{"type":"thread.started","thread_id":"t-1"}\n'
              '{"type":"item.completed","item":{"type":"agent_message","text":"Merhaba"}}\n'
              '{"type":"turn.completed"}\n')
    assert parse_codex_events(events) == ('Merhaba', 't-1')
    assert codex_diagnostics('{"type":"error","message":"model unavailable"}', '') == 'model unavailable'
    assert codex_diagnostics('{"type":"turn.failed","error":{"message":"sandbox denied"}}', '') == 'sandbox denied'
    try:
        parse_codex_events(events.replace('turn.completed', 'turn.failed'))
    except ValueError:
        pass
    else:
        raise AssertionError('Incomplete Codex turn was accepted')
    print('Runner self-test passed')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest='command', required=True)
    subs.add_parser('validate')
    subs.add_parser('self-test')
    runner = subs.add_parser('run')
    runner.add_argument('--provider', choices=('codex', 'api'), default='codex',
                        help='Local ChatGPT subscription via Codex CLI (default), or Responses API')
    runner.add_argument('--model', required=True, help='Pin a specific model ID')
    runner.add_argument('--output', required=True, help='JSONL transcript; resumes matching runs')
    grader = subs.add_parser('grade')
    grader.add_argument('--output', required=True)
    grader.add_argument('--review', help='JSON object: case ID -> {verdict: pass|fail, note: rationale}')
    grader.add_argument('--report')
    grader.add_argument('--strict', action='store_true', help='Exit nonzero unless all 148 cases pass review')
    args = parser.parse_args()
    if args.command == 'validate':
        print(f'Validated {len(validate())} cases ({len(fixtures())} long-form)')
    elif args.command == 'self-test':
        self_test()
    elif args.command == 'run':
        run(args)
    else:
        grade(args)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, urllib.error.HTTPError) as exc:
        raise SystemExit(str(exc)) from exc
