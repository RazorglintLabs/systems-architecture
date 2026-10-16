# Razorglint Labs — Systems Architecture

**Governed actions. Inspectable evidence. Bounded claims.**  
**Public portfolio overview · reviewed 16 October 2026**

Razorglint Labs (TCOG Collective LLC) develops local-first tooling around policy governance, evidence continuity, verification, software assurance and carefully bounded AI-assisted workflows. This repository is a **public architecture and evidence index**, not an integrated product distribution, audit certificate, source-code license or proof that every described system is deployed.

[Current evidence register](PUBLIC_EVIDENCE_REGISTER_2026-10-16.md) · [Historical April 2026 proof audit](assets/proof/PROOF_AUDIT_2026-04-26.md) · [Evidence image manifest](assets/proof/PROOF_MANIFEST.md) · [Commercial problem map](https://github.com/RazorglintLabs/razorglint-pain-to-proof-map) · [Damian Ketting's portfolio](https://github.com/RazorglintLabs/damian-ketting-ai-systems-portfolio)

## What we're building

The common design principle is straightforward: **a consequential decision should have a clear authority boundary, a reconstructable evidence trail and an honest statement of what that evidence does not establish.**

```text
Declared policy / scoped authority
             |
             v
Governance decision ----> allow / deny / unresolved
             |
             v
Covered operation or read-only observation
             |
             v
Evidence + lineage + integrity checks
             |
             v
Claim review / independent challenge
             |
             v
Operator or buyer: inspect the bounded result
```

This is a **reference architecture**. It does not assert that every named component is currently wired to every other component. Authorization, execution, evidence custody, evaluation and independent adversarial challenge remain separate responsibilities.

## Selected technology surfaces

| System / family | Demonstrated or documented role | Public maturity / disclosure boundary |
| --- | --- | --- |
| **Prestige-Reforged** (successor to Prestige-Forge) | Evidence admission, verification, claim evaluation, drift/history and proof handoff; ongoing product UI work | Proprietary and actively qualified in staged phases. Current Windows customer UI / installer and search behavior are **not** represented as final or generally available. |
| **Compliance Drift Detector** | Deterministic analysis of operator-supplied structured policy claims and pre-classified observations across checkpoints | [Public technical-preview repository](https://github.com/RazorglintLabs/ComplianceDriftDetector); Windows v0.2 controlled-evaluation preview accepted 16 Oct; **unsigned**, not enterprise-certified. |
| **SAR** | Explicit governance/enforcement boundary and receipted decisions | Independent proprietary engineering asset; historical April qualification exists, not proof of current deployment or integrated production rollout. |
| **Viventia** | Local-first incident/evidence cockpit and scoped operational handoff | Product development / qualification; **not SIEM or EDR**, not a proven large-scale multi-tenant service. |
| **VEAC** | Independent adversarial challenge against exact target behavior and claims | Separate assurance authority; individual campaign results do not certify the overall target. |
| **Governed AI Control & Assurance (GCA) Stack** | Candidate integration of governance, controlled execution, evidence and assurance | Acquisition/integration project under source, IP, dependency and admission review; **not** an admitted, integrated finished product. |
| **Command Guardian** | Terminal-command enforcement prototype and audit records | Historical 131-test local result; hardened prototype, not production-ready, not SAR-integrated; signing deferred. |
| **ReasonForge** | Dataset validation, deduplication, leakage detection and evaluation workflows | Separate AI-data tooling asset; no current general deployment claim established by this page. |
| **Blackiron / ProofChain / SealVault** | Cryptographic/evidence primitives, hash chains and provenance | Historical/local or component evidence; no single current integrated release is implied. |
| **FleetSim** | Simulation-grade fleet/node trust and degraded-state transitions | Historical simulation tests; **not** proof of safety on a real fleet. |
| **EU AI Act Evidence Readiness Sprint** | Read-only evidence-to-article mappings and gap reports | Limited to specified evidence mappings; **not** legal advice, certification or EU AI Act compliance. |

Other portfolio components exist at different proof levels; their names alone are not current build, ownership, packaging or customer-readiness evidence.

## Current results — do not mix snapshots

- **16 Oct 2026 · Compliance Drift Detector:** source commit `662f84caa2ed372abde6a83245c58b466e52ce94`; **76 passed** in Windows/Linux, Python 3.11/3.12 qualification; native Windows x64 preview and v2 JSON verification accepted under a controlled-evaluation boundary. [Exact release receipt](https://github.com/RazorglintLabs/ComplianceDriftDetector/blob/main/docs/RELEASE_STATUS.md).
- **26 Apr 2026 · historical portfolio audit:** **3,505 executed passing tests** aggregated across reported suites, **not a current all-repository retest**. Some environment-related failures/skips were recorded. [Audit and methodology](assets/proof/PROOF_AUDIT_2026-04-26.md).
- **October 2026 · Prestige-Reforged:** product/UI search and native Windows delivery are undergoing branch-level qualification and review. No all-green installer, customer acceptance or universally merged release claim is made here.

These observations refer to **different source states and dates**. Do not add them into a new “portfolio test total.” Local test evidence is not independent certification.

## A realistic verification path

1. Select the **exact** named repository, source commit and environment.
2. Read that repository's current README, release-status and non-claims before running anything.
3. Follow its own build/test instructions; check skipped/failed tests and whether the workflow covers your platform.
4. Verify report identity, custody and signatures **only where the specific tool actually supports them**.
5. Distinguish an integrity check from authenticated provenance, genuine input truth, operational effectiveness or regulatory compliance.

For an actually accessible public example, start with [Compliance Drift Detector](https://github.com/RazorglintLabs/ComplianceDriftDetector). Private systems are not silently available for public reproduction.

## Architectural safeguards

- Human or explicitly granted authority owns consequential decisions; an LLM response is not authorization.
- Governance does not become execution simply because the components are adjacent on a diagram.
- Verification does not strengthen source truth: correctly hashed **false** data stays false.
- Independent assurance should challenge product claims, not mark its own target “safe.”
- Local-first describes applicable operating paths; it does **not** promise every historical system has zero external dependencies.
- Every product has its own source/IP/third-party-license boundary. Public visibility does not imply open-source rights.

## What is not claimed

No universal production readiness, certification, total test coverage, impossibility of bypass, flawless incident prevention, uninterrupted offline operation across all products, guaranteed compliance, customer traction or portfolio-wide signed receipts. Older public statements have been preserved for historical context, **not automatically reapproved**.

**Commercial/technical contact:** [razorglint.ops@protonmail.com](mailto:razorglint.ops@protonmail.com)  
© 2026 Razorglint Labs / TCOG Collective LLC. Individual repository notices and agreements govern use and rights.
