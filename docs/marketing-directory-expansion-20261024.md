# Marketing Agencies: reviewed directory expansion, 24 October 2026

The collection grows from 68 to 106 company records (revision 5), retaining every original member and monitor reference. Added 12 verified native sources and 26 explicit FreeHire employer boards. There are now 63 native monitor references, 42 provider boards and the original unavailable Omnicom parent card. Company identities and public-board metadata remain authored once; membership contains references only.

## Native source observations

These are fresh public-only runs of the canonical public collector, with employer ownership checked against the raw listing labels and official career links. Counts are observations, not guaranteed vacancies. Sources explicitly retain partial-listing semantics: regional and brand scopes do not establish worldwide completeness. Cossette browser recipes do not supply full descriptions. Workday description enrichment remains bounded and checkpointed.

| Company / monitor | Observed jobs | Pages including details | Checked at (UTC) | Representative posting |
| --- | ---: | ---: | --- | --- |
| OMD Canada (`omd-canada`) | 9 | 10 | 2026-10-24T17:39:57.742392+00:00 | [Senior Manager, Programmatic ](https://interpublic.wd5.myworkdayjobs.com/OMC/job/Toronto-Ontario-Canada/Senior-Manager--Programmatic_R15974) |
| PHD Canada (`phd-canada`) | 5 | 6 | 2026-10-24T17:39:57.743390+00:00 | [Programmatic Manager ](https://interpublic.wd5.myworkdayjobs.com/OMC/job/Toronto-Ontario-Canada/Programmatic-Manager_R16891-1) |
| Initiative (`initiative-canada`) | 8 | 9 | 2026-10-24T17:39:58.760718+00:00 | [Buyer, Investment ](https://interpublic.wd5.myworkdayjobs.com/OMC/job/Toronto-Ontario-Canada/Buyer--Investment_R16694) |
| UM Canada (`um-canada`) | 28 | 30 | 2026-10-24T17:40:13.887833+00:00 | [Campaign Manager, Programmatic ](https://interpublic.wd5.myworkdayjobs.com/OMC/job/Toronto-Ontario-Canada/Campaign-Manager--Programmatic_R15816) |
| McCann (`mccann`) | 22 | 24 | 2026-10-24T17:40:21.623673+00:00 | [People Services Administrator (6 Month FTC) ](https://interpublic.wd5.myworkdayjobs.com/OMC/job/Solihull-West-Midlands-United-Kingdom/People-Services-Administrator--6-Month-FTC-_R16994) |
| AREA 23 (`area-23`) | 55 | 58 | 2026-10-24T17:40:23.582010+00:00 | [Associate Director, Medical Strategy ](https://interpublic.wd5.myworkdayjobs.com/OMC/job/New-York-New-York-United-States-of-America/Associate-Director--Medical-Strategy_R16214) |
| GSD&M (`gsdm`) | 3 | 4 | 2026-10-24T17:41:21.841208+00:00 | [Account Supervisor ](https://interpublic.wd5.myworkdayjobs.com/OMC/job/Austin-Texas-United-States-of-America/Account-Supervisor_R16932) |
| The Martin Agency (`the-martin-agency`) | 15 | 16 | 2026-10-24T17:41:31.276392+00:00 | [Account Supervisor II ](https://interpublic.wd5.myworkdayjobs.com/OMC/job/Richmond-Virginia-United-States-of-America/Account-Supervisor-II_R17369) |
| Momentum Worldwide (`momentum-worldwide`) | 19 | 20 | 2026-10-24T17:41:32.070593+00:00 | [Account Manager, Business Leadership - Commerce/CPG ](https://interpublic.wd5.myworkdayjobs.com/OMC/job/Remote-Missouri-United-States-of-America/Account-Manager--Business-Leadership---Commerce-CPG_R17104) |
| TBWA (`tbwa`) | 9 | 10 | 2026-10-24T17:42:11.141465+00:00 | [Creative Director ](https://interpublic.wd5.myworkdayjobs.com/OMC/job/Chicago-Illinois-United-States-of-America/Creative-Director_R11998) |
| Cossette (`cossette`) | 9 | 2 | 2026-10-24T17:49:12.272699+00:00 | [Chargé·e de produits , Cossette ](https://cossette.talentpoolbuilder.com/Chargee%2520de%2520produits/296871?l=en-ca) |
| Cossette Media (`cossette-media`) | 17 | 2 | 2026-10-24T17:49:12.272699+00:00 | [Senior Buyer (Video & Audio) , Cossette Media ](https://cossette.talentpoolbuilder.com/Senior%2520Buyer%2520Video%2520%2526%2520Audio/297130?l=en-ca) |

Total observed native listings: 199. This total excludes FreeHire counts.

The Omnicom sources use the official Workday board linked from [The Martin Agency careers](https://www.martinagency.com/careers/). Every recipe pins the source-advertised Agency facet and applies a second exact raw `bulletFields.2` employer predicate. OMD, PHD, Initiative and UM additionally pin Canada and require explicit Canada listing text. Other agencies on the shared board are excluded. [Omnicom Media Canada](https://omnicommedia.com/canada/) establishes the Canadian brand relationships.

[Cossette careers](https://www.cossette.com/en/careers?sc=true) links its TalentPoolBuilder board. Two bounded anonymous browsers read two rendered listing pages and filter exact employer labels: 9 Cossette and 17 Cossette Media jobs; the 2 Septième jobs are excluded. Employer-rendered double-encoded application URLs are retained verbatim and checked for reachability. No API authentication or account is used.

The canonical Workday parser now identifies requisitions from the bullet that matches the public posting path, rather than assuming the first display bullet is an ID. This board lists job category first; the old assumption collapsed distinct postings. Adapter and traversal share one helper. Regression tests cover bounded/all-role traversal, distinct IDs, explicit detail IDs and safe path fallback. Publish the matching generated public-runtime/feed change alongside this catalog change.

## FreeHire employer boards

Each admitted profile returned current job samples and at least one original employer posting was reachable. No native monitor is fabricated for provider-only companies. Samples and counts may be regional or stale; the provider board is supplementary discovery, not exhaustive coverage. Separate global/US identities are reused or created without relabelling Canada-only records.

| Company | Provider identity | Sample location | Evidence |
| --- | --- | --- | --- |
| Rethink | `fh_company:rethinkcanada` | Toronto, Ontario, Canada | [Profile](https://freehire.me/api/v1/companies/rethinkcanada?limit=2) |
| Havas | `fh_company:havas` | Puteaux | [Profile](https://freehire.me/api/v1/companies/havas?limit=2) |
| LG2 | `fh_company:groupe-lg2` | Montréal, Québec, Canada | [Profile](https://freehire.me/api/v1/companies/groupe-lg2?limit=2) |
| We Are Social | `fh_company:we-are-social` | Singapore, Central Singapore, Singapore | [Profile](https://freehire.me/api/v1/companies/we-are-social?limit=2) |
| Bond Brand Loyalty | `fh_company:bond-brand-loyalty` | Recruitment: Toronto, Ontario, Canada | [Profile](https://freehire.me/api/v1/companies/bond-brand-loyalty?limit=2) |
| Brand Momentum | `fh_company:brand-momentum` | Summerside, Canada | [Profile](https://freehire.me/api/v1/companies/brand-momentum?limit=2) |
| Circana | `fh_company:circana` | Cape Town, Western Cape, South Africa | [Profile](https://freehire.me/api/v1/companies/circana?limit=2) |
| Ipsos | `fh_company:ipsos` | Genève, Switzerland | [Profile](https://freehire.me/api/v1/companies/ipsos?limit=2) |
| Serviceplan Group | `fh_company:serviceplan-gruppe` | Hamburg, Hamburg, Deutschland | [Profile](https://freehire.me/api/v1/companies/serviceplan-gruppe?limit=2) |
| BETC | `fh_company:betc` | Pantin, FR | [Profile](https://freehire.me/api/v1/companies/betc?limit=2) |
| TBWA Media Arts Lab | `fh_company:media-arts-lab` | Singapore | [Profile](https://freehire.me/api/v1/companies/media-arts-lab?limit=2) |
| Goodby Silverstein & Partners | `fh_company:goodby-silverstein-partners` | New York | [Profile](https://freehire.me/api/v1/companies/goodby-silverstein-partners?limit=2) |
| INNOCEAN Canada | `fh_company:innocean-canada` | Toronto, Ontario, Canada | [Profile](https://freehire.me/api/v1/companies/innocean-canada?limit=2) |
| INNOCEAN USA | `fh_company:innocean` | Huntington Beach HQ Office - Huntington Beach, CA 92648 | [Profile](https://freehire.me/api/v1/companies/innocean?limit=2) |
| VCCP | `fh_company:vccp-group` | London | [Profile](https://freehire.me/api/v1/companies/vccp-group?limit=2) |
| Tombras | `fh_company:tombras` | Knoxville, TN | [Profile](https://freehire.me/api/v1/companies/tombras?limit=2) |
| Goodway Group | `fh_company:goodway-group` | Remote | [Profile](https://freehire.me/api/v1/companies/goodway-group?limit=2) |
| Jack Morton Worldwide | `fh_company:jack-morton-worldwide` | Addison, Illinois, United States | [Profile](https://freehire.me/api/v1/companies/jack-morton-worldwide?limit=2) |
| MiQ | `fh_company:miq` | Vancouver | [Profile](https://freehire.me/api/v1/companies/miq?limit=2) |
| TANK Worldwide | `fh_company:tank-worldwide` | Montreal | [Profile](https://freehire.me/api/v1/companies/tank-worldwide?limit=2) |
| Next Level Marketing | `fh_company:next-level-marketing` | Shelton, United States | [Profile](https://freehire.me/api/v1/companies/next-level-marketing?limit=2) |
| M2W | `fh_company:m2w` | Joliet, United States | [Profile](https://freehire.me/api/v1/companies/m2w?limit=2) |
| Allen & Gerritsen | `fh_company:allen-gerritsen` | Boston, MA, US | [Profile](https://freehire.me/api/v1/companies/allen-gerritsen?limit=2) |
| RPA | `fh_company:rpa` | Santa Monica, CA - Hybrid | [Profile](https://freehire.me/api/v1/companies/rpa?limit=2) |
| BarkleyOKRP | `fh_company:barkleyokrp` | Kansas City, MO / Chicago, IL | [Profile](https://freehire.me/api/v1/companies/barkleyokrp?limit=2) |
| Huge | `fh_company:hugeinc` | United States | [Profile](https://freehire.me/api/v1/companies/hugeinc?limit=2) |

Identity exclusions: Rethink uses `rethinkcanada`, not the CRM employer `rethink`. Huge uses `hugeinc`, and BarkleyOKRP uses `barkleyokrp`; their alternate provider profiles are not merged. The existing catalog `rga` remains the reinsurer; no R/GA identity is admitted. Conflicting Grey, PMG, Jellyfish and Anomaly profiles remain deferred. The provider `phd` is an industrial employer and is not used.

## Deferred and remaining work

Hearts & Science Canada returned no jobs for the exact current agency/country scope. KINESSO’s old domain redirects to Acxiom, Media Experts lacks a confirmed distinct current employer scope, and Touché’s linked Montreal source no longer provides an accessible board. Their existing unavailable records are not presented as repaired.

Cheil, George P. Johnson and Octagon remain deferred in this batch: no original sample could be retrieved successfully (Paycor gateway errors / official job-page 403 responses). No attempt was made to bypass those failures. LePub, DAVID, Droga5, Johannes Leonardo, Cramer-Krasselt, Productions Plus, The Hype Agency and Legacy Marketing remain further source-discovery/build work; this release does not claim to complete the whole research shortlist.

## Validation

Catalog schema validation, catalog build and 11 unit tests. The corresponding generated public runtime passes 198 tests and export integrity; the canonical web production build passes. Every original collection reference is preserved. Per-source evidence, raw public listing observations and validation scripts remain in the Site coordination workspace under `research/marketing-expansion-20261024/`. No personal application data, criteria, credentials or tracker state is used.
