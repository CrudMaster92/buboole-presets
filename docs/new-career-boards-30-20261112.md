# 30 new career board scrapers

Created 30 employer-specific deterministic Ashby recipes; live validation returned 1,040 postings, all with descriptions.

Status: authored and validated locally. Public submission and merge remain pending authorization.

Each source uses all-role coverage and no pagination, role-count or description-count sampling cap. The public API supplies the full board in one response. Ownership comes from the employer’s official site; complete source IDs were independently compared with the real runtime result. Counts reflect validation time.

| Employer | Official ownership page | Public board | Observed postings |
|---|---|---|---:|
| Linear | [Official site](https://linear.app/careers) | [Careers](https://jobs.ashbyhq.com/linear) | 33 |
| Ramp | [Official site](https://ramp.com/careers) | [Careers](https://jobs.ashbyhq.com/ramp) | 176 |
| Drata | [Official site](https://drata.com/about/careers) | [Careers](https://jobs.ashbyhq.com/drata) | 23 |
| Supabase | [Official site](https://supabase.com/careers) | [Careers](https://jobs.ashbyhq.com/supabase) | 77 |
| MotherDuck | [Official site](https://motherduck.com/careers/) | [Careers](https://jobs.ashbyhq.com/MotherDuck) | 6 |
| Rillet | [Official site](https://www.rillet.com/about/careers) | [Careers](https://jobs.ashbyhq.com/rillet) | 42 |
| Numeric | [Official site](https://www.numeric.io/careers) | [Careers](https://jobs.ashbyhq.com/numeric) | 24 |
| Campfire | [Official site](https://campfire.ai/careers) | [Careers](https://jobs.ashbyhq.com/campfire) | 52 |
| Zip | [Official site](https://zip.com/careers) | [Careers](https://jobs.ashbyhq.com/zip) | 98 |
| AirOps | [Official site](https://www.airops.com/) | [Careers](https://jobs.ashbyhq.com/airops) | 15 |
| Writer | [Official site](https://writer.com/company/careers/) | [Careers](https://jobs.ashbyhq.com/writer) | 43 |
| Mutiny | [Official site](https://www.mutinyhq.com/join-us) | [Careers](https://jobs.ashbyhq.com/Mutiny) | 7 |
| Unify | [Official site](https://www.unifygtm.com/careers) | [Careers](https://jobs.ashbyhq.com/unify) | 11 |
| Plain | [Official site](https://www.plain.com/careers/forward-deployed-engineer) | [Careers](https://jobs.ashbyhq.com/plain) | 5 |
| Pylon | [Official site](https://www.usepylon.com/careers) | [Careers](https://jobs.ashbyhq.com/pylon-labs) | 14 |
| Delphi | [Official site](https://www.delphi.co/careers) | [Careers](https://jobs.ashbyhq.com/delphi) | 5 |
| Trigger.dev | [Official site](https://trigger.dev/careers) | [Careers](https://jobs.ashbyhq.com/triggerdev) | 5 |
| Inngest | [Official site](https://www.inngest.com/) | [Careers](https://jobs.ashbyhq.com/inngest) | 2 |
| Runpod | [Official site](https://www.runpod.io/careers) | [Careers](https://jobs.ashbyhq.com/runpod) | 21 |
| Inference.net | [Official site](https://inference.net/) | [Careers](https://jobs.ashbyhq.com/inference) | 5 |
| Prime Intellect | [Official site](https://www.primeintellect.ai/careers/cbaa59ec-c133-400a-a0ae-ae95857f0690) | [Careers](https://jobs.ashbyhq.com/PrimeIntellect) | 37 |
| Lambda | [Official site](https://lambda.com/careers) | [Careers](https://jobs.ashbyhq.com/lambda) | 92 |
| Pika | [Official site](https://pika.art/careers) | [Careers](https://jobs.ashbyhq.com/pika) | 18 |
| Higgsfield | [Official site](https://higgsfield.ai/) | [Careers](https://jobs.ashbyhq.com/higgsfieldai) | 97 |
| Cartesia | [Official site](https://www.cartesia.ai/careers) | [Careers](https://jobs.ashbyhq.com/cartesia) | 23 |
| Deepgram | [Official site](https://deepgram.com/careers) | [Careers](https://jobs.ashbyhq.com/Deepgram) | 66 |
| Rime | [Official site](https://www.rime.ai/) | [Careers](https://jobs.ashbyhq.com/rime) | 3 |
| Bland AI | [Official site](https://www.bland.ai/careers) | [Careers](https://jobs.ashbyhq.com/bland) | 16 |
| Vapi | [Official site](https://vapi.ai/careers) | [Careers](https://jobs.ashbyhq.com/vapi) | 5 |
| Retell AI | [Official site](https://www.retellai.com/careers) | [Careers](https://jobs.ashbyhq.com/retell-ai) | 19 |

The adjacent JSON includes validation timestamps, recipe and inventory hashes, ownership evidence, warning lists, source samples and runtime provenance. Raw official pages, independent inventories and normalized results are retained in the Site workspace research folder.

Validation: catalog schema, catalog production build and catalog tests; canonical runtime export integrity; public collector tests; exact feed-pin hashes and preservation of prior pins. See the Site review record for final check results.
