# Public Claims Safety Pack — Razorglint Labs

**Generated:** 2026-04-27  
**Engine:** Prestige-Forge Claims Safety methodology  
**Scope:** All public-facing language — LinkedIn, README, outreach, GitHub profile, buyer summaries  
**Audit inputs:** systems-architecture README, PROOF_AUDIT_2026-04-26.md, PROOF_MANIFEST.md, Command Guardian README, Command Guardian ENTERPRISE_AUDIT_REPORT.md, Command Guardian audit_pass2/PROOF_MANIFEST.md

---

## Pack Contents

| File | Purpose |
|------|---------|
| `APPROVED_PUBLIC_CLAIMS.md` | Claims classified SAFE_TO_SAY with evidence mapping |
| `FORBIDDEN_PUBLIC_CLAIMS.md` | Claims classified FORBIDDEN or UNSAFE_OVERCLAIM |
| `CLAIMS_WITH_REQUIRED_QUALIFIERS.md` | Claims that are SAFE_WITH_QUALIFIER only |
| `OUTREACH_LANGUAGE_GUARDRAILS.md` | Pitch snippets for CSO, Security, Compliance audiences |
| `LINKEDIN_POST_CLAIM_CHECK.md` | 10 LinkedIn-safe posts with claim verdicts |

---

## Audit Summary

| Metric | Count |
|--------|-------|
| Total claims reviewed | **78** |
| SAFE_TO_SAY | **28** |
| SAFE_WITH_QUALIFIER | **18** |
| UNSAFE_OVERCLAIM | **14** |
| FORBIDDEN | **12** |
| NEEDS_MORE_EVIDENCE | **6** |

---

## Claim Areas Audited

1. Total test counts and portfolio proof surface
2. Command Guardian remediation and current status
3. SAR governance enforcement
4. OpenClaw governed agents
5. FleetSim trust plane
6. Prestige-Forge proof engine
7. EU AI Act evidence readiness
8. Cryptographic receipt chains
9. Hash chain integrity
10. Ed25519 signing
11. Audit readiness
12. Compliance language
13. Production readiness
14. Security claims
15. Defense / military / national-security wording
16. Buyer / investor wording
17. "Zero trust" language
18. "Tamper-proof" vs "tamper-evident"
19. "Certified" vs "evidence-mapped"
20. "SAR-integrated" vs "deferred integration"

---

## Evidence Sources Referenced

| Source | Location |
|--------|----------|
| Portfolio proof audit | `assets/proof/PROOF_AUDIT_2026-04-26.md` |
| Portfolio proof manifest | `assets/proof/PROOF_MANIFEST.md` |
| Aggregate proof image | `assets/proof/proof_aggregate_summary.jpg` |
| CG proof image | `assets/proof/proof_command_guardian_131_pass_hardened.jpg` |
| CG enterprise audit | `Command Guardian/ENTERPRISE_AUDIT_REPORT.md` |
| CG README | `Command Guardian/README.md` |
| Systems-architecture README | `README.md` |

---

## Top 10 Strongest Approved Claims

1. "Razorglint has 3,400+ executed passing tests across its audited portfolio proof surface." — `PROOF_AUDIT_2026-04-26.md` (actual: 3,505)
2. "Every enforcement decision produces a SHA-256 hash-chained receipt." — SAR, CG, OpenClaw receipt code
3. "The system that approves the operation never runs the operation." — SAR architecture, OpenClaw dual-write
4. "Command Guardian closes the critical bypass classes identified in the audit's tested set." — `ENTERPRISE_AUDIT_REPORT.md` §14, `test_adversarial_bypasses.py`
5. "DENY receipts store command hashes instead of raw dangerous command strings." — `test_receipt_sanitization.py`, CG receipts.py
6. "EU AI Act tooling maps evidence to articles and exposes gaps — it does not claim compliance." — EU AI Act Sprint source, README
7. "Prestige-Forge checks claims against evidence before publication." — Client Zero 25/25, Claims Safety Engine M-018
8. "OpenClaw agents run under SAR governance. No agent defines its own rules." — OpenClaw 1,578 tests, dual-write architecture
9. "FleetSim tests trust-plane enforcement with severity ladder and transition receipts." — 103 tests passing
10. "All proof images are reproducible by running pytest or cargo test in the corresponding repo." — `PROOF_AUDIT_2026-04-26.md` methodology

---

## Top 10 Forbidden Claims

1. "Razorglint systems are production-ready."
2. "Certified compliant with the EU AI Act."
3. "Tamper-proof audit trail."
4. "Impossible to bypass."
5. "Military-grade security."
6. "Command Guardian is SAR-integrated."
7. "All bypasses have been closed."
8. "No failures across the portfolio."
9. "AV-proof — antivirus cannot flag these systems."
10. "Zero-trust verified by independent authority."

---

## Required Pre-Post Check

Before any LinkedIn post, outreach email, README revision, buyer summary, or GitHub profile update is published, check it against the six ambiguous claims in this pack:

1. "Shipped infrastructure"
2. "Zero trust assumptions"
3. "Verified tests"
4. Blanket "signed" records
5. Blanket "no override exists"
6. "Proves it cryptographically"

If any phrase appears, it must be replaced, scoped, or qualified before publication.

---

## Ambiguous Claims Requiring Human Review

| # | Claim | Issue | Recommendation |
|---|-------|-------|----------------|
| 1 | "Shipped infrastructure" (README headline) | Most systems are hardened prototypes, not production deployments. "Shipped" may imply customer deployments. | Replace with "built and tested infrastructure" or add qualifier "shipped as open-source prototypes" |
| 2 | "Zero trust assumptions" (README headline badge) | "Zero trust" is an overloaded industry term (NIST SP 800-207). Razorglint implements deny-by-default, not full ZTA. | Replace with "deny-by-default enforcement" or qualify "zero-trust-inspired" |
| 3 | "3,400+ verified tests" (headline) | "Verified" could imply independent third-party verification. Actual: self-run pytest/cargo test. | Prefer "3,400+ executed passing tests" in all contexts |
| 4 | "Append-only records — Hash-chained. Signed." (Design Law) | SAR receipts are Ed25519 signed; CG receipts are NOT signed (deferred). Blanket "signed" overclaims. | Qualify: "Hash-chained. Signed where implemented (SAR). Signing deferred in Command Guardian." |
| 5 | "No override exists" (SAR section) | True for SAR's hard-deny. But "no override exists" as a blanket statement across all systems is unchecked. | Scope to SAR explicitly |
| 6 | "proves it cryptographically" (README opening) | Some systems prove via hash chains (strong). Others prove via test results (weaker). "Cryptographically" doesn't apply uniformly. | Qualify: "produces cryptographic evidence where implemented" |

---

## Public Language Law

1. If proof does not support it, do not say it.
2. If the system has limitations, name them before someone else does.
3. Prefer "tamper-evident" over "tamper-proof."
4. Prefer "evidence-ready" over "compliant."
5. Prefer "hardened prototype" over "production-ready."
6. Prefer "tested bypass classes closed" over "all bypasses closed."
7. Prefer "executed passing tests" over vague "verified tests."
8. Never turn a proof artifact into a certification claim.

---

*This pack is a point-in-time governance artifact. Re-audit after any test count change, new system addition, or public language revision.*
