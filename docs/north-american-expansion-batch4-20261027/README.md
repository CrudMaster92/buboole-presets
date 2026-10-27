# 25 more employers, without sampling caps — batch 4

Validated October 27, 2026. Catalog baseline: `1aca5890ff9bc879d2ad688f9c3365bd97143137`, including the preceding 75-employer expansion and uncapped-collection repair.

Adds 25 previously absent employer identities and 25 public HTTP monitors. Every recipe uses `coverage_mode: all` and `pagination.max_pages: null`, with no role-count or description-attempt quota. Existing catalog entries and generated runtime files are unchanged.

## Observed results

All 25 listing traversals completed with no pending continuation. They returned **303 public job records**. These are current source records, not a permanent or deduplicated vacancy total.

| Employer | Records | HTTP pages including details |
|---|---:|---:|
| ASDR | 12 | 15 |
| Dubé Excavation | 24 | 27 |
| Environnement Routier NRJ | 12 | 14 |
| Estérel Resort | 12 | 15 |
| Fournier Industries | 15 | 18 |
| Gaudreau Environnement | 10 | 12 |
| Groupe Alco-TMI | 11 | 13 |
| Groupe Demex-Centrem | 16 | 18 |
| Groupe Nutech | 4 | 6 |
| Groupe VIF | 2 | 4 |
| Horizon Santé | 15 | 17 |
| Interprojet | 12 | 15 |
| Lepage Millwork | 10 | 11 |
| Les Produits Fraco | 5 | 7 |
| Les Équipements d’érablière CDL | 26 | 28 |
| Moreau | 26 | 29 |
| Navada | 7 | 9 |
| Nordikeau | 9 | 11 |
| Palais des congrès de Montréal | 2 | 4 |
| Scelltech | 4 | 6 |
| Shellex Groupe Conseil | 21 | 24 |
| Soucy Industriel | 12 | 15 |
| Thermafix | 11 | 14 |
| Tisseur | 22 | 24 |
| Yourbarfactory | 3 | 5 |

## Traversal and ownership

- Twenty-four Folks boards traverse native page numbers until the first empty terminal page. Logical page size 1 controls page-number increments, not a one-role quota. Source response sizes vary; no page-count or role-count ceiling is used.
- Lepage Millwork uses its full employer listing, linked from the employer website, rather than its three-job company profile preview. Exact employer posting paths exclude navigation/recommendation links. Its inspected full listing exposes ten ItemList entries and an empty pagination control.
- General spontaneous applications and candidate banks are excluded using case-insensitive posting-title attributes. A generic Navada application, a CDL spontaneous-application entry and Moreau spontaneous applications were detected and excluded. These are not advertised roles.
- NRJ, Demex-Centrem, Alco-TMI and Horizon Santé expose their own operating divisions/locations on group boards. They remain one employer identity each; locations and subsidiaries are not counted as extra companies. The group labels were inspected before verification.
- Navada uses the table-layout selector and source-provided address cells. Other Folks boards support French/English address, territory and employment-type labels. Missing individual locations remain unspecified; headquarters are not substituted.
- Listing completeness is separate from description completeness. Full descriptions are attempted for every posting without a count quota. Many Folks pages publish malformed structured data or otherwise lack safely matchable descriptions; those failures remain visible in the live evidence and do not discard valid roles.
- The native runtime already checkpoints interrupted all-role listing/detail work. Request/time/response-size safeguards remain in place; they do not impose a total role or page quota or convert an interrupted run into a successful absence check.

## Duplicate and FreeHire screening

A new offset-based directory scan returned 438,158 unique FreeHire slugs in 44 nonempty pages, then an empty page at offset 440000. Name and alias searches were performed for every selected employer. `freehire-screen.json` retains query URLs, timestamps and returned metadata. `screening-summary.json` records the exact directory digest and baseline.

Catalog review checked normalized names/IDs/aliases, broader name fragments and exact source URLs. No selected identity or recipe already exists in the expanded baseline. Similar FreeHire names were inspected through public profiles rather than assumed identical:

- CDL/CDL Group profiles point to UK insurance software roles and other unrelated organizations, rather than the Quebec maple-sugaring equipment manufacturer. Inconsistent profile taglines were not treated as reliable identity evidence; actual posting URLs and descriptions drove the review.
- FreeHire VIF jobs come from `vifsoftware.recruitee.com` in France; the selected Groupe VIF source is the Quebec plastics/pool-equipment employer. RPG CARVIN in Spain is also distinct.
- FreeHire Soucy jobs concern the Drummondville/Saint-Jérôme manufacturing group. Soucy Industriel’s employer-linked official site describes a separate 90-year industrial-service business in eastern Canada. [Soucy Industriel](https://soucyindustriel.com/) and the [Drummondville group’s operating units](https://www.soucy-group.com/en/contact) provide distinct identity evidence.
- NRJ GROUP profile postings concern French broadcasting/media and IT, rather than Environnement Routier NRJ construction services. Fournierfils uses its own construction/mining BambooHR board, rather than Les Industries Fournier’s manufacturing board.
- Estrel profile jobs are based at the Berlin hotel; Estérel Resort is the Quebec hotel. Nutech Integrasi is an Indonesian technology employer rather than the Quebec manufacturing source. Moreau Physical Therapy is distinct from the Canadian construction employer.

Provider profile checks retain source job URLs and locations in `provider-profile-checks.json`. Familiprix and Talentify were not selected after overlapping FreeHire entries were observed. Other pharmacy and agency boards were left out of the final shortlist rather than counted as additional divisions.

These are Canadian employer sources. This batch does not claim confirmed current openings in both the USA and Canada for every employer. FreeHire is mutable and fuzzy search can return unrelated companies; no matching employer found describes this review, not a guarantee against every intermediary or unknown spelling.

## Runtime, checks and publication

Live tests ran the unchanged `server.scrapers.runtime.run_scraper` from jobs commit `ce167e507c1a66fd3c6f378fb5c32e0d8150dceb`. Real HTTPS responses were fetched using the supported HTTPX client argument and approved environment proxy. No mocks, credentials or cookies were used; source host allowlists are preserved.

Required catalog schema/build/unit checks and public collector runtime-export/tests run before publishing. The feed appends only these 25 exact verified pins at the published catalog commit, preserving all 1,072 existing pins and every exclusion. `validation-results.json` records completed checks. `pagination-ownership-audit.json` records native empty terminal-page checks, Lepage’s explicit item count, employer URL checks and duplicate checks.
