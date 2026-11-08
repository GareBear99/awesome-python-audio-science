#!/usr/bin/env python3
"""Real link checker for the TizWildin awesome lists.

The old scripts/check_links.py only COUNTED markdown links — it never
fetched them, so a dead link passed silently. This script actually
fetches every unique http(s) URL in the given repos' Markdown files
and reports which ones are dead.

Usage:
    python3 scripts/check_links_live.py [REPO ...]
Default repos: this repo + the three sibling awesome lists
(../awesome-audio-plugins-dev, ../awesome-audio-lists,
../awesome-music-platforms), when those directories exist.

Method: GET with `Range: bytes=0-0` (minimal transfer), 15 s timeout,
12 workers. A URL is DEAD on 404/410 or on connection/DNS failure.
403/429 (bot-blocked / rate-limited) is reported as BLOCKED, not dead —
those need a human/browser check, not an edit.

Output: summary on stdout + full JSON report at
/tmp/link_health_report.json (per-URL status, repo, and source files).
Exit code 1 if any URL is DEAD or FAILED.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPOS = [
    ROOT,
    ROOT.parent / "awesome-audio-plugins-dev",
    ROOT.parent / "awesome-audio-lists",
    ROOT.parent / "awesome-music-platforms",
]

TIMEOUT = 15
WORKERS = 12
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36 "
    "TizWildin-link-checker/1.0"
)

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def collect(repo: Path) -> dict[str, list[str]]:
    """url -> list of 'file' locations where it appears."""
    found: dict[str, list[str]] = {}
    for md in sorted(repo.rglob("*.md")):
        try:
            text = md.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for link in LINK_RE.findall(text):
            if link.startswith("#") or link.startswith("mailto:"):
                continue
            if not link.startswith(("http://", "https://")):
                continue
            found.setdefault(link, []).append(str(md.relative_to(repo)))
    return found


def check(url: str) -> tuple[str, str]:
    """Return (verdict, detail). Verdict: ALIVE | REDIRECT | DEAD |
    BLOCKED | FAILED."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Range": "bytes=0-0"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            code = resp.status
            if code in (200, 206):
                return "ALIVE", str(code)
            if code in (301, 302, 303, 307, 308):
                return "REDIRECT", f"{code} -> {resp.headers.get('Location', '')}"
            return "DEAD", str(code)
    except urllib.error.HTTPError as e:
        if e.code in (403, 429):
            return "BLOCKED", str(e.code)
        if e.code in (301, 302, 303, 307, 308):
            return "REDIRECT", f"{e.code} -> {e.headers.get('Location', '')}"
        return "DEAD", str(e.code)
    except urllib.error.URLError as e:
        return "FAILED", str(e.reason)[:120]
    except (TimeoutError, OSError) as e:
        return "FAILED", str(e)[:120]


def main() -> int:
    repos = [Path(a) for a in sys.argv[1:]] or DEFAULT_REPOS
    repos = [r for r in repos if r.is_dir()]
    all_urls: dict[str, dict] = {}
    for repo in repos:
        for url, files in collect(repo).items():
            slot = all_urls.setdefault(url, {"repos": [], "files": []})
            slot["repos"].append(repo.name)
            slot["files"].extend(f"{repo.name}/{f}" for f in files)

    urls = sorted(all_urls)
    print(f"Checking {len(urls)} unique URLs across {len(repos)} repos ...")
    results: dict[str, tuple[str, str]] = {}
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        for url, verdict in zip(urls, pool.map(check, urls)):
            results[url] = verdict

    counts: dict[str, int] = {}
    for verdict, _ in results.values():
        counts[verdict] = counts.get(verdict, 0) + 1
    print("Verdicts:", dict(sorted(counts.items())))

    report = {
        url: {
            "verdict": v,
            "detail": d,
            "repos": sorted(set(all_urls[url]["repos"])),
            "files": sorted(set(all_urls[url]["files"])),
        }
        for url, (v, d) in sorted(results.items())
    }
    out = Path("/tmp/link_health_report.json")
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Full report: {out}")

    for verdict in ("DEAD", "FAILED", "BLOCKED"):
        bad = [(u, d) for u, (v, d) in sorted(results.items()) if v == verdict]
        if bad:
            print(f"\n--- {verdict} ({len(bad)}) ---")
            for u, d in bad:
                print(f"  [{d}] {u}")
    return 1 if counts.get("DEAD", 0) or counts.get("FAILED", 0) else 0


if __name__ == "__main__":
    raise SystemExit(main())
