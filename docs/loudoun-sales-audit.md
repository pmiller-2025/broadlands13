# Broadlands Section 13 — Loudoun sales history audit

Audited **2026-09-11** against live Loudoun County Real Property Information (RPI) Sales / Transfers pages and Loudoun GIS parcel inventory.

This is a neighbor-shareable reconciliation. It is not a title search. Always confirm a deed with [Loudoun RPI](https://reparcelasmt.loudoun.gov/pt/search/CommonSearch.aspx?mode=PARID) or the Clerk’s land-records index before relying on a name, date, or price.

## How this was checked

1. **Lot inventory** — Loudoun GIS `COL/LandRecordData` parcels where `PA_SUBD_NAME` contains BROADLANDS and `PA_SUBD_SECT='13'`. Every parcel is plat **1998-0187**. Result: **55 numbered house lots + 5 open-space parcels (A–E)**. The map already had exactly those 60 PINs; none missing, none extra.
2. **Sales history** — for each PIN, the official RPI datalet `mode=sales` at `reparcelasmt.loudoun.gov` (date, price, buyer) plus each sale’s detail card (seller, instrument, valuation, notes). Pulled live; nothing invented.
3. **PIN remap** — every Section 13 PIN shows a 2005 parcel-tracking split from parent PIN `156488930000`. That parent is the old developer tract (1994 Broadlands Associates sale), not a per-lot owner history. It does **not** restore missing 1999–2000 house deeds.
4. **Clerk land records (PAX / LandMARC / GIS)** — every public path was tried before treating a lot as still unavailable. LandMARC is permits, not deeds. GIS has no grantor/grantee. Historic indexes stop in 1903. Sales-report downloads start in 2013. The Clerk PAX index at `lisweb.loudoun.gov/paxworld` is the official next step; it requires a free occasional-user account. This audit did **not** create one and did **not** invent originals from Zillow, book numbers, or building permits.

## New totals (55 houses)

| Measure | Previous published (~) | After this audit |
| --- | --- | --- |
| Houses | 55 | **55** |
| Priced sales (RPI, price > $0) | ~90 | **90** |
| Originalers remaining (first deed + later $0/title tweaks only) | — | **21** |
| Turnovers (2nd+ owner era) | ~39 | **34** |
| Median of each house’s last priced sale | ~$622,000 | **$622,000** |

The old “~39 turnovers” treated four lots whose **first recorded deed is $0** (Cervantes, George, Watkins, Jarral) as turnovers. Those $0 first deeds are the first recorded owner and **stay originalers**. Same-day Moran restatement (lot 24, two $492,000 rows, same household) is kept in history but does **not** start a second era.

## What changed in the map data

No priced county rows were missing from the map.

No published house rows contradicted county (no extras to delete).

Lot 24 (Moran) same-day pair is now ordered by instrument (`…022516` then `…022517`). Lot 51 (Hewitt Relocation → Goodwyn, same day) stays two priced eras — different households.

HOA / open space A–E: county records a **1999-01-12 $0** deed to Broadlands Association Inc on each. The map still leaves those parcels as **no-data** so they do not count as houses or originalers.

## Known checks

| Check | County RPI | Map after audit |
| --- | --- | --- |
| Earliest priced house sales | **1999-09-03** Landino 42759 Hollowind ($305,840) and Gordon/Getter 42767 Hollowind ($308,400) | Same. Landino still originalers. Gordon/Getter sold 2020-03-17 ($710,000) — not still originalers. |
| Paul & Jessica Chestnut 42770 Hollowind | 1999-10-19 $268,915; 2021-11-09 $0 trust | Same. Still originalers ($0 does not start a new era). |
| Crisp 21666 Stillbrook Farm | First deed **2000-02-02** $250,658 (closing date on the card); 2017-05-22 $0 trust | Same. Still originalers. |
| Thompson 42734 Hollowind | 1999-09-21 $273,017; 2023-02-14 $0 trust | Same. Still originalers. |

## Lots whose 1999–2000 original priced sale is **not** in Loudoun RPI

A neighbor was right that several original buyers are missing from the **assessment** sales history. RPI simply does not list a 1999–2000 priced first sale on these PINs. This audit **does not invent** those deeds. The first *recorded* RPI deed is what the map uses unless a later clerk-verified original is merged from `data/loudoun-clerk-deeds.json` (that file is empty until PAX returns grantor, grantee, and date).

| Lot | Address | PIN | First RPI deed | Still originaler? | Gap |
| --- | --- | --- | --- | --- | --- |
| 4 | 21662 STILLBROOK FARM DR | 156491719000 | 2002-12-30 $445,000 SICA, ALBERT J & CAROLYN T R/S | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 6 | 21670 STILLBROOK FARM DR | 156491305000 | 2003-09-03 $450,250 HARGENRATER, MARK E & YELENA R R/S | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 7 | 21674 STILLBROOK FARM DR | 156391198000 | 2003-10-02 $488,000 LEE, JEFFREY B & DONNA K R/S | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 8 | 21678 STILLBROOK FARM DR | 156390793000 | 2001-10-30 $395,000 MALONEY, JOSEPH W & JOYANN R | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 11 | 42810 EVENING BREEZE CT | 156392083000 | 2002-04-30 $399,900 TROESTER, DOUGLAS C & KAREN L | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 13 | 42815 EVENING BREEZE CT | 156392566000 | 2005-07-06 $739,500 DZWILEWSKI, PETE G & TRACY J R/S | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 16 | 42803 EVENING BREEZE CT | 156389962000 | 2007-08-30 $585,000 BANKUS, ANDREW KYLE & DAWNA R R/S | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 18 | 42795 EVENING BREEZE CT | 156388062000 | 2001-10-05 $0 CERVANTES, EDWARD R & DEBORAH A | N | first recorded deed is $0 / unpriced (no 1999–2000 priced first sale in RPI) |
| 19 | 42791 EVENING BREEZE CT | 156388471000 | 2001-12-26 $0 GEORGE, JEFFREY A & KELLY R | Y | first recorded deed is $0 / unpriced (no 1999–2000 priced first sale in RPI) |
| 20 | 42787 EVENING BREEZE CT | 156388379000 | 2004-03-30 $595,000 COLANGELO, DAVID A & LISA D | Y | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 22 | 42771 EVENING BREEZE CT | 156387092000 | 2004-11-30 $560,000 FOCHT, ERIC M & TERRI M SCANLAN R/S | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 23 | 42767 EVENING BREEZE CT | 156386392000 | 2004-08-25 $550,000 GRINDER, JOSEPH B II & MICHAELA R/S | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 24 | 42762 EVENING BREEZE CT | 156486214000 | 2004-03-12 $492,000 MORAN, BRIAN R & SHERYL S R/S | Y | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 25 | 42766 EVENING BREEZE CT | 156486915000 | 2002-06-20 $415,000 MURPHY, JOHN P JR & SHARON C | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 28 | 21683 STILLBROOK FARM DR | 156388898000 | 2006-07-28 $635,000 LAMBDIN, TODD & ERICA R/S | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 30 | 21671 STILLBROOK FARM DR | 156489512000 | 2004-02-10 $0 WATKINS, ALAN G | N | first recorded deed is $0 / unpriced (no 1999–2000 priced first sale in RPI) |
| 32 | 42779 HOLLOWIND CT | 156488619000 | 2005-07-15 $685,000 JONNADULA, VASUDEVARAO & SUJATHA | Y | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 36 | 42763 HOLLOWIND CT | 156487042000 | 2004-03-24 $452,000 REDDY, SHAILA | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 42 | 42739 HOLLOWIND CT | 156484850000 | 2001-03-06 $510,500 NELSON, GAYLE J | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 46 | 42742 HOLLOWIND CT | 156486275000 | 2002-04-26 $0 JARRAL, RAVINDER S | N | first recorded deed is $0 / unpriced (no 1999–2000 priced first sale in RPI) |
| 50 | 42758 HOLLOWIND CT | 156488855000 | 2002-02-28 $395,500 ALBERS, EDWARD J & LAURALYN C | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 51 | 42762 HOLLOWIND CT | 156488648000 | 2004-12-06 $603,000 HEWITT RELOCATION SERVICES INC | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |
| 54 | 21651 STILLBROOK FARM DR | 156489840000 | 2002-03-20 $394,900 CLARK, ROBERT W & CAROLYN B | N | first recorded sale is a later resale (no 1999–2000 first sale in RPI) |

## Clerk / deed-index lookup (2026-09-11)

Goal: find the original builder deed (grantor, grantee, date, price if shown, instrument or book/page) for each of the 23 gap lots, and add only what the clerk index actually shows.

**Lots that gained a clerk-verified original on the map: none.** The overlay file `data/loudoun-clerk-deeds.json` has zero rows. Map totals stay at 90 priced sales / 21 originalers / 34 turnovers.

### What was reachable without a login

- **Loudoun RPI Sales / Transfers** — https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx — Current tax year (2026) is the only year that returns sales. Older taxyr values return empty. First-sale seller is blank on every gap lot. Instruments on later sales do not reveal the prior grantor/grantee without PAX.
- **Loudoun RPI profile legal description** — https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx — Public. Yields book--page and/or instrument tokens on the legal line. These are pointers, not grantor/grantee/date/price.
- **Loudoun RPI permits (NEWCON)** — https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?mode=permits — Public. Every gap lot has a 1999 or early-2000 NEWCON permit, so the house existed in the original-sale window. A permit is not a deed and was not added to map sales.
- **Clerk PAX occasional-user index** — https://lisweb.loudoun.gov/paxworld/ — Login wall. Free index after Create Account. Search/API routes without a session return 404. No account was created (would require inventing a personal identity). Stopped this path.
- **Clerk PAX subscription download site** — https://lisweb.loudoun.gov/PAXSubscription/ — Same DTS login wall.
- **Clerk Online Land Records (county page)** — https://www.loudoun.gov/Clerk/OnlineLandRecords — Explains free occasional-user signup and $0.50/page images. Does not expose the index without an account.
- **LandMARC (Tyler EnerGov)** — https://loudouncountyvaeg.tylerhost.net/prod/selfservice — Permits and land-development applications, not the deed index. GIS LMARC/LandMARC_Permits is the same domain.
- **Loudoun GIS LandRecords / LandRecordData / LMIS platfile** — https://logis.loudoun.gov/gis/rest/services — No grantor/grantee/consideration. LMISVPC_PAR_CURR owner-start/sale dates are the current owner, not the 1999 builder.
- **Public Real Estate Sales Reports** — https://www.loudoun.gov/649/Public-Real-Estate-Reports — Downloadable sales reports start 2013. Too late for 1999–2000 builder deeds.
- **Historic deed indexes** — https://www.loudoun.gov/2184/Deeds — PDF indexes 1757–1903 only. FamilySearch / LVA films likewise stop far before 1999.

### Login Paul must do himself

- Start: [https://www.loudoun.gov/Clerk/OnlineLandRecords](https://www.loudoun.gov/Clerk/OnlineLandRecords)
- Create a **free occasional-user account** (your own name) and log in at [https://lisweb.loudoun.gov/paxworld/](https://lisweb.loudoun.gov/paxworld/). Index search is free; images cost $0.50/page plus a convenience fee.
- Manual: [PAX Occasional User guide (PDF)](https://lfportal.loudoun.gov/LFPortalInternet/0/edoc/1960913/DTSPAXOccasionalManual.pdf)
- Or use the free in-person kiosks: Public kiosks, Clerk’s Office, 18 E Market St, Leesburg, Mon–Fri 8:00 a.m.–4:00 p.m. No account needed.
- After you have grantor / grantee / date (and price only if the index shows it), add a row to `data/loudoun-clerk-deeds.json` and re-run `python3 scripts/rebuild_from_loudoun.py`. Do not add a guessed buyer or a date inferred from a book number.

### Best public pointers (not yet deeds)

Lots that already have a 1999–2000 priced first sale in RPI cite deed books **1711–1750** (Landino `1711--539`, Gordon `1711--520`, Thompson `1714--1293`, Paul `1722--977`, Gavva `1741--779`, Crisp `1750--515`). Three gap lots still show a second book/page in that same range on the RPI legal line. That is a **pointer for PAX Book+Page search**, not enough to put a buyer or price on the map.

| Lot | Address | Possible original book/page (pointer only) | Later legal cite | First RPI instrument to cross-ref | NEWCON permit (not a deed) |
| --- | --- | --- | --- | --- | --- |
| 4 | 21662 STILLBROOK FARM DR | — | 200606290056941 | — | 08/12/1999 B00003380100 |
| 6 | 21670 STILLBROOK FARM DR | — | 200309030115377 | 200309030115377 | 08/12/1999 B00003370100 |
| 7 | 21674 STILLBROOK FARM DR | — | 200310020130330 | 200310020130330 | 08/12/1999 B00003410100 |
| 8 | 21678 STILLBROOK FARM DR | — | 2032--1156 | — | 07/26/1999 B00001190100 |
| 11 | 42810 EVENING BREEZE CT | — | 2165--1055 | — | 09/01/1999 B00011960100 |
| 13 | 42815 EVENING BREEZE CT | — | 200703200021104 | 200507060072948 | 06/08/1999 B00062540100 |
| 16 | 42803 EVENING BREEZE CT | — | 200708300064171 | 200708300064171 | 06/08/1999 B00062520100 |
| 18 | 42795 EVENING BREEZE CT | 1746--2101 | 2017--2042 | — | 06/08/1999 B00062510100 |
| 19 | 42791 EVENING BREEZE CT | 1771--919 | 2076--1861 | — | 07/26/1999 B00001260100 |
| 20 | 42787 EVENING BREEZE CT | — | 200403300028789 | 200403300028789 | 07/26/1999 B00001270100 |
| 22 | 42771 EVENING BREEZE CT | — | 200806250039192 | 200411300126959 | 07/26/1999 B00001180100 |
| 23 | 42767 EVENING BREEZE CT | — | 200408250090076 | 200408250090076 | 08/12/1999 B00002570100 |
| 24 | 42762 EVENING BREEZE CT | — | 200403120022516 | 200403120022516 | 08/12/1999 B00003390100 |
| 25 | 42766 EVENING BREEZE CT | — | 2198--1235 | — | 07/26/1999 B00001280100 |
| 28 | 21683 STILLBROOK FARM DR | — | 200607280065235 | 200607280065235 | 01/14/2000 B00046500100 |
| 30 | 21671 STILLBROOK FARM DR | — | 200906290043236, 201112060076260 | 200402100012477 | 11/02/1999 B00035330100 |
| 32 | 42779 HOLLOWIND CT | — | 200507150075985 | 200507150075985 | 06/25/1999 B00065860100 |
| 36 | 42763 HOLLOWIND CT | — | 200412300139341, 200403240026087, 201101030000379 | 200403240026087 | 08/09/1999 B00005000100 |
| 42 | 42739 HOLLOWIND CT | — | 200405260053152 | — | 05/07/1999 B90070030100 |
| 46 | 42742 HOLLOWIND CT | 1769--79 | 2161--425 | — | 11/02/1999 B00035300100 |
| 50 | 42758 HOLLOWIND CT | — | 2122--873 | — | 05/07/1999 B90070080100 |
| 51 | 42762 HOLLOWIND CT | — | 200412060129162 | 200412060129161 | 09/29/1999 B00015820100 |
| 54 | 21651 STILLBROOK FARM DR | — | 2135--2239 | — | 03/17/2000 B10009960100 |

Every one of the 23 gap lots has a **1999 or January–March 2000 NEWCON** permit on the public RPI permits tab, so the house was built in the original-sale window. That does **not** name the first buyer and was not added as a sale.

### Still county-unavailable (all 23)

Until PAX (or a kiosk) returns parties and a recording date, the map keeps using the first RPI deed. Neighbor-facing: these lots do **not** yet show a clerk-proven 1999–2000 originaler.

## Lot-by-lot reconciliation (55 houses)

Columns: original buyer = first RPI deed (priced or $0). Still originaler = only one owner era after skipping later $0 / same-household same-day restatements. County vs map = whether the published card already matched RPI before this audit.

### Lot 1 — 21646 STILLBROOK FARM DR

- PIN `156491637000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156491637000&taxyr=2026)
- Original buyer (first RPI deed): **MILLER, STEVEN R & ELIZABETH A** · 2000-03-27 · $283,684
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-03-27 | $283,684 | MILLER, STEVEN R & ELIZABETH A | — | — | Y #1 | MARKET SALE |
| 2021-10-25 | $800,000 | GAHLOT, ASHWANI SINGH & RATHORE, SUNAINA | MILLER, STEVENS R & MILLER, ELIZABETH A | 202110250108579 | Y #2 | MARKET SALE |

### Lot 2 — 21654 STILLBROOK FARM DR

- PIN `156491327000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156491327000&taxyr=2026)
- Original buyer (first RPI deed): **BANE, CHRISTOPHER S & TAMMY M R/S** · 2000-05-02 · $298,304
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-05-02 | $298,304 | BANE, CHRISTOPHER S & TAMMY M R/S | — | — | Y #1 | MARKET SALE |
| 2009-10-06 | $0 | BANE, CHRISTOPHER S | — | 200910060068173 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 3 — 21658 STILLBROOK FARM DR

- PIN `156492427000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156492427000&taxyr=2026)
- Original buyer (first RPI deed): **BRUNST, GERALD JR & ANNE M** · 2000-03-30 · $305,864
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-03-30 | $305,864 | BRUNST, GERALD JR & ANNE M | — | — | Y #1 | MARKET SALE |
| 2019-12-11 | $0 | BRUNST, ANNE M TR & BRUNST, GERALD JR TR & ANNE MARIE BRUNST & GERALD ROBERT BRUNST JR LIVING TRUST | BRUNST, ANNE M & BRUNST, GERALD JR | 201912110077077 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 4 — 21662 STILLBROOK FARM DR

- PIN `156491719000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156491719000&taxyr=2026)
- Original buyer (first RPI deed): **SICA, ALBERT J & CAROLYN T R/S** · 2002-12-30 · $445,000
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2002-12-30 | $445,000 | SICA, ALBERT J & CAROLYN T R/S | — | — | Y #1 | MARKET SALE |
| 2006-06-29 | $715,000 | YEE, RICHARD & REBECCA | — | 200606290056941 | Y #2 | MARKET SALE |

### Lot 5 — 21666 STILLBROOK FARM DR

- PIN `156491613000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156491613000&taxyr=2026)
- Original buyer (first RPI deed): **CRISP, DANIEL E & KIM D** · 2000-02-02 · $250,658
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-02-02 | $250,658 | CRISP, DANIEL E & KIM D | — | — | Y #1 | MARKET SALE |
| 2017-05-22 | $0 | CRISP, DANIEL E & KIM D TEES | CRISP, DANIEL E & KIM D | 201705220030599 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 6 — 21670 STILLBROOK FARM DR

- PIN `156491305000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156491305000&taxyr=2026)
- Original buyer (first RPI deed): **HARGENRATER, MARK E & YELENA R R/S** · 2003-09-03 · $450,250
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2003-09-03 | $450,250 | HARGENRATER, MARK E & YELENA R R/S | — | 200309030115377 | Y #1 | SALE FOR 5 LOTS |
| 2014-11-05 | $0 | HARGENRATER, MARK E & YELENA R TEES | HARGENRATER, MARK E & YELENA R | 201411050062764 | skip | N/A; $0/unpriced — kept, skipped for eras |
| 2015-03-12 | $0 | HARGENRATER, MARK E & YELENA R | HARGENRATER, MARK E & YELENA R TEES | 201503120014457 | skip | D/G; $0/unpriced — kept, skipped for eras |
| 2022-04-18 | $880,000 | SREEDHAR, SREEJU & SREEJU, ANILA | HARGENRATER, MARK E & HARGENRATER, YELENA R | 202204180022929 | Y #2 | MARKET SALE |

### Lot 7 — 21674 STILLBROOK FARM DR

- PIN `156391198000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156391198000&taxyr=2026)
- Original buyer (first RPI deed): **LEE, JEFFREY B & DONNA K R/S** · 2003-10-02 · $488,000
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2003-10-02 | $488,000 | LEE, JEFFREY B & DONNA K R/S | — | 200310020130330 | Y #1 | MARKET SALE |
| 2012-04-03 | $505,000 | HICKS, JAMES T & KATHRYN N | LEE, JEFFREY B & DONNA K | 201204030024659 | Y #2 | SHORT SALE |
| 2025-03-31 | $0 | HICKS, JAMES T TR & HICKS, KATHRYN N TR & HICKS LIVING TRUST | HICKS, JAMES T & HICKS, KATHRYN N | 202503310013558 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 8 — 21678 STILLBROOK FARM DR

- PIN `156390793000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156390793000&taxyr=2026)
- Original buyer (first RPI deed): **MALONEY, JOSEPH W & JOYANN R** · 2001-10-30 · $395,000
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2001-10-30 | $395,000 | MALONEY, JOSEPH W & JOYANN R | — | — | Y #1 | MARKET SALE |
| 2017-10-16 | $625,000 | SPANGLER, WILLIAM & KATHRYN L | MALONEY, JOSEPH W & JOYANN R | 201710160064647 | Y #2 | MARKET SALE |
| 2024-03-01 | $0 | SPANGLER, WILLIAM A TR & SPANGLER, KATHRYN L TR & SPANGLER FAMILY TRUST | SPANGLER, WILLIAM A & SPANGLER, KATHRYN L | 202403010007785 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 9 — 42790 EVENING BREEZE CT

- PIN `156389888000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156389888000&taxyr=2026)
- Original buyer (first RPI deed): **BEGIN, MICHAEL L & DAWN L** · 2000-02-08 · $321,525
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-02-08 | $321,525 | BEGIN, MICHAEL L & DAWN L | — | — | Y #1 | MARKET SALE |
| 2015-09-22 | $670,000 | PATEL, VIVEK & PRIYANKA MIRSI | BEGIN, MICHAEL L & DAWN L | 201509220064115 | Y #2 | MARKET SALE |
| 2018-02-01 | $0 | PATEL, VIVEK & PRIYANKA MISRI | PATEL, VIVEK & PRIYANKA MIRSI | 201802010006137 | skip | D/C CORRECTS SPELLING OF GRANTEE'S NAME; $0/unpriced — kept, skipped for eras |
| 2019-07-15 | $0 | PATEL, PRIYANKA M TR & PATEL, VIVEK A TR & PRIYANKA & VIVEK PATEL FAMILY TRUST | PATEL, VIVEK A & PATEL, PRIYANKA M | 201907150038562 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 10 — 42806 EVENING BREEZE CT

- PIN `156391284000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156391284000&taxyr=2026)
- Original buyer (first RPI deed): **CORBETT, DOUGLAS R & CHERYL ANN** · 2000-03-09 · $310,530
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-03-09 | $310,530 | CORBETT, DOUGLAS R & CHERYL ANN | — | — | Y #1 | MARKET SALE |
| 2020-12-30 | $0 | CORBETT, CHERYL ANN | CORBETT, DOUGLAS R & CORBETT, CHERYL ANN | 202012300129018 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 11 — 42810 EVENING BREEZE CT

- PIN `156392083000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156392083000&taxyr=2026)
- Original buyer (first RPI deed): **TROESTER, DOUGLAS C & KAREN L** · 2002-04-30 · $399,900
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2002-04-30 | $399,900 | TROESTER, DOUGLAS C & KAREN L | — | — | Y #1 | MARKET SALE |
| 2016-06-17 | $625,000 | TRUMPOWER, TODD & RACHELLE MCCULLOUGH | TROESTER, DOUGLAS C & KAREN L | 201606170037318 | Y #2 | MARKET SALE |
| 2025-01-14 | $0 | TRUMPOWER, TODD A TR & TODD A TRUMPOWER LIVING TRUST | TRUMPOWER, RACHELLE & MCCULLOUGH, RACHELLE & TRUMPOWER, TODD | 202501140001952 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 12 — 42814 EVENING BREEZE CT

- PIN `156392879000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156392879000&taxyr=2026)
- Original buyer (first RPI deed): **VINCENT, ALEX & DIANE S** · 2000-04-03 · $247,485
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-04-03 | $247,485 | VINCENT, ALEX & DIANE S | — | — | Y #1 | MARKET SALE |
| 2024-11-22 | $0 | VINCENT, ALEX HINMAN TR & VINCENT, DIANE SETTLAGE TR & ALEX & DIANE VINCENT LIVING TRUST | VINCENT, ALEX HINMAN & VINCENT, DIANE SETTLAGE | 202411220050670 | skip | N/A; $0/unpriced — kept, skipped for eras |
| 2025-01-09 | $0 | VINCENT, ALEX HINMAN TR & VINCENT, DIANE SETTLAGE TR & ALEX & DIANE VINCENT LIVING TRUST | VINCENT, ALEX HINMAN & VINCENT, DIANE SETTLAGE | 202501090001220 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 13 — 42815 EVENING BREEZE CT

- PIN `156392566000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156392566000&taxyr=2026)
- Original buyer (first RPI deed): **DZWILEWSKI, PETE G & TRACY J R/S** · 2005-07-06 · $739,500
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2005-07-06 | $739,500 | DZWILEWSKI, PETE G & TRACY J R/S | — | 200507060072948 | Y #1 | MARKET SALE |
| 2007-03-20 | $622,000 | MESSNER, THOMAS J & LISA B | — | 200703200021104 | Y #2 | MARKET SALE |

### Lot 14 — 42811 EVENING BREEZE CT

- PIN `156391467000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156391467000&taxyr=2026)
- Original buyer (first RPI deed): **RAGLAND, DAVID M & C L CAMPBELL** · 2000-03-13 · $275,745
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-03-13 | $275,745 | RAGLAND, DAVID M & C L CAMPBELL | — | — | Y #1 | MARKET SALE |
| 2014-01-24 | $0 | CAMPBELL, CYNDI L | RAGLAND, DAVID M & C L CAMPBELL | 201401240004030 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 15 — 42807 EVENING BREEZE CT

- PIN `156390667000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156390667000&taxyr=2026)
- Original buyer (first RPI deed): **CLEMENT, PAUL E SR & CLAUDIA P** · 2000-05-01 · $264,181
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-05-01 | $264,181 | CLEMENT, PAUL E SR & CLAUDIA P | — | — | Y #1 | MARKET SALE |

### Lot 16 — 42803 EVENING BREEZE CT

- PIN `156389962000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156389962000&taxyr=2026)
- Original buyer (first RPI deed): **BANKUS, ANDREW KYLE & DAWNA R R/S** · 2007-08-30 · $585,000
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2007-08-30 | $585,000 | BANKUS, ANDREW KYLE & DAWNA R R/S | — | 200708300064171 | Y #1 | MARKET SALE |
| 2021-10-26 | $882,000 | PANDYA, BHAVIK TUSHAR & SINGH, MALVIKA VIJAYBAHADUR | BANKUS, ANDREW KYLE & BANKUS, DAWNA RAE | 202110260109284 | Y #2 | MARKET SALE |

### Lot 17 — 42799 EVENING BREEZE CT

- PIN `156388958000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156388958000&taxyr=2026)
- Original buyer (first RPI deed): **VIPPA, SRINIVAS & PALLAVI PENDUM** · 2000-04-04 · $296,338
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-04-04 | $296,338 | VIPPA, SRINIVAS & PALLAVI PENDUM | — | — | Y #1 | MARKET SALE |

### Lot 18 — 42795 EVENING BREEZE CT

- PIN `156388062000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156388062000&taxyr=2026)
- Original buyer (first RPI deed): **CERVANTES, EDWARD R & DEBORAH A** · 2001-10-05 · $0
- Still originaler: **N** · owner eras 2 · priced sales 1
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded deed is $0 / unpriced (no 1999–2000 priced first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2001-10-05 | $0 | CERVANTES, EDWARD R & DEBORAH A | — | — | Y #1 | N/A; $0 first deed — starts originaler era |
| 2021-10-28 | $810,000 | WHEATON, BRIAN & WHEATON, MEGAN | CERVANTES, EDWARD R & CERVANTES, DEBORAH A | 202110280110191 | Y #2 | UNABLE TO VERIFY |

### Lot 19 — 42791 EVENING BREEZE CT

- PIN `156388471000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156388471000&taxyr=2026)
- Original buyer (first RPI deed): **GEORGE, JEFFREY A & KELLY R** · 2001-12-26 · $0
- Still originaler: **Y** · owner eras 1 · priced sales 0
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded deed is $0 / unpriced (no 1999–2000 priced first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2001-12-26 | $0 | GEORGE, JEFFREY A & KELLY R | — | — | Y #1 | N/A; $0 first deed — starts originaler era |

### Lot 20 — 42787 EVENING BREEZE CT

- PIN `156388379000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156388379000&taxyr=2026)
- Original buyer (first RPI deed): **COLANGELO, DAVID A & LISA D** · 2004-03-30 · $595,000
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2004-03-30 | $595,000 | COLANGELO, DAVID A & LISA D | — | 200403300028789 | Y #1 | MARKET SALE |

### Lot 21 — 42779 EVENING BREEZE CT

- PIN `156387886000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156387886000&taxyr=2026)
- Original buyer (first RPI deed): **LINTELMAN, GILBERT & DEBORAH R/S** · 2000-04-06 · $238,645
- Still originaler: **N** · owner eras 3 · priced sales 3
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-04-06 | $238,645 | LINTELMAN, GILBERT & DEBORAH R/S | — | — | Y #1 | MARKET SALE |
| 2009-12-29 | $470,000 | RODRIGUEZ, BARBARA & P CRUNKLETON | — | 200912290085637 | Y #2 | MARKET SALE |
| 2020-08-18 | $0 | RODRIGUEZ, BARBARA E | RODRIGUEZ, BARBARA E & CRUNKLETON, PATRICK E | 202008180070225 | skip | N/A; $0/unpriced — kept, skipped for eras |
| 2023-12-01 | $895,000 | CHAVAN, SIDDHESH & BHOR, DIPEEKA GULAB | RODRIGUEZ, BARBARA E | 202312010047888 | Y #3 | MARKET SALE |

### Lot 22 — 42771 EVENING BREEZE CT

- PIN `156387092000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156387092000&taxyr=2026)
- Original buyer (first RPI deed): **FOCHT, ERIC M & TERRI M SCANLAN R/S** · 2004-11-30 · $560,000
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2004-11-30 | $560,000 | FOCHT, ERIC M & TERRI M SCANLAN R/S | — | 200411300126959 | Y #1 | MARKET SALE |
| 2008-06-25 | $515,000 | BURCH, SEAN A & ERIN P | — | 200806250039192 | Y #2 | MARKET SALE |

### Lot 23 — 42767 EVENING BREEZE CT

- PIN `156386392000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156386392000&taxyr=2026)
- Original buyer (first RPI deed): **GRINDER, JOSEPH B II & MICHAELA R/S** · 2004-08-25 · $550,000
- Still originaler: **N** · owner eras 3 · priced sales 3
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2004-08-25 | $550,000 | GRINDER, JOSEPH B II & MICHAELA R/S | — | 200408250090076 | Y #1 | MARKET SALE |
| 2015-06-08 | $605,000 | LAKE, TARA SANTELLA & JESSE KYLE | GRINDER, JOSEPH B II & MICHAELA | 201506080036941 | Y #2 | MARKET SALE |
| 2015-07-09 | $0 | LAKE, TARA SANTELLA & JESSE KYLE | LAKE, TARA SANTELLA & JESSE KYLE | 201507090046052 | skip | D/C TO CORRECT LEGAL; $0/unpriced — kept, skipped for eras |
| 2022-03-22 | $925,000 | ALAM, IMTIAZ M & HAIDER, SHARMEEN F | LAKE, TARA SANTELLA & LAKE, JESSE KYLE | 202203220017175 | Y #3 | UNABLE TO VERIFY |
| 2026-03-20 | $0 | ALAM, IMTIAZ MUHAMMAD TR & HAIDER, SHARMEEN FATIMA TR & SHARMEEN F HAIDER LIVING TRUST & ALAM LIVING TRUST | ALAM, IMTIAZ M & HAIDER, SHARMEEN F | 202603200013812 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 24 — 42762 EVENING BREEZE CT

- PIN `156486214000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156486214000&taxyr=2026)
- Original buyer (first RPI deed): **MORAN, BRIAN R & SHERYL S R/S** · 2004-03-12 · $492,000
- Still originaler: **Y** · owner eras 1 · priced sales 2
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2004-03-12 | $492,000 | MORAN, BRIAN R & SHERYL S R/S | — | 200403120022516 | Y #1 | MARKET SALE |
| 2004-03-12 | $492,000 | MORAN, BRIAN R & SHERYL S | — | 200403120022517 | skip | MARKET SALE |

### Lot 25 — 42766 EVENING BREEZE CT

- PIN `156486915000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156486915000&taxyr=2026)
- Original buyer (first RPI deed): **MURPHY, JOHN P JR & SHARON C** · 2002-06-20 · $415,000
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2002-06-20 | $415,000 | MURPHY, JOHN P JR & SHARON C | — | — | Y #1 | MARKET SALE |
| 2022-06-06 | $897,500 | EDWIN, PRABHU STEWARD & SAM, RUTH | MURPHY, JOHN P JR & MURPHY, SHARON C | 202206060033612 | Y #2 | MARKET SALE |

### Lot 26 — 42770 EVENING BREEZE CT

- PIN `156487612000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156487612000&taxyr=2026)
- Original buyer (first RPI deed): **REID, DAVID & BARBARA** · 2000-02-02 · $257,691
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-02-02 | $257,691 | REID, DAVID & BARBARA | — | — | Y #1 | MARKET SALE |
| 2024-05-17 | $0 | REID, DAVID A TR & REID, BARBARA E TR & REID FAMILY LIVING TRUST | REID, DAVID & REID, BARBARA | 202405170020002 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 27 — 42774 EVENING BREEZE CT

- PIN `156488207000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156488207000&taxyr=2026)
- Original buyer (first RPI deed): **QU, YUJIANG, & YING HUANG** · 2000-03-30 · $239,971
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-03-30 | $239,971 | QU, YUJIANG, & YING HUANG | — | — | Y #1 | MARKET SALE |
| 2025-09-25 | $0 | QU, YUJIANG TR & HUANG, YING TR & QU FAMILY LIVING TRUST | QU, YUJIANG & HUANG, YING | 202509250046369 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 28 — 21683 STILLBROOK FARM DR

- PIN `156388898000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156388898000&taxyr=2026)
- Original buyer (first RPI deed): **LAMBDIN, TODD & ERICA R/S** · 2006-07-28 · $635,000
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2006-07-28 | $635,000 | LAMBDIN, TODD & ERICA R/S | — | 200607280065235 | Y #1 | MARKET SALE |
| 2021-10-25 | $850,000 | NERGUI, TAMIR & PUREVDAVAA, BAIGAL | LAMBDIN, TODD & LAMBDIN, ERICA | 202110250108701 | Y #2 | MARKET SALE |

### Lot 29 — 21679 STILLBROOK FARM DR

- PIN `156489404000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156489404000&taxyr=2026)
- Original buyer (first RPI deed): **CONNORS, GEORGE J & STACY A** · 2000-05-03 · $303,030
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-05-03 | $303,030 | CONNORS, GEORGE J & STACY A | — | — | Y #1 | MARKET SALE |
| 2021-03-29 | $0 | CONNORS, STACY A TR & CONNORS, GEORGE J TR & CONNORS LIVING TRUST | CONNORS, GEORGE J & CONNORS, STACY A | 202103290036939 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 30 — 21671 STILLBROOK FARM DR

- PIN `156489512000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156489512000&taxyr=2026)
- Original buyer (first RPI deed): **WATKINS, ALAN G** · 2004-02-10 · $0
- Still originaler: **N** · owner eras 2 · priced sales 1
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded deed is $0 / unpriced (no 1999–2000 priced first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2004-02-10 | $0 | WATKINS, ALAN G | — | 200402100012477 | Y #1 | N/A; $0 first deed — starts originaler era |
| 2009-06-29 | $510,000 | KUNC, DOUGLAS E & KAREN STEFFEL J/T | — | 200906290043236 | Y #2 | MARKET SALE |
| 2011-12-06 | $0 | KUNC, DOUGLAS E & KAREN STEFFEL | — | 201112060076260 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 31 — 21663 STILLBROOK FARM DR

- PIN `156489619000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156489619000&taxyr=2026)
- Original buyer (first RPI deed): **GAVVA, SANTOSH R & VINITHA R** · 1999-12-28 · $269,200
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1999-12-28 | $269,200 | GAVVA, SANTOSH R & VINITHA R | — | — | Y #1 | MARKET SALE |
| 2016-06-01 | $0 | GAVVA, VINITHA R | GAVVA, SANTOSH R & VINITHA R | 201606010032918 | skip | WILL; $0/unpriced — kept, skipped for eras |

### Lot 32 — 42779 HOLLOWIND CT

- PIN `156488619000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156488619000&taxyr=2026)
- Original buyer (first RPI deed): **JONNADULA, VASUDEVARAO & SUJATHA** · 2005-07-15 · $685,000
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2005-07-15 | $685,000 | JONNADULA, VASUDEVARAO & SUJATHA | — | 200507150075985 | Y #1 | MARKET SALE |

### Lot 33 — 42775 HOLLOWIND CT

- PIN `156488023000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156488023000&taxyr=2026)
- Original buyer (first RPI deed): **MOLTHEN, DANIEL B & CAROLINE E** · 2000-02-01 · $278,530
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-02-01 | $278,530 | MOLTHEN, DANIEL B & CAROLINE E | — | — | Y #1 | MARKET SALE |
| 2016-04-29 | $625,000 | FINN, DANIEL M & MARIA E | MOLTHEN, DANIEL B & CAROLINE E | 201604290024964 | Y #2 | MARKET SALE |

### Lot 34 — 42771 HOLLOWIND CT

- PIN `156487428000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156487428000&taxyr=2026)
- Original buyer (first RPI deed): **SORBERA, JOSEPH A & L MARGARET** · 1999-10-21 · $276,570
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1999-10-21 | $276,570 | SORBERA, JOSEPH A & L MARGARET | — | — | Y #1 | MARKET SALE |
| 2016-07-05 | $624,950 | LANG, JULIA M & NICHOLAS R | SORBERA, JOSEPH A & L MARGARET | 201607050041538 | Y #2 | MARKET SALE |

### Lot 35 — 42767 HOLLOWIND CT

- PIN `156487235000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156487235000&taxyr=2026)
- Original buyer (first RPI deed): **GORDON, STEVEN C & SANDRA GETTER** · 1999-09-03 · $308,400
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1999-09-03 | $308,400 | GORDON, STEVEN C & SANDRA GETTER | — | — | Y #1 | MARKET SALE |
| 2020-03-17 | $710,000 | SMITH, MICHAEL & CLAY, KELLY | GORDON, STEVEN CRAIG & GORDON, SANDRA PAIGE & GETTER, SANDRA PAIGE | 202003170018316 | Y #2 | MARKET SALE |

### Lot 36 — 42763 HOLLOWIND CT

- PIN `156487042000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156487042000&taxyr=2026)
- Original buyer (first RPI deed): **REDDY, SHAILA** · 2004-03-24 · $452,000
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2004-03-24 | $452,000 | REDDY, SHAILA | — | 200403240026087 | Y #1 | MARKET SALE |
| 2004-12-30 | $0 | REDDY, SHAILA & CHRIS MILL TRUSTEES | — | 200412300139341 | skip | N/A; $0/unpriced — kept, skipped for eras |
| 2011-01-03 | $0 | REDDY, SHAILA & CHRIS MILL TRUSTEES | — | 201101030000379 | skip | N/A; $0/unpriced — kept, skipped for eras |
| 2018-07-09 | $622,000 | KONA, RAVIKANTH & VADIYALA, SHALINI | REDDY, SHAILA & CHRIS MILL TRUSTEES | 201807090039230 | Y #2 | MARKET SALE |

### Lot 37 — 42759 HOLLOWIND CT

- PIN `156486950000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156486950000&taxyr=2026)
- Original buyer (first RPI deed): **LANDINO, JOSEPH JR & KATHERINE** · 1999-09-03 · $305,840
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1999-09-03 | $305,840 | LANDINO, JOSEPH JR & KATHERINE | — | — | Y #1 | MARKET SALE |

### Lot 38 — 42754 EVENING BREEZE CT

- PIN `156485621000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156485621000&taxyr=2026)
- Original buyer (first RPI deed): **PHILLIPS, JEFF R & KAREN M** · 2000-02-29 · $280,617
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-02-29 | $280,617 | PHILLIPS, JEFF R & KAREN M | — | — | Y #1 | MARKET SALE |
| 2019-07-17 | $669,000 | JEFFRIES, JAMES DAVID & JEFFRIES, RACHEL ANNETTE | PHILLIPS, JEFF R & PHILLIPS, KAREN M | 201907170039569 | Y #2 | MARKET SALE |

### Lot 39 — 42750 EVENING BREEZE CT

- PIN `156485729000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156485729000&taxyr=2026)
- Original buyer (first RPI deed): **TERCERO, RAFAEL E** · 2000-03-02 · $270,444
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-03-02 | $270,444 | TERCERO, RAFAEL E | — | — | Y #1 | MARKET SALE |
| 2017-01-11 | $0 | TERCERO, NICHOLAS C & RAFAEL D S TERCERO | TERCERO, RAFAEL E | 201701110002054 | skip | WILL; $0/unpriced — kept, skipped for eras |
| 2019-10-30 | $541,500 | LEWIS, OLDRINE GEORGE | TERCERO, NICHOLAS C & RAFAEL D S TERCERO | 201910300066905 | Y #2 | FORECLOSURE |

### Lot 40 — 42747 HOLLOWIND CT

- PIN `156485235000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156485235000&taxyr=2026)
- Original buyer (first RPI deed): **STEPHENSON, JOHN & LORINE BRYANT** · 1999-11-03 · $314,260
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1999-11-03 | $314,260 | STEPHENSON, JOHN & LORINE BRYANT | — | — | Y #1 | MARKET SALE |
| 2023-03-21 | $0 | STEPHENSON, JOHN ANDREW TR & JOHN A STEPHENSON TRUST | STEPHENSON, JOHN A & STEPHENSON, JOHN ANDREW | 202303210010071 | skip | N/A; $0/unpriced — kept, skipped for eras |
| 2025-08-21 | $1,075,013 | BARRY, HENRY ALEXANDER & BARRY, KATHERINE COLLINS | STEPHENSON, JOHN ANDREW TR & JOHN A STEPHENSON TRUST & STEPHENSON, JOHN A TR | 202508210040082 | Y #2 | MARKET SALE |

### Lot 41 — 42743 HOLLOWIND CT

- PIN `156484642000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156484642000&taxyr=2026)
- Original buyer (first RPI deed): **LUZIER, DAVID A & JENNIFER L** · 1999-10-05 · $288,870
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1999-10-05 | $288,870 | LUZIER, DAVID A & JENNIFER L | — | — | Y #1 | MARKET SALE |
| 2012-11-19 | $526,000 | KERR, JAMES & TANYA | LUZIER, DAVID A & JENNIFER L | 201211190091143 | Y #2 | UNABLE TO VERIFY |

### Lot 42 — 42739 HOLLOWIND CT

- PIN `156484850000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156484850000&taxyr=2026)
- Original buyer (first RPI deed): **NELSON, GAYLE J** · 2001-03-06 · $510,500
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2001-03-06 | $510,500 | NELSON, GAYLE J | — | — | Y #1 | MARKET SALE |
| 2004-05-26 | $599,900 | GORDON, DAVID B & EILEEN M KING | — | 200405260053152 | Y #2 | MARKET SALE |

### Lot 43 — 42735 HOLLOWIND CT

- PIN `156484958000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156484958000&taxyr=2026)
- Original buyer (first RPI deed): **HORNBECK, BRIAN D & ERIN B** · 1999-10-08 · $300,190
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1999-10-08 | $300,190 | HORNBECK, BRIAN D & ERIN B | — | — | Y #1 | MARKET SALE |

### Lot 44 — 42734 HOLLOWIND CT

- PIN `156484987000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156484987000&taxyr=2026)
- Original buyer (first RPI deed): **THOMPSON, RAYMOND M JR & KARYN E** · 1999-09-21 · $273,017
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1999-09-21 | $273,017 | THOMPSON, RAYMOND M JR & KARYN E | — | — | Y #1 | MARKET SALE |
| 2023-02-14 | $0 | THOMPSON, RAYMOND M JR TR & THOMPSON, KARYN TR & RAYMOND & KARYN TRUST | THOMPSON, RAYMOND M JR & THOMPSON, KARYN & THOMPSON, KARYN E | 202302140005511 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 45 — 42738 HOLLOWIND CT

- PIN `156485780000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156485780000&taxyr=2026)
- Original buyer (first RPI deed): **GARRITY, SCOTT T & CHRISTINE C** · 2000-06-06 · $277,395
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-06-06 | $277,395 | GARRITY, SCOTT T & CHRISTINE C | — | — | Y #1 | MARKET SALE |
| 2024-12-05 | $915,000 | WILLIAMS, BENJAMIN J & WILLIAMS, TIFFANY | GARRITY, SCOTT T & GARRITY, CHRISTINE C | 202412050052356 | Y #2 | MARKET SALE |

### Lot 46 — 42742 HOLLOWIND CT

- PIN `156486275000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156486275000&taxyr=2026)
- Original buyer (first RPI deed): **JARRAL, RAVINDER S** · 2002-04-26 · $0
- Still originaler: **N** · owner eras 2 · priced sales 1
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded deed is $0 / unpriced (no 1999–2000 priced first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2002-04-26 | $0 | JARRAL, RAVINDER S | — | — | Y #1 | N/A; $0 first deed — starts originaler era |
| 2019-06-11 | $655,000 | CARTER, SCOTT & PARTHREE, LESLEY | JARRAL, RAVINDER S | 201906110030858 | Y #2 | MARKET SALE |

### Lot 47 — 42746 HOLLOWIND CT

- PIN `156487071000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156487071000&taxyr=2026)
- Original buyer (first RPI deed): **CAULFIELD, WILLIAM R III & JOANN** · 2000-01-31 · $273,550
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-01-31 | $273,550 | CAULFIELD, WILLIAM R III & JOANN | — | — | Y #1 | MARKET SALE |
| 2023-07-24 | $0 | CAULFIELD, JOANN MARIE TR & CAULFIELD, WILLIAM RUSSELL III TR & WILLIAM & JOANN CAULFIELD LIVING TRUST | CAULFIELD, WILLIAM R III & CAULFIELD, JOANN M | 202307240028931 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 48 — 42750 HOLLOWIND CT

- PIN `156487666000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156487666000&taxyr=2026)
- Original buyer (first RPI deed): **CONWAY, JOSEPH W & LISA M** · 2000-02-24 · $318,775
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-02-24 | $318,775 | CONWAY, JOSEPH W & LISA M | — | — | Y #1 | MARKET SALE |
| 2026-05-11 | $1,175,000 | BARKSDALE, LORAINNE RAMOS & BARKSDALE, CHRISTOPHER DUANE | CONWAY, JOSEPH W & CONWAY, LISA M | 202605110024329 | Y #2 | MARKET SALE |

### Lot 49 — 42754 HOLLOWIND CT

- PIN `156488261000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156488261000&taxyr=2026)
- Original buyer (first RPI deed): **FLOWERS, BARRY WAYNE & ANGELA E** · 1999-11-08 · $304,685
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1999-11-08 | $304,685 | FLOWERS, BARRY WAYNE & ANGELA E | — | — | Y #1 | MARKET SALE |
| 2014-07-01 | $0 | FLOWERS, ANGELA EVERETT TEE | FLOWERS, BARRY WAYNE & ANGELA E | 201407010035663 | skip | N/A; $0/unpriced — kept, skipped for eras |
| 2025-04-30 | $1,075,000 | LI, HUI & LI, RUI | FLOWERS, ANGELA EVERETT TR & ANGELA EVERETT FLOWERS TRUST | 202504300019208 | Y #2 | MARKET SALE |

### Lot 50 — 42758 HOLLOWIND CT

- PIN `156488855000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156488855000&taxyr=2026)
- Original buyer (first RPI deed): **ALBERS, EDWARD J & LAURALYN C** · 2002-02-28 · $395,500
- Still originaler: **N** · owner eras 3 · priced sales 3
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2002-02-28 | $395,500 | ALBERS, EDWARD J & LAURALYN C | — | — | Y #1 | MARKET SALE |
| 2018-06-05 | $665,000 | KILGANNON, MICHAEL & LINDSEY | ALBERS, EDWARD J & LAURALYN C | 201806050031653 | Y #2 | MARKET SALE |
| 2021-05-26 | $907,775 | KIRKLAND, KERREE & KIRKLAND, SCOTT | KILGANNON, MICHAEL & KILGANNON, LINDSEY | 202105260059925 | Y #3 | MARKET SALE |

### Lot 51 — 42762 HOLLOWIND CT

- PIN `156488648000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156488648000&taxyr=2026)
- Original buyer (first RPI deed): **HEWITT RELOCATION SERVICES INC** · 2004-12-06 · $603,000
- Still originaler: **N** · owner eras 3 · priced sales 3
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2004-12-06 | $603,000 | HEWITT RELOCATION SERVICES INC | — | 200412060129161 | Y #1 | MARKET SALE |
| 2004-12-06 | $603,000 | GOODWYN, RICHARD W & LORRIE L R/S | — | 200412060129162 | Y #2 | MARKET SALE |
| 2021-07-29 | $875,000 | DARAB, ELIZABETH & DARAB, IBRAHEEM | GOODWYN, RICHARD W & GOODWYN, LORRIE L | 202107290081547 | Y #3 | MARKET SALE |

### Lot 52 — 42770 HOLLOWIND CT

- PIN `156488740000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156488740000&taxyr=2026)
- Original buyer (first RPI deed): **MILLER, PAUL & JESSICA CHESTNUT** · 1999-10-19 · $268,915
- Still originaler: **Y** · owner eras 1 · priced sales 1
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1999-10-19 | $268,915 | MILLER, PAUL & JESSICA CHESTNUT | — | — | Y #1 | MARKET SALE |
| 2021-11-09 | $0 | MILLER, PAUL D TR & CHESTNUT, JESSICA L TR & PAUL D MILLER REVOCABLE TRUST & JESSICA L CHESTNUT REVOCABLE TRUST | MILLER, PAUL D & CHESTNUT, JESSICA L | 202111090113307 | skip | N/A; $0/unpriced — kept, skipped for eras |

### Lot 53 — 21655 STILLBROOK FARM DR

- PIN `156489633000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156489633000&taxyr=2026)
- Original buyer (first RPI deed): **FRITZ, JOHN & KAREN D** · 2000-03-24 · $293,030
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-03-24 | $293,030 | FRITZ, JOHN & KAREN D | — | — | Y #1 | MARKET SALE |
| 2013-01-22 | $559,900 | COLVIN, BRADFORD & WENDY SCHAFER-COLVIN | FRITZ, JOHN & KAREN D | 201301220006274 | Y #2 | NEED D/C, NO LEGAL |

### Lot 54 — 21651 STILLBROOK FARM DR

- PIN `156489840000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156489840000&taxyr=2026)
- Original buyer (first RPI deed): **CLARK, ROBERT W & CAROLYN B** · 2002-03-20 · $394,900
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: matched county; original 1999–2000 priced sale not in RPI
- County gap: first recorded sale is a later resale (no 1999–2000 first sale in RPI)
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2002-03-20 | $394,900 | CLARK, ROBERT W & CAROLYN B | — | — | Y #1 | MARKET SALE |
| 2021-02-04 | $0 | CLARK, ROBERT | CLARK, ROBERT W & CAROLYN B | 202102040014471 | skip | WILL; $0/unpriced — kept, skipped for eras |
| 2021-03-03 | $0 | CLARK, ROBERT WINSLOW TR & ROBERT WINSLOW CLARK LIVING TRUST | CLARK, ROBERT W | 202103030025657 | skip | N/A; $0/unpriced — kept, skipped for eras |
| 2024-08-29 | $1,000,000 | HANK, LINDSAY CAMPBELL KENIN & HANK, PAUL LEE | CLARK, ROBERT WINSLOW TR & ROBERT WINSLOW CLARK LIVING TRUST | 202408290036831 | Y #2 | MARKET SALE |

### Lot 55 — 21647 STILLBROOK FARM DR

- PIN `156489646000` · [RPI sales](https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=156489646000&taxyr=2026)
- Original buyer (first RPI deed): **MOHAN, SANDESH & NAMRATA** · 2000-01-21 · $308,500
- Still originaler: **N** · owner eras 2 · priced sales 2
- Status: already matched county
- County / map history (oldest first):

| Date | Price | Buyer | Seller (RPI) | Instrument | Era? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2000-01-21 | $308,500 | MOHAN, SANDESH & NAMRATA | — | — | Y #1 | MARKET SALE |
| 2020-08-25 | $825,000 | ABRAHAM, PAUL JOSEPH & ABRAHAM, LISA SHAIA | MOHAN, SANDESH & MOHAN, NAMRATA | 202008250073527 | Y #2 | MARKET SALE |

## Open-space parcels (not houses)

| Parcel | PIN | County first deed | Map |
| --- | --- | --- | --- |
| A | 156487178000 | 1999-01-12 $0 Broadlands Association Inc | left as no-data (not a house) |
| B | 156492339000 | 1999-01-12 $0 Broadlands Association Inc | left as no-data (not a house) |
| C | 156484702000 | 1999-01-12 $0 Broadlands Association Inc | left as no-data (not a house) |
| D | 156486433000 | 1999-01-12 $0 Broadlands Association Inc | left as no-data (not a house) |
| E | 156485167000 | 1999-01-12 $0 Broadlands Association Inc | left as no-data (not a house) |

## $0 / trust / title rows (kept, skipped for later eras)

| Lot | Address | Date | Buyer | Instrument |
| --- | --- | --- | --- | --- |
| 14 | 42811 EVENING BREEZE CT | 2014-01-24 | CAMPBELL, CYNDI L | 201401240004030 |
| 12 | 42814 EVENING BREEZE CT | 2024-11-22 | VINCENT, ALEX HINMAN TR & VINCENT, DIANE SETTLAGE TR & ALEX & DIANE VINCENT LIVING TRUST | 202411220050670 |
| 12 | 42814 EVENING BREEZE CT | 2025-01-09 | VINCENT, ALEX HINMAN TR & VINCENT, DIANE SETTLAGE TR & ALEX & DIANE VINCENT LIVING TRUST | 202501090001220 |
| 11 | 42810 EVENING BREEZE CT | 2025-01-14 | TRUMPOWER, TODD A TR & TODD A TRUMPOWER LIVING TRUST | 202501140001952 |
| 10 | 42806 EVENING BREEZE CT | 2020-12-30 | CORBETT, CHERYL ANN | 202012300129018 |
| 9 | 42790 EVENING BREEZE CT | 2018-02-01 | PATEL, VIVEK & PRIYANKA MISRI | 201802010006137 |
| 9 | 42790 EVENING BREEZE CT | 2019-07-15 | PATEL, PRIYANKA M TR & PATEL, VIVEK A TR & PRIYANKA & VIVEK PATEL FAMILY TRUST | 201907150038562 |
| 21 | 42779 EVENING BREEZE CT | 2020-08-18 | RODRIGUEZ, BARBARA E | 202008180070225 |
| 8 | 21678 STILLBROOK FARM DR | 2024-03-01 | SPANGLER, WILLIAM A TR & SPANGLER, KATHRYN L TR & SPANGLER FAMILY TRUST | 202403010007785 |
| 23 | 42767 EVENING BREEZE CT | 2015-07-09 | LAKE, TARA SANTELLA & JESSE KYLE | 201507090046052 |
| 23 | 42767 EVENING BREEZE CT | 2026-03-20 | ALAM, IMTIAZ MUHAMMAD TR & HAIDER, SHARMEEN FATIMA TR & SHARMEEN F HAIDER LIVING TRUST & ALAM LIVING TRUST | 202603200013812 |
| 7 | 21674 STILLBROOK FARM DR | 2025-03-31 | HICKS, JAMES T TR & HICKS, KATHRYN N TR & HICKS LIVING TRUST | 202503310013558 |
| 29 | 21679 STILLBROOK FARM DR | 2021-03-29 | CONNORS, STACY A TR & CONNORS, GEORGE J TR & CONNORS LIVING TRUST | 202103290036939 |
| 6 | 21670 STILLBROOK FARM DR | 2014-11-05 | HARGENRATER, MARK E & YELENA R TEES | 201411050062764 |
| 6 | 21670 STILLBROOK FARM DR | 2015-03-12 | HARGENRATER, MARK E & YELENA R | 201503120014457 |
| 30 | 21671 STILLBROOK FARM DR | 2011-12-06 | KUNC, DOUGLAS E & KAREN STEFFEL | 201112060076260 |
| 27 | 42774 EVENING BREEZE CT | 2025-09-25 | QU, YUJIANG TR & HUANG, YING TR & QU FAMILY LIVING TRUST | 202509250046369 |
| 5 | 21666 STILLBROOK FARM DR | 2017-05-22 | CRISP, DANIEL E & KIM D TEES | 201705220030599 |
| 26 | 42770 EVENING BREEZE CT | 2024-05-17 | REID, DAVID A TR & REID, BARBARA E TR & REID FAMILY LIVING TRUST | 202405170020002 |
| 31 | 21663 STILLBROOK FARM DR | 2016-06-01 | GAVVA, VINITHA R | 201606010032918 |
| 2 | 21654 STILLBROOK FARM DR | 2009-10-06 | BANE, CHRISTOPHER S | 200910060068173 |
| 39 | 42750 EVENING BREEZE CT | 2017-01-11 | TERCERO, NICHOLAS C & RAFAEL D S TERCERO | 201701110002054 |
| 3 | 21658 STILLBROOK FARM DR | 2019-12-11 | BRUNST, ANNE M TR & BRUNST, GERALD JR TR & ANNE MARIE BRUNST & GERALD ROBERT BRUNST JR LIVING TRUST | 201912110077077 |
| 54 | 21651 STILLBROOK FARM DR | 2021-02-04 | CLARK, ROBERT | 202102040014471 |
| 54 | 21651 STILLBROOK FARM DR | 2021-03-03 | CLARK, ROBERT WINSLOW TR & ROBERT WINSLOW CLARK LIVING TRUST | 202103030025657 |
| 36 | 42763 HOLLOWIND CT | 2004-12-30 | REDDY, SHAILA & CHRIS MILL TRUSTEES | 200412300139341 |
| 36 | 42763 HOLLOWIND CT | 2011-01-03 | REDDY, SHAILA & CHRIS MILL TRUSTEES | 201101030000379 |
| 52 | 42770 HOLLOWIND CT | 2021-11-09 | MILLER, PAUL D TR & CHESTNUT, JESSICA L TR & PAUL D MILLER REVOCABLE TRUST & JESSICA L CHESTNUT REVOCABLE TRUST | 202111090113307 |
| 40 | 42747 HOLLOWIND CT | 2023-03-21 | STEPHENSON, JOHN ANDREW TR & JOHN A STEPHENSON TRUST | 202303210010071 |
| 49 | 42754 HOLLOWIND CT | 2014-07-01 | FLOWERS, ANGELA EVERETT TEE | 201407010035663 |
| 47 | 42746 HOLLOWIND CT | 2023-07-24 | CAULFIELD, JOANN MARIE TR & CAULFIELD, WILLIAM RUSSELL III TR & WILLIAM & JOANN CAULFIELD LIVING TRUST | 202307240028931 |
| 44 | 42734 HOLLOWIND CT | 2023-02-14 | THOMPSON, RAYMOND M JR TR & THOMPSON, KARYN TR & RAYMOND & KARYN TRUST | 202302140005511 |

## Sources

- Loudoun County Real Property Information — Sales / Transfers per PIN, e.g. `https://reparcelasmt.loudoun.gov/PT/datalets/datalet.aspx?UseSearch=no&jur=107&mode=sales&pin=<PIN>&taxyr=2026`
- Loudoun GIS Land Records parcels — Broadlands Section 13, plat 1998-0187 (`https://logis.loudoun.gov/gis/rest/services/COL/LandRecordData/MapServer/4`)
- Snapshot of the RPI pull used for this audit: `data/loudoun-rpi-sales.json`
- Clerk public-path lookup (pointers only): `data/loudoun-clerk-lookup.json`
- Clerk-verified originals overlay (empty until PAX): `data/loudoun-clerk-deeds.json`
- Refresh: `python3 scripts/fetch_loudoun_sales.py && python3 scripts/rebuild_from_loudoun.py`

Clerk of Circuit Court **images** were not purchased. The free PAX **index** was not searched because it requires a personal occasional-user account. Any original 1999–2000 builder deed that is absent from RPI is documented as a gap, not guessed.
