# Thirty new Canadian employer scrapers — 27 October 2026

Built **30 deterministic employer scrapers** with **535 observed records and 535 distinct posting URLs**. Each exact authored recipe returned jobs through the canonical JobHound runtime. All thirty public proposal documents and trimmed fixtures passed the canonical contribution contracts and fixture parser.

## Coverage and exclusions

Compared with the current catalog at `fa302b9485289a85592ce9019e92535af5747395`, earlier local expansion batches, and company records from both saved local tracker databases. The tracker MCP service was unavailable, so no claim is made about unsaved or remote tracker state. Checked the open catalog PRs: no selected employer duplicates those proposals.

Refreshed all 44 public FreeHire company-directory pages: **438,158 distinct slugs**. Also ran targeted live company-name/alias queries. No matching FreeHire employer was found for the selected thirty. The provider directory is mutable and name/domain screening is good-faith evidence, not a guarantee of exhaustive provider coverage.

AutoTrader.ca/TRADER, Day & Ross and Canada’s National Ballet School were excluded after actual FreeHire identities were found. Studio be (German photography/design), Studio B (UK creative studio) and Transport (Australian government transport data role) were inspected and rejected as unrelated fuzzy matches to National Music Centre/Studio Bell and Transport Guilbault. Their public source evidence is retained.

## Practical limits

All thirty recipes explicitly declare partial coverage. Some read a bounded set of listing pages; others deliberately cover only one official board, language, or ongoing-opening section. Unseen jobs must not be inferred closed. 125 records contain nonempty description text, including listing snippets; this is not a count of complete job descriptions. PDF adverts remain public document links. Canadian employers can advertise international roles, so the observed total is not a Canada-only vacancy count.

Current official adverts and representative posting links were inspected. Every sampled link returned HTTP 200. Counts are dated observations; openings, deadlines and sources can change. No access challenges were bypassed, and no credentials, private criteria, schedules or application history are included.

## Employers

| Employer | Observed listings | Official board |
|---|---:|---|
| Apotex | 92 | [Careers](https://careers.apotex.com/search) |
| Westburne | 82 | [Careers](https://rexel.ca/westburne-view-jobs-en) |
| Royal Ottawa Health Care Group | 72 | [Careers](https://jobs.jobvite.com/theroyal/jobs?nl=1) |
| College of New Caledonia | 49 | [Careers](https://cnc.peopleadmin.ca/postings/search) |
| Headwaters Health Care Centre | 40 | [Careers](https://hwaternew.bluelemonmedia.com/hr) |
| Region of Waterloo | 25 | [Careers](https://careers.regionofwaterloo.ca/RoW/search?createNewAlert=false&q=) |
| Transport Bourassa | 25 | [Careers](https://bourassa.ca/carriere) |
| District of Saanich | 21 | [Careers](https://www.saanich.ca/EN/main/local-government/careers-at-saanich/current-employment-opportunities.html) |
| Cambridge Memorial Hospital | 20 | [Careers](https://encareers-cmh.icims.com/jobs/search) |
| Joseph Brant Hospital | 15 | [Careers](https://josephbranthospital.hiringplatform.ca/list/careers) |
| Ocean Choice International | 13 | [Careers](https://oceanchoice.com/careers) |
| City of Maple Ridge | 11 | [Careers](https://mapleridge.hiringplatform.ca/list/external) |
| Niagara Health | 10 | [Careers](https://careers.niagarahealth.on.ca/erecruit/Search_Results.aspx) |
| Lakeridge Health | 10 | [Careers](https://careers.lakeridgehealth.on.ca/erecruit/Search_Results.aspx) |
| City of North Vancouver | 9 | [Careers](https://cnv.peopleadmin.ca/postings/search) |
| Campbellford Memorial Hospital | 9 | [Careers](https://cmh.ca/job-postings) |
| West Neighbourhood House | 7 | [Careers](https://www.westnh.org/jobopportunities) |
| Lumenus Community Services | 5 | [Careers](https://lumenus.hiringplatform.ca/list/careers) |
| Flemingdon Health Centre | 3 | [Careers](https://www.fhc-chc.com/get-involved/employment) |
| Groupe Guilbault | 3 | [Careers](https://www.groupeguilbault.com/en/career/job-opportunities-all) |
| City of Langley | 2 | [Careers](https://www.langleycity.ca/careers) |
| Contemporary Calgary | 2 | [Careers](https://www.contemporarycalgary.com/opportunities) |
| Polycultural Immigrant and Community Services | 2 | [Careers](https://www.polycultural.org/about-us/careers) |
| National Music Centre | 2 | [Careers](https://www.studiobell.ca/careers) |
| Genome Quebec | 1 | [Careers](https://genomequebec.com/carrieres) |
| Ballet BC | 1 | [Careers](https://balletbc.com/employment) |
| Soulpepper Theatre | 1 | [Careers](https://soulpepper.ca/work-with-us) |
| City of Chilliwack | 1 | [Careers](https://jobs.chilliwack.com/postings) |
| City of Parksville | 1 | [Careers](https://www.parksville.ca/cms.asp?wpID=94) |
| Central Toronto Youth Services | 1 | [Careers](https://ctys.org/about-us/careers) |

## Validation and delivery

- Exact live recipe execution: 30/30.
- Canonical proposal schema/ownership contracts and fixture parsing: 30/30.
- Catalog validator, production catalog build and repository tests: see validation-results.json.
- Existing active Site tests and production site build: see validation-results.json.

Authored monitor verification remains unverified pending the upstream trusted review process. No local tracker was installed or modified. No source was submitted, merged, enabled in a feed lock, or published. The public feed and website therefore do not yet contain these additions.

Publication needs explicit submission consent and the documented maintainer review/merge gate. The local typed preparation package is ready; JobHound’s unavailable loopback preparation tool was not reported as having created a run or receipt. `publication-plan.json` records the thirty exact source hashes and remaining canonical admission steps. Repository PR #22 currently contains the unmerged trusted-contribution infrastructure; do not claim those hosted checks ran for this batch.
