#!/usr/bin/env python3
"""Check whether the Turkish fork needs a reviewed upstream port."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / ".upstream.json"
EXPECTED_REPOSITORY = "petergyang/no-ai-slop"
EXPECTED_BRANCH = "main"
SHA_RE = re.compile(r"^[0-9a-fA-F]{40}$")
API_ROOT = "https://api.github.com"

# Upstream paths that have a known Turkish destination and handling rule.
FILE_MAP = {
    "skills/no-ai-slop/SKILL.md": ("skills/no-ai-slop-tr/SKILL.md", "SEMANTIC"),
    "skills/no-ai-slop/eval.md": ("skills/no-ai-slop-tr/eval.md", "SEMANTIC"),
    "skills/no-ai-slop/agents/openai.yaml": (
        "skills/no-ai-slop-tr/agents/openai.yaml",
        "STRUCTURAL",
    ),
    "agents/openai.yaml": ("agents/openai.yaml", "STRUCTURAL"),
    ".codex-plugin/plugin.json": (".codex-plugin/plugin.json", "STRUCTURAL"),
    "scripts/build_plugin.py": ("scripts/build_plugin.py", "STRUCTURAL"),
    ".github/workflows/plugin.yml": (".github/workflows/plugin.yml", "STRUCTURAL"),
    "README.md": ("README.md", "DOCS"),
}

TURKISH_OWNED_PATHS = (
    "evals/",
    "skills/no-ai-slop-tr/",
)
TURKISH_OWNED_FILES = {
    ".upstream.json",
    "UPSTREAM.md",
    "scripts/check_turkish_surface.py",
    "scripts/check_upstream.py",
}


class UpstreamError(RuntimeError):
    """An actionable configuration or GitHub API error."""


def valid_sha(value: object) -> bool:
    return isinstance(value, str) and SHA_RE.fullmatch(value) is not None


def validate_config_data(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return [".upstream.json must contain a JSON object"]

    if data.get("repository") != EXPECTED_REPOSITORY:
        errors.append(f"repository must be {EXPECTED_REPOSITORY!r}")
    if data.get("branch") != EXPECTED_BRANCH:
        errors.append(f"branch must be {EXPECTED_BRANCH!r}")
    if not valid_sha(data.get("tracked_commit")):
        errors.append("tracked_commit must be a non-empty 40-character hexadecimal SHA")
    return errors


def load_config() -> dict[str, str]:
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise UpstreamError(f"Missing config: {CONFIG_PATH.relative_to(ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise UpstreamError(f"Invalid JSON in {CONFIG_PATH.relative_to(ROOT)}: {exc}") from exc

    errors = validate_config_data(data)
    for source_path, (target_path, _category) in FILE_MAP.items():
        if not (ROOT / target_path).is_file():
            errors.append(f"Mapped destination for {source_path} is missing: {target_path}")
    if errors:
        raise UpstreamError("Invalid upstream config:\n- " + "\n- ".join(errors))
    return data


def classify_path(path: str) -> tuple[str, str | None]:
    """Return a review category and, where known, the Turkish destination."""
    if path in TURKISH_OWNED_FILES or path.startswith(TURKISH_OWNED_PATHS):
        return "TURKISH_OWNED", None
    if path in FILE_MAP:
        target, category = FILE_MAP[path]
        return category, target
    if path in {"README.md", "PRIVACY.md", "TERMS.md"}:
        return "DOCS", path
    if path.startswith(("scripts/", ".github/workflows/")) or path in {
        ".codex-plugin/plugin.json",
        "agents/openai.yaml",
    }:
        return "STRUCTURAL", path
    return "REVIEW", None


def github_get(url: str) -> tuple[Any, dict[str, str]]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "no-ai-slop-turkish-upstream-check",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
            return payload, dict(response.headers.items())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise UpstreamError(f"GitHub API returned HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise UpstreamError(f"Could not reach GitHub API: {exc.reason}") from exc
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise UpstreamError(f"GitHub API returned invalid JSON: {exc}") from exc


def fetch_status(repository: str, branch: str, tracked_commit: str) -> dict[str, Any]:
    encoded_branch = urllib.parse.quote(branch, safe="")
    head_url = f"{API_ROOT}/repos/{repository}/commits/{encoded_branch}"
    head_data, _headers = github_get(head_url)
    latest_commit = head_data.get("sha") if isinstance(head_data, dict) else None
    if not valid_sha(latest_commit):
        raise UpstreamError("GitHub API did not return a valid upstream head SHA")

    report: dict[str, Any] = {
        "repository": repository,
        "branch": branch,
        "tracked_commit": tracked_commit.lower(),
        "latest_commit": latest_commit.lower(),
        "status": "up_to_date",
        "ahead_by": 0,
        "behind_by": 0,
        "total_commits": 0,
        "commits": [],
        "changed_files": [],
        "compare_url": f"https://github.com/{repository}/compare/{tracked_commit}...{latest_commit}",
        "commit_list_truncated": False,
    }
    if latest_commit.lower() == tracked_commit.lower():
        return report

    compare_url = (
        f"{API_ROOT}/repos/{repository}/compare/"
        f"{urllib.parse.quote(tracked_commit, safe='')}...{urllib.parse.quote(latest_commit, safe='')}"
        "?per_page=100"
    )
    comparison, _headers = github_get(compare_url)
    status = comparison.get("status", "unknown")
    ahead_by = int(comparison.get("ahead_by", 0))
    behind_by = int(comparison.get("behind_by", 0))
    if status == "identical":
        result_status = "up_to_date"
    elif status == "ahead" and ahead_by > 0 and behind_by == 0:
        result_status = "behind"
    elif status == "diverged":
        result_status = "diverged"
    elif status == "behind":
        result_status = "baseline_ahead"
    else:
        result_status = "unknown"

    commits = []
    for item in comparison.get("commits", []):
        commit_data = item.get("commit", {})
        message = commit_data.get("message", "").splitlines()
        commits.append(
            {
                "sha": item.get("sha", ""),
                "short_sha": item.get("sha", "")[:7],
                "message": message[0] if message else "(commit mesajı yok)",
                "url": item.get("html_url", ""),
            }
        )

    changed_files = []
    for item in comparison.get("files", []):
        path = item.get("filename", "")
        category, destination = classify_path(path)
        changed_files.append(
            {
                "path": path,
                "category": category,
                "destination": destination,
                "status": item.get("status", "modified"),
                "additions": item.get("additions", 0),
                "deletions": item.get("deletions", 0),
                "changes": item.get("changes", 0),
            }
        )

    total_commits = int(comparison.get("total_commits", len(commits)))
    report.update(
        {
            "status": result_status,
            "compare_status": status,
            "ahead_by": ahead_by,
            "behind_by": behind_by,
            "total_commits": total_commits,
            "commits": commits,
            "changed_files": changed_files,
            "commit_list_truncated": total_commits > len(commits),
        }
    )
    return report


def render_report(report: dict[str, Any]) -> str:
    lines = [
        f"Upstream: {report['repository']}:{report['branch']}",
        f"Takip edilen: {report['tracked_commit']}",
        f"Güncel upstream: {report['latest_commit']}",
    ]
    if report["status"] == "up_to_date":
        lines.append("Durum: güncel")
        return "\n".join(lines)

    lines.extend(
        [
            f"Durum: {report['status']}",
            f"İncelenecek commit sayısı: {report['total_commits']}",
            "Commitler:",
        ]
    )
    for commit in report["commits"]:
        lines.append(f"- {commit['short_sha']} {commit['message']}")
    if report["commit_list_truncated"]:
        lines.append("- Commit listesi API sınırında kesildi; compare bağlantısını açıp kalanları inceleyin.")
    lines.append("Değişen dosyalar:")
    for item in report["changed_files"]:
        destination = f" -> {item['destination']}" if item["destination"] else ""
        lines.append(f"- [{item['category']}] {item['path']}{destination}")
    if report["status"] in {"behind", "diverged", "baseline_ahead", "unknown"}:
        lines.append("Kararları kaydedip Türkçe uyarlamayı tamamlamadan taban commit'i ilerletmeyin.")
    lines.append(f"Karşılaştırma: {report['compare_url']}")
    return "\n".join(lines)


def run_self_tests() -> None:
    valid_config = {
        "repository": EXPECTED_REPOSITORY,
        "branch": EXPECTED_BRANCH,
        "tracked_commit": "0" * 40,
    }
    assert validate_config_data(valid_config) == []
    assert validate_config_data({**valid_config, "tracked_commit": ""})
    assert classify_path("skills/no-ai-slop/SKILL.md") == (
        "SEMANTIC",
        "skills/no-ai-slop-tr/SKILL.md",
    )
    assert classify_path("scripts/build_plugin.py") == ("STRUCTURAL", "scripts/build_plugin.py")
    assert classify_path("evals/cases.jsonl") == ("TURKISH_OWNED", None)
    assert classify_path("docs/new-upstream-file.md") == ("REVIEW", None)
    print("Upstream kontrolü öz testleri geçti.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Upstream değişikliklerini Türkçe fork'a aktarmadan önce raporlar."
    )
    parser.add_argument("--json", action="store_true", help="Makinece okunabilir JSON yazdır")
    parser.add_argument(
        "--validate-config",
        action="store_true",
        help="Config ve dosya eşlemesini ağ isteği yapmadan doğrula",
    )
    parser.add_argument("--self-test", action="store_true", help="Ağsız öz testleri çalıştır")
    parser.add_argument(
        "--tracked-commit",
        help="Yalnızca kontrol için .upstream.json tabanını geçici olarak geçersiz kıl",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.self_test:
        run_self_tests()
        return 0

    try:
        config = load_config()
        if args.validate_config:
            print("Upstream config ve dosya eşlemesi geçerli.")
            return 0

        tracked_commit = args.tracked_commit or config["tracked_commit"]
        if not valid_sha(tracked_commit):
            raise UpstreamError("--tracked-commit 40 karakterlik hexadecimal SHA olmalı")
        report = fetch_status(config["repository"], config["branch"], tracked_commit)
    except UpstreamError as exc:
        if args.json:
            print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False, indent=2))
        else:
            print(f"Hata: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render_report(report))
    return 0 if report["status"] == "up_to_date" else 2


if __name__ == "__main__":
    raise SystemExit(main())
