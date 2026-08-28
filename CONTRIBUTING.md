# Contributing

Adding a new source: drop a file into `scripts/sources/<name>.py` exporting `NAME`, `DISPLAY`, and `fetch() -> list[Item]`. Add `<name>` to `SOURCES` in `scripts/ingest.py`. The daily workflow discovers sources automatically via `--list`.

Local run: `pip install -r scripts/requirements.txt && python scripts/ingest.py --source <name>`.
