# Source-Bound Verification Playbook

**Updated 16 October 2026.** This repository is an architecture and evidence index. A reader should be able to trace each numeric claim to a defined source, environment, test command and evidence receipt—not merely to a screenshot.

## Acceptance rule

For each claimed passing suite, record the following as one immutable row:

| Field | Required |
| --- | --- |
| System | Product or named component; never a vague shared-portfolio label |
| Source identity | Repository, branch **and full commit SHA**, with an exact tree/build SHA when material |
| Test population | Command, test directory/families and whether subset, full suite or target-specific check |
| Environment | Operating system, runtime version and important dependencies |
| Execution proof | GitHub Actions run/job or retained exact-head locally executed log, dated |
| Outcome | Passes, failures, errors, skips, warnings, known N/A |
| Scope | Which proposition passed, and what **does not** follow |
| Status | Current source CI / exact branch CI / local retained qualification / smoke only / evidence absent |

## Never double-count

1. Python 3.11 and 3.12 CI running the **same** suite are repetitions, not twice as many independent tests.
2. Windows/Linux matrices do **not** increase unique test count unless each has truly distinct test cases, and the difference is documented.
3. Re-running `tests/test_self_service.py` after `pytest -q` does not add unique cases when already part of the full suite. CDD's extra 24-case invocation is a subset of the **76**.
4. Different frozen phase suites at the **same source SHA**, executed as disjoint paths, may be added when the test population is explicit: Prestige-Reforged Receiver reports **532 Phase 6 + 112 Phase 7 = 644**.
5. A development-branch successful run does **not** qualify `main`. A local source-bound result is not independent GitHub CI. Different products may use unrelated suites, so a multi-repository sum is only a snapshot subtotal.

## Current accessible evidence

See [current 15-system test ledger](CURRENT_TEST_EVIDENCE_2026-10-16.md), which records five countable test snapshots, CI/log provenance, **1,453 source-bound Viventia Python passes**, and all missing same-head results.

Two numerical examples:
- [CDD latest qualifying workflow](https://github.com/RazorglintLabs/ComplianceDriftDetector/actions/runs/38898754185), exact main commit `70e4bb865e149e0321151ef57a6a3adee7cbfa2d`: 76 unique Python tests.
- [Prestige-Reforged Receiver](https://github.com/RazorglintLabs/Prestige-Reforged/actions/runs/38883382477), exact candidate commit `fbeab53e9af27363a95c6eef151b8069c6df2842`: 532 + 112 disjoint tests.

**No all-15 recent test total has been established.** Private repositories with no retrievable Actions runs require an owner-provided exact-head qualification receipt or an explicitly authorized CI execution. A successful test suite does not mean system security, commercial availability, source authenticity or regulatory compliance.

[Architecture overview](../README.md) · [Test evidence ledger](CURRENT_TEST_EVIDENCE_2026-10-16.md).
