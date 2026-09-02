"""Shared types and helpers for source fetchers."""
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
import json
import re

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "src" / "content" / "posts"
SEEN_FILE = ROOT / "content" / "seen.json"

IOT_KEYWORDS = re.compile(
    r"\b(iot|embedded|firmware|mqtt|modbus|lora(wan)?|zigbee|bluetooth|ble|"
    r"nb-iot|matter|thread|zephyr|freertos|esp32|esp8266|stm32|nordic|nrf|"
    r"scada|ics|plc|opc-?ua|profinet|ethercat|can-?bus|j1939|automotive|"
    r"traction|inverter|bms|battery|motor|pmsm|foc|charging|ev|e-mobility|"
    r"grid|substation|energy|solar|wind|hardware)\b",
    re.IGNORECASE,
)


@dataclass
class Item:
    id: str                # stable unique id (used for dedupe)
    title: str
    url: str
    source: str            # short human name, e.g. "NVD", "arXiv"
    published: datetime    # timezone-aware
    summary: str = ""
    tags: list[str] = field(default_factory=list)


def load_seen() -> set[str]:
    if not SEEN_FILE.exists():
        return set()
    return set(json.loads(SEEN_FILE.read_text()).get("ids", []))


def save_seen(ids: Iterable[str]) -> None:
    SEEN_FILE.parent.mkdir(parents=True, exist_ok=True)
    SEEN_FILE.write_text(json.dumps({"ids": sorted(set(ids))}, indent=2))


def infer_tags(text: str, extra: Iterable[str] = ()) -> list[str]:
    t = set(extra)
    low = text.lower()
    if re.search(r"\bcve-\d{4}-\d+", low) or "vulnerab" in low or "exploit" in low:
        t.add("security")
    if re.search(r"\b(traction|motor|pmsm|inverter|bms|battery|ev|e-mobility|charging)\b", low):
        t.add("traction")
    if re.search(r"\b(iot|mqtt|lora|zigbee|matter|thread|ble|nb-iot|modbus|opc-?ua)\b", low):
        t.add("iot")
    if re.search(r"\b(mcu|stm32|esp32|esp8266|nrf|nordic|zephyr|freertos|firmware|pcb|fpga|silicon)\b", low):
        t.add("hardware")
    if re.search(r"\b(model|llm|transformer|neural|inference|edge-ai|tinyml)\b", low):
        t.add("models")
    if re.search(r"\b(ics|scada|plc|profinet|ethercat|substation|grid)\b", low):
        t.add("industrial")
    return sorted(t) or ["hardware"]


def slugify_id(s: str) -> str:
    from slugify import slugify
    return slugify(s)[:80] or "post"


def write_post(item: Item, body: str) -> Path:
    day = item.published.astimezone(timezone.utc)
    dir_ = POSTS_DIR / f"{day.year:04d}" / f"{day.month:02d}"
    dir_.mkdir(parents=True, exist_ok=True)
    fname = f"{day.strftime('%Y-%m-%d')}-{slugify_id(item.title)}.md"
    path = dir_ / fname
    # Escape title double quotes for YAML
    safe_title = item.title.replace('"', "'")
    front = [
        "---",
        f'title: "{safe_title}"',
        f"date: {day.isoformat()}",
        f'source: "{item.source}"',
        f'source_url: "{item.url}"',
        f'ext_id: "{item.id}"',
        f"tags: {json.dumps(item.tags)}",
    ]
    if item.summary:
        safe_sum = item.summary.replace('"', "'").replace("\n", " ")
        front.append(f'summary: "{safe_sum[:400]}"')
    front.append("---\n")
    path.write_text("\n".join(front) + "\n" + body.strip() + "\n")
    return path
