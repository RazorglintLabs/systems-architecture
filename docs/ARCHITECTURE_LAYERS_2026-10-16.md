# Architecture Layers and Authority Boundaries
**16 October 2026 — Reference design, NOT a completed integrated product**

\`\`\`text
SOURCE + SCOPE -> AUTHORIZED POLICY
                      |
               allow / deny / unresolved
                      |
                      v
               BOUNDED OPERATION
                      |
            structured events and receipts
                      |
                      v
              EVIDENCE / CUSTODY
                      |
                      v
              CLAIM / HISTORY CHECK
                      |
                      v
             INDEPENDENT CHALLENGE
                      |
                      v
                HUMAN DECISION
\`\`\`

## Non-negotiable seams

| Seam | Requirement | Unacceptable inference |
| --- | --- | --- |
| Human/operator to policy | Source of authority named, scoped and separately controlled | AI recommendation is authorization |
| Policy to executor | Covered action binds to an explicit verdict/constraint | All executors are integrated just because SAR exists |
| Executor to evidence | Observation, source identity and record limitations explicit | Receipt equals full ground truth |
| Evidence to evaluation | Exact artifact bytes or constrained references and versioned checks | Matching SHA-256 authenticates input origin |
| Evaluation to examiner | Independent hostile propositions scoped to target commit/tree | Product can certify itself |
| Examiner to buyer | Clear limitations, unknowns and verification reproducibility | Internal PASS means independent certification |

**SAR** is governance, not an execution engine. **OpenClaw** is a potential governed action surface; IP/source admission remains gated. **Voidlock** is an execution-boundary mechanism, not universally qualified sandbox isolation. **Viventia** presents scoped IR/customer evidence, not incident authorization. **VEAC** challenges a defined target independently and never produces global certification. **Prestige-Reforged** evaluates evidence/claims under defined contracts rather than proving source truth. **CDD** takes pre-classified operator input and performs checkpoint analysis, not live telemetry.

## GCA Stack — candidate integration only

The Governed AI Control & Assurance Stack proposes a source-bound buyer pathway:

\`\`\`text
SAR policy -> OpenClaw covered actions -> Voidlock constraints
     -> Viventia evidence + Blackiron crypto -> VEAC challenge
\`\`\`

**This is a proposed responsibility map.** GCA remains in Phase 0 source recovery, ownership/dependency reconciliation and component admission. Candidate components include SAR, Viventia, VEAC, OpenClaw, Voidlock, Blackiron, optional FleetSim. Every component must be explicitly **ADMITTED**, **BLOCKED** or **EXCLUDED**. Historical test counts do not imply present admission or a finished joined product.

## Why the cryptographic language is limited

- A digest supports checking content consistency; without trusted provenance an attacker may change both data and digest.
- A hash chain helps expose modifications to covered chain links, not necessarily omission or source lies.
- An Ed25519 signature authenticates the holder of a verified key under its trust model; it does not certify a real-world claim.
- A verification verdict is about specified propositions, inputs, implementation and tests; it cannot license a broad “safe” claim.

[Overview](../README.md) · [Verification playbook](VERIFICATION_PLAYBOOK.md).
