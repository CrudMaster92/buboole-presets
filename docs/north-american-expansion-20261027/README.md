# 25 additional North American employer sources

Live validation: October 27, 2026. Catalog baseline: `05303a55815b10221903a6f2fc400745cc268624`.

## Release scope

Adds 25 company identities, 25 deterministic HTTP scrapers, and one referenced collection. No scraper runtime, existing identity, existing recipe, or generated catalog artifact changes. All 25 were absent from the baseline catalog; their names, public publisher boards, and relevant aliases were checked against FreeHire. EQ3 was rejected when its FreeHire `eq-3` profile resolved to the same Canadian furniture board. Existing catalog and FreeHire-covered candidates were excluded, rather than counted as new sources.

## Live results

| Employer | Observed records | Listing pages |
|---|---:|---:|
| Accès Industriel | 10 | 4 |
| Air Inuit | 12 | 4 |
| Amisco | 7 | 4 |
| Artopex | 9 | 1 |
| Avianor | 20 | 4 |
| Canadel | 8 | 4 |
| Chrono Aviation | 1 | 2 |
| Groupe Duroking | 24 | 1 |
| Groupe Mundial | 6 | 4 |
| Houle Electric | 30 | 4 |
| Infrastructel | 7 | 4 |
| Keilhauer | 2 | 3 |
| Leclerc Foods | 30 | 4 |
| LemayMichaud | 2 | 3 |
| Meridian Lightweight Technologies | 20 | 4 |
| NanoXplore | 8 | 4 |
| Nolinor Aviation | 14 | 4 |
| Polykar | 2 | 3 |
| Provencher_Roy | 8 | 4 |
| RIMAP Hospitality | 10 | 4 |
| Solmatech | 10 | 4 |
| St-Denis Thompson | 14 | 4 |
| Verbom | 10 | 4 |
| Vicwest | 2 | 3 |
| Wiptec | 1 | 1 |

Total: **267 source records**, not a deduplicated vacancy count. All recipes use public HTTPS GET requests and the existing `generic_html` adapter. Each returned at least one job in a fresh real-network run through the deployed public-feed runtime.

## Canada and United States

Leclerc Foods, NanoXplore, and Meridian Lightweight Technologies each returned roles in both countries in the same live listing run:

- **Leclerc Foods**: [Corporate Controller](https://leclerc.ca/en/job/7185) (Saint-Augustin-de-Desmaures, Québec); [Sanitation Worker - Weekend](https://leclerc.ca/en/job/7460) (Kingsport, Tennessee).
- **NanoXplore**: [Analyste en systèmes applicatifs](https://nanoxplore.prevueaps.com/iframe/mobile/340037.html) (Montréal, QC, CAN); [2nd Shift Production Operator](https://nanoxplore.prevueaps.com/iframe/mobile/334920.html) (Statesville, NC, USA).
- **Meridian Lightweight Technologies**: [Business Analyst](https://mlti.prevueaps.com/iframe/mobile/340119.html) (Strathroy-Caradoc, ON, CAN); [Business Analyst](https://mlti.prevueaps.com/iframe/mobile/340124.html) (Eaton Rapids, MI, USA).

## Coverage and ownership review

- Each source is explicitly partial (`metadata.partial_listing: true`): one visible listing page or one visible public board. Missing roles must not close previously seen jobs. Platforms with more listing pages remain partial.
- The default bounded detail budget is three postings. Descriptions and locations may remain incomplete, particularly when a site does not expose canonical, title-matched JobPosting data. `live-evidence.json` retains actual warnings and description character counts rather than asserting full descriptions.
- Only company-owned/branded feeds are selected. Group boards intentionally retain the group’s own divisions: NanoXplore, Groupe Mundial, and Infrastructel/APUR. No unrelated marketplace search is used as a scraper source.
- Artopex: the spontaneous application is excluded. The assembler card incorrectly links to the shipping-agent vacancy; that card is also excluded instead of publishing the wrong posting.
- Chrono Aviation and LemayMichaud: spontaneous application links are excluded. EasyApply scrapers select actual job title links, not repeated “View Job” buttons. Tests against live results reject action labels and duplicate canonical URLs.
- Source ownership was reviewed using the listing identity, posting titles and source URLs. For employer-linked ATS endpoints, the official careers page or branded publisher page supplied the destination. The endpoints and returned titles are recorded in the evidence.

## FreeHire screening

`screening-summary.json` records a fresh 44-page, 438,158-slug directory scan and its digest, followed by targeted live company/alias queries in `freehire-screen.json`. Search is fuzzy: unrelated names such as Oxford Nanopore versus NanoXplore, Provencher & Company versus Provencher_Roy, and industrial-access versus Accès Industriel were not treated as identity matches. The EQ3 collision was checked with its actual profile/jobs, then excluded.

The paged directory is mutable rather than an atomic export. “No matching employer found” describes the observed directory and alias review; it does not prove absence under every intermediary, acquired business, hotel franchise, or unrecognized spelling.

## Runtime and validation

Real network requests used `server.scrapers.runtime.run_scraper` from `CrudMaster92/buboole-jobs` commit `2dd3ed4c07bd49d7d243c53064d796d764976b1f`. A normal HTTPX client was injected through the supported runtime client parameter to use this workspace’s approved proxy. The default standalone DNS guard rejects synthetic workspace DNS; recipes and endpoint allowlists were unchanged, and responses were not mocked. Runtime results are retained in compact form with counts, timestamps, all returned titles/URLs, pages, completeness, and warnings.

Required catalog checks: `python scripts/validate_presets.py`, `python scripts/build_catalog.py`, and `python -m unittest discover -s tests`. Build output is validation-only and excluded from the commit. The release will also pin only these 25 exact recipes in the public-feed lock while preserving existing reviewed historical pins.
