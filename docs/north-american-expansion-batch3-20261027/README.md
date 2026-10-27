# 25 more employers — batch 3

Validated October 27, 2026. Baseline: `46e983f03c40601398167737c8a823dff90aeedb`, including the two preceding 25-company expansions.

Adds 25 previously absent employer identities and 26 verified public HTML monitors. Madysta has separate Canadian and US boards under one company identity. Existing companies, recipes, generated output and runtime behavior are unchanged.

## Live results

| Employer | Source records | Monitors |
|---|---:|---:|
| Call Center Guys | 2 | 1 |
| Centre de services scolaire des Hautes-Rivières | 18 | 1 |
| Communauté métropolitaine de Montréal | 2 | 1 |
| Deloupe | 7 | 1 |
| Groupe Contant | 10 | 1 |
| Groupe Loiselle | 8 | 1 |
| Groupe Madysta | 8 | 2 |
| Groupe Santé Arbec | 26 | 1 |
| LJL Mécanique | 8 | 1 |
| Mennonite New Life Centre | 1 | 1 |
| Musée McCord Stewart | 2 | 1 |
| NTS Amega West Canada | 1 | 1 |
| Office Interiors | 1 | 1 |
| Pavages Métropolitain | 1 | 1 |
| Port de Montréal | 8 | 1 |
| Québec International | 1 | 1 |
| Ripplecove Hotel & Spa | 10 | 1 |
| Robertson College | 10 | 1 |
| Ropack Pharma Solutions | 10 | 1 |
| Smitty’s Car Wash Canada | 2 | 1 |
| SOPFEU | 5 | 1 |
| Transcol | 10 | 1 |
| Transport Hervé Lemieux | 10 | 1 |
| Transport Laberge | 10 | 1 |
| XDI Energy Solutions | 1 | 1 |

**172 public source records** returned through the real collector runtime across 26 sources. These are point-in-time records, not a deduplicated vacancy total.

## Canada and USA

Madysta returned five Canada-board jobs plus three US-board jobs based in Thomasville, North Carolina: Telecom Technician, Telecom Tophand and Telecom Foreman. The Canada board advertises roles in Quebec and New Brunswick. One card labels Dieppe as Quebec while another labels it New Brunswick; source labels are preserved without correction. Both boards require a Client label containing Madysta. Other group-company cards are excluded and never counted as additional employers.

## Ownership and record quality

- LJL Mécanique mixes its own positions with Agnico-Eagle client-site placements. The selector requires the explicit Client label to contain LJL; ten client-labelled cards are excluded.
- Office Interiors excludes its general Careers page expression-of-interest entry. Only the advertised Marketing Coordinator position is retained.
- Robertson College URLs retain historical slugs: `/job/health-care-aide-instructor` currently titles itself Early Childhood Education Instructor, while `/job/elc-practicum-observer-2` titles itself Health Care Aide Instructor. Direct detail-page checks confirmed the current displayed titles. All ten distinct current URLs are retained; URL slugs are not treated as titles.
- CSSDHR excludes the leadership succession program and substitute candidate bank. Advertised replacement and on-call opportunities remain eligible jobs. This collection includes public and nonprofit employers; 25 refers to distinct employer identities.
- Groupe Santé Arbec care homes remain one group employer. Groupe Contant dealer locations likewise remain one identity. No location or division is counted as another employer.
- French and English address, territory and employment-type labels are supported. Source territories are preserved when available; headquarters are never inferred as individual work locations.
- All sources are explicitly partial and bounded to the current listing page. Detail enrichment is capped at three postings. Folks boards often lack safely matchable structured descriptions, so some descriptions remain empty. EasyApply listing summaries can be truncated. The evidence preserves actual warnings, completeness, description lengths, URLs and timestamps. Missing records must not trigger closure.

## FreeHire and duplicate screening

A fresh directory scan retrieved 438,158 distinct company slugs in 44 nonempty pages using offsets, followed by empty offset 440000. Targeted name and alias queries were reviewed for all 25 selected employers. `freehire-screen.json` stores URLs, timestamps and returned metadata. `screening-summary.json` records the directory digest. Exact normalized identities and all 26 request URLs were also checked against the catalog.

Ambiguous names were reviewed through full public company/job profiles. FreeHire ropac advertises structural-steel work in Alabama, distinct from Montreal Ropack Pharma Solutions. Lemieux et Cie describes luxury home furnishings, rather than Transport Hervé Lemieux. CCG describes Utah commercial furniture/interior design, rather than Call Center Guys. NTS describes high-tech precision manufacturing in Europe and Singapore, distinct from the NTS Amega West oil-and-gas business. Contemporary Office Interiors uses a different employer board from Atlantic Canadian Office Interiors. Profile source URLs and review times are retained in `provider-profile-checks.json`.

FreeHire-covered candidates excluded: ECO Canada, Focus on the Family Canada, Canada’s Island Garden, John Ross & Sons, Heritage Park, Village Media, QCA Systems, ABC Head Start and Toronto French School. Twin Anchors and Canadian Musicians had no current inspected cards. Réseau MAclinique did not yield usable cards with the inspected listing selectors and was not admitted. Hitachi Cyber was not selected while its broader corporate/legacy identity overlap remained unresolved.

FreeHire is mutable and fuzzy search can be broad. No matching employer found describes this review; it does not guarantee absence through every intermediary or unknown spelling. This batch does not claim all 25 employers hire in both countries.

## Runtime and release checks

Live tests use unchanged `server.scrapers.runtime.run_scraper` from jobs commit `66e1877f56b6e604035730aac1e1cf4fcff3dddc`. A normal HTTPX client is injected through the supported argument to use the approved environment proxy; standalone DNS checks reject its synthetic DNS. Responses are real HTTPS, no mocks; recipe host restrictions remain in effect.

Catalog validation, build and unit tests run before publication. Jobs runtime export and collector tests also run. Exactly 26 new pins are appended at the published catalog commit; all previous 1,046 source entries and every exclusion remain unchanged. Generated output is excluded. Completed checks are in `validation-results.json`.
