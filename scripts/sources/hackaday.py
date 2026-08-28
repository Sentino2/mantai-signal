"""Hackaday front-page RSS."""
from __future__ import annotations
from datetime import datetime, timezone
import feedparser
from common import Item, infer_tags

NAME = "hackaday"
DISPLAY = "Hackaday"
FEED = "https://hackaday.com/feed/"


def fetch(limit: int = 8) -> list[Item]:
    try:
        feed = feedparser.parse(FEED)
    except Exception as e:
        print(f"[hackaday] parse failed: {e}")
        return []
    items: list[Item] = []
    for e in feed.entries[:limit]:
        link = e.get("link", "")
        if not link:
            continue
        try:
            published = datetime(*e.published_parsed[:6], tzinfo=timezone.utc)
        except Exception:
            published = datetime.now(timezone.utc)
        summary = e.get("summary", "")
        # crude html strip
        import re
        summary = re.sub(r"<[^>]+>", "", summary).strip()
        items.append(Item(
            id=f"hackaday:{link}",
            title=e.get("title", "").strip(),
            url=link,
            source=DISPLAY,
            published=published,
            summary=summary[:600],
            tags=infer_tags(f"{e.get('title','')} {summary}", ["hardware"]),
        ))
    return items
