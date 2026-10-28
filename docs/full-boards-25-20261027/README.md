# 25 new employer boards with complete listing traversal

Observed October 27, 2026 in America/Toronto; UTC evidence timestamps fall on October 28.

Adds 25 new employer identities and 25 deterministic HTTP monitors. Every recipe uses `coverage_mode: all`, `pagination.max_pages: null` and `partial_listing: false`. There is no role-count or description-attempt quota. This is whole-board listing coverage, not a claim of complete descriptions or vacancies outside each linked employer board.

## Live listing results

The unchanged collector returned 274 source records. All 25 traversals completed with no pending continuation. An independent raw-card audit fetched every page through an empty terminal page and compared all eligible posting URLs to runtime results: zero missing and zero extra URLs. Excluding general applications did not stop pagination early. English/French first-page posting URLs matched for every board. Counts are point-in-time observations.

| Employer | Listings |
|---|---:|
| BVA | 8 |
| Balnea | 11 |
| CETAM | 3 |
| Collège Communautaire du Nouveau-Brunswick | 10 |
| Coopérative Aide Chez Soi en Beauce | 8 |
| Excavations Tourigny | 7 |
| Excelpro | 18 |
| Fondation Paul Gérin-Lajoie | 1 |
| Groupe Beaucage | 26 |
| Hôtel Gault | 1 |
| Hôtel Monville | 2 |
| Hôtel Universel Rivière-du-Loup | 8 |
| La HUTTE | 4 |
| Morehouse Foods Canada | 7 |
| Nitek Laser | 5 |
| PECH | 3 |
| Pluritec | 63 |
| Red Deer Polytechnic | 33 |
| SOPIAR gestion sportive | 5 |
| Solidev | 14 |
| Teccart | 3 |
| Tristan | 25 |
| Ville de Joliette | 2 |
| Ville de Kirkland | 4 |
| Ville de Nicolet | 3 |

## Ownership and scope

Each employer-branded Folks board was reviewed using its page title, public identity, card labels and source URLs. Group branches/dealerships/campuses remain one employer identity. Solidev includes its operating brands; CCNB includes all campuses; Red Deer Polytechnic includes explicitly titled advertised pools/instructor opportunities. Morehouse Foods Canada is labelled as the Canadian employer rather than claiming its US parent's separate vacancies. Public bodies and nonprofits are employers alongside businesses. No current USA-and-Canada hiring claim is made.

Ficodis was excluded because its corporate page does not establish coverage of all separate subsidiary boards. Stageline was excluded while its Scene Ethique scope was unresolved. OSM's administrative board was excluded rather than claiming it includes separate auditions. Ripplecove was rejected as a catalog duplicate. Empty/unparseable boards were not included.

## FreeHire and catalog screening

A fresh scan returned 438,158 unique FreeHire company slugs in 44 nonempty pages, followed by empty pages. The digest, offsets and name-search responses are retained. None of these 25 employer identities or request URLs existed in the baseline catalog. Same-fragment results refer to different employers: Morehouse General Hospital/Instrument Company, Gault Energy, Faymonville Polska, Nicolet National Bank/Plastics, Keulahutte and Brazilian Balneario recruiting. BVA is the Quebec accounting firm (bvacpa.ca), distinct from BVAEB/BBVA. PECH is the Quebec community organization; transliterated `pech` fragments and Pecheles/Pechanga names are unrelated. No matching employer was found; this cannot exclude every intermediary posting or undisclosed alias in a mutable provider.

## Description limitation

Full description enrichment was attempted for every role. Most Folks detail pages contain literal control characters in JSON-LD, rejected by the existing strict runtime; some lack safely identifiable canonical structured details. Per-role description lengths and failure warnings are retained in live evidence and verification. No fabricated descriptions or unrelated text is substituted. These recipes collect every listed role but do not claim complete descriptions. Missing locations remain Unspecified where the board publishes none; table addresses are extracted explicitly.

## Validation and publication

Schema validation, catalog build, catalog unit tests, runtime export integrity and collector tests are recorded in validation-results.json. The feed update appends only 25 exact pins and preserves existing pins/exclusions. Generated runtime files remain unchanged. Evidence includes request traces, terminal-page counts, language checks and screening results.
