# mantai-signal

Daily intelligence digest for IoT, embedded hardware, traction / e-mobility, and industrial control. Published as a static blog at https://sentino2.github.io/mantai-signal.

## How it works

A GitHub Action runs every morning (06:00 UTC ≈ 08:00 Europe/Madrid). For each configured source it:

1. Pulls the latest items (CVEs, papers, releases, blog posts).
2. Deduplicates against `content/seen.json`.
3. Writes fresh items as markdown posts under `src/content/posts/YYYY/MM/`.
4. Opens one pull request per source, waits ~30s, and auto-merges.

The Astro site rebuilds on every merge to `main` and redeploys to GitHub Pages.

## Sources

| Source | What | Cadence |
|---|---|---|
| NVD | CVEs tagged IoT / ICS / embedded / MQTT / Modbus / LoRa / Zigbee | daily |
| arXiv | New papers in `cs.AR` and `eess.SY` | daily |
| Hackaday | Front-page RSS | daily |
| Zephyr | New GitHub releases from `zephyrproject-rtos/zephyr` | daily |
| Semtech | Company blog RSS (LoRa / LoRaWAN ecosystem) | daily |

Add more in `scripts/sources/` — each file exports `fetch()` returning `Item[]`.

## Local development

```bash
# Install
npm install
pip install -r scripts/requirements.txt

# Run ingestion once (writes posts, updates seen.json)
python scripts/ingest.py

# Preview site
npm run dev
```

## Manual on-demand run

- **GitHub UI**: Actions → *daily-digest* → *Run workflow*.
- **CLI**: `gh workflow run daily-digest.yml -R Sentino2/mantai-signal`.
- **Local**: `bash scripts/run_now.sh` (runs ingest + commits + pushes; requires `gh` authed).

## Optional: LLM summaries

Set repo secret `ANTHROPIC_API_KEY` to enable Claude-based summarization instead of extractive. The Action picks it up automatically.
