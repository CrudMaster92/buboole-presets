# Gaming expansion — 24 October 2026

## Scope and evidence

The supplied Newzoo URL redirects to https://newzoo.com/products/games-market-reports. It no longer exposes a public company ranking; the former top-25 ranking URL redirects to the articles index. No paid report or account access was used.

Compared all 25 names in Table 20 (printed page 86) of the EU European Media Industry Outlook (September 2025), explicitly attributed to **Newzoo Games Market Report & Forecast, December 2024 Update**, with 2023 revenues. This is a historical benchmark, not the current paid top 100. Source: https://www.europacreativa-media.it/documenti/allegati/2025/the-european-media-industry-outlook.pdf

FreeHire cross-check: 30 targeted ranking/gap queries; all 18 offset pages of the `domains=gamedev` company search (1,727 unique slugs). This domain includes unrelated companies and is not a gaming-employer roster. Exact-name/alias comparison identified 139 records explicitly tagged gaming outside the original collection; these include aliases, parents, platforms and gambling businesses, so they are leads, not 139 proven missing employers. Detailed source review covered 41 selected records plus the six earlier gaming-gap leads. The remaining directory leads were not all live-validated. Raw queries and responses are retained in the Site research folder.

## Result

Prepared **21 new company identities and 21 deterministic monitors**, taking Gaming from **101 to 122** members (revision 8). The live canonical scraper checks observed **572 normalized source listings**. This includes general-interest/talent listings, and is not 572 newly deduplicated jobs: existing parent sources and FreeHire may already contain some postings. Recipes run through the canonical application runtime and the independent public collector; no app code or personal tracker state is changed.

| Company | Strategy | Observed listings | Complete | Ownership evidence |
|---|---|---:|---|---|
| Xsolla | lever | 187 | yes | https://xsolla.com/careers |
| Spellbrush | ashby | 10 | yes | https://spellbrush.com/careers |
| VRChat | lever | 11 | yes | https://hello.vrchat.com/careers |
| Sky Mavis | ashby | 6 | yes | https://skymavis.com/ |
| Mob Entertainment | generic_json | 8 | yes | https://mobentertainment.com/ |
| Linden Lab | generic_json | 4 | yes | https://lindenlab.com/careers |
| Voldex | ashby | 5 | yes | https://voldex.com/careers/ |
| A Thinking Ape | generic_json | 1 | yes | https://athinkingape.com/careers/ |
| PlayQ | generic_json | 2 | yes | https://www.playq.com/careers |
| Second Dinner | ashby | 1 | yes | https://seconddinner.com/ |
| Garena | generic_json | 85 | partial | https://careers.garena.com/global/careers |
| 37 Interactive Entertainment | generic_html | 40 | partial | https://zhaopin.37.com/index.php?a=viewPublishList&c=index&campus=1&m=mobile&type=1 |
| Pearl Abyss | generic_json | 9 | partial | https://www.pearlabyss.com/en-US/Company/Careers/Intro |
| Ludia | generic_json | 9 | partial | https://ludia.bamboohr.com/careers |
| Virtuos | generic_json | 80 | partial | https://www.virtuosgames.com/careers/ |
| Scorewarrior | ashby | 23 | yes | https://scorewarrior.com/careers |
| NEOWIZ | lever | 24 | yes | https://www.neowiz.com/kr/career |
| Discord | generic_json | 46 | yes | https://discord.com/careers |
| Pocket Worlds | ashby | 4 | yes | https://www.pocketworlds.com/careers.js |
| Smoking Gun Interactive | generic_json | 10 | partial | https://smokingguninc.com/careers/ |
| Huuuge Games | generic_json | 7 | partial | https://huuugegames.com/ |

## Ranking reconciliation

- Existing publisher/platform records cover Tencent, Sony Interactive Entertainment, Microsoft Gaming, NetEase, Electronic Arts, Nintendo, Take-Two, Nexon, Roblox, Bandai Namco, Playtika, Warner Bros. Games, Ubisoft, Square Enix, Krafton and Sega. Parent ranking names do not establish that all divisions are collected.
- Added Garena as the gaming-business lead for ranked Sea Group, and 37 Interactive Entertainment. Garena is a dedicated gaming board, not a general Sea/Shopee feed.
- Apple and Google already have catalog identities outside Gaming. Their broad corporate feeds are not silently added to Gaming without a supported gaming-unit scope.
- CyberAgent has related Cygames coverage in Gaming; this is subsidiary coverage, not a full parent-group scraper.
- Netmarble: official `/home` is public; attempted job-list routes returned 401. Its US Workable board reported no openings in earlier research. No credentials or access bypass used.
- Embracer: official Join Our Team page delegates recruitment to individual subsidiaries. Existing studio monitors do not prove a consolidated group feed.
- Konami Digital Entertainment: the US page exposes one inline opening plus an applicant privacy notice; Japan list responses lacked populated role links, and the EU URL returned a country selector. No casino-company namesake or privacy notice is imported as a video-game vacancy. A robust general inline-role extractor remains a separate adapter task.
- Century Huatong: do not equate the whole ranked parent with Century Games. The international Century Games careers page links LinkedIn; the China careers endpoint did not complete successfully during this research. Its FreeHire jobs are third-party board leads. No fabricated group monitor.

## FreeHire holds and source decisions

- `ncsoft.pinpointhq.com` contains ACME/Hooli sample divisions, demo locations and placeholder content. It is not accepted as production NCSoft coverage. The real NC America page exposes general applications; the Korea listing API returned 403 under the canonical supported request formats.
- Devolver: FreeHire reports a QA Manager, but the referenced BambooHR listing endpoint currently returns zero and the official careers request returned 429.
- Pipeworks: the dedicated Pinpoint board returned four listings including an unpartitioned Virtuos Montreal HR role. Held rather than assign group jobs to the studio.
- Amber Studio, Kokku and Arkadium: official linked feeds returned no normalized listings. Fortis Games’ official declared board returned no listings. They are not added as verified sources.
- Scorewarrior: Telegram mirror ignored; official Ashby board used. PlayQ: Trakstar test posting ignored; official Greenhouse board used. Big Viking Games test/talent listings were not promoted.
- Existing PlayStation, Nexon, King, Homa and other parent/alias records require overlap review before adding name-only duplicates. Event-company Insomniac is not Insomniac Games.

## Coverage limits

Garena uses the observed official global POST job-list API (85 records, all single-location at validation). 37 Interactive uses the public mobile operations category (40 records), not all departments. Pearl Abyss is Europe-only. Virtuos uses the first 100 group requisitions (80 returned) and may include its own studio brands. Its group ownership is explicit. Ludia and other feeds preserve visible general-application titles. Workable duplicate source IDs are deduplicated by the canonical runtime. Bounded detail enrichment and partial feeds keep `metadata.partial_listing: true`; incomplete source records must not close unseen jobs. No request uses cookies or credentials.

## Review and publication

Required catalog validator, production catalog builder and repository tests are run on this source-only worktree. Generated `dist` artifacts are excluded from the contribution. Public-collector results and an isolated feed smoke generation validate the dependent pins. The dependent feed change preserves every existing pin and adds only these reviewed sources.

These changes are local review candidates. Submission requires explicit human publication consent under the public-contribution workflow. No merge or production publication is authorized by an audit result. After approval and reviewed merge, verify catalog hashes, source commit, deployed feed generation, all added source statuses, and website collection/company coverage. Until then the live collection remains unchanged.
