"""arXiv new submissions in cs.AR (hardware architecture) and eess.SY (systems/control)."""
from __future__ import annotations
from datetime import datetime, timezone
import feedparser
from common import Item, infer_tags

NAME = "arxiv"
DISPLAY = "arXiv"
CATS = ["cs.AR", "eess.SY"]


def fetch(limit: int = 10) -> list[Item]:
    items: list[Item] = []
    for cat in CATS:
        url = f"http://export.arxiv.org/api/query?search_query=cat:{cat}&sortBy=submittedDate&sortOrder=descending&max_results=15"
        try:
            feed = feedparser.parse(url)
        except Exception as e:
            print(f"[arxiv:{cat}] parse failed: {e}")
            continue
        for e in feed.entries:
            aid = e.get("id", "").split("/abs/")[-1]
            if not aid:
                continue
            title = e.get("title", "").replace("\n", " ").strip()
            summary = e.get("summary", "").replace("\n", " ").strip()
            try:
                published = datetime(*e.published_parsed[:6], tzinfo=timezone.utc)
            except Exception:
                published = datetime.now(timezone.utc)
            items.append(Item(
                id=f"arxiv:{aid}",
                title=title,
                url=e.get("link", f"https://arxiv.org/abs/{aid}"),
                source=DISPLAY,
                published=published,
                summary=summary,
                tags=infer_tags(f"{title} {summary}", ["models" if cat == "cs.AR" else "hardware"]),
            ))
    items.sort(key=lambda i: i.published, reverse=True)
    return items[:limit]
