"""NVD CVE feed — filter to IoT / ICS / embedded keywords."""
from __future__ import annotations
from datetime import datetime, timedelta, timezone
import requests
from common import Item, IOT_KEYWORDS, infer_tags

NAME = "nvd"
DISPLAY = "NVD"
API = "https://services.nvd.nist.gov/rest/json/cves/2.0"


def fetch(limit: int = 15) -> list[Item]:
    now = datetime.now(timezone.utc)
    start = now - timedelta(days=2)
    params = {
        "pubStartDate": start.strftime("%Y-%m-%dT%H:%M:%S.000"),
        "pubEndDate": now.strftime("%Y-%m-%dT%H:%M:%S.000"),
        "resultsPerPage": 100,
    }
    try:
        r = requests.get(API, params=params, timeout=30,
                         headers={"User-Agent": "mantai-signal/0.1"})
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        print(f"[nvd] fetch failed: {e}")
        return []

    items: list[Item] = []
    for entry in data.get("vulnerabilities", []):
        cve = entry.get("cve", {})
        cid = cve.get("id")
        if not cid:
            continue
        descs = cve.get("descriptions", [])
        desc = next((d["value"] for d in descs if d.get("lang") == "en"), "")
        if not IOT_KEYWORDS.search(desc):
            continue
        pub = cve.get("published") or now.isoformat()
        try:
            published = datetime.fromisoformat(pub.replace("Z", "+00:00"))
        except ValueError:
            published = now
        items.append(Item(
            id=f"nvd:{cid}",
            title=f"{cid}: {desc[:120]}",
            url=f"https://nvd.nist.gov/vuln/detail/{cid}",
            source=DISPLAY,
            published=published,
            summary=desc,
            tags=infer_tags(desc, ["security"]),
        ))
        if len(items) >= limit:
            break
    return items
