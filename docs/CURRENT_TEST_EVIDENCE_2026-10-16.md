# Current GitHub Test Evidence — 16 October 2026

**Audited through GitHub repository contents, branch identity, Actions metadata and selected job logs.** This is a read-only evidence reconciliation: GitHub connector access in this session does **not** provide a general dispatch of new test runs across private repositories. Thus **not all 15 systems were freshly executed today**.

## What the numbers mean

The README displays **five distinct test-suite snapshots**, not one synchronized project-wide execution. Every numeric row below identifies its specific candidate source, proof, platform and limitations.

| System | Qualified source | Passes (unique suite) | Evidence | Qualification boundary |
| --- | --- | ---: | --- | --- |
| **Viventia** | `931ac7462e30df16ff83ae857853ab07fe231681` (private `work/veac-restart-continuity-001-recovery-truth`) | **1,453** | [Exact-branch retained evidence, 13 Sep](https://github.com/RazorglintLabs/viventia-veac/blob/main/scars/RESTART-CONTINUITY-001/evidence/2026-09-13_corrected_branch_clear.md) | Python full suite, **1 skipped**, 1 known warning. Locally reported against clean correction branch, not an Oct 16 `main` or independent CI rerun. Separate [11 Sep GitHub Actions qualification](https://github.com/RazorglintLabs/razorglint-sentinel/actions/runs/34602143209) confirms 1,429 Windows Python passes at a *different* exact commit, plus Go and Rust success; **do not add 1,429 to 1,453**. |
| **Prestige-Reforged** | `fbeab53e9af27363a95c6eef151b8069c6df2842` (private `release/windows-markdown-filter-20261016`) | **644** | [16 Oct Receiver Gate](https://github.com/RazorglintLabs/Prestige-Reforged/actions/runs/38883382477) | Receiver log reports Phase 6 **532/532** and a **separate** Phase 7 `unittest discover -s phase7_tests` **112/112** with no failures. Disjoint named suites. A distinct G2 source-import gate failed; no released customer installer claim. |
| **EU AI Act Evidence Readiness** | `e36f1eae49e8309ebc696ea53b5510fa31686122` (private `ux/evidence-readiness-figma-and-ci-gate`) | **86** | [14 Oct regression job](https://github.com/RazorglintLabs/EU-AI-Act-Evidence-Readiness-Sprint/actions/runs/38637473818) | `pytest` reported **86 passed**; branch candidate, not re-executed at default `main`. |
| **Compliance Drift Detector** | `70e4bb865e149e0321151ef57a6a3adee7cbfa2d` (public `main`) | **76** | [16 Oct CI matrix](https://github.com/RazorglintLabs/ComplianceDriftDetector/actions/runs/38898754185) | 76 full-suite passes on Python 3.11/3.12 Windows/Linux; later 24-case `tests/test_self_service.py` rerun **is a subset** of those 76, so counted **once only**. Separate [Windows native build](https://github.com/RazorglintLabs/ComplianceDriftDetector/actions/runs/38898754224) succeeded. |
| **VEAC** | `cc245ddd118884d54a9909545b9448a146522b79` (private `feature/veac-local-intake-preflight`) | **66** | [14 Oct examiner self-assurance](https://github.com/RazorglintLabs/viventia-veac/actions/runs/38639994394) | `unittest` **Ran 66 tests ... OK**; four OS/Python matrix jobs are **repeat executions of the same suite**, not 264 distinct tests. Examiner self-tests do not certify Viventia. |

**Traceable subtotal:** 1,453 + 644 + 86 + 76 + 66 = **2,325 distinct cases across five selected suite snapshots**. The Viventia receipt is repository-retained local execution, whereas the other four figures were independently checked in CI logs. These are not simultaneous, not all against default branches and **not** a count of the entire Razorglint engineering estate.

## All 15 GitHub reconnaissance records

| # | Asset | Accessible code/evidence source | GitHub status observed 16 Oct | Why not added to the five-suite subtotal |
| ---: | --- | --- | --- | --- |
| 01 | Prestige-Reforged | [private source](https://github.com/RazorglintLabs/Prestige-Reforged) | **644 branch-qualified** | Counted once; UI G2 import gate [fails separately](https://github.com/RazorglintLabs/Prestige-Reforged/actions/runs/38895762509) |
| 02 | SAR | [private `sar`](https://github.com/RazorglintLabs/sar), `main` at `7c6f2aab2317d44b46241eee0c953619b0612d84` | Repository with test modules, **no Actions runs found** | No current same-head runner summary |
| 03 | Viventia | [private `razorglint-sentinel`](https://github.com/RazorglintLabs/razorglint-sentinel), `main` at `49fe0f77a50739eccc78d9bd9819447c61f6df7a` | **1,453 in a dated exact correction branch** | Counted once, *not* represented as a `main` PASS |
| 04 | VEAC | [private `viventia-veac`](https://github.com/RazorglintLabs/viventia-veac), `main` at `c764a0f2d4969862a2211b0fa8abc9e9868f11b7` | **66 feature-branch CI** | Counted once; not a `main` test |
| 05 | CDD | [public repo](https://github.com/RazorglintLabs/ComplianceDriftDetector) | **76 current-`main` CI** | Counted once |
| 06 | OpenClaw | Standalone repo not located in installed repository listing | **Not independently testable from accessible GitHub sources** | Requires canonical repo/ref + current test receipt |
| 07 | Voidlock | Standalone repo not located in installed repository listing | **Not independently testable from accessible GitHub sources** | Requires canonical repo/ref + current test receipt |
| 08 | Blackiron | [private `Blackiron`](https://github.com/RazorglintLabs/Blackiron), `main` at `24e12dbcaba3402868dd8e02a91b73a2918b1e7f` | Rust test source present, **no Actions runs found** | `cargo test` latest-head result not evidenced |
| 09 | ProofChain | Standalone repo not located in installed repository listing | **Not independently testable from accessible GitHub sources** | Requires canonical repo/ref + current test receipt |
| 10 | SealVault | [private `SealVault`](https://github.com/RazorglintLabs/SealVault), `main` at `2319af4158b2f7ada1f49af0eaa753a62c164580` | Rust, Go, TypeScript code present; **no Actions runs found** | Missing latest-head multi-language test receipt |
| 11 | Command Guardian | [private `command-guardian`](https://github.com/RazorglintLabs/command-guardian), `main` at `bbd013adf21f921f948d2ee489f39be8e7d4a16b` | Successful latest-head CI exists but is **outside the Sep/Oct current audit window** | Intentionally no stale count republished |
| 12 | FleetSim | Standalone repo not located in installed repository listing | **Not independently testable from accessible GitHub sources** | Requires canonical repo/ref + current test receipt |
| 13 | EU AI Act evidence readiness | [private source](https://github.com/RazorglintLabs/EU-AI-Act-Evidence-Readiness-Sprint), `main` at `90d8dc2591c731391f3dbc5f89cab3e475090215` | **86 feature-branch CI** | Counted once; no `main` retest |
| 14 | ReasonForge | [private `rdl-showroom`](https://github.com/RazorglintLabs/rdl-showroom), `main` at `8c73dcce1e875b6adf0355a66e9b7ec4da81d3b7` | [12 Oct CI smoke](https://github.com/RazorglintLabs/rdl-showroom/actions/runs/38229965533) **success** on 3 Python versions | Smoke does not disclose a comparable whole-product unique test count |
| 15 | CalledIt | [private `CalledIt`](https://github.com/RazorglintLabs/CalledIt), `main` at `72cecd2652ac7a3350cc59bfe38733cb41036ef1` | Source repo exists, **no Actions runs found** | No recent full-suite execution available |

### Languages confirmed in source

- **Python:** CDD and Viventia Python source/test trees, Prestige-Reforged and VEAC execution.
- **Go:** Viventia `product/launcher/go.mod` with Go source; SealVault `server/go.mod` and Go source. Viventia [qualification run 34602143209](https://github.com/RazorglintLabs/razorglint-sentinel/actions/runs/34602143209) includes a successful Go job. A Go **test case count** was not established in that log, so no integer is invented.
- **Rust:** Viventia Rust verifier and Blackiron/SealVault Rust implementations. Viventia Go/Rust success lanes should not be added to Python counts without distinct exact-suite summaries.
- **TypeScript:** SealVault source and additional documented UI/client components, not necessarily every asset.

### Required to publish a complete all-15 headline

For each missing row, obtain an executable source path, exact commit, local or GitHub Actions run, test command, results (**passed/failed/skipped**) and any dependency/IP restrictions. For multi-language assets, count nonoverlapping test functions **once**, not repeated Windows/Linux/Python matrix jobs. Source archives and the original historical records remain preserved separately; none are part of the current README's numerical assertions.

A full contemporary 15-system total **cannot currently be substantiated** from the accessible evidence. This is an actionable audit finding, not permission to insert an impressive guess.
