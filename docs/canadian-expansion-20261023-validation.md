# Canadian employer expansion — October 23, 2026

Adds 20 large Canadian employers absent from the base Buboole catalog. Each uses its official public Workday board, with a reusable normalized identity and recipe. Existing companies and monitors are unchanged.

FreeHire was screened directly through its public companies API because the ChatGPT Buboole connector required reauthentication. Most targets already have FreeHire matches: this is independent Buboole coverage, not a claim that these employers are missing from both feeds. FreeHire company counts are global and are not comparable to Canadian posting totals. Search can be fuzzy; all returned candidates and query parameters are retained in the evidence file.

## Validation status

Direct public HTTP checks returned job listings and descriptions for all 20. Forty trimmed real records replayed successfully through the current canonical runtime, including descriptions and original source URLs. Logos were downloaded, decoded and visually inspected. The read-only GitHub workflow runs fresh live runtime and Chromium embedding checks using an exact exported runtime commit; all 20 source checks have passed on GitHub and author verification now records those dated counts and warnings. The combined workflow then failed on a Playwright viewport argument in its logo helper; that helper is fixed and the browser embedding check is being rerun. The workspace DNS guard was not disabled.

## Scope

Country facets are pinned where the employer publishes them. Canada Goose, Intact and Element use explicitly Canadian-labelled location subsets; those can omit other current or future Canadian locations. Desjardins does not publish a country facet on this board. Canadian Tire includes group brands such as Marks; Restaurant Brands includes Tim Hortons; Enbridge includes its group subsidiaries. Cross-border postings may list Canada as an additional location rather than the primary country. Every recipe declares partial listing coverage and supports resumable all-role traversal within that scope.

| Employer | Scope | Observed advertised count |
|---|---|---:|
| BMO Financial Group | Canada country facet | 535 |
| CIBC | Canada country facet | 477 |
| Desjardins | Official Desjardins board with Canadian roles; no country facet published; partial employer scope | 298 |
| Manulife | Canada country facet | 169 |
| Sun Life | Canada country facet | 79 |
| Intact Financial Corporation | Explicitly labelled Canadian location subset; additional Canadian locations may be omitted | 152 |
| Enbridge | Canada country facet | 22 |
| Suncor Energy | Canada country facet | 27 |
| Cenovus Energy | Canada country facet | 25 |
| Canadian Tire Corporation | Canada country facet | 133 |
| AtkinsRéalis | Canada country facet | 717 |
| Saputo | Canada country facet | 95 |
| Finning International | Canada country facet | 63 |
| Thomson Reuters | Canada country facet | 72 |
| CAE | Canada country facet | 100 |
| TC Energy | Canada country facet | 27 |
| Restaurant Brands International | Canada country facet | 34 |
| Canada Goose | Explicitly labelled Canadian location subset; additional Canadian locations may be omitted | 53 |
| Element Fleet Management | Explicitly labelled Canadian location subset; additional Canadian locations may be omitted | 3 |
| GFL Environmental | Canada country facet | 345 |

Advertised counts are point-in-time source observations, not promises of unique or complete live feed coverage.

## Publication

This batch changes authored preset data only. It does not activate sources in the public jobs feed. The collector still needs an intentional reviewed catalog-lock update before collecting these new monitors.

[HTTP, ownership, logo and FreeHire evidence](canadian-expansion-20261023-evidence.json) · [Trimmed parser fixtures](canadian-expansion-20261023-fixtures.json)

Live runtime evidence: https://github.com/CrudMaster92/buboole-presets/actions/runs/39997135793 (all 20 recipe checks passed; browser helper failure is recorded separately).
