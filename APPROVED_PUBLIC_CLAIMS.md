# Approved Public Claims — Razorglint Labs

**Generated:** 2026-04-27  
**Verdict:** SAFE_TO_SAY — each claim below is directly supported by cited evidence.

---

## Portfolio — Test Counts

| # | Claim | Verdict | Evidence Artifact | Notes |
|---|-------|---------|-------------------|-------|
| 1 | "Razorglint has 3,400+ executed passing tests across its audited portfolio proof surface." | SAFE_TO_SAY | `PROOF_AUDIT_2026-04-26.md` — actual total 3,505 | Rounded down. Defensible. |
| 2 | "15 independently testable systems." | SAFE_TO_SAY | `README.md` system inventory | Each system has its own repo and test suite |
| 3 | "Every number can be reproduced by running pytest or cargo test in the corresponding repository." | SAFE_TO_SAY | `PROOF_AUDIT_2026-04-26.md` methodology section | Assumes Python 3.11+ / Rust 2021 installed |
| 4 | "Test counts are from direct execution, not inventory or marketing math." | SAFE_TO_SAY | `PROOF_AUDIT_2026-04-26.md` methodology section | |

---

## Command Guardian

| # | Claim | Verdict | Evidence Artifact | Notes |
|---|-------|---------|-------------------|-------|
| 5 | "Command Guardian is a hardened local-first command enforcement prototype with 131/131 tests passing after emergency remediation." | SAFE_TO_SAY | `proof_command_guardian_131_pass_hardened.jpg`, `ENTERPRISE_AUDIT_REPORT.md` §14–15 | |
| 6 | "Command Guardian closes the critical bypass classes identified in the audit's tested set." | SAFE_TO_SAY | `ENTERPRISE_AUDIT_REPORT.md` §14, `test_adversarial_bypasses.py` (35 tests) | Scoped to "tested set" — not "all bypasses" |
| 7 | "DENY receipts now store command hashes instead of raw dangerous command strings." | SAFE_TO_SAY | `test_receipt_sanitization.py`, `receipts.py` sanitization logic | |
| 8 | "Token issuance is now audit-receipted in Command Guardian." | SAFE_TO_SAY | `ENTERPRISE_AUDIT_REPORT.md` §14, `test_runner_enforcement.py` token tests | |
| 9 | "Command Guardian's earlier v1.0.0 release has been marked superseded." | SAFE_TO_SAY | GitHub release metadata, `ENTERPRISE_AUDIT_REPORT.md` §7 | |

---

## SAR Governance

| # | Claim | Verdict | Evidence Artifact | Notes |
|---|-------|---------|-------------------|-------|
| 10 | "SAR enforces policy with fail-closed behavior. Invalid policy = hard stop." | SAFE_TO_SAY | SAR test suite (497 Python + 13 Rust), `_CONTROL/SAR_APPROVED_CLAIMS.md` | |
| 11 | "The system that approves the operation never runs the operation." | SAFE_TO_SAY | SAR architecture, separation of governance and execution | Core design principle with structural enforcement |
| 12 | "SAR receipts are Ed25519 signed and hash-chained." | SAFE_TO_SAY | SAR receipt chain code, cross-verification tests | |
| 13 | "SAR has 10 approved claims, each backed by test evidence, from a 29-claim universe." | SAFE_TO_SAY | `_CONTROL/SAR_APPROVED_CLAIMS.md`, `_CONTROL/SAR_FORBIDDEN_CLAIMS.md` | |

---

## OpenClaw

| # | Claim | Verdict | Evidence Artifact | Notes |
|---|-------|---------|-------------------|-------|
| 14 | "OpenClaw agents run under SAR governance. No agent defines its own rules." | SAFE_TO_SAY | OpenClaw dual-write architecture, 1,578 passing tests | |
| 15 | "Every agent action produces a receipt. Every output is exportable as a Truthpack." | SAFE_TO_SAY | OpenClaw test modules — dual-write + truthpack coverage | |
| 16 | "1,578 tests passing across 45 test modules." | SAFE_TO_SAY | `PROOF_AUDIT_2026-04-26.md`, `proof_openclaw_test_1578_pass.jpg` | 156 skipped noted in audit |

---

## Prestige-Forge

| # | Claim | Verdict | Evidence Artifact | Notes |
|---|-------|---------|-------------------|-------|
| 17 | "Prestige-Forge checks claims against evidence before publication. Unsafe claim = blocked." | SAFE_TO_SAY | Claims Safety Engine M-018, Client Zero 25/25 PASS, 15/15 SAFE TO SAY | |
| 18 | "690 core tests across 15 constitutional families and 19 core modules." | SAFE_TO_SAY | `PROOF_AUDIT_2026-04-26.md`, `proof_pf_test_690_pass.jpg` | |
| 19 | "stdlib-only Python in the proof path. Reproducible on any machine with Python 3.11+." | SAFE_TO_SAY | Prestige-Forge CHECKPOINT.md, codebase inspection | |

---

## EU AI Act Sprint

| # | Claim | Verdict | Evidence Artifact | Notes |
|---|-------|---------|-------------------|-------|
| 20 | "EU AI Act tooling maps evidence to articles and exposes gaps — it does not claim compliance." | SAFE_TO_SAY | EU AI Act Sprint README, report output contract | |
| 21 | "194 tests passing. Covers Articles 9, 11, 12, 13, 14, 15." | SAFE_TO_SAY | `PROOF_AUDIT_2026-04-26.md`, `proof_euai_test_194_full.jpg` | 6 env-drift exclusions documented |
| 22 | "The evidence compiler never writes back into any source system." | SAFE_TO_SAY | EU AI Act Sprint architecture — one-directional data flow | |

---

## FleetSim

| # | Claim | Verdict | Evidence Artifact | Notes |
|---|-------|---------|-------------------|-------|
| 23 | "FleetSim tests trust-plane enforcement with severity ladder and transition receipts." | SAFE_TO_SAY | 103 tests, `proof_fleetsim_test_103_pass.jpg` | |
| 24 | "103 tests passing. Fleet Reflex Loop: heartbeat → distress pulse → reflex receipt." | SAFE_TO_SAY | `PROOF_AUDIT_2026-04-26.md` | |

---

## Cryptographic Infrastructure

| # | Claim | Verdict | Evidence Artifact | Notes |
|---|-------|---------|-------------------|-------|
| 25 | "The systems produce tamper-evident evidence through hash-chained receipts." | SAFE_TO_SAY | SAR, CG, OpenClaw receipt chains; Blackiron chain module | "Tamper-evident" not "tamper-proof" |
| 26 | "Blackiron provides domain-separated Merkle trees that prevent second-preimage attacks." | SAFE_TO_SAY | Blackiron source, 53 tests, `DOCTRINE.md` | |
| 27 | "132 Rust tests across 6 infrastructure crates, all passing." | SAFE_TO_SAY | `PROOF_AUDIT_2026-04-26.md`, `proof_rust_modules_test_132_pass.jpg` | 24 env-skip documented |

---

## Architecture

| # | Claim | Verdict | Evidence Artifact | Notes |
|---|-------|---------|-------------------|-------|
| 28 | "Every system is sovereign — independently deployable, independently testable, independently sellable. No shared runtime." | SAFE_TO_SAY | Non-Dilution Architecture Doctrine, system inventory | |

---

*28 claims classified SAFE_TO_SAY. Each is directly reproducible from the cited evidence artifact.*
