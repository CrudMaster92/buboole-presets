# 25 more screened employer scrapers — batch 2

Validation date: October 27, 2026. Catalog baseline: `8a10080c616ff4c8457edcd80786b3aeea87a796`, including the first 25-source batch.

## Release scope

Adds 25 previously absent company identities, 25 deterministic public HTTP scraper recipes, and one collection referencing those identities. No existing company, scraper runtime, or generated artifact changes. Each selected recipe returned at least one public, employer-owned job through the real public-feed runtime. These are another 25 employers, not renamed sources from batch 1.

## Observed results

| Employer | Source records | HTTP pages, including details |
|---|---:|---:|
| Aéroport de Québec | 3 | 4 |
| Barrette Structural | 12 | 4 |
| Cabco Technologies | 4 | 1 |
| Café William | 5 | 4 |
| Chantiers Chibougamau | 38 | 1 |
| Christie Innomed | 6 | 4 |
| CO7 Technologies | 8 | 4 |
| Construction PBM | 7 | 4 |
| DECAST | 4 | 4 |
| Dermapure | 10 | 4 |
| Groupe Lebel | 20 | 4 |
| Groupe Petra | 8 | 4 |
| Groupe PMI | 10 | 4 |
| Gérances Westcliff | 5 | 4 |
| Hyperflo | 8 | 4 |
| Infosignal | 2 | 3 |
| KRB Avocats | 4 | 4 |
| LightForm Canada | 6 | 4 |
| Lumenwerx | 4 | 4 |
| OVC Assurance | 8 | 4 |
| Preverco | 3 | 4 |
| Produits Boréal | 2 | 3 |
| Sonele | 11 | 4 |
| TMS Bâtiments préfabriqués | 20 | 4 |
| YHU Terminal | 8 | 4 |

**216 observed source records**, not a deduplicated vacancy count. Twenty-four recipes use the existing `generic_html` adapter; Barrette Structural uses `generic_json` against its public employer WordPress jobs API. Counts are point-in-time observations.

## Ownership and scope

- Hyperflo shares a portal with independent Groupe VM. Its recipe requires the explicit `Client` label to contain Hyperflo; Groupe VM records are excluded. This is tested against the live source, not inferred from job titles.
- Preverco’s official careers page links to the selected Jobillico profile. The selector requires the exact `/en/job-offer/preverco-inc-.zYsdUe/` employer path, so recommendation/navigation links from other companies are not admitted.
- Chantiers Chibougamau’s employer-operated group board includes its Nordic and sawmill workplaces; Groupe Lebel’s group board includes its own lumber divisions. These group boards remain single company identities. Their divisions are not counted as extra employers.
- EasyApply recipes select job cards and their titles, excluding the repeated action labels. The Cabco template is handled separately from the newer EasyApply template.
- Barrette Structural’s source API exposes 12 published records, including French and English records with complete source descriptions. It covers more than the single English plant listing. Language variants may represent the same vacancy; location taxonomy IDs are left unflattened rather than guessed.
- All recipes explicitly mark listing coverage partial. Most HTML sources read the current visible page, so additional pages or language variants can remain outside coverage. Missing records never prove closure.
- Detail enrichment is bounded to three postings. Some sources do not provide safely matchable structured descriptions or locations; actual warnings and description character counts are retained in `live-evidence.json`. Known data is preserved without inferring work locations from a corporate headquarters.

## FreeHire screening

A new 44-page directory scan returned 438,158 unique slugs, followed by targeted live name and alias queries. `screening-summary.json` records the scan digest and timestamp; `freehire-screen.json` retains the selected employers’ query URLs, observation times, and returned company metadata.

Ambiguous matches were inspected through public company/job profiles. FreeHire’s `christie` entries concern entertainment lighting and digital projection rather than Christie Innomed. `petra-group` is a separate recruiting business rather than the Canadian property operator. German PMI marketing jobs differ from Groupe PMI’s industrial-service jobs; TMS software/industrial entries differ from the prefabricated-building employer. Profile checks retain source URLs for review.

Mattr was investigated as a potential Canada/US addition and rejected: FreeHire’s `mattr` profile mixes a different digital-identity company with the same `careers.mattr.com` manufacturing jobs. Merely seeing a similar name was not the basis of exclusion. Fenplast’s public endpoint and Mon Technicien’s inspected board returned no current records and were not admitted.

This selected batch is Canadian employer coverage. It does not assert confirmed openings in both countries for every company. The paged FreeHire directory is mutable and search is fuzzy. “No matching employer found” describes the current review, not a guarantee against unknown intermediaries, subsidiaries, or spellings.

## Runtime and validation

Live runs used the exported `server.scrapers.runtime.run_scraper` from `CrudMaster92/buboole-jobs` commit `f7fb9412d3290a2297ddc8b05dbb4bc887dadb02`. A normal HTTPX client was injected through the supported runtime parameter to use the approved workspace proxy. Requests used HTTPS and recipe allowlists; responses were not mocked. The default standalone DNS guard rejects synthetic workspace DNS, so this transport detail is explicit.

Required checks: `python scripts/validate_presets.py`, `python scripts/build_catalog.py`, and `python -m unittest discover -s tests`. The public feed release also runs the runtime export check and all collector tests, then appends only these exact 25 pins while preserving the preceding 1,021 pins and every exclusion. Generated catalog output is validation-only and excluded from the commit.
