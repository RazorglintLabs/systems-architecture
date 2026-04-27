# Forbidden Public Claims — Razorglint Labs

**Generated:** 2026-04-27  
**Verdict:** FORBIDDEN or UNSAFE_OVERCLAIM — these claims must not appear in any public-facing material.

---

## FORBIDDEN — Absolute Prohibitions

These claims have zero supporting evidence or directly contradict known truth.

| # | Forbidden Claim | Verdict | Reason | Safer Replacement |
|---|----------------|---------|--------|-------------------|
| 1 | "Razorglint systems are production-ready." | FORBIDDEN | No system has undergone independent production hardening review. CG explicitly "not production-ready." | "Hardened prototypes with executed test suites." |
| 2 | "Certified compliant with the EU AI Act." | FORBIDDEN | No certification body has reviewed. EU AI Act Sprint explicitly disclaims compliance. | "Evidence-mapped to EU AI Act Articles 9, 11, 12, 13, 14, 15. Gaps identified, not hidden." |
| 3 | "EU AI Act compliant." | FORBIDDEN | Same as above. No compliance certification exists. | "EU AI Act evidence-ready." |
| 4 | "Tamper-proof audit trail." | FORBIDDEN | Hash chains are tamper-*evident*, not tamper-*proof*. Tampering is detectable, not prevented. | "Tamper-evident audit trail — alteration is mathematically detectable." |
| 5 | "Impossible to bypass." | FORBIDDEN | CG enterprise audit (§4) documents bypass classes that existed and were closed. Only the *tested* classes are covered. | "Tested bypass classes closed. Coverage of all possible vectors is not claimed." |
| 6 | "Military-grade security." | FORBIDDEN | No military certification (FIPS, CC, DISA STIG). No defense contracts. No independent security audit. | Do not use. No replacement needed. |
| 7 | "Hardware-grade security." | FORBIDDEN | All enforcement is software-only. No HSM, TPM, or hardware root of trust. | Do not use. No replacement needed. |
| 8 | "AV-proof — antivirus cannot flag these systems." | FORBIDDEN | Bitdefender flagged DENY receipt files as `Generic.BAT.Downloader` before sanitization. AV no-quarantine after remediation is observation-based only. | "AV retest passed under active Bitdefender observation. External quarantine-log confirmation not available." |
| 9 | "Unhackable." | FORBIDDEN | No system is unhackable. This is a universal overclaim. | Do not use. No replacement exists. |
| 10 | "Zero-trust verified by independent authority." | FORBIDDEN | No independent verification has occurred. "Zero trust" is a specific NIST framework (SP 800-207) — Razorglint implements deny-by-default, not full ZTA. | "Deny-by-default enforcement architecture." |
| 11 | "Legal compliance guaranteed." | FORBIDDEN | No legal guarantee exists. Legal compliance depends on jurisdiction, deployment, and auditor. | "Evidence compilation supports compliance readiness. Legal determination is yours." |
| 12 | "Buyer-ready certification." | FORBIDDEN | No certification program exists. | "Buyer-ready evidence packs and proof artifacts." |

---

## UNSAFE_OVERCLAIM — Will Be Read as Overclaim by Hostile Readers

These claims are partially true but worded too broadly. A skeptical engineer, lawyer, or security reviewer would flag them.

| # | Unsafe Claim | Verdict | Reason | Safer Replacement |
|---|-------------|---------|--------|-------------------|
| 13 | "All bypasses closed." | UNSAFE_OVERCLAIM | Only the bypass classes identified and tested in the enterprise audit are closed. Unknown vectors remain possible. | "Critical bypass classes identified in audit testing are closed." |
| 14 | "All tests pass across all systems." | UNSAFE_OVERCLAIM | SAR has 3 env-failures, EU AI Act has 6 env-drift exclusions, Rust has 24 env-skips, PF UI has 2 module-miss. | "3,400+ executed passing tests. Environment-gated failures documented." |
| 15 | "No failures in the portfolio." | UNSAFE_OVERCLAIM | Same as above. Failures exist; they are documented and understood. | "No regressions. Environment-gated edge cases documented." |
| 16 | "Command Guardian is SAR-integrated." | UNSAFE_OVERCLAIM | CG has zero integration with SAR. Different codebases, schemas, and protocols. Explicitly deferred. | "SAR integration is deferred. Command Guardian operates independently." |
| 17 | "SAR-integrated Command Guardian." | UNSAFE_OVERCLAIM | Same as #16. | Same as #16. |
| 18 | "Command Guardian receipts are signed." | UNSAFE_OVERCLAIM | CG receipts are hash-chained (SHA-256) but NOT Ed25519 signed. Signing is deferred. | "Command Guardian receipts are SHA-256 hash-chained. Cryptographic signing is deferred." |
| 19 | "3,500+ tests." | UNSAFE_OVERCLAIM | Actual is 3,505 but headline should use 3,400+ to leave margin against env-gated fluctuation. | "3,400+ executed passing tests." |
| 20 | "Complete test coverage across all systems." | UNSAFE_OVERCLAIM | No system claims 100% code coverage. Test suites cover documented behavior, not all code paths. | "Executed test suites covering documented behavior." |
| 21 | "Command Guardian v1.0.0 shipped and production-ready." | UNSAFE_OVERCLAIM | v1.0.0 was marked superseded. Current version is 0.2.0-security-hardening. | "Command Guardian 0.2.0-security-hardening — hardened prototype." |
| 22 | "Runs commands safely." | UNSAFE_OVERCLAIM | Without qualifier, implies absolute safety. CG has a 300s timeout, `shell=True`, and tested-but-not-exhaustive bypass coverage. | "Runs commands through a deny-by-default enforcement model with hash-chained audit receipts." |
| 23 | "Cryptographically proven." | UNSAFE_OVERCLAIM | Some systems use SHA-256 chains (strong). Others rely on test results (weaker). "Cryptographically proven" doesn't apply uniformly. | "Produces cryptographic evidence where implemented." |
| 24 | "Fully audited." | UNSAFE_OVERCLAIM | Self-audited, not independently audited. | "Self-audited with documented methodology. Independent audit not yet performed." |
| 25 | "No cloud dependency." | UNSAFE_OVERCLAIM | True for core enforcement paths. CTLM uses OpenAI API. FAISS is local but sentence-transformers downloads models. | "No cloud dependency at runtime for core enforcement and proof paths." |
| 26 | "Signed receipts across all systems." | UNSAFE_OVERCLAIM | SAR: Ed25519 signed. CG: NOT signed. OpenClaw: inherits SAR signing. Others: varies. | "Ed25519 signed receipts in SAR. Hash-chained receipts in other systems. Signing coverage varies." |

---

## NEEDS_MORE_EVIDENCE

| # | Claim | Verdict | Reason | What Would Make It Safe |
|---|-------|---------|--------|------------------------|
| 27 | "Voidlock prevents capability escalation." | NEEDS_MORE_EVIDENCE | 54 tests exist but no adversarial escalation test suite documented. Design enforces attenuation but proof surface is thin. | Add adversarial capability-escalation tests. |
| 28 | "CalledIt predictions cannot be tampered with." | NEEDS_MORE_EVIDENCE | AES-256-GCM is strong, but no test count or audit trail documented in portfolio proof surface. | Add CalledIt to proof audit with test count. |
| 29 | "Truthpack evidence is fresh within 24 hours." | NEEDS_MORE_EVIDENCE | Stated in README but no test or proof artifact specifically verifies the 24h staleness gate. | Add staleness-gate test to Truthpack test suite. |
| 30 | "CTLM reasoning steps are fully auditable." | NEEDS_MORE_EVIDENCE | Stated architecturally but no test count in proof audit. | Add CTLM to proof audit with executed test count. |
| 31 | "Receipt chain tamper detection is reliable across all systems." | NEEDS_MORE_EVIDENCE | Proven in SAR (cross-verification tests) and CG (verify tests). Not proven across Truthpack, CalledIt. | Extend cross-verification to all receipt-producing systems. |
| 32 | "Blackiron preimage formats enable cross-language verification." | NEEDS_MORE_EVIDENCE | Documented in DOCTRINE.md but no cross-language verification test exists (only Rust tests). | Add Python or JS verification against Blackiron output. |

---

*26 claims classified UNSAFE_OVERCLAIM or FORBIDDEN. 6 claims require additional evidence before public use.*
