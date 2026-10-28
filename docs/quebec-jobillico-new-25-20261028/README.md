# 25 complete employer boards — October 28, 2026

Adds 25 new employer identities and 25 deterministic all-role monitors. All selected sources are dedicated Jobillico employer listings in Québec. Each current board fits in one complete listing page; no capped page or role limit is configured. Job details were fetched for every listing in the validation run.

## Live results

The Buboole runtime returned **317 current postings** across all 25 boards. Each count matched both the Jobillico employer directory count and an independent raw-card URL audit. All 317 results have a job detail description. Every traversal completed with no continuation and no warnings.

| Employer | Current postings |
|---|---:|
| Acier Trimax | 7 |
| Aliments Asta inc. | 12 |
| ATTITUDEliving | 20 |
| CBR Laser inc. | 6 |
| Cegerco inc. | 9 |
| Entosystem | 6 |
| Fabrimet inc. | 13 |
| Genifab inc. | 6 |
| Gosselin Express ltée & Les Sables Olimag inc. | 7 |
| Groupe Castech/Plessitech Inc. | 8 |
| Groupe conseil UDA | 20 |
| Groupe Maska inc. | 7 |
| GUAY | 23 |
| IGA Alimentation A.D.R. Inc. | 17 |
| Inter-Cité Construction ltée | 20 |
| Le Groupe Bell-Horizon inc. | 11 |
| Le Marché Végétarien | 17 |
| Machitech | 22 |
| Novolecs inc. | 11 |
| Pièces d’auto GGM | 11 |
| Posi-Plus Technologies inc. | 8 |
| Structures d'acier Élite INC. | 13 |
| Terapro | 17 |
| Valcourt Sécurité inc. | 14 |
| Équipements ART | 12 |

## Source scope

Each monitor reads the full employer-specific Jobillico listing. The recipe selector requires a dated posting card and an exact company-specific `/fr/offre-d-emploi/<employer>/` or `/fr/opportunite-d-emploi/<employer>/` URL. A fresh raw-board parse found no missing or extra posting URLs compared with runtime output. No spontaneous-application bank or neighboring employer postings are included. Counts are point-in-time observations.

## Catalog and FreeHire screen

The 25 identities were checked against baseline preset commit `695b506aad1c6f6b1f4762e238aa38f89358950d` (1395 company identities): no normalized ID, company-name or alias match was found. A fresh public FreeHire `/api/v1/companies?q=` check returned successfully for every name and found zero normalized exact company-name matches. The raw query responses and nearby names are retained in `freehire-screen.json`; token-level results can include unrelated employers with common words.

## Geography

All 25 boards are Canada-only listings. I make no USA-and-Canada hiring claim for this batch.

## Evidence

`live-evidence.json` records runtime counts, completeness, detail coverage and timestamps. `pagination-audit.json` records raw employer card counts and URL-set comparisons. `freehire-screen.json` records catalog and FreeHire checks. `runtime-provenance.json` and `validation-results.json` record the runtime and required repository checks.
