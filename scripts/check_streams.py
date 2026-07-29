#!/usr/bin/env python3
"""
check_streams.py — validate IPTV stream URLs in an M3U playlist.

Usage:
    python scripts/check_streams.py [playlist.m3u]

Outputs a Markdown table with per-channel status (OK / DEAD / TIMEOUT / ERROR).
Exits with code 1 if fewer than 50% of streams are reachable.
"""

import re
import sys
import time
import concurrent.futures
from pathlib import Path

import requests

TIMEOUT = 8          # seconds per stream request
MAX_WORKERS = 10     # concurrent checks
USER_AGENT = "Mozilla/5.0 (compatible; stream-checker/1.0)"


def parse_m3u(path: str) -> list:
    """Parse an M3U file and return a list of dicts: {name, group, url}."""
    channels = []
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("#EXTINF"):
            group_match = re.search(r'group-title="([^"]*)"', line)
            group = group_match.group(1) if group_match else "Unknown"
            name = line.rsplit(",", 1)[-1].strip() if "," in line else "Unknown"
            # URL is on the next non-empty, non-comment line
            i += 1
            while i < len(lines) and (not lines[i].strip() or lines[i].strip().startswith("#")):
                i += 1
            if i < len(lines):
                url = lines[i].strip()
                if url:
                    channels.append({"name": name, "group": group, "url": url})
        i += 1
    return channels


def check_stream(channel: dict) -> dict:
    """Check a single stream URL and return the channel dict with 'status' added."""
    url = channel["url"]
    result = {**channel}
    try:
        resp = requests.head(
            url, timeout=TIMEOUT, allow_redirects=True,
            headers={"User-Agent": USER_AGENT}
        )
        # Some servers reject HEAD — fall back to a streaming GET
        if resp.status_code == 405:
            resp = requests.get(
                url, timeout=TIMEOUT, stream=True,
                headers={"User-Agent": USER_AGENT}
            )
            resp.close()
        result["http"] = resp.status_code
        result["status"] = "✅ OK" if resp.status_code < 400 else f"❌ HTTP {resp.status_code}"
    except requests.exceptions.Timeout:
        result["http"] = None
        result["status"] = "⏱️ TIMEOUT"
    except requests.exceptions.ConnectionError:
        result["http"] = None
        result["status"] = "❌ DEAD"
    except Exception as exc:
        result["http"] = None
        result["status"] = f"⚠️ {type(exc).__name__}"
    return result


def main():
    playlist = sys.argv[1] if len(sys.argv) > 1 else "playlist.m3u"
    channels = parse_m3u(playlist)

    print(f"Checking {len(channels)} streams …\n", file=sys.stderr)

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(check_stream, ch): ch for ch in channels}
        for i, future in enumerate(concurrent.futures.as_completed(futures), 1):
            r = future.result()
            results.append(r)
            print(f"  [{i}/{len(channels)}] {r['name']} — {r['status']}", file=sys.stderr)

    results.sort(key=lambda x: (x["group"], x["name"]))

    ok = sum(1 for r in results if r["status"].startswith("✅"))
    total = len(results)
    timestamp = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())

    print(f"## Stream Health Report")
    print(f"")
    print(f"**{ok}/{total} streams online** — checked {timestamp}")
    print(f"")
    print(f"| Group | Channel | Status |")
    print(f"|-------|---------|--------|")
    for r in results:
        print(f"| {r['group']} | {r['name']} | {r['status']} |")
    print(f"")

    dead = [r for r in results if not r["status"].startswith("✅")]
    if dead:
        print(f"### Dead / unreachable streams ({len(dead)})")
        print(f"")
        for r in dead:
            print(f"- **{r['name']}** ({r['group']}) — {r['status']}  ")
            print(f"  `{r['url']}`")

    if ok < total * 0.5:
        print(f"\n⚠️ Warning: fewer than 50% of streams are reachable.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
