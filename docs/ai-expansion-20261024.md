# AI collection expansion — 24 October 2026

AI grows from 15 to 66 companies (revision 13), preserving every original membership and adding 51 employer-controlled public careers sources. All 51 new recipes were run through the canonical JobHound scraper and public collector. Their combined point-in-time listing count was 4,816; this is not a guarantee of future openings or deduplicated role types.

## Discovery sources

- [Forbes AI 50, 2026](https://www.forbes.com/lists/ai50/): all 50 records read from the public list data. This list selects privately held AI companies; private status is the list’s inclusion basis, not a new ownership/IPO audit. 49 now have AI collection membership. Safe Superintelligence is deferred: the official site links to Ashby, but its public posting API returned an empty jobs list. No verified monitor was fabricated.
- [FreeHire AI collection](https://freehire.me/collections): all 35 records returned by `GET /api/v1/companies?collections=ai&limit=100` were examined. Duplicate brands (Harvey/Harvey AI, Mistral/Mistral AI, Perplexity/Perplexity AI) are collapsed; DeepMind reuses Google’s existing member. All 31 distinct FreeHire identities are represented. FreeHire is discovery evidence; new recipes collect employer-controlled public sources directly.

## Ownership and limitations

- Clay uses the official `claylabs` Ashby board, excluding the unrelated hospitality employer in the FreeHire Clay record.
- Krea uses the AI company’s official Ashby board, excluding Krea Sweden credit-sales records. Glean uses `gleanwork`, excluding the other SmartRecruiters Glean source.
- Mercor uses its own internal careers Ashby board, excluding external expert/client placement jobs. Modal uses the official company page and its linked `modal` board rather than a WhatJobs lead.
- Weights & Biases uses only the `weights_and_biases` board hosted by CoreWeave, excluding the parent CoreWeave board. Its brand membership does not assert independent private ownership.
- Hugging Face, AI21 Labs and Cyera have listing coverage with incomplete or missing description enrichment. Their source warnings remain explicit. Cyera’s 18 public listing pages returned 256 postings, and full listing traversal completed.
- The canonical runtime now omits invalid reversed salary ranges without dropping jobs or changing original description text. This change is exported to the feed; 56 focused scraper tests, all 195 public-runtime tests and the canonical web production build pass.

## Live source validation

| Company | Strategy | Jobs | Pages | Checked (UTC) | Public board |
|---|---|---:|---:|---|---|
| Abridge | ashby | 36 | 1 | 2026-10-24T15:03:56.601854+00:00 | [Careers](https://jobs.ashbyhq.com/Abridge) |
| Applied Intuition | ashby | 328 | 1 | 2026-10-24T15:03:56.603280+00:00 | [Careers](https://jobs.ashbyhq.com/applied) |
| Baseten | ashby | 106 | 1 | 2026-10-24T15:03:56.604377+00:00 | [Careers](https://jobs.ashbyhq.com/baseten) |
| Black Forest Labs | ashby | 13 | 1 | 2026-10-24T15:03:56.605612+00:00 | [Careers](https://jobs.ashbyhq.com/black-forest-labs) |
| Chai Discovery | ashby | 20 | 1 | 2026-10-24T15:03:57.788931+00:00 | [Careers](https://jobs.ashbyhq.com/chaidiscovery) |
| Cognition | ashby | 105 | 1 | 2026-10-24T15:03:58.480193+00:00 | [Careers](https://jobs.ashbyhq.com/cognition) |
| Crusoe | generic_json | 349 | 1 | 2026-10-24T15:07:40.177364+00:00 | [Careers](https://jobs.ashbyhq.com/crusoe) |
| Decagon | ashby | 134 | 1 | 2026-10-24T15:04:01.670915+00:00 | [Careers](https://jobs.ashbyhq.com/decagon) |
| EliseAI | ashby | 121 | 1 | 2026-10-24T15:04:02.036093+00:00 | [Careers](https://jobs.ashbyhq.com/EliseAI) |
| Fal | ashby | 44 | 1 | 2026-10-24T15:04:03.032714+00:00 | [Careers](https://jobs.ashbyhq.com/fal-ai) |
| Fireworks AI | ashby | 91 | 1 | 2026-10-24T15:04:04.226580+00:00 | [Careers](https://jobs.ashbyhq.com/fireworks) |
| Gamma | ashby | 21 | 1 | 2026-10-24T15:04:04.935737+00:00 | [Careers](https://jobs.ashbyhq.com/gamma) |
| Genspark.ai | ashby | 10 | 1 | 2026-10-24T15:04:05.844178+00:00 | [Careers](https://jobs.ashbyhq.com/genspark) |
| Glean | generic_json | 131 | 1 | 2026-10-24T15:07:40.179747+00:00 | [Careers](https://job-boards.greenhouse.io/gleanwork) |
| Harvey | ashby | 358 | 1 | 2026-10-24T15:04:06.478292+00:00 | [Careers](https://jobs.ashbyhq.com/harvey) |
| HeyGen | generic_json | 20 | 1 | 2026-10-24T15:05:17.406685+00:00 | [Careers](https://job-boards.greenhouse.io/heygen) |
| Krea | ashby | 12 | 1 | 2026-10-24T15:04:07.467970+00:00 | [Careers](https://jobs.ashbyhq.com/krea) |
| Legora | ashby | 310 | 1 | 2026-10-24T15:04:08.030501+00:00 | [Careers](https://jobs.ashbyhq.com/legora) |
| Listen Labs | ashby | 32 | 1 | 2026-10-24T15:04:08.136021+00:00 | [Careers](https://jobs.ashbyhq.com/listenlabs) |
| Notion | ashby | 140 | 1 | 2026-10-24T15:04:10.230058+00:00 | [Careers](https://jobs.ashbyhq.com/notion) |
| OpenEvidence | ashby | 8 | 1 | 2026-10-24T15:04:10.243378+00:00 | [Careers](https://jobs.ashbyhq.com/openevidence) |
| Physical Intelligence | ashby | 45 | 1 | 2026-10-24T15:04:12.195946+00:00 | [Careers](https://jobs.ashbyhq.com/physicalintelligence) |
| Reflection | ashby | 45 | 1 | 2026-10-24T15:04:12.406607+00:00 | [Careers](https://jobs.ashbyhq.com/reflectionai) |
| Replit | ashby | 37 | 1 | 2026-10-24T15:04:13.694954+00:00 | [Careers](https://jobs.ashbyhq.com/replit) |
| Rogo | ashby | 98 | 1 | 2026-10-24T15:04:13.766235+00:00 | [Careers](https://jobs.ashbyhq.com/rogo) |
| Sierra | ashby | 210 | 1 | 2026-10-24T15:04:14.146132+00:00 | [Careers](https://jobs.ashbyhq.com/Sierra) |
| Skild AI | generic_json | 50 | 1 | 2026-10-24T15:05:17.414374+00:00 | [Careers](https://job-boards.greenhouse.io/skildai-careers) |
| Speak | ashby | 33 | 1 | 2026-10-24T15:04:15.054276+00:00 | [Careers](https://jobs.ashbyhq.com/speak) |
| Surge AI | ashby | 28 | 1 | 2026-10-24T15:04:16.239046+00:00 | [Careers](https://jobs.ashbyhq.com/surge-ai) |
| Synthesia | ashby | 34 | 1 | 2026-10-24T15:04:17.646035+00:00 | [Careers](https://jobs.ashbyhq.com/synthesia) |
| Thinking Machines Lab | ashby | 52 | 1 | 2026-10-24T15:04:17.793417+00:00 | [Careers](https://jobs.ashbyhq.com/ThinkingMachines) |
| Together AI | generic_json | 85 | 1 | 2026-10-24T15:05:18.909088+00:00 | [Careers](https://job-boards.greenhouse.io/togetherai) |
| World Labs | ashby | 8 | 1 | 2026-10-24T15:04:18.583773+00:00 | [Careers](https://jobs.ashbyhq.com/worldlabs) |
| LangChain | generic_json | 104 | 1 | 2026-10-24T15:07:40.188712+00:00 | [Careers](https://jobs.ashbyhq.com/langchain) |
| Cresta | generic_json | 87 | 1 | 2026-10-24T15:04:19.843256+00:00 | [Careers](https://job-boards.greenhouse.io/cresta) |
| Anyscale | ashby | 21 | 1 | 2026-10-24T15:04:21.613732+00:00 | [Careers](https://jobs.ashbyhq.com/anyscale) |
| Character.AI | ashby | 13 | 1 | 2026-10-24T15:04:21.835515+00:00 | [Careers](https://jobs.ashbyhq.com/character) |
| Descript | generic_json | 10 | 1 | 2026-10-24T15:05:21.314474+00:00 | [Careers](https://boards.greenhouse.io/descript) |
| Jasper | ashby | 9 | 1 | 2026-10-24T15:04:22.423434+00:00 | [Careers](https://jobs.ashbyhq.com/Jasper%20AI) |
| Pinecone | ashby | 8 | 1 | 2026-10-24T15:04:23.194836+00:00 | [Careers](https://jobs.ashbyhq.com/pinecone) |
| Weights & Biases | generic_json | 7 | 1 | 2026-10-24T15:07:40.193169+00:00 | [Careers](https://coreweave.com/careers/weights-biases) |
| LlamaIndex | ashby | 4 | 1 | 2026-10-24T15:04:24.015461+00:00 | [Careers](https://jobs.ashbyhq.com/llamaindex) |
| Clay | ashby | 58 | 1 | 2026-10-24T15:05:25.083648+00:00 | [Careers](https://jobs.ashbyhq.com/claylabs) |
| SambaNova | generic_json | 60 | 1 | 2026-10-24T15:05:25.493475+00:00 | [Careers](https://boards.greenhouse.io/sambanovasystems) |
| Stability AI | generic_json | 5 | 1 | 2026-10-24T15:08:31.926813+00:00 | [Careers](https://stability.ai/careers) |
| Hugging Face | generic_json | 6 | 7 | 2026-10-24T15:05:26.000988+00:00 | [Careers](https://apply.workable.com/huggingface/) |
| Modal Labs | ashby | 43 | 1 | 2026-10-24T15:07:47.370040+00:00 | [Careers](https://jobs.ashbyhq.com/modal) |
| Mercor | ashby | 112 | 1 | 2026-10-24T15:07:50.044097+00:00 | [Careers](https://jobs.ashbyhq.com/mercor) |
| Databricks | generic_json | 896 | 1 | 2026-10-24T15:07:50.137242+00:00 | [Careers](https://job-boards.greenhouse.io/databricks) |
| AI21 Labs | generic_html | 3 | 1 | 2026-10-24T15:08:31.956815+00:00 | [Careers](https://www.ai21.com/careers) |
| Cyera | generic_html | 256 | 18 | 2026-10-24T15:08:31.961816+00:00 | [Careers](https://www.cyera.com/careers) |

Representative source URLs, listing samples, warnings and original source responses are retained in the Site coordination workspace under `research/ai-expansion-20261024`. No private tracker data was used. Catalog schema/build, hash integrity and all catalog tests are required before publication.
