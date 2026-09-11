#!/usr/bin/env python3
"""Checks password hashes, era rules, and audited totals against county snapshot."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from rebuild_from_loudoun import counts_as_new_owner, eras, parse_price  # noqa: E402


def sha(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()


def load_js() -> dict:
    src = (ROOT / "data.js").read_text()
    return json.loads(re.search(r"const PARCEL_DATA = ({.*});", src, re.S).group(1))


def by_lot(data):
    return {str(f["properties"]["lot"]): f["properties"] for f in data["features"]}


def main() -> None:
    html = (ROOT / "index.html").read_text()
    assert sha("Broadlands13") in html
    assert sha("Broadlands13$$") in html
    assert sha("Hollowind$$") in html
    assert "PRICE_PW_HASHES" in html
    assert "sameHousehold" in html
    assert "isHouseLot" in html
    assert "Start neutral" in html
    assert "MILLER, PAUL" not in html  # do not label Paul's house in the page shell

    data = load_js()
    parcels = json.loads((ROOT / "sec13_parcels.json").read_text())
    assert data == parcels
    lots = by_lot(data)
    houses = [lots[k] for k in lots if k.isdigit()]
    hoa = [lots[k] for k in lots if not k.isdigit()]
    assert len(houses) == 55
    assert sorted(int(k) for k in lots if k.isdigit()) == list(range(1, 56))
    assert sorted(k for k in lots if not k.isdigit()) == ["A", "B", "C", "D", "E"]
    for h in hoa:
        assert not h.get("sales"), h["lot"]
        assert h.get("highlight") in (None, "")
    for p in lots.values():
        assert p.get("highlight") in (None, "")
        assert p.get("highlight_note") in (None, "")

    # Known originalers / trusts
    def era_of(lot):
        return eras(lots[lot]["sales"])

    assert era_of("37") == 1, "Landino still originaler"
    assert era_of("35") == 2, "Gordon/Getter sold 2020"
    assert era_of("52") == 1, "Paul $0 trust stays originaler"
    assert era_of("5") == 1, "Crisp $0 trust stays originaler"
    assert era_of("44") == 1, "Thompson $0 trust stays originaler"
    assert era_of("31") == 1, "Gavva 2016 will stays originaler"
    assert era_of("24") == 1, "Moran same-day restatement is one era"
    assert era_of("51") == 3, "Hewitt → Goodwyn → Darab"
    assert lots["31"]["sales"][1]["date"] == "2016-06-01"
    assert parse_price(lots["31"]["sales"][1]["price"]) is None
    assert lots["52"]["sales"][0]["date"] == "1999-10-19"
    assert lots["37"]["sales"][0]["date"] == "1999-09-03"
    assert lots["35"]["sales"][0]["date"] == "1999-09-03"
    assert lots["5"]["sales"][0]["date"] == "2000-02-02"

    orig = turn = priced = 0
    last_priced = []
    for p in houses:
        n = eras(p["sales"])
        if n <= 1:
            orig += 1
        else:
            turn += 1
        last = None
        for s in p["sales"]:
            pr = parse_price(s.get("price"))
            if pr:
                priced += 1
                last = pr
        if last:
            last_priced.append(last)
    last_priced.sort()
    med = last_priced[len(last_priced) // 2]
    assert orig == 21, orig
    assert turn == 34, turn
    assert priced == 90, priced
    assert med == 622000, med
    assert orig + turn == 55

    # No invented 1999 sale on lot 16
    assert lots["16"]["sales"][0]["date"] == "2007-08-30"

    # Snapshot exists and covers every PIN
    snap = json.loads((ROOT / "data" / "loudoun-rpi-sales.json").read_text())
    pins = {f["properties"]["pin"] for f in data["features"]}
    assert {p["pin"] for p in snap["parcels"]} == pins
    assert not snap.get("errors")

    print("ok: passwords, 55 lots, 21 originalers, 34 turnovers, 90 priced, median $622,000")


if __name__ == "__main__":
    main()
