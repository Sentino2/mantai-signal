# Architecture

```
sources/*.py  ->  ingest.py  ->  src/content/posts/YYYY/MM/*.md
                     |
                     +--> content/seen.json (dedupe index)

GitHub Actions
  daily-digest.yml     (cron 06:00 UTC)
    -> one branch+PR per source, merged by github-actions[bot]
  deploy-pages.yml     (on push to main)
    -> Astro build -> Pages
```

Each source module exports `fetch() -> list[Item]`. Items are deduped against `content/seen.json` by stable `id`. Posts are written under `src/content/posts/YYYY/MM/` with front-matter validated by Astro content collections (`src/content/config.ts`).
