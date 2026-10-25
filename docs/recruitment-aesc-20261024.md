# Recruitment agency expansion — 24 October 2026

The collection grows from 34 to 44 agencies: eight new native monitors and two explicitly provider-backed boards. The existing internal-employment scope and North America focus are retained; several employers publish global internal boards. No client-placement feed was knowingly admitted.

All 184 name/tagline-screened FreeHire leads received a public detail/sample review with no failed detail requests. See `recruitment-aesc-20261024-freehire-review.json`. Samples that contain recruiter titles are leads only: agencies can recruit recruiters for clients. Mixed/client boards and insufficient ownership proof remain excluded. This sample review cannot establish every vacancy on every provider board.

## Validated additions

| Agency | Native strategy | Jobs observed | Listing complete | Ownership evidence |
|---|---|---:|---|---|
| CHG Healthcare | workday | 36 | True | [Official careers](https://chghealthcare.com/work-with-us/chg-careers/careers-overview) |
| Talentful | ashby | 52 | True | [Official careers](https://www.talentful.com/careers/) |
| Egon Zehnder | generic_json | 68 | False | [Official careers](https://www.egonzehnder.com/join-us) |
| Onward Search | generic_json | 14 | False | [Official careers](https://www.onwardsearch.com/join-our-team/) |
| Sheffield Haworth | generic_html | 3 | False | [Official careers](https://www.sheffieldhaworth.com/careers/) |
| Ingenovis Health | workday | 18 | True | [Official careers](https://www.ingenovishealth.com/corporate-careers) |
| SThree | generic_html | 25 | False | [Official careers](https://www.sthree.com/en-gb/careers/job-search/) |
| Employbridge | FreeHire only | — | Not asserted | [Official careers](https://www.employbridge.com/about-us/join-our-team) |
| Express Employment International Headquarters | FreeHire only | — | Not asserted | [Official careers](https://www.expresspros.com/who-we-are/international-hq) |
| Stone Harbor Staffing Group (formerly Epic Staffing Group) | workday | 4 | False | [Official careers](https://stoneharborstaffing.com/careers/) |

Native counts are live observations through canonical `ScraperRecipe` and `run_scraper`, using the public collector HTTP client and host limiter. All 220 normalized jobs have distinct HTTPS posting URLs within their source. Completeness refers to listing traversal, not description enrichment. See validation JSON for exact timestamps, pages, warnings and sample URLs. Public collection enriches descriptions under its own canonical budget. Bounded feeds remain explicitly partial.

CHG and Ingenovis official corporate pages link their Workday boards. Talentful links its Ashby board. Onward embeds its named BambooHR tenant on Join Our Team. Sheffield Haworth lists three internal positions on its own careers page. Egon Zehnder’s employer-branded Workable `ezrecruiting` widget returns 68 internal positions; its previous guessed tenant was rejected. SThree uses its employer-branded careers subdomain and a bounded first search page.

Employbridge’s official Join Our Team links the exact UKG board observed in FreeHire. Express headquarters embeds the exact Paycom account observed in FreeHire. Their reviewed samples were internal staffing, sales and corporate positions. These two entries have no installable native monitor; no scraper verification is implied. Provider counts are inconsistent across search/detail and are not asserted as current vacancy totals.

## Directory and provider audit

Compared all **207** entries in [AESC’s current public interim member directory](https://www.aesc.org/membership/aesc-member-firms/) with catalog names/aliases and public official-site discovery. The full per-entry results are in `recruitment-aesc-20261024-directory.json`. Heidrick & Struggles and Spencer Stuart already exist; their monitors were preserved. Sheffield Haworth is the validated new AESC source. AESC directory membership is not a public job-board warranty. No claim is made that every non-admitted firm has no jobs: many public checks found client searches, general expressions of interest, inaccessible pages or no validated internal board. Further browser/manual research may find additional sources.

Paged all **3,324** FreeHire `company_type=agency` records (34 pages), plus targeted searches for every AESC name and prior recruitment leads. The agency flag contains many non-recruiters, mixed boards and client-placement sources. Name/tagline screening found **184** recruitment-related leads; this is lead discovery, not a completed ownership review of every one. All 184 leads received a detail/sample review; deeper official ownership validation focused on the supported internal boards listed above and recorded holds below. Raw inventories and public responses are retained in the Site workspace under `research/recruitment-aesc-20261024`.

## Holds and rejected mappings

- Calibrate, EXEC, Pathfinder and Progress: namesakes map to healthcare, coaching, industrial-service or software businesses, not the AESC firm.
- GGA Partners, kpCompanies, JacksonGrant, Signium and Mercuri Urval: observed listings were client placements or lacked internal ownership proof.
- Odgers: its Canada “careers portal” resolves to client searches; do not treat all portal listings as agency employment. A FreeHire UK internal lead needs distinct ownership review before admission.
- Russell Reynolds Associates: official careers page returned 403. Acertitude and Coulter Partners public Join pages provide general talent/contact routes rather than validated current postings.
- Epic Staffing Group redirects to Stone Harbor Staffing Group. Official JSON-LD confirms the former brand; the current corporate careers page links a new Workday board. Added one Stone Harbor identity with Epic as an alias, not two companies. The old FreeHire Epic board is not attached as current coverage.
- FreeHire Cielo resolves to a different business; Hays and Robert Half show mixed or conflicting source/company metadata. Preserve existing monitors and do not attach those provider records.
- Randstad Digital overlaps open catalog PR #43 and includes client-placement aggregators. No duplicate identity or membership was added.
- Planet Group and Alexander Mann Solutions sample feeds are client placements. Broad placement feeds, marketing agencies and ATS vendors are not admitted as internal recruitment employers.

## Release gates

Required catalog validator, production catalog builder and repository tests must pass before review. Generated outputs are not committed. New public-feed pins are prepared in a separate dependent PR. No automatic merge, publication or claim of live availability. After approved merges, verify catalog hashes, feed generation/source statuses and website company coverage.
