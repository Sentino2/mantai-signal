"""Zephyr RTOS GitHub releases."""
from __future__ import annotations
from datetime import datetime, timezone
import os, requests
from common import Item, infer_tags

NAME = "zephyr"
DISPLAY = "Zephyr"
API = "https://api.github.com/repos/zephyrproject-rtos/zephyr/releases"


def fetch(limit: int = 5) -> list[Item]:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "mantai-signal/0.1"}
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        headers["Authorization"] = f"Bearer {tok}"
    try:
        r = requests.get(API, headers=headers, params={"per_page": 10}, timeout=20)
        r.raise_for_status()
        rels = r.json()
    except Exception as e:
        print(f"[zephyr] fetch failed: {e}")
        return []
    items: list[Item] = []
    for rel in rels[:limit]:
        tag = rel.get("tag_name")
        if not tag:
            continue
        try:
            published = datetime.fromisoformat(rel["published_at"].replace("Z", "+00:00"))
        except Exception:
            published = datetime.now(timezone.utc)
        body = (rel.get("body") or "")[:1500]
        items.append(Item(
            id=f"zephyr:{tag}",
            title=f"Zephyr {tag}",
            url=rel.get("html_url", ""),
            source=DISPLAY,
            published=published,
            summary=body,
            tags=infer_tags(body, ["hardware", "iot"]),
        ))
    return items
