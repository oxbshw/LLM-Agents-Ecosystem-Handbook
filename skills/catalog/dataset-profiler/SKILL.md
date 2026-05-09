---
name: dataset-profiler
description: Use when first encountering a new dataset — produces a structured profile (schema, missingness, distributions, outliers, gotchas) before any analysis.
version: 0.1.0
status: experimental
risk: low
tags: [data, read-only, writes-files]
---

# Dataset Profiler

## When to use
- A new dataset arrives and you need to understand it before using it
- Before reproducing an analysis that referenced a dataset
- When data quality is suspect ("the chart looked wrong")

## When NOT to use
- Streaming / online data (this is point-in-time)
- Sensitive PII without an explicit allow-list

## Inputs
| Name | Type | Required | Notes |
|---|---|---|---|
| `path` | path | yes | CSV / Parquet / JSONL |
| `target` | string | no | column of interest (gets extra distribution detail) |

## Outputs
`profile.md` with: Source, Schema, Missingness, Distributions, Outliers, Joins / keys, Gotchas, Open questions.

## Workflow
1. Load with the right reader (extension-detected); record row count, file size
2. Schema: column → dtype → nullable → example value
3. Missingness: % per column, top columns by missingness
4. Distributions: numeric (min, p50, p95, max, std), categorical (top-k, cardinality)
5. Outliers: flag rows beyond p99 + 3·IQR for numerics
6. Identify potential keys (unique columns) and join candidates
7. **Gotchas**: timezone columns, mixed encodings, suspicious all-zero rows, magic values (`-1`, `9999-12-31`)
8. **Open questions**: ambiguous columns / values that need owner input

## References
- [`references/profile-template.md`](references/profile-template.md)

## Success criteria
- Every column appears in Schema + Missingness
- Outliers section includes example rows
- Gotchas section is non-empty (real datasets always have some)

## Failure modes
- File too large to read in memory → switch to streaming + sampled stats; flag prominently
- Encoding fails → try common alternatives; if all fail, surface and stop
