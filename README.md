# Broadlands Section 13

Password-gated ownership timeline map.

Site: GitHub Pages (this repo).

- Map password `Broadlands13` — colors + medians, prices hidden
- Price passwords `Broadlands13$$` or `Hollowind$$` — same session unlocks sale amounts
- Lot-by-lot Loudoun RPI + clerk-pointer audit: [docs/loudoun-sales-audit.md](docs/loudoun-sales-audit.md)
- Clerk public-path findings (no invented deeds): `data/loudoun-clerk-lookup.json`
- Clerk-verified originals overlay (empty until PAX): `data/loudoun-clerk-deeds.json`
- Refresh from county: `python3 scripts/fetch_loudoun_sales.py && python3 scripts/rebuild_from_loudoun.py`
- Checks: `python3 scripts/verify_sec13.py`
