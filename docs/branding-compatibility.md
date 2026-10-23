# Buboole branding and compatibility

Use **Buboole** in human-facing product names, catalog messages, documentation,
and schema titles. The older name remains in compatibility identifiers; those
identifiers are not display branding and must not be replaced mechanically.

## Catalog contracts

Keep the existing schema filenames and `$id`, `jobhound-*` format values,
`min_jobhound_version`, install payloads, and loopback install endpoint intact.
Current Buboole readers require these exact contracts. The version-1 preset
schema's recipe definitions also validate current monitor documents through
`scripts/build_catalog.py`; they are not limited to legacy import validation.

A branding-only change must preserve company and monitor IDs, recipe behavior,
verification evidence, and request hosts. Historical structured evidence and
submitted proposal packages retain their recorded contents. If a collection's
display metadata changes, increment that collection's revision.

## Application migration

The public jobs runtime is generated from the canonical Buboole application
using `scripts/export_public_jobs.py`. Workspace launcher/docs are generated
from its `integrations/agent-workspace` source. Make application and launcher
changes there and export them together with their required manifests; do not
patch release archives or fork the exported runtime.

An application migration should introduce new command and configuration names
as aliases first, retain old command entry points and tool names, accept old
serialized formats and repository identities during transition, and keep using
the existing private profile/database unless an explicit tested migration is
provided. Renaming a profile directory by default can make an existing account
appear empty. Repository URLs and strict repository identity checks need to be
updated together. A repository slug can change without changing a schema format.

The currently deployed public jobs workflow reads `catalog-lock.json` directly.
It does not invoke the newer receipt-admission modules. A catalog branding
change does not automatically admit or refresh public-feed sources, and this
cleanup does not change that publication path.

## Verification

Run the existing catalog build, legacy import validation, and unit tests.
Verify that the browser handoff still emits `jobhound-catalog-install` version 1
with the existing selection limits and endpoint. Review changes to authored JSON
separately from generated output, and do not commit `dist`.
