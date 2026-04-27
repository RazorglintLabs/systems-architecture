# Claims With Required Qualifiers — Razorglint Labs

**Generated:** 2026-04-27  
**Verdict:** SAFE_WITH_QUALIFIER — each claim below is true only when the stated qualifier is included.

Removing the qualifier converts the claim to UNSAFE_OVERCLAIM.

---

## Portfolio-Level Claims

| # | Claim (with qualifier) | Verdict | Required Qualifier | Evidence | Why Qualifier Is Needed |
|---|------------------------|---------|-------------------|----------|------------------------|
| 1 | "3,400+ executed passing tests across the audited portfolio." | SAFE_WITH_QUALIFIER | "executed passing" — not "verified" or "certified" | `PROOF_AUDIT_2026-04-26.md` | "Verified" implies independent verification. "Executed passing" is factual. |
| 2 | "15 systems, all independently testable." | SAFE_WITH_QUALIFIER | "independently testable" — not "independently deployed" or "production-deployed" | `README.md` system inventory | Testable ≠ deployed. No customer deployment exists. |
| 3 | "Shipped infrastructure across governance, verification, and compliance." | SAFE_WITH_QUALIFIER | Add "as open-source prototypes" or "built and tested" | `README.md` | "Shipped" without qualifier implies customer deployments. |
| 4 | "Zero trust assumptions." | SAFE_WITH_QUALIFIER | Replace with "deny-by-default enforcement" or qualify "zero-trust-inspired architecture" | Architecture section | "Zero trust" is NIST SP 800-207. Razorglint implements deny-by-default, not full ZTA. |

---

## Command Guardian Claims

| # | Claim (with qualifier) | Verdict | Required Qualifier | Evidence | Why Qualifier Is Needed |
|---|------------------------|---------|-------------------|----------|------------------------|
| 5 | "Command Guardian closes critical bypass classes." | SAFE_WITH_QUALIFIER | "identified in the audit's tested set" | `ENTERPRISE_AUDIT_REPORT.md` §14, `test_adversarial_bypasses.py` | Without "tested set" scoping, implies all possible bypasses. |
| 6 | "131/131 tests passing." | SAFE_WITH_QUALIFIER | "after emergency security remediation" + "hardened prototype" | `proof_command_guardian_131_pass_hardened.jpg` | Without context, could imply stable production software. |
| 7 | "AV retest passed." | SAFE_WITH_QUALIFIER | "under active Bitdefender observation — external quarantine-log confirmation not available" | `PROOF_MANIFEST.md` "does NOT prove" section | Without qualifier, implies independent AV certification. |
| 8 | "Command Guardian emits hash-chained audit receipts." | SAFE_WITH_QUALIFIER | "SHA-256 hash-chained — cryptographic signing is deferred" | CG `receipts.py`, `verify.py` | Without qualifier, could be read as "signed receipts" — which is false for CG. |
| 9 | "Gate 0 deny-first scanner blocks known destructive patterns." | SAFE_WITH_QUALIFIER | "known" and "tested" — not "all" | `ENTERPRISE_AUDIT_REPORT.md` §4, `danger_scan.py` | Pattern-based. Unknown patterns not covered. |

---

## SAR Claims

| # | Claim (with qualifier) | Verdict | Required Qualifier | Evidence | Why Qualifier Is Needed |
|---|------------------------|---------|-------------------|----------|------------------------|
| 10 | "497 Python tests passing." | SAFE_WITH_QUALIFIER | "3 environment-gated failures documented" | `PROOF_AUDIT_2026-04-26.md` | Without noting env-failures, implies 100% clean run. |
| 11 | "No override exists for SAR hard-deny decisions." | SAFE_WITH_QUALIFIER | Scope to "SAR" — not a portfolio-wide claim | SAR architecture, policy enforcement | Other systems may have different override models. |

---

## EU AI Act Claims

| # | Claim (with qualifier) | Verdict | Required Qualifier | Evidence | Why Qualifier Is Needed |
|---|------------------------|---------|-------------------|----------|------------------------|
| 12 | "194 tests covering 6 EU AI Act articles." | SAFE_WITH_QUALIFIER | "147 excluding environment-sensitive chain replay" | `PROOF_AUDIT_2026-04-26.md` | Full 194 count includes tests that fail in some environments. |
| 13 | "Evidence-ready for EU AI Act assessment." | SAFE_WITH_QUALIFIER | "readiness" not "compliance" — "V1 covers 6 articles, not the full regulation" | EU AI Act Sprint README | V1 scope is explicit. Full-law coverage not claimed. |

---

## Cryptographic Claims

| # | Claim (with qualifier) | Verdict | Required Qualifier | Evidence | Why Qualifier Is Needed |
|---|------------------------|---------|-------------------|----------|------------------------|
| 14 | "Append-only records. Hash-chained. Signed." | SAFE_WITH_QUALIFIER | "Signed where implemented (SAR, OpenClaw). Signing deferred in Command Guardian." | SAR receipt chain, CG `ENTERPRISE_AUDIT_REPORT.md` §8 | CG receipts are NOT signed. Blanket "signed" is false. |
| 15 | "Tamper is detected." | SAFE_WITH_QUALIFIER | "tamper-evident" — not "tamper-proof" or "tamper-prevented" | Hash chain architecture across SAR, CG, Blackiron | Detection ≠ prevention. |
| 16 | "Independent verification — no trust required." | SAFE_WITH_QUALIFIER | "for hash-chain integrity" — not "for all system behavior" | Receipt chain verification commands | Verification scope is chain integrity, not full-system correctness. |

---

## Architecture Claims

| # | Claim (with qualifier) | Verdict | Required Qualifier | Evidence | Why Qualifier Is Needed |
|---|------------------------|---------|-------------------|----------|------------------------|
| 17 | "No cloud dependency." | SAFE_WITH_QUALIFIER | "at runtime for core enforcement and proof paths" | Architecture section | CTLM uses OpenAI API. sentence-transformers downloads models at setup time. |
| 18 | "Proves it cryptographically — or refuses to run." | SAFE_WITH_QUALIFIER | "produces cryptographic evidence where implemented" | SAR, PF, Blackiron, CG chain | Not all 15 systems produce cryptographic proof. Some produce test evidence only. |

---

*18 claims classified SAFE_WITH_QUALIFIER. Each becomes UNSAFE_OVERCLAIM if the qualifier is removed.*
