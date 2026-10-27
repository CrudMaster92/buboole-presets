# Collect all roles across the three employer batches

The first-page and three-description sampling limits were unnecessary. This release repairs all 76 monitors for the 75 employers added in these batches.

Every monitor now uses `coverage_mode: all` and `pagination.max_pages: null`. No role-count or description-count cap is configured. Native page traversal continues to exhaustion on Folks, Air Inuit and Groupe Lebel. The WordPress jobs API paginates by page/per_page; per_page controls response size, not total coverage. Sources that currently expose their whole board on one page remain single-page sources. Preverco now uses its full employer listing instead of the three-job profile preview. EasyApply listing summaries are removed so the runtime attempts full posting descriptions for every role.

## Live results

All 76 real runtime traversals finished with complete listing coverage and no pending continuation. They returned **781 records**, versus **655** in the preceding snapshots. Counts can change as employers publish or remove positions.

| Employer/source | Previous | Current | HTTP pages including details |
|---|---:|---:|---:|
| Accès Industriel (acces-industriel) | 10 | 10 | 12 |
| Aéroport de Québec (aeroport-de-quebec) | 3 | 3 | 5 |
| Air Inuit (air-inuit) | 12 | 25 | 29 |
| Amisco (amisco) | 7 | 7 | 8 |
| Artopex (artopex) | 9 | 9 | 1 |
| Avianor (avianor) | 20 | 20 | 22 |
| Barrette Structural (barrette-structural) | 12 | 12 | 13 |
| Cabco Technologies (cabco) | 4 | 4 | 5 |
| Café William (cafe-william) | 5 | 5 | 7 |
| Call Center Guys (call-center-guys) | 2 | 2 | 3 |
| Canadel (canadel) | 8 | 8 | 9 |
| Chantiers Chibougamau (chantiers-chibougamau) | 38 | 38 | 1 |
| Christie Innomed (christie-innomed) | 6 | 6 | 8 |
| Chrono Aviation (chrono-aviation) | 1 | 1 | 2 |
| CO7 Technologies (co7-technologies) | 8 | 8 | 10 |
| Communauté métropolitaine de Montréal (communaute-metropolitaine-montreal) | 2 | 2 | 4 |
| Construction PBM (construction-pbm) | 7 | 7 | 9 |
| Centre de services scolaire des Hautes-Rivières (cssdhr) | 18 | 27 | 30 |
| DECAST (decast) | 4 | 4 | 6 |
| Deloupe (deloupe) | 7 | 7 | 9 |
| Dermapure (dermapure) | 10 | 35 | 40 |
| Groupe Duroking (duroking) | 24 | 24 | 1 |
| Groupe Contant (groupe-contant) | 10 | 10 | 12 |
| Groupe Lebel (groupe-lebel) | 20 | 31 | 34 |
| Groupe Mundial (groupe-mundial) | 6 | 6 | 7 |
| Groupe Petra (groupe-petra) | 8 | 8 | 10 |
| Groupe PMI (groupe-pmi) | 10 | 14 | 17 |
| Houle Electric (houle-electric) | 30 | 30 | 31 |
| Hyperflo (hyperflo) | 8 | 8 | 10 |
| Infosignal (infosignal) | 2 | 2 | 3 |
| Infrastructel (infrastructel) | 7 | 7 | 8 |
| Keilhauer (keilhauer) | 2 | 2 | 3 |
| KRB Avocats (krb-avocats) | 4 | 4 | 6 |
| Leclerc Foods (leclerc) | 30 | 30 | 31 |
| LemayMichaud (lemaymichaud) | 2 | 2 | 3 |
| LightForm Canada (lightform) | 6 | 6 | 7 |
| LJL Mécanique (ljl-mecanique) | 8 | 8 | 10 |
| Groupe Loiselle (loiselle) | 8 | 8 | 10 |
| Lumenwerx (lumenwerx) | 4 | 4 | 6 |
| Groupe Madysta (madysta) | 5 | 5 | 7 |
| Groupe Madysta (madysta-usa) | 3 | 3 | 5 |
| Musée McCord Stewart (mccord-stewart) | 2 | 2 | 4 |
| Meridian Lightweight Technologies (meridian-lightweight-technologies) | 20 | 20 | 21 |
| Mennonite New Life Centre (mnlct) | 1 | 1 | 2 |
| NanoXplore (nanoxplore) | 8 | 8 | 9 |
| Nolinor Aviation (nolinor) | 14 | 14 | 15 |
| NTS Amega West Canada (nts-amega) | 1 | 1 | 2 |
| Office Interiors (office-interiors) | 1 | 1 | 2 |
| OVC Assurance (ovc-assurance) | 8 | 8 | 10 |
| Pavages Métropolitain (pavages-metropolitain) | 1 | 1 | 3 |
| Polykar (polykar) | 2 | 2 | 3 |
| Port de Montréal (port-montreal) | 8 | 8 | 10 |
| Preverco (preverco) | 3 | 11 | 12 |
| Produits Boréal (produits-boreal) | 2 | 2 | 4 |
| Provencher_Roy (provencher-roy) | 8 | 8 | 9 |
| Québec International (quebec-international) | 1 | 1 | 3 |
| RIMAP Hospitality (rimap-hospitality) | 10 | 49 | 55 |
| Ripplecove Hotel & Spa (ripplecove) | 10 | 11 | 14 |
| Robertson College (robertson-college) | 10 | 10 | 11 |
| Ropack Pharma Solutions (ropack) | 10 | 15 | 18 |
| Groupe Santé Arbec (sante-arbec) | 26 | 26 | 28 |
| Smitty’s Car Wash Canada (smittys-car-wash) | 2 | 2 | 3 |
| Solmatech (solmatech) | 10 | 17 | 20 |
| Sonele (sonele) | 11 | 11 | 13 |
| SOPFEU (sopfeu) | 5 | 5 | 7 |
| St-Denis Thompson (st-denis-thompson) | 14 | 14 | 16 |
| TMS Bâtiments préfabriqués (tms-systeme) | 20 | 20 | 22 |
| Transcol (transcol) | 10 | 12 | 15 |
| Transport Laberge (transport-laberge) | 10 | 10 | 12 |
| Transport Hervé Lemieux (transport-lemieux) | 10 | 12 | 15 |
| Verbom (verbom) | 10 | 10 | 11 |
| Vicwest (vicwest) | 2 | 2 | 3 |
| Gérances Westcliff (westcliff) | 5 | 5 | 7 |
| Wiptec (wiptec) | 1 | 1 | 1 |
| XDI Energy Solutions (xdi-energy) | 1 | 1 | 2 |
| YHU Terminal (yhu-terminal) | 8 | 8 | 10 |

## Correctness and operational behavior

Ownership exclusions remain in place for unrelated employers on shared boards. General applications and known mismatched URLs are not jobs. Each monitor revision is incremented; company identities stay the same. Historical batch evidence records the earlier limited snapshots and is superseded for current behavior by this repair.

Listing completeness and description completeness are separate. Some Folks job pages publish malformed JSON-LD and some other sources return empty description fields. Those extraction failures remain in the evidence rather than being called complete descriptions. They do not discard otherwise valid roles. No attempt quota remains.

The collector already checkpoints interrupted all-role work and resumes it in subsequent slices. Existing request, response-size and time budgets protect reliable execution; they do not cap the number of roles or pages and do not establish a completed absence check. Runtime and DNS/host safeguards are unchanged. Live testing uses real HTTPS requests through the supported HTTPX client argument and approved environment proxy; nothing is mocked.

AGENTS.md and CONTRIBUTING.md now require all-role collection by default and prohibit sampling caps unless the human requests a sample. Sources with real failures must remain incomplete rather than marking unseen jobs closed.

`live-evidence.json` includes every title, URL, location, description length, request URL/status and run timestamp. The jobs release replaces exactly these 76 pins at the new catalog commit and preserves every unrelated pin and exclusion.
