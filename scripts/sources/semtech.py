"""Semtech blog RSS — LoRa / LoRaWAN ecosystem news."""
from __future__ import annotations
from datetime import datetime, timezone
import re, feedparser
from common import Item, infer_tags

NAME = "semtech"
DISPLAY = "Semtech"
FEED = "https://blog.semtech.com/rss.xml"


def fetch(limit: int = 5) -> list[Item]:
    try:
        feed = feedparser.parse(FEED)
    except Exception as e:
        print(f"[semtech] parse failed: {e}")
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
        summary = re.sub(r"<[^>]+>", "", e.get("summary", "")).strip()
        items.append(Item(
            id=f"semtech:{link}",
            title=e.get("title", "").strip(),
            url=link,
            source=DISPLAY,
            published=published,
            summary=summary[:600],
            tags=infer_tags(f"{e.get('title','')} {summary}", ["iot"]),
        ))
    return items
