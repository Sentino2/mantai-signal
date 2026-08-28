"""Orchestrator: fetch each source, dedupe, write markdown posts.

Usage:
  python scripts/ingest.py                # ingest all sources
  python scripts/ingest.py --source nvd   # single source (used per-PR by CI)
  python scripts/ingest.py --list         # print source names and exit

Output on stdout: one line per written post: "<source>\t<relative-path>".
Exit code 0 always (empty source is not an error).
"""
from __future__ import annotations
import argparse, importlib, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import Item, load_seen, save_seen, write_post

SOURCES = ["nvd", "arxiv", "hackaday", "zephyr", "semtech"]


def render_body(item: Item) -> str:
    body = item.summary.strip() or "_No summary available. See original source._"
    return f"{body}\n\n[Read the original at {item.source} →]({item.url})"


def run(source_names: list[str]) -> list[Path]:
    seen = load_seen()
    new_ids: list[str] = []
    written: list[Path] = []
    for name in source_names:
        try:
            mod = importlib.import_module(f"sources.{name}")
        except Exception as e:
            print(f"[ingest] cannot import {name}: {e}", file=sys.stderr)
            continue
        try:
            items = mod.fetch()
        except Exception as e:
            print(f"[ingest] {name}.fetch() failed: {e}", file=sys.stderr)
            continue
        for it in items:
            if it.id in seen:
                continue
            try:
                path = write_post(it, render_body(it))
            except Exception as e:
                print(f"[ingest] write failed for {it.id}: {e}", file=sys.stderr)
                continue
            written.append(path)
            new_ids.append(it.id)
            rel = path.relative_to(Path(__file__).resolve().parent.parent)
            print(f"{name}\t{rel}")
    if new_ids:
        save_seen(list(seen) + new_ids)
    return written


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", action="append", help="limit to one or more sources")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()
    if args.list:
        print("\n".join(SOURCES))
        return 0
    names = args.source or SOURCES
    unknown = [n for n in names if n not in SOURCES]
    if unknown:
        print(f"unknown source(s): {unknown}", file=sys.stderr)
        return 2
    run(names)
    return 0


if __name__ == "__main__":
    sys.exit(main())
