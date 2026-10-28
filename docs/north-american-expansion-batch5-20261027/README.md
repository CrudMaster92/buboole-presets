# 25 more employers without sampling caps — batch 5

Validated October 27, 2026 (America/Toronto). Catalog baseline: `5810abc3b6fde64a4e89a1f37011ab71dc1bc171`, including the preceding 100-employer expansion and uncapped-collection repair. UTC observation timestamps can fall on October 28.

Adds 25 previously absent employer identities and 26 public HTTP monitors. Mecart Canada and USA use two official careers pages under one employer identity. Every recipe uses `coverage_mode: all` and `pagination.max_pages: null`, with no role-count or description-attempt quota. Existing entries and generated runtime files are unchanged.

## Live results

All 26 listing traversals completed without pending continuation and returned **219 source records**. Counts are point-in-time records, not a permanent or deduplicated vacancy total.

| Employer | Records | Monitors |
|---|---:|---:|
| Atelier Val-d’Or | 5 | 1 |
| Automatisation JRT | 8 | 1 |
| BRAVAD | 24 | 1 |
| Buropro Citation | 9 | 1 |
| Centre de services scolaire de l’Or-et-des-Bois | 3 | 1 |
| Corem | 5 | 1 |
| Femtum | 9 | 1 |
| Fédération québécoise des coopératives forestières | 2 | 1 |
| GRICS | 5 | 1 |
| Groupe Automobile Desjardins | 50 | 1 |
| Groupe Symac | 10 | 1 |
| Groupe VL | 15 | 1 |
| Groupement des assureurs automobiles | 4 | 1 |
| JOELLE Collection | 14 | 1 |
| Les Pères Nature | 8 | 1 |
| Mecart | 5 | 2 |
| Phaneuf Équipements Agricoles | 6 | 1 |
| Prometek | 2 | 1 |
| Robovic | 3 | 1 |
| Rousseau Métal | 10 | 1 |
| Structures RBR | 11 | 1 |
| Technosoude | 2 | 1 |
| Tremblay Cantin Assurances | 3 | 1 |
| Ville de Saint-Sauveur | 2 | 1 |
| Ville de Thetford Mines | 4 | 1 |

## Canada and USA

Mecart’s official [Canada page](https://mecart.com/fr/emplois/) advertises three jobs, including a welder/assembler explicitly located in Saint-Augustin-de-Desmaures, Quebec. Its [US page](https://mecart.com/careers/) advertises Welder-Assembler, Team Leader and Press Brake and Sheet Metal Machine Operator, both explicitly labelled Greenville, South Carolina. Both pages are included. Older unlinked job detail pages and the generic spontaneous-application form are excluded. This confirms current advertised roles in both countries for Mecart; it does not claim every employer hires in both countries.

## Pagination and ownership

- Seventeen Folks sources traverse native page numbers until an empty terminal page, including a second check that the terminal has zero unfiltered cards. Logical page size 1 advances page numbers; it is not a one-role quota. Groupe Automobile Desjardins yielded 50 records, BRAVAD 24 and Groupe VL 15, so the recipes do not stop at the first page.
- Five Jobillico sources use full employer job lists, not company-profile previews. Exact employer URL prefixes and dated job cards exclude recommendation links and separate spontaneous-application banks. English source paths can differ from profile slugs: Phaneuf uses phaneuf-agricultural-equipment and RBR uses rbr-structures. The paths were observed, not inferred.
- Robovic and Automatisation JRT read their complete current official careers sections. Robovic includes its advertised design internship as well as regular positions; the headline vacancy number is not a cap. Neither generic application form is admitted.
- FQCF’s shared federation/member board contains independent cooperative employers. Its recipe requires the explicit Client label to identify the Fédération québécoise des coopératives forestières. Only its two corporate positions are admitted; six member-cooperative cards in the inspected snapshot are excluded.
- Groupe Automobile Desjardins dealership brands, BRAVAD operating locations and Groupe VL pharmacies remain one identity per group. Divisions, locations and Mecart’s country boards are not counted as separate employers.
- CSSOB candidate-bank entries are excluded. Its current advertised school-support roles remain included. Public bodies and nonprofit organizations are employer identities alongside businesses.
- Full descriptions are attempted without a count quota. Some sources lack safely matchable structured descriptions or publish malformed data; actual failures and description lengths remain in live evidence. Listing completeness is separate from description completeness, and otherwise valid roles are preserved.
- Existing request/time/response-size safeguards remain unchanged. The runtime checkpoints interrupted all-role work rather than treating a work slice as source exhaustion. Missing jobs are not closed based on failed or interrupted traversals.

## Catalog and FreeHire screening

A fresh offset-based scan returned 438,158 unique FreeHire company slugs in 44 nonempty pages, followed by empty offset 440000. Every selected employer has current name/alias queries recorded in `freehire-screen.json`, with URLs, timestamps and returned metadata. `screening-summary.json` records the directory digest and baseline.

Catalog review checked normalized IDs/names/aliases, name fragments and exact request URLs against the expanded baseline. None of the 25 selected identities or 26 request URLs already exists there. Similar FreeHire names were reviewed through company/job profiles:

- RBR profile postings come from an Ottawa oceanographic-instrument manufacturer at rbr.recruitee.com, distinct from the Quebec wood-structure employer Structures RBR.
- ROUSSEAU SOLUTION METAL has French postings and is distinct from Rousseau Métal in Saint-Jean-Port-Joli. Groupe Tremblay construction jobs are distinct from Tremblay Cantin Assurances. JRT Mechanical’s US pipefitting jobs differ from Automatisation JRT’s Quebec automation jobs.
- FreeHire’s Familiprix and Familiprix siège-social profiles expose corporate software/developer roles. The selected Groupe VL source is the separately branded pharmacy operator; no matching Groupe VL board or employer identity was found.

Rotobec was rejected because FreeHire’s rotobec-usa profile already includes its Littleton, New Hampshire factory roles. PharmaPlus was rejected because [Horizon Santé’s own presentation](https://presentation.horizonsante.ca/) connects Distribution Pharmaplus and the existing Horizon Santé group. Mindcore was held out while a same-name FreeHire identity remained unresolved. Champlain campus boards were not counted as additional independent employers in this release; none is included.

The directory is mutable and search can be fuzzy or incomplete. No matching employer found describes this review; it is not a guarantee against every intermediary posting or unknown alias. Profile-check evidence retains titles, locations, source URLs and timestamps.

## Runtime and publication checks

Live tests use unchanged `server.scrapers.runtime.run_scraper` from jobs commit `67c1cf6eb1f3580a6e15bad123d9e8217ad0276e`. Actual HTTPS responses were fetched using the supported HTTPX client argument and approved environment proxy. No mocks, credentials or cookies are used; host allowlists remain enforced.

Catalog schema/build/unit checks and the public runtime export/collector tests run before publication. The jobs release appends only these 26 exact verified pins at the published catalog commit, preserving all 1,097 preceding source pins and every exclusion. Validation, request traces, pagination termination and source-ownership evidence are retained in the accompanying JSON files.
