#!/usr/bin/env python3
"""Türkçe kullanıcı yüzeyinde eski upstream ve İngilizce UX sızıntılarını denetle."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".codex-plugin" / "plugin.json"

SURFACE_FILES = (
    "README.md",
    "PRIVACY.md",
    "TERMS.md",
    "UPSTREAM.md",
    "plugin-submission.md",
    ".codex-plugin/plugin.json",
    "agents/openai.yaml",
    "skills/no-ai-slop-tr/agents/openai.yaml",
    "skills/no-ai-slop-tr/SKILL.md",
    "skills/no-ai-slop-tr/eval.md",
)

AGENT_FILES = (
    "agents/openai.yaml",
    "skills/no-ai-slop-tr/agents/openai.yaml",
)

ALLOWED_UPSTREAM_REFERENCE_FILES = {
    "README.md",
    "UPSTREAM.md",
    "plugin-submission.md",
}

EXPECTED_MANIFEST = {
    "name": "no-ai-slop-turkish",
    "repository": "https://github.com/aliereny/no-ai-slop-turkish",
    "skills": "./skills/",
}

EXPECTED_DISPLAY_NAME = "No AI Slop Türkçe"

UPSTREAM_REFERENCE = "petergyang/no-ai-slop"

BLOCKED_UPSTREAM_PHRASES = (
    "What changed",
    "Remove AI slop",
    "Preserve voice",
    "Edit your writing",
    "Detect slop",
    "Is this slop?",
    "Here's the thing",
    "Let me be clear",
    "The future isn't coming",
    "It's not X. It's Y.",
)

BLOCKED_IDENTITY_PATTERNS = (
    (
        re.compile(r"(?<![\w./-])/no-ai-slop(?!-tr)", re.IGNORECASE),
        "Eski skill komutu bulundu",
        "/no-ai-slop-tr",
    ),
    (
        re.compile(r"\$no-ai-slop(?!-tr)", re.IGNORECASE),
        "Eski skill değişkeni bulundu",
        "$no-ai-slop-tr",
    ),
    (
        re.compile(r"skills/no-ai-slop/(?!tr)", re.IGNORECASE),
        "Eski skill yolu bulundu",
        "skills/no-ai-slop-tr/",
    ),
    (
        re.compile(r'["\']name["\']\s*:\s*["\']no-ai-slop["\']', re.IGNORECASE),
        "Eski plugin kimliği bulundu",
        '"name": "no-ai-slop-turkish"',
    ),
)


@dataclass(frozen=True)
class Finding:
    path: str
    message: str
    line: int | None = None
    found: str | None = None
    expected: str | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Türkçe kullanıcı yüzeyindeki upstream/İngilizce sızıntılarını denetler."
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Repo dosyalarını taramadan denetleyicinin kendi regresyon testlerini çalıştır.",
    )
    return parser.parse_args()


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def add_match_finding(
    findings: list[Finding],
    *,
    path: str,
    text: str,
    match: re.Match[str],
    message: str,
    expected: str | None = None,
) -> None:
    findings.append(
        Finding(
            path=path,
            line=line_number(text, match.start()),
            message=message,
            found=match.group(0),
            expected=expected,
        )
    )


def scan_surface_text(path: str, text: str) -> list[Finding]:
    findings: list[Finding] = []

    for pattern, message, expected in BLOCKED_IDENTITY_PATTERNS:
        for match in pattern.finditer(text):
            add_match_finding(
                findings,
                path=path,
                text=text,
                match=match,
                message=message,
                expected=expected,
            )

    for phrase in BLOCKED_UPSTREAM_PHRASES:
        pattern = re.compile(re.escape(phrase), re.IGNORECASE)
        for match in pattern.finditer(text):
            add_match_finding(
                findings,
                path=path,
                text=text,
                match=match,
                message="Upstream'den kalan İngilizce kullanıcı yüzeyi ifadesi bulundu",
                expected="Türkçe karşılığını kullan",
            )

    if path not in ALLOWED_UPSTREAM_REFERENCE_FILES:
        pattern = re.compile(re.escape(UPSTREAM_REFERENCE), re.IGNORECASE)
        for match in pattern.finditer(text):
            add_match_finding(
                findings,
                path=path,
                text=text,
                match=match,
                message="Upstream repo referansı bu dosyada izinli değil",
                expected="Referansı yalnızca attribution/bakım dokümanlarında tut",
            )

    return findings


def validate_manifest_data(data: object) -> list[Finding]:
    findings: list[Finding] = []
    path = ".codex-plugin/plugin.json"

    if not isinstance(data, dict):
        return [Finding(path=path, message="Manifest kökü bir JSON nesnesi olmalı")]

    for key, expected in EXPECTED_MANIFEST.items():
        actual = data.get(key)
        if actual != expected:
            findings.append(
                Finding(
                    path=path,
                    message=f"Manifest alanı beklenen değerden farklı: {key}",
                    found=repr(actual),
                    expected=repr(expected),
                )
            )

    interface = data.get("interface")
    if not isinstance(interface, dict):
        findings.append(Finding(path=path, message="Manifest interface alanı bir nesne olmalı"))
        return findings

    display_name = interface.get("displayName")
    if display_name != EXPECTED_DISPLAY_NAME:
        findings.append(
            Finding(
                path=path,
                message="Plugin görünen adı beklenen Türkçe kimlikle eşleşmiyor",
                found=repr(display_name),
                expected=repr(EXPECTED_DISPLAY_NAME),
            )
        )

    required_turkish_fields = (
        ("description", data.get("description")),
        ("interface.shortDescription", interface.get("shortDescription")),
        ("interface.longDescription", interface.get("longDescription")),
    )
    for field, value in required_turkish_fields:
        if not isinstance(value, str) or "Türkçe" not in value:
            findings.append(
                Finding(
                    path=path,
                    message=f"{field} Türkçe ürün kapsamını açıkça belirtmeli",
                    found=repr(value),
                    expected="'Türkçe' ifadesini içeren metin",
                )
            )

    prompts = interface.get("defaultPrompt")
    if not isinstance(prompts, list) or not prompts or not all(isinstance(item, str) for item in prompts):
        findings.append(
            Finding(
                path=path,
                message="interface.defaultPrompt en az bir metin istemi içeren liste olmalı",
            )
        )
    else:
        for index, prompt in enumerate(prompts):
            if "met" not in prompt.lower():
                findings.append(
                    Finding(
                        path=path,
                        message=f"defaultPrompt[{index}] Türkçe metin iş akışını açıkça belirtmeli",
                        found=repr(prompt),
                        expected="Türkçe metin/düzenleme/tespit bağlamı",
                    )
                )

    capabilities = interface.get("capabilities")
    if not isinstance(capabilities, list) or not capabilities or not all(
        isinstance(item, str) for item in capabilities
    ):
        findings.append(
            Finding(
                path=path,
                message="interface.capabilities en az bir metin değeri içeren liste olmalı",
            )
        )

    return findings


def validate_manifest_file() -> list[Finding]:
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [Finding(path=".codex-plugin/plugin.json", message="Manifest dosyası bulunamadı")]
    except json.JSONDecodeError as exc:
        return [
            Finding(
                path=".codex-plugin/plugin.json",
                line=exc.lineno,
                message=f"Manifest geçerli JSON değil: {exc.msg}",
            )
        ]
    return validate_manifest_data(data)


def validate_agent_contents(agent_contents: dict[str, str]) -> list[Finding]:
    findings: list[Finding] = []

    missing = [path for path in AGENT_FILES if path not in agent_contents]
    for path in missing:
        findings.append(Finding(path=path, message="Agent metadata dosyası bulunamadı"))

    if missing:
        return findings

    root_agent = agent_contents[AGENT_FILES[0]]
    skill_agent = agent_contents[AGENT_FILES[1]]
    if root_agent.encode("utf-8") != skill_agent.encode("utf-8"):
        findings.append(
            Finding(
                path=AGENT_FILES[1],
                message="İki openai.yaml kaynağı birebir aynı olmalı",
                expected=f"{AGENT_FILES[0]} ile byte-for-byte eşleşme",
            )
        )

    for path, content in agent_contents.items():
        if 'display_name: "/no-ai-slop-tr"' not in content:
            findings.append(
                Finding(
                    path=path,
                    message="Agent görünen komutu eksik veya yanlış",
                    expected='display_name: "/no-ai-slop-tr"',
                )
            )
        if "$no-ai-slop-tr" not in content:
            findings.append(
                Finding(
                    path=path,
                    message="Agent varsayılan isteminde skill kimliği eksik",
                    expected="$no-ai-slop-tr",
                )
            )

    return findings


def read_surface_files() -> tuple[dict[str, str], list[Finding]]:
    contents: dict[str, str] = {}
    findings: list[Finding] = []

    for path in SURFACE_FILES:
        file_path = ROOT / path
        try:
            contents[path] = file_path.read_text(encoding="utf-8")
        except FileNotFoundError:
            findings.append(Finding(path=path, message="Zorunlu yüzey dosyası bulunamadı"))
        except UnicodeDecodeError:
            findings.append(Finding(path=path, message="Dosya UTF-8 olarak okunamadı"))

    return contents, findings


def run_repo_checks() -> list[Finding]:
    contents, findings = read_surface_files()

    for path, text in contents.items():
        findings.extend(scan_surface_text(path, text))

    findings.extend(validate_manifest_file())

    agent_contents = {
        path: contents[path]
        for path in AGENT_FILES
        if path in contents
    }
    findings.extend(validate_agent_contents(agent_contents))

    return findings


def run_self_tests() -> None:
    def assert_pass(path: str, text: str) -> None:
        findings = scan_surface_text(path, text)
        if findings:
            raise AssertionError(f"PASS beklenirken bulgu üretildi: {path}: {findings}")

    def assert_fail(path: str, text: str) -> None:
        findings = scan_surface_text(path, text)
        if not findings:
            raise AssertionError(f"FAIL beklenirken bulgu üretilmedi: {path}: {text!r}")

    assert_fail("README.md", "/no-ai-slop")
    assert_pass("README.md", "/no-ai-slop-tr")

    assert_fail("agents/openai.yaml", "$no-ai-slop")
    assert_pass("agents/openai.yaml", "$no-ai-slop-tr")

    assert_pass("README.md", "Kaynak: petergyang/no-ai-slop")
    assert_fail("agents/openai.yaml", "Kaynak: petergyang/no-ai-slop")

    assert_fail("README.md", "What changed")
    assert_pass("README.md", "Neleri değiştirdim?")

    manifest = {
        "name": "no-ai-slop-turkish",
        "repository": "https://github.com/aliereny/no-ai-slop-turkish",
        "skills": "./skills/",
        "description": "Türkçe metinleri düzenler.",
        "interface": {
            "displayName": "No AI Slop Türkçe",
            "shortDescription": "Türkçe metin düzenleme",
            "longDescription": "Türkçe metinlerde AI slop kalıplarını azaltır.",
            "defaultPrompt": ["Bu Türkçe metni düzenle."],
            "capabilities": ["Düzenle"],
            "category": "Productivity",
        },
    }
    manifest_findings = validate_manifest_data(manifest)
    if manifest_findings:
        raise AssertionError(f"Geçerli manifest reddedildi: {manifest_findings}")

    bad_manifest = dict(manifest)
    bad_manifest["name"] = "no-ai-slop"
    if not validate_manifest_data(bad_manifest):
        raise AssertionError("Eski manifest kimliği reddedilmedi")

    matching_agents = {
        AGENT_FILES[0]: 'interface:\n  display_name: "/no-ai-slop-tr"\n  default_prompt: "$no-ai-slop-tr ile düzenle."\n',
        AGENT_FILES[1]: 'interface:\n  display_name: "/no-ai-slop-tr"\n  default_prompt: "$no-ai-slop-tr ile düzenle."\n',
    }
    if validate_agent_contents(matching_agents):
        raise AssertionError("Eş agent metadata dosyaları reddedildi")

    drifted_agents = dict(matching_agents)
    drifted_agents[AGENT_FILES[1]] += "# drift\n"
    if not validate_agent_contents(drifted_agents):
        raise AssertionError("Ayrışan agent metadata dosyaları reddedilmedi")


def print_findings(findings: list[Finding]) -> None:
    print("Türkçe yüzey kontrolü başarısız.\n")

    for finding in findings:
        location = finding.path
        if finding.line is not None:
            location += f":{finding.line}"
        print(location)
        print(f"  {finding.message}")
        if finding.found is not None:
            print(f"  Bulunan: {finding.found}")
        if finding.expected is not None:
            print(f"  Beklenen: {finding.expected}")
        print()

    print(f"{len(findings)} hata bulundu.")


def main() -> None:
    args = parse_args()

    if args.self_test:
        try:
            run_self_tests()
        except AssertionError as exc:
            print(f"Self-test başarısız: {exc}", file=sys.stderr)
            raise SystemExit(1)
        print("Türkçe yüzey denetleyicisi self-test başarılı.")
        return

    findings = run_repo_checks()
    if findings:
        print_findings(findings)
        raise SystemExit(1)

    print("Türkçe yüzey kontrolü başarılı.")


if __name__ == "__main__":
    main()
