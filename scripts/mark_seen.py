"""Read post file paths from stdin, extract ext_id from each front-matter,
and add them to content/seen.json (preserving whatever's already there)."""
from __future__ import annotations
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import load_seen, save_seen

ID_RE = re.compile(r'^ext_id:\s*"([^"]+)"', re.MULTILINE)


def id_from(path: Path) -> str | None:
    try:
        text = path.read_text(errors="ignore")
    except Exception:
        return None
    m = ID_RE.search(text)
    return m.group(1) if m else None


def main() -> int:
    seen = load_seen()
    added = 0
    for line in sys.stdin:
        p = Path(line.strip())
        if not p.exists():
            continue
        eid = id_from(p)
        if eid and eid not in seen:
            seen.add(eid)
            added += 1
    save_seen(seen)
    print(f"[mark_seen] added {added} ids; total {len(seen)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
