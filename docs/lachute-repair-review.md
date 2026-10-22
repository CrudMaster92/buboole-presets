# Lachute coverage repair — 2026-10-22

Five recipes were freshly run through the canonical Buboole runtime; point-in-time receipts are in lachute-repair-evidence.json.

| Monitor | Strategy | Jobs | Pages | Lachute jobs | Listing boundary |
|---|---|---:|---:|---:|---|
| Be Well | generic_html | 7 | 1 | 7 | Bounded official listing |
| Luxor | generic_html | 1 | 1 | 1 | Bounded official listing |
| FBL | generic_html | 42 | 1 | 4 | Bounded official listing, data-ville location |
| Cascades | generic_json | 110 | 11 | 4 | Full advertised listing traversed; descriptions not enriched |
| Super C — Lachute | playwright | 2 | 1 | 2 | Explicit brand/city scope, not all Super C jobs |

Cascades uses the anonymous public SAP recruiting endpoint and the UI newest-first order, zero-based page numbers and advertised totalJobs. Its stable posting route was checked against the displayed title. Four existing revisions advance to 2. The new Super C monitor retains the broad monitor and filters Super C ownership and Lachute city in the response. It captures official browser JSON without saved cookies, tokens or credentials.

Be Well and Luxor use their official employment listing location. FBL exposes each location in the public data-ville attribute; all ten values are Quebec offices, so the explicit jurisdiction suffix is source-proven. Locations are not inferred from a user search. Partial listings never authorize closing unseen jobs.

Requires the accompanying canonical runtime export for data-* location attributes, explicit jurisdiction suffixes, zero-based page APIs and totalJobs traversal. The shared geographic parser repair is published separately. No guessed monitors were created for employers whose public listings remain unavailable.
