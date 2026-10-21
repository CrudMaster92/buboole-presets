# FreeHire membership in the Car Industry preset — separate implementation plan

The 2026-10-21 catalog change ships native monitor references only. FreeHire already contributes public discovery jobs to Buboole's combined search. A provider employer is not currently an installable native monitor, and the current catalog collection contract has no provider-membership field. Do not put `fh_company:*` IDs into `companies[].company_id` or silently extend the strict v3 schema.

## Proposed contract and behavior

1. Author a separate, versioned public discovery-membership artifact for each collection. Reference reviewed FreeHire employer slugs and evidence revisions, not copied jobs or scraper recipes. Keep native catalog v3 and its install/selection contract unchanged. The new capability must be explicit in its own manifest/schema and supported by consumers before publication.
2. Use a reviewed employer binding table. Prove each binding with matching original posting URLs, an employer-owned careers link or an explicit ATS employer identifier. Names, logos, common hosts and shared parent ownership alone are insufficient. Keep subsidiaries/regions distinct and preserve source IDs. The audit accompanying this change records observed overlaps; it does not authorize identity merges.
3. The canonical app's shared public-search adapter should resolve a collection into native company/monitor membership plus its reviewed provider references. Site owns only the hosted transport. Keep one typed behavior for human controls, browser tools and MCP callers. Read each peer project's instructions before implementation; do not edit a generated shared snapshot.
4. Apply exact `company_slug` filters through the existing FreeHire adapter, respecting its bounded query window, moving pages, caches and error states. Union results using the existing URL identity rules. Do not crawl or mirror FreeHire into the native collector, and do not infer membership from FreeHire's unrelated collections.
5. A single Car Industry filter may display both sources once the consumer supports the new manifest. Native monitors retain preview/install behavior. Provider-only employers are discovery-only and have no installation action until an independent native monitor exists. Existing personal criteria never change silently.
6. Show missing/stale/failed supplementary coverage honestly. A provider failure must not become zero jobs or a closure signal. Preserve successful native results and saved snapshots.

## Required checks before rollout

- Verified native/provider overlap deduplicates; similarly named dealers and unrelated NIO telecom jobs remain separate.
- Corporate BMW and BMWDealerCareers cannot alias by name; independent NAPA dealers cannot alias to UAP.
- Exact provider employer filters are applied; ignored parameters fail explicitly.
- Multiple company slugs, provider query-window exhaustion, cursor revision changes, offline reads and stale caches remain bounded and visible.
- Collection discovery and native monitor installation remain distinct in human UI, browser tools and MCP.
- Canonical shared tests, app build, generated-snapshot parity, Site tests/build, hosted API smoke tests and live collection coverage all pass before activation.

No runtime, shared UI, plugin, Muse, hosted Site or FreeHire service change is included in the scraper PR. This phase is a concrete design proposal for the separate step requested by the user.
