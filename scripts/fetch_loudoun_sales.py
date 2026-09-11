#!/usr/bin/env python3
"""Fetch live Loudoun RPI Sales / Transfers for every Section 13 PIN.

Writes data/loudoun-rpi-sales.json. Then run rebuild_from_loudoun.py to
refresh data.js / sec13_parcels.json and the audit report.

Official source: reparcelasmt.loudoun.gov (Commissioner of the Revenue).
Does not invent sales. If a request fails, that PIN is recorded as
unverified instead of guessed.
"""
from __future__ import annotations

import json
import re
import time
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "loudoun-rpi-sales.json"
PARCELS = ROOT / "sec13_parcels.json"
DATA_JS = ROOT / "data.js"
UA = "Mozilla/5.0 (compatible; Broadlands13-audit/1.0; +https://pmiller-2025.github.io/broadlands13/)"


class TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tables = []
        self._cur = None
        self._row = None
        self._cell = None
        self._in_td = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "table":
            self._cur = {"id": attrs.get("id", ""), "rows": []}
        elif tag == "tr" and self._cur is not None:
            self._row = []
        elif tag in ("td", "th") and self._row is not None:
            self._cell = []
            self._in_td = True

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self._in_td:
            self._row.append(re.sub(r"\s+", " ", "".join(self._cell)).replace("\xa0", " ").strip())
            self._in_td = False
        elif tag == "tr" and self._row is not None and self._cur is not None:
            if any(self._row):
                self._cur["rows"].append(self._row)
            self._row = None
        elif tag == "table" and self._cur is not None:
            self.tables.append(self._cur)
            self._cur = None

    def handle_data(self, data):
        if self._in_td:
            self._cell.append(data)


def fetch(url: str, retries: int = 4) -> bytes:
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
            with urllib.request.urlopen(req, timeout=45) as r:
                return r.read()
        except Exception as e:
            last = e
            time.sleep(1.2 * (i + 1))
    raise RuntimeError(f"{url}: {last}")


def parse_sales_table(html: str) -> list[dict]:
    p = TableParser()
    p.feed(html)
    sales = []
    for t in p.tables:
        rows = t["rows"]
        if rows and rows[0][:3] == ["Date", "Sale Price", "Buyer"]:
            for row in rows[1:]:
                if len(row) >= 3:
                    sales.append({"date": row[0], "price": row[1], "buyer": row[2]})
    return sales


def parse_detail(html: str) -> dict:
    p = TableParser()
    p.feed(html)
    for t in p.tables:
        kv = {}
        for row in t["rows"]:
            if len(row) >= 2:
                kv[row[0]] = row[1]
        if "Sale Date" in kv or "Seller" in kv:
            return kv
    return {}


def pins_from_repo() -> list[tuple[str, str, str | None]]:
    if PARCELS.exists():
        data = json.loads(PARCELS.read_text())
    else:
        src = DATA_JS.read_text()
        m = re.search(r"const PARCEL_DATA = ({.*});", src, re.S)
        data = json.loads(m.group(1))
    out = []
    for f in data["features"]:
        p = f["properties"]
        out.append((p["pin"], str(p.get("lot")), p.get("address")))
    return out


def main() -> None:
    pins = pins_from_repo()
    parcels = []
    errors = []
    for i, (pin, lot, addr) in enumerate(pins, 1):
        url = (
            "https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx"
            f"?UseSearch=no&jur=107&mode=sales&pin={pin}&taxyr=2026"
        )
        try:
            html = fetch(url).decode("utf-8", "replace")
            sales = parse_sales_table(html)
            details = []
            for card in range(1, max(len(sales), 1) + 1):
                if not sales:
                    break
                durl = (
                    "https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx"
                    f"?mode=sales&UseSearch=no&pin={pin}&jur=107&taxyr=2026"
                    f"&card={card}&item=1&State=1|1&items=1"
                )
                dhtml = fetch(durl).decode("utf-8", "replace")
                details.append(parse_detail(dhtml))
                time.sleep(0.12)
            parcels.append(
                {
                    "pin": pin,
                    "lot": lot,
                    "address": addr,
                    "n_sales": len(sales),
                    "sales": sales,
                    "sale_details": details,
                    "url": url,
                    "verified": True,
                }
            )
            print(f"{i:02d}/{len(pins)} lot={lot} pin={pin} sales={len(sales)}")
        except Exception as e:
            errors.append({"pin": pin, "lot": lot, "address": addr, "error": str(e)})
            parcels.append(
                {
                    "pin": pin,
                    "lot": lot,
                    "address": addr,
                    "n_sales": 0,
                    "sales": [],
                    "sale_details": [],
                    "url": url,
                    "verified": False,
                    "error": str(e),
                }
            )
            print(f"{i:02d}/{len(pins)} FAIL lot={lot} {e}")
        time.sleep(0.12)

    payload = {
        "source": "Loudoun County Real Property Information (reparcelasmt.loudoun.gov) Sales / Transfers",
        "fetched": datetime.now(timezone.utc).isoformat(),
        "fetched_date": datetime.now(timezone.utc).date().isoformat(),
        "parcels": parcels,
        "errors": errors,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2))
    print(f"wrote {OUT} parcels={len(parcels)} errors={len(errors)}")


if __name__ == "__main__":
    main()
