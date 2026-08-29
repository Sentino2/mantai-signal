# Sources

| Name | URL | Why it's here |
|---|---|---|
| nvd | https://services.nvd.nist.gov/rest/json/cves/2.0 | Primary feed for embedded/ICS CVEs |
| arxiv | http://export.arxiv.org/api/query | Papers in cs.AR (hardware architecture) and eess.SY (control systems) |
| hackaday | https://hackaday.com/feed/ | Community pulse — teardowns, firmware, reverse-engineering |
| zephyr | GitHub releases (zephyrproject-rtos/zephyr) | RTOS release cadence relevant to IoT devs |
| semtech | https://blog.semtech.com/rss.xml | LoRa / LoRaWAN ecosystem news |

To propose a source, open an issue using the `source-request` template.

## Cadence

The digest cron runs at 06:00 UTC daily. Sources with no fresh items past the dedupe are skipped silently — this is normal and correct behaviour.
