# Marketing Agencies expansion

Observed 2026-10-24T04:19:13.304154+00:00. The collection grows from 52 to 68 companies while retaining its stable ID. The original 51 monitor references remain unchanged. Sixteen additions use explicit public FreeHire company boards; no placeholder scrapers or employer alias merges are created.

| Agency | FreeHire identity | Observed jobs | Official careers | Public evidence |
| --- | --- | ---: | --- | --- |
| Wpromote | `fh_company:wpromote` | 34 | [Careers](https://www.wpromote.com/careers/) | [Provider profile](https://freehire.me/api/v1/companies/wpromote?limit=2) |
| Tinuiti | `fh_company:tinuiti` | 16 | [Careers](https://tinuiti.com/careers/) | [Provider profile](https://freehire.me/api/v1/companies/tinuiti?limit=2) |
| AKQA | `fh_company:akqa` | 24 | [Careers](https://www.akqa.com/careers/) | [Provider profile](https://freehire.me/api/v1/companies/akqa?limit=2) |
| Burson | `fh_company:burson` | 95 | [Careers](https://www.bursonglobal.com/careers) | [Provider profile](https://freehire.me/api/v1/companies/burson?limit=2) |
| FleishmanHillard | `fh_company:fleishmanhillard` | 1 | [Careers](https://fleishmanhillard.com/join-us/) | [Provider profile](https://freehire.me/api/v1/companies/fleishmanhillard?limit=2) |
| Weber Shandwick | `fh_company:weber-shandwick` | 9 | [Careers](https://webershandwick.com/careers) | [Provider profile](https://freehire.me/api/v1/companies/weber-shandwick?limit=2) |
| Marketing for Change | `fh_company:marketing-for-change` | 2 | [Careers](https://marketingforchange.com/careers/) | [Provider profile](https://freehire.me/api/v1/companies/marketing-for-change?limit=2) |
| Marketing Architects | `fh_company:marketing-architects` | 1 | [Careers](https://www.marketingarchitects.com/careers) | [Provider profile](https://freehire.me/api/v1/companies/marketing-architects?limit=2) |
| NVE Experience Agency | `fh_company:nve-experience-agency` | 9 | [Careers](https://experiencenve.com/careers/) | [Provider profile](https://freehire.me/api/v1/companies/nve-experience-agency?limit=2) |
| MaxPlus Advertising | `fh_company:maxplus-advertising` | 3 | [Careers](https://www.maxplus-advertising.com/jobs) | [Provider profile](https://freehire.me/api/v1/companies/maxplus-advertising?limit=2) |
| Pulse Advertising GmbH | `fh_company:pulse-advertising` | 14 | [Careers](https://www.pulse-advertising.com/jobs/) | [Provider profile](https://freehire.me/api/v1/companies/pulse-advertising?limit=2) |
| MDG Advertising | `fh_company:mdg-advertising` | 6 | [Careers](https://www.mdgsolutions.com/marketing-and-advertising-careers/) | [Provider profile](https://freehire.me/api/v1/companies/mdg-advertising?limit=2) |
| Power Digital Marketing | `fh_company:power-digital-marketing` | 44 | [Careers](https://powerdigitalmarketing.com/company/careers/) | [Provider profile](https://freehire.me/api/v1/companies/power-digital-marketing?limit=2) |
| RAPP | `fh_company:rapp` | 7 | [Careers](https://www.rapp.com/careers/) | [Provider profile](https://freehire.me/api/v1/companies/rapp?limit=2) |
| GMR Marketing | `fh_company:gmr-marketing` | 4 | [Careers](https://gmrmarketing.com/about/careers/) | [Provider profile](https://freehire.me/api/v1/companies/gmr-marketing?limit=2) |
| Enthuse Marketing | `fh_company:enthuse-marketing` | 4 | [Careers](https://careers.smartrecruiters.com/Enthuse-Marketing/enthuse) | [Provider profile](https://freehire.me/api/v1/companies/enthuse-marketing?limit=2) |

These are bounded name-based searches, not an exhaustive survey of every provider employer. Counts are cached observations, not guaranteed current vacancies or complete global coverage. FleishmanHillard exposes German regional posts and reports one job while returning two sample records. Weber Shandwick samples are Brazilian posts. Tinuiti careers returned HTTP 403 to direct retrieval; its public Workday postings and provider profile identify the employer. Jellyfish, Huge/HugeInc and Barkley/BarkleyOKRP are excluded pending identity clarification.

The optional `public_job_board` schema and generated-member/search propagation use the same contract proposed in PR #43. This change does not add that PR's AI or recruitment memberships. All company and collection artifacts remain hashed; recipes stay in monitor artifacts only.

Validation: schema validator, catalog build (1,107 companies, 1,006 monitors, 18 collections), and all 11 tests passed. The expansion test checks 68 members, 16 provider-only members, stable provider IDs, hashes and absence of fabricated monitors.
