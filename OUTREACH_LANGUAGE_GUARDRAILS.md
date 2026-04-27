# Outreach Language Guardrails — Razorglint Labs

**Generated:** 2026-04-27  
**Purpose:** Claim-safe pitch snippets for three buyer personas. Each snippet has been checked against the approved and forbidden claim registers.

---

## Guardrail Rules for All Outreach

1. Never say "compliant," "certified," or "production-ready."
2. Never say "military-grade," "hardware-grade," or "unhackable."
3. Never imply customer deployments exist unless they do.
4. Always say "evidence" before "proof" — let the reader decide if it's proof.
5. Always name limitations before the reader finds them.
6. Never promise outcomes. Promise evidence of process.
7. If the system has a gap, say "we know where the gaps are" — not "there are no gaps."

---

## Snippet 1 — Chief Strategy Officer

**Audience:** C-suite, strategy, M&A, due-diligence

> **Subject: Systems that prove what they did — not just say it**
>
> We build governance infrastructure and verification systems. The portfolio currently has 3,400+ executed passing tests across 15 independently testable systems — covering governance enforcement, cryptographic verification, AI reasoning orchestration, regulatory evidence mapping, and zero-trust execution.
>
> The core idea is simple: every enforcement decision produces a tamper-evident receipt. Every claim maps to evidence. If the evidence doesn't exist, the claim doesn't ship.
>
> Our EU AI Act evidence compiler maps artifacts to Articles 9, 11, 12, 13, 14, and 15 — and explicitly identifies gaps. It does not say "compliant." It says "here is the evidence, here is what's missing, the auditor decides."
>
> These are hardened prototypes, not SaaS platforms. They run on your infrastructure, under your control. No cloud dependency at runtime for core enforcement paths.
>
> Happy to walk through the proof artifacts directly.

**Claim check:**
- "3,400+ executed passing tests" — SAFE_TO_SAY (`PROOF_AUDIT_2026-04-26.md`)
- "15 independently testable systems" — SAFE_WITH_QUALIFIER (testable, not deployed)
- "tamper-evident receipt" — SAFE_TO_SAY (not "tamper-proof")
- "does not say compliant" — SAFE_TO_SAY (explicit EU AI Act Sprint design)
- "hardened prototypes" — SAFE_TO_SAY (accurate status)
- "no cloud dependency at runtime for core enforcement" — SAFE_WITH_QUALIFIER (CTLM uses API)

**Risk notes:** None. All claims within approved bounds.

---

## Snippet 2 — Security / Risk Leader

**Audience:** CISO, VP Security, Risk Officer, penetration test buyers

> **Subject: Governance infrastructure with hash-chained audit receipts**
>
> Our systems enforce deny-by-default policy and emit SHA-256 hash-chained audit receipts for every enforcement decision. Tampering with the chain is mathematically detectable by any independent verifier.
>
> SAR (Safety Automation Readiness) is our governance enforcement engine — 497 Python tests, 13 Rust verification tests, Ed25519 signed receipts, fail-closed behavior. The system that approves the operation never runs the operation. Invalid policy is a hard stop, not a warning.
>
> Command Guardian is a hardened local-first command enforcement prototype — 131/131 tests passing after emergency security remediation. Critical bypass classes identified in adversarial testing are closed. DENY receipts store command hashes, not raw dangerous command strings. It is not production-ready, not externally audited, and receipt signing is deferred.
>
> We document limitations before you find them. The enterprise audit report for Command Guardian preserves the original hostile findings alongside the remediation trail.
>
> No SaaS. No accounts. Runs on your infrastructure.

**Claim check:**
- "deny-by-default" — SAFE_TO_SAY (structural enforcement in SAR, CG, Voidlock)
- "SHA-256 hash-chained" — SAFE_TO_SAY
- "tampering mathematically detectable" — SAFE_TO_SAY (tamper-evident, not tamper-proof)
- "Ed25519 signed receipts" — SAFE_TO_SAY (SAR-specific, correctly scoped)
- "131/131 after emergency remediation" — SAFE_TO_SAY
- "not production-ready" — correct limitation disclosure
- "receipt signing deferred" — correct limitation disclosure

**Risk notes:** Explicitly names CG limitations. Strong posture for security audience.

---

## Snippet 3 — Governance / Compliance Leader

**Audience:** Chief Compliance Officer, GRC lead, regulatory readiness teams

> **Subject: Evidence-mapped regulatory readiness — not compliance theater**
>
> We built an evidence compiler that maps sealed proof artifacts from our governance and verification systems to specific EU AI Act articles (9, 11, 12, 13, 14, 15). It produces article-mapped evidence packs, gap registers, and readiness reports.
>
> What it does: compiles evidence from five sovereign systems through read-only adapters. Maps each artifact to the relevant article. Identifies where evidence exists and where gaps remain.
>
> What it does not do: say "compliant." That word requires a regulator. We provide the evidence and the gap map. Your auditor decides.
>
> The compiler sits on top of a portfolio with 3,400+ executed passing tests. The proof engine (Prestige-Forge, 690 tests) validates claims against evidence before they can be published. The governance engine (SAR, 497+ tests) enforces policy with fail-closed behavior and signed receipts.
>
> V1 covers 6 articles. We do not claim full-law coverage. Expansion is planned and documented.
>
> All systems are stdlib-only Python or minimal-dependency Rust. No frameworks in the proof path. Reproducible on any machine.

**Claim check:**
- "evidence-mapped" — SAFE_TO_SAY (not "compliant")
- "gap registers" — SAFE_TO_SAY (explicit gap identification)
- "read-only adapters" — SAFE_TO_SAY (EU AI Act Sprint architecture)
- "3,400+ executed passing tests" — SAFE_TO_SAY
- "validates claims against evidence" — SAFE_TO_SAY (PF Claims Safety Engine)
- "fail-closed" — SAFE_TO_SAY (SAR design)
- "V1 covers 6 articles — not full-law" — correct scope disclosure

**Risk notes:** None. Strongest posture for compliance audience — shows evidence discipline, not certification theater.

---

## Language Substitution Quick Reference

| Do NOT Say | Say Instead |
|------------|-------------|
| compliant | evidence-ready / evidence-mapped |
| certified | audited / self-audited with documented methodology |
| production-ready | hardened prototype |
| tamper-proof | tamper-evident |
| impossible to bypass | tested bypass classes closed |
| all tests pass | 3,400+ executed passing tests; env-gated edge cases documented |
| military-grade | do not use |
| zero-trust verified | deny-by-default enforcement |
| SAR-integrated (for CG) | SAR integration deferred |
| signed receipts (blanket) | Ed25519 signed (SAR); hash-chained (CG); signing coverage varies |
| no limitations | limitations documented |
| verified | executed passing |
| shipped | built and tested |

---

*All snippets checked against APPROVED_PUBLIC_CLAIMS.md and FORBIDDEN_PUBLIC_CLAIMS.md. No forbidden language detected.*
