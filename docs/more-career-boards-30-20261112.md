# 30 new career board scrapers

Created 30 employer-specific deterministic Ashby recipes; live validation returned 588 postings, all with descriptions.

Status: authored and validated; continuing the approved publication workflow after required checks.

Each source uses all-role coverage and no pagination, role-count or description-count sampling cap. The public API supplies the full board in one response. Ownership comes from the employer’s official site; complete source IDs were independently compared with the real runtime result. Counts reflect validation time.

| Employer | Official ownership page | Public board | Observed postings |
|---|---|---|---:|
| LiveKit | [Official site](https://livekit.com/careers) | [Careers](https://jobs.ashbyhq.com/livekit) | 30 |
| Paraform | [Official site](https://www.paraform.com/careers) | [Careers](https://jobs.ashbyhq.com/paraform) | 12 |
| Metaview | [Official site](https://www.metaview.ai/careers) | [Careers](https://jobs.ashbyhq.com/metaview) | 39 |
| Compa | [Official site](https://www.compa.ai/careers) | [Careers](https://jobs.ashbyhq.com/compa) | 6 |
| 9fin | [Official site](https://9fin.com/careers) | [Careers](https://jobs.ashbyhq.com/9fin) | 35 |
| Quo | [Official site](https://www.quo.com/careers) | [Careers](https://jobs.ashbyhq.com/quo) | 13 |
| Front | [Official site](https://front.com/jobs) | [Careers](https://jobs.ashbyhq.com/frontcareers) | 4 |
| Fathom | [Official site](https://www.fathom.ai/) | [Careers](https://jobs.ashbyhq.com/fathom) | 1 |
| Read AI | [Official site](https://www.read.ai/careers) | [Careers](https://jobs.ashbyhq.com/read-ai) | 16 |
| E2B | [Official site](https://e2b.dev/careers) | [Careers](https://jobs.ashbyhq.com/e2b) | 14 |
| Steel | [Official site](https://steel.dev/) | [Careers](https://jobs.ashbyhq.com/steel) | 1 |
| Firecrawl | [Official site](https://www.firecrawl.dev/careers) | [Careers](https://jobs.ashbyhq.com/firecrawl) | 24 |
| Exa | [Official site](https://exa.ai/careers) | [Careers](https://jobs.ashbyhq.com/exa) | 65 |
| Parallel | [Official site](https://parallel.ai/careers) | [Careers](https://jobs.ashbyhq.com/parallel) | 34 |
| Linkup | [Official site](https://www.linkup.so/careers) | [Careers](https://jobs.ashbyhq.com/Linkup) | 14 |
| Render | [Official site](https://render.com/careers) | [Careers](https://jobs.ashbyhq.com/render) | 35 |
| Knock | [Official site](https://knock.app/) | [Careers](https://jobs.ashbyhq.com/knock) | 2 |
| Svix | [Official site](https://www.svix.com/careers/) | [Careers](https://jobs.ashbyhq.com/svix) | 3 |
| Convex | [Official site](https://www.convex.dev/jobs) | [Careers](https://jobs.ashbyhq.com/convex-dev) | 10 |
| Clerk | [Official site](https://clerk.com/careers) | [Careers](https://jobs.ashbyhq.com/Clerk) | 2 |
| WorkOS | [Official site](https://workos.com/careers) | [Careers](https://jobs.ashbyhq.com/workos) | 27 |
| Authzed | [Official site](https://authzed.com/careers) | [Careers](https://jobs.ashbyhq.com/authzed) | 5 |
| Oso | [Official site](https://www.osohq.com/company/jobs) | [Careers](https://jobs.ashbyhq.com/Oso) | 7 |
| Teleport | [Official site](https://goteleport.com/careers/) | [Careers](https://jobs.ashbyhq.com/goteleport) | 25 |
| Opal Security | [Official site](https://www.opal.dev/careers) | [Careers](https://jobs.ashbyhq.com/Opal) | 11 |
| Socket | [Official site](https://socket.dev/careers) | [Careers](https://jobs.ashbyhq.com/socket) | 25 |
| Semgrep | [Official site](https://semgrep.dev/about/careers/) | [Careers](https://jobs.ashbyhq.com/semgrep) | 14 |
| Snyk | [Official site](https://snyk.io/careers/all-jobs/) | [Careers](https://jobs.ashbyhq.com/Snyk) | 38 |
| Braintrust | [Official site](https://www.braintrust.dev/careers) | [Careers](https://jobs.ashbyhq.com/Braintrust) | 32 |
| Dash0 | [Official site](https://www.dash0.com/) | [Careers](https://jobs.ashbyhq.com/dash0) | 44 |

The adjacent JSON includes validation timestamps, recipe and inventory hashes, ownership evidence, warning lists, source samples and runtime provenance. Raw official pages, independent inventories and normalized results are retained in the Site workspace research folder.

Validation: catalog schema, catalog production build and catalog tests; canonical runtime export integrity; public collector tests; exact feed-pin hashes and preservation of prior pins. See the Site review record for final check results.
