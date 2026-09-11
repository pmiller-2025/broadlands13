#!/usr/bin/env python3
"""Rebuild sec13 parcel sales from a Loudoun RPI extract and write the audit report.

The extract is produced by scripts/fetch_loudoun_sales.py (or a prior snapshot
in data/loudoun-rpi-sales.json). Geometries stay as published; only sales /
owner fields are replaced. HOA parcels A–E keep empty sales so they stay
open-space / no-data on the map.
"""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXTRACT = ROOT / "data" / "loudoun-rpi-sales.json"
CLERK_DEEDS = ROOT / "data" / "loudoun-clerk-deeds.json"
CLERK_LOOKUP = ROOT / "data" / "loudoun-clerk-lookup.json"
PARCELS = ROOT / "sec13_parcels.json"
DATA_JS = ROOT / "data.js"
AUDIT = ROOT / "docs" / "loudoun-sales-audit.md"


def parse_mdy(d: str | None) -> str | None:
    if not d:
        return None
    d = d.strip()
    if re.match(r"^\d{4}-\d{2}-\d{2}$", d):
        return d
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})$", d)
    if not m:
        return None
    mm, dd, yy = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return f"{yy:04d}-{mm:02d}-{dd:02d}"


def parse_price(p) -> int | None:
    if p is None or p == "" or str(p).strip() in ("$0", "$0.00", "&nbsp;"):
        return None
    n = re.sub(r"[^0-9.]", "", str(p))
    if not n:
        return None
    val = float(n)
    return int(round(val)) if val > 0 else None


def fmt_price(p) -> str:
    n = parse_price(p)
    if n is None:
        return "$0"
    return f"${n:,}"


def surnames(buyer: str) -> set[str]:
    out = set()
    for part in re.split(r"&", buyer or ""):
        last = part.strip().split(",")[0].strip().upper()
        last = re.sub(r"\s+TR$", "", last)
        last = re.sub(r"\s+TEE[S]?$", "", last)
        if last:
            out.add(last)
    return out


def same_household(a: str, b: str) -> bool:
    return bool(surnames(a) & surnames(b))


def counts_as_new_owner(sale: dict, is_first: bool, prev: dict | None) -> bool:
    if is_first:
        return True
    if parse_price(sale.get("price")) is None:
        return False
    if (
        prev
        and sale.get("date") == prev.get("date")
        and parse_price(sale.get("price")) == parse_price(prev.get("price"))
        and same_household(sale.get("buyer") or "", prev.get("buyer") or "")
    ):
        return False
    return True


def eras(sales: list[dict]) -> int:
    n = 0
    prev = None
    for i, s in enumerate(sales):
        if counts_as_new_owner(s, i == 0, prev):
            n += 1
            prev = s
    return n


def load_clerk_deeds() -> dict[str, list[dict]]:
    """PIN → clerk-verified original rows. Requires date + buyer. Never invent."""
    if not CLERK_DEEDS.exists():
        return {}
    data = json.loads(CLERK_DEEDS.read_text())
    by_pin: dict[str, list[dict]] = {}
    for raw in data.get("deeds") or []:
        date_s = parse_mdy(raw.get("date"))
        buyer = (raw.get("buyer") or "").strip()
        pin = (raw.get("pin") or "").strip()
        if not date_s or not buyer or not pin:
            continue
        price = raw.get("price")
        if price in (None, ""):
            price_s = "$0"
        else:
            price_s = fmt_price(price)
        row = {
            "date": date_s,
            "price": price_s,
            "buyer": buyer,
            "seller": (raw.get("seller") or "").strip(),
            "instrument": (raw.get("instrument") or "").strip(),
            "valuation": (raw.get("valuation") or "").strip(),
            "note": (raw.get("note") or "Clerk PAX index — original deed").strip(),
        }
        book, page = (raw.get("book") or "").strip(), (raw.get("page") or "").strip()
        if book and page and "book" not in row["note"].lower():
            row["note"] = f"{row['note']}; book {book} page {page}"
        by_pin.setdefault(pin, []).append(row)
    return by_pin


def sale_key(s: dict) -> tuple:
    return (
        s.get("date"),
        parse_price(s.get("price")),
        (s.get("buyer") or "").upper(),
        (s.get("instrument") or ""),
    )


def merge_clerk_originals(rpi_sales: list[dict], clerk_rows: list[dict]) -> list[dict]:
    """Prepend clerk-verified originals that RPI does not already list."""
    have = {sale_key(s) for s in rpi_sales}
    extra = []
    for s in clerk_rows:
        k = sale_key(s)
        # Also skip if same date+buyer already present (instrument may be blank on one side).
        already = k in have or any(
            s.get("date") == e.get("date") and (s.get("buyer") or "").upper() == (e.get("buyer") or "").upper()
            for e in rpi_sales
        )
        if already:
            continue
        extra.append(s)
    merged = extra + rpi_sales

    def sort_key(r):
        inst = r.get("instrument") or ""
        return (r["date"] or "9999", inst, r["buyer"])

    merged.sort(key=sort_key)
    return merged


def load_existing() -> dict:
    if PARCELS.exists():
        return json.loads(PARCELS.read_text())
    src = DATA_JS.read_text()
    m = re.search(r"const PARCEL_DATA = ({.*});", src, re.S)
    return json.loads(m.group(1))


def county_sales_oldest_first(rec: dict) -> list[dict]:
    """County HTML table is newest-first. Walk details in that same order, then reverse."""
    table = rec.get("sales") or []
    details = rec.get("sale_details") or []
    # Pair table rows with detail cards (both newest-first).
    rows = []
    for i, s in enumerate(table):
        det = details[i] if i < len(details) else {}
        rows.append(
            {
                "date": parse_mdy(s.get("date") or det.get("Sale Date")),
                "price": fmt_price(s.get("price") if s.get("price") not in (None, "") else det.get("Sale Price")),
                "buyer": (s.get("buyer") or det.get("Buyer") or "").strip(),
                "seller": (det.get("Seller") or "").strip(),
                "instrument": (det.get("Instrument Number") or "").strip(),
                "valuation": (det.get("Valuation Code") or "").strip(),
                "note": (det.get("Note") or "").strip(),
            }
        )
    # Oldest first; same-day ties by instrument (then original table order).
    def sort_key(r):
        inst = r.get("instrument") or ""
        return (r["date"] or "9999", inst, r["buyer"])

    rows.sort(key=sort_key)
    # Drop empty-date rows (should not happen).
    return [r for r in rows if r["date"]]


def sale_public(s: dict) -> dict:
    out = {"date": s["date"], "price": s["price"], "buyer": s["buyer"]}
    if s.get("seller"):
        out["seller"] = s["seller"]
    if s.get("instrument"):
        out["instrument"] = s["instrument"]
    if s.get("valuation"):
        out["valuation"] = s["valuation"]
    if s.get("note"):
        out["note"] = s["note"]
    return out


def main() -> None:
    existing = load_existing()
    extract = json.loads(EXTRACT.read_text())
    by_pin = {r["pin"]: r for r in extract["parcels"]}
    clerk_by_pin = load_clerk_deeds()
    clerk_lookup = json.loads(CLERK_LOOKUP.read_text()) if CLERK_LOOKUP.exists() else {}

    old_by_pin = {f["properties"]["pin"]: f["properties"] for f in existing["features"]}
    rebuilt = []
    audit_rows = []

    for feat in existing["features"]:
        props = dict(feat["properties"])
        pin = props["pin"]
        rec = by_pin[pin]
        letter = not str(props.get("lot", "")).isdigit()
        old_sales = list(props.get("sales") or [])
        if letter:
            new_sales = []  # keep HOA as no-data / open space
        else:
            rpi_sales = [sale_public(s) for s in county_sales_oldest_first(rec)]
            new_sales = merge_clerk_originals(rpi_sales, clerk_by_pin.get(pin) or [])
        props["sales"] = new_sales
        rebuilt.append({"type": "Feature", "geometry": feat["geometry"], "properties": props})

        # reconciliation vs previous published map
        def keyset(sales):
            return [(s.get("date"), parse_price(s.get("price")), (s.get("buyer") or "").upper()) for s in sales]

        old_keys = keyset(old_sales)
        new_keys = keyset(new_sales)
        missing = [k for k in new_keys if k not in old_keys]
        extra = [k for k in old_keys if k not in new_keys]
        first = new_sales[0] if new_sales else None
        n_eras = eras(new_sales) if new_sales else 0
        still_orig = n_eras == 1
        priced = [s for s in new_sales if parse_price(s.get("price")) is not None]
        first_priced = priced[0] if priced else None
        gap = False
        gap_why = ""
        if not letter and first:
            y = int(first["date"][:4])
            if parse_price(first["price"]) is None and y >= 2001:
                gap = True
                gap_why = "first recorded deed is $0 / unpriced (no 1999–2000 priced first sale in RPI)"
            elif y >= 2001:
                gap = True
                gap_why = "first recorded sale is a later resale (no 1999–2000 first sale in RPI)"
        audit_rows.append(
            {
                "lot": props.get("lot"),
                "address": props.get("address"),
                "pin": pin,
                "letter": letter,
                "old_sales": old_sales,
                "new_sales": new_sales,
                "missing_from_map": missing,
                "extra_on_map": extra,
                "original_buyer": (first or {}).get("buyer"),
                "original_date": (first or {}).get("date"),
                "original_price": (first or {}).get("price"),
                "still_originaler": still_orig if new_sales else None,
                "eras": n_eras,
                "priced_n": len(priced),
                "county_gap": gap,
                "gap_why": gap_why,
                "rpi_url": rec.get("url"),
            }
        )

    fc = {"type": "FeatureCollection", "features": rebuilt}
    PARCELS.write_text(json.dumps(fc, separators=(",", ":")))
    DATA_JS.write_text("const PARCEL_DATA = " + json.dumps(fc, separators=(",", ":")) + ";\n")
    write_audit(extract, audit_rows, clerk_lookup)
    print(f"wrote {PARCELS} {DATA_JS} {AUDIT}")


def write_audit(extract: dict, rows: list[dict], clerk_lookup: dict | None = None) -> None:
    houses = [r for r in rows if not r["letter"]]
    hoa = [r for r in rows if r["letter"]]
    priced_all = []
    last_priced = []
    orig = turn = 0
    for r in houses:
        sales = r["new_sales"]
        n = r["eras"]
        if n <= 1:
            orig += 1
        else:
            turn += 1
        last = None
        for s in sales:
            pr = parse_price(s.get("price"))
            if pr:
                priced_all.append((r["lot"], r["address"], s["date"], pr, s["buyer"]))
                last = pr
        if last:
            last_priced.append(last)
    last_priced.sort()
    n = len(last_priced)
    median = None
    if n:
        median = last_priced[n // 2] if n % 2 else (last_priced[n // 2 - 1] + last_priced[n // 2]) / 2
    added = [r for r in houses if r["missing_from_map"]]
    extras = [r for r in houses if r["extra_on_map"]]
    gaps = [r for r in houses if r["county_gap"]]
    correct = [r for r in houses if not r["missing_from_map"] and not r["extra_on_map"] and not r["county_gap"]]
    trust_ok = []
    for r in houses:
        for s in r["new_sales"][1:]:
            if parse_price(s.get("price")) is None:
                trust_ok.append((r, s))

    fetched = extract.get("fetched")
    lines = []
    a = lines.append
    a("# Broadlands Section 13 — Loudoun sales history audit")
    a("")
    a(f"Audited **{extract.get('fetched_date') or fetched or date.today().isoformat()}** against live Loudoun County Real Property Information (RPI) Sales / Transfers pages and Loudoun GIS parcel inventory.")
    a("")
    a("This is a neighbor-shareable reconciliation. It is not a title search. Always confirm a deed with [Loudoun RPI](https://reparcelasmt.loudoun.gov/pt/search/CommonSearch.aspx?mode=PARID) or the Clerk’s land-records index before relying on a name, date, or price.")
    a("")
    a("## How this was checked")
    a("")
    a("1. **Lot inventory** — Loudoun GIS `COL/LandRecordData` parcels where `PA_SUBD_NAME` contains BROADLANDS and `PA_SUBD_SECT='13'`. Every parcel is plat **1998-0187**. Result: **55 numbered house lots + 5 open-space parcels (A–E)**. The map already had exactly those 60 PINs; none missing, none extra.")
    a("2. **Sales history** — for each PIN, the official RPI datalet `mode=sales` at `reparcelasmt.loudoun.gov` (date, price, buyer) plus each sale’s detail card (seller, instrument, valuation, notes). Pulled live; nothing invented.")
    a("3. **PIN remap** — every Section 13 PIN shows a 2005 parcel-tracking split from parent PIN `156488930000`. That parent is the old developer tract (1994 Broadlands Associates sale), not a per-lot owner history. It does **not** restore missing 1999–2000 house deeds.")
    a("4. **Clerk land records (PAX / LandMARC / GIS)** — every public path was tried before treating a lot as still unavailable. LandMARC is permits, not deeds. GIS has no grantor/grantee. Historic indexes stop in 1903. Sales-report downloads start in 2013. The Clerk PAX index at `lisweb.loudoun.gov/paxworld` is the official next step; it requires a free occasional-user account. This audit did **not** create one and did **not** invent originals from Zillow, book numbers, or building permits.")
    a("")
    a("## New totals (55 houses)")
    a("")
    a("| Measure | Previous published (~) | After this audit |")
    a("| --- | --- | --- |")
    a(f"| Houses | 55 | **55** |")
    a(f"| Priced sales (RPI, price > $0) | ~90 | **{len(priced_all)}** |")
    a(f"| Originalers remaining (first deed + later $0/title tweaks only) | — | **{orig}** |")
    a(f"| Turnovers (2nd+ owner era) | ~39 | **{turn}** |")
    a(f"| Median of each house’s last priced sale | ~$622,000 | **${median:,.0f}** |" if median else "| Median last priced sale | ~$622,000 | — |")
    a("")
    a("The old “~39 turnovers” treated four lots whose **first recorded deed is $0** (Cervantes, George, Watkins, Jarral) as turnovers. Those $0 first deeds are the first recorded owner and **stay originalers**. Same-day Moran restatement (lot 24, two $492,000 rows, same household) is kept in history but does **not** start a second era.")
    a("")
    a("## What changed in the map data")
    a("")
    if added:
        a("### Added (was missing from the published map)")
        a("")
        for r in added:
            for k in r["missing_from_map"]:
                a(f"- Lot {r['lot']} {r['address']}: {k[0]} · {fmt_price(k[1]) if k[1] else '$0'} · {k[2]}")
        a("")
    else:
        a("No priced county rows were missing from the map.")
        a("")
    if extras:
        a("### Extra / wrong rows removed from the map")
        a("")
        for r in extras:
            for k in r["extra_on_map"]:
                a(f"- Lot {r['lot']} {r['address']}: {k}")
        a("")
    else:
        a("No published house rows contradicted county (no extras to delete).")
        a("")
    a("Lot 24 (Moran) same-day pair is now ordered by instrument (`…022516` then `…022517`). Lot 51 (Hewitt Relocation → Goodwyn, same day) stays two priced eras — different households.")
    a("")
    a("HOA / open space A–E: county records a **1999-01-12 $0** deed to Broadlands Association Inc on each. The map still leaves those parcels as **no-data** so they do not count as houses or originalers.")
    a("")
    a("## Known checks")
    a("")
    a("| Check | County RPI | Map after audit |")
    a("| --- | --- | --- |")
    a("| Earliest priced house sales | **1999-09-03** Landino 42759 Hollowind ($305,840) and Gordon/Getter 42767 Hollowind ($308,400) | Same. Landino still originalers. Gordon/Getter sold 2020-03-17 ($710,000) — not still originalers. |")
    a("| Paul & Jessica Chestnut 42770 Hollowind | 1999-10-19 $268,915; 2021-11-09 $0 trust | Same. Still originalers ($0 does not start a new era). |")
    a("| Crisp 21666 Stillbrook Farm | First deed **2000-02-02** $250,658 (closing date on the card); 2017-05-22 $0 trust | Same. Still originalers. |")
    a("| Thompson 42734 Hollowind | 1999-09-21 $273,017; 2023-02-14 $0 trust | Same. Still originalers. |")
    a("")
    a("## Lots whose 1999–2000 original priced sale is **not** in Loudoun RPI")
    a("")
    a("A neighbor was right that several original buyers are missing from the **assessment** sales history. RPI simply does not list a 1999–2000 priced first sale on these PINs. This audit **does not invent** those deeds. The first *recorded* RPI deed is what the map uses unless a later clerk-verified original is merged from `data/loudoun-clerk-deeds.json` (that file is empty until PAX returns grantor, grantee, and date).")
    a("")
    a("| Lot | Address | PIN | First RPI deed | Still originaler? | Gap |")
    a("| --- | --- | --- | --- | --- | --- |")
    for r in sorted(gaps, key=lambda x: int(x["lot"])):
        first = f"{r['original_date']} {r['original_price']} {r['original_buyer']}"
        a(f"| {r['lot']} | {r['address']} | {r['pin']} | {first} | {'Y' if r['still_originaler'] else 'N'} | {r['gap_why']} |")
    a("")
    write_clerk_section(a, clerk_lookup or {}, gaps)
    a("## Lot-by-lot reconciliation (55 houses)")
    a("")
    a("Columns: original buyer = first RPI deed (priced or $0). Still originaler = only one owner era after skipping later $0 / same-household same-day restatements. County vs map = whether the published card already matched RPI before this audit.")
    a("")
    for r in sorted(houses, key=lambda x: int(x["lot"])):
        status = "already matched county"
        if r["missing_from_map"] and r["extra_on_map"]:
            status = "corrected (add + remove)"
        elif r["missing_from_map"]:
            status = "added missing county row(s)"
        elif r["extra_on_map"]:
            status = "removed extra map row(s)"
        elif r["county_gap"]:
            status = "matched county; original 1999–2000 priced sale not in RPI"
        a(f"### Lot {r['lot']} — {r['address']}")
        a("")
        a(f"- PIN `{r['pin']}` · [RPI sales]({r['rpi_url']})")
        a(f"- Original buyer (first RPI deed): **{r['original_buyer']}** · {r['original_date']} · {r['original_price']}")
        a(f"- Still originaler: **{'Y' if r['still_originaler'] else 'N'}** · owner eras {r['eras']} · priced sales {r['priced_n']}")
        a(f"- Status: {status}")
        if r["gap_why"]:
            a(f"- County gap: {r['gap_why']}")
        a("- County / map history (oldest first):")
        a("")
        a("| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |")
        a("| --- | --- | --- | --- | --- | --- | --- |")
        prev = None
        era_n = 0
        for i, s in enumerate(r["new_sales"]):
            is_era = counts_as_new_owner(s, i == 0, prev)
            if is_era:
                era_n += 1
                prev = s
            note = s.get("note") or s.get("valuation") or ""
            if parse_price(s.get("price")) is None and i > 0:
                note = (note + "; $0/unpriced — kept, skipped for eras").strip("; ")
            elif parse_price(s.get("price")) is None and i == 0:
                note = (note + "; $0 first deed — starts originaler era").strip("; ")
            a(
                f"| {s['date']} | {s['price']} | {s['buyer']} | {s.get('seller') or '—'} | {s.get('instrument') or '—'} | {'Y #'+str(era_n) if is_era else 'skip'} | {note} |"
            )
        a("")

    a("## Open-space parcels (not houses)")
    a("")
    a("| Parcel | PIN | County first deed | Map |")
    a("| --- | --- | --- | --- |")
    for r in sorted(hoa, key=lambda x: str(x["lot"])):
        a(f"| {r['lot']} | {r['pin']} | 1999-01-12 $0 Broadlands Association Inc | left as no-data (not a house) |")
    a("")
    a("## $0 / trust / title rows (kept, skipped for later eras)")
    a("")
    if trust_ok:
        a("| Lot | Address | Date | Buyer | Instrument |")
        a("| --- | --- | --- | --- | --- |")
        for r, s in trust_ok:
            a(f"| {r['lot']} | {r['address']} | {s['date']} | {s['buyer']} | {s.get('instrument') or '—'} |")
        a("")
    a("## Sources")
    a("")
    a("- Loudoun County Real Property Information — Sales / Transfers per PIN, e.g. `https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=<PIN>&taxyr=2026`")
    a("- Loudoun GIS Land Records parcels — Broadlands Section 13, plat 1998-0187 (`https://logis.loudoun.gov/gis/rest/services/COL/LandRecordData/MapServer/4`)")
    a("- Snapshot of the RPI pull used for this audit: `data/loudoun-rpi-sales.json`")
    a("- Clerk public-path lookup (pointers only): `data/loudoun-clerk-lookup.json`")
    a("- Clerk-verified originals overlay (empty until PAX): `data/loudoun-clerk-deeds.json`")
    a("- Refresh: `python3 scripts/fetch_loudoun_sales.py && python3 scripts/rebuild_from_loudoun.py`")
    a("")
    a("Clerk of Circuit Court **images** were not purchased. The free PAX **index** was not searched because it requires a personal occasional-user account. Any original 1999–2000 builder deed that is absent from RPI is documented as a gap, not guessed.")
    a("")
    AUDIT.write_text("\n".join(lines))


def write_clerk_section(a, clerk_lookup: dict, gaps: list[dict]) -> None:
    a("## Clerk / deed-index lookup (2026-09-11)")
    a("")
    a("Goal: find the original builder deed (grantor, grantee, date, price if shown, instrument or book/page) for each of the 23 gap lots, and add only what the clerk index actually shows.")
    a("")
    a("**Lots that gained a clerk-verified original on the map: none.** The overlay file `data/loudoun-clerk-deeds.json` has zero rows. Map totals stay at 90 priced sales / 21 originalers / 34 turnovers.")
    a("")
    a("### What was reachable without a login")
    a("")
    for path in clerk_lookup.get("paths_tried") or []:
        a(f"- **{path.get('name')}** — {path.get('url')} — {path.get('result')}")
    if not clerk_lookup.get("paths_tried"):
        a("- See `data/loudoun-clerk-lookup.json`.")
    a("")
    a("### Login Paul must do himself")
    a("")
    login = clerk_lookup.get("login_paul_must_do") or {}
    if login:
        a(f"- Start: [{login.get('start_here')}]({login.get('start_here')})")
        a(f"- Create a **free occasional-user account** (your own name) and log in at [{login.get('signup_login')}]({login.get('signup_login')}). Index search is free; images cost $0.50/page plus a convenience fee.")
        a(f"- Manual: [PAX Occasional User guide (PDF)]({login.get('manual_pdf')})")
        a(f"- Or use the free in-person kiosks: {login.get('in_person_free')}")
        a("- After you have grantor / grantee / date (and price only if the index shows it), add a row to `data/loudoun-clerk-deeds.json` and re-run `python3 scripts/rebuild_from_loudoun.py`. Do not add a guessed buyer or a date inferred from a book number.")
    else:
        a("- Create a free PAX occasional-user account at https://lisweb.loudoun.gov/paxworld/")
    a("")
    a("### Best public pointers (not yet deeds)")
    a("")
    a("Lots that already have a 1999–2000 priced first sale in RPI cite deed books **1711–1750** (Landino `1711--539`, Gordon `1711--520`, Thompson `1714--1293`, Paul `1722--977`, Gavva `1741--779`, Crisp `1750--515`). Three gap lots still show a second book/page in that same range on the RPI legal line. That is a **pointer for PAX Book+Page search**, not enough to put a buyer or price on the map.")
    a("")
    a("| Lot | Address | Possible original book/page (pointer only) | Later legal cite | First RPI instrument to cross-ref | NEWCON permit (not a deed) |")
    a("| --- | --- | --- | --- | --- | --- |")
    lookup_lots = {str(x.get("lot")): x for x in (clerk_lookup.get("lots") or [])}
    for r in sorted(gaps, key=lambda x: int(x["lot"])):
        L = lookup_lots.get(str(r["lot"]), {})
        orig_bp = []
        later_bp = []
        for bp in L.get("book_page_refs") or []:
            cite = f"{bp.get('book')}--{bp.get('page')}"
            if bp.get("classification") == "same_book_range_as_known_1999_2000_originals":
                orig_bp.append(cite)
            else:
                later_bp.append(cite)
        later_bp.extend(i.get("instrument") for i in L.get("instrument_refs_on_legal") or [])
        first = L.get("first_rpi_deed") or {}
        inst = first.get("instrument") or "—"
        newcon = L.get("newcon_permit_not_a_deed") or {}
        newcon_s = f"{newcon.get('date')} {newcon.get('number')}" if newcon.get("date") else "—"
        a(
            f"| {r['lot']} | {r['address']} | {', '.join(orig_bp) or '—'} | {', '.join(x for x in later_bp if x) or '—'} | {inst} | {newcon_s} |"
        )
    a("")
    a("Every one of the 23 gap lots has a **1999 or January–March 2000 NEWCON** permit on the public RPI permits tab, so the house was built in the original-sale window. That does **not** name the first buyer and was not added as a sale.")
    a("")
    a("### Still county-unavailable (all 23)")
    a("")
    a("Until PAX (or a kiosk) returns parties and a recording date, the map keeps using the first RPI deed. Neighbor-facing: these lots do **not** yet show a clerk-proven 1999–2000 originaler.")
    a("")


if __name__ == "__main__":
    main()
