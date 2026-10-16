<h1 align="center">Razorglint Systems Architecture</h1>
<p align="center"><strong>Governance that holds its boundary. Evidence you can inspect. Claims that know their limits.</strong></p>
<p align="center"><strong>15 engineering systems · Python, Go, Rust &amp; TypeScript · Source-bound qualification</strong></p>

<p align="center">
<img alt="Python" src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square"/>
<img alt="Go" src="https://img.shields.io/badge/Go-tested%20launcher%20%26%20services-00ADD8?style=flat-square"/>
<img alt="Rust" src="https://img.shields.io/badge/Rust-2021-CE422B?style=flat-square"/>
<img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-selected%20clients-3178C6?style=flat-square"/>
<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-selected%20services-009688?style=flat-square"/>
<img alt="Ed25519" src="https://img.shields.io/badge/Ed25519-where%20implemented-555?style=flat-square"/>
<img alt="SHA256" src="https://img.shields.io/badge/SHA--256-evidence%20integrity-F59E0B?style=flat-square"/>
<img alt="AES256" src="https://img.shields.io/badge/AES--256--GCM-selected%20assets-7C3AED?style=flat-square"/>
<img alt="Local first" src="https://img.shields.io/badge/Local--first-qualified%20paths-161B22?style=flat-square"/>
</p>
<p align="center"><sub>Technology labels identify particular components, not a uniform certification or deployment promise.</sub></p>

<p align="center">
<a href="#the-proof"><strong>THE PROOF</strong></a> ·
<a href="#the-architecture"><strong>THE ARCHITECTURE</strong></a> ·
<a href="#the-systems"><strong>THE SYSTEMS</strong></a> ·
<a href="#independent-verification"><strong>VERIFY</strong></a> ·
<a href="mailto:razorglint.ops@protonmail.com"><strong>CONTACT</strong></a>
</p>

---

## Why Razorglint exists

Most software can tell you that an action *happened*. Much less can establish **which authority permitted it, which evidence was retained, which assumptions failed, and which public claim is still justified**.

Razorglint Labs designs independent software assets around that missing chain: **govern → observe → preserve → verify → challenge → explain**. Our products and research span governed automation, evidence continuity, independent adversarial challenge, deterministic evaluation, operational security interfaces, and software provenance.

**Our rule:** *If the evidence runs out, the claim stops there.*

This repository is an **architecture and qualification index**, not a universal installer, open-source grant, or statement that all systems are already interconnected.

## The proof

<blockquote>
<strong>Five recent source-bound qualification snapshots are documented below.</strong> Their test counts refer to distinct suites, different source revisions and differing disclosure levels—not a single fresh all-portfolio test execution.
</blockquote>

| System | Passing tests | When / where | Verification boundary |
| --- | ---: | --- | --- |
| **Viventia** | **1,453** | 13 Sep · exact clean private correction branch | Recorded Python full-suite result; one skip and one known warning. **Not** an Oct 16 rerun of product `main`. |
| **Prestige-Reforged** | **644** | 16 Oct · [Receiver Gate CI](https://github.com/RazorglintLabs/Prestige-Reforged/actions/runs/38883382477) | **532** Phase 6 + **112** separate Phase 7 tests at one exact source SHA. Another G2 source-import gate failed and remains excluded. |
| **EU AI Act Evidence Readiness** | **86** | 14 Oct · [regression CI](https://github.com/RazorglintLabs/EU-AI-Act-Evidence-Readiness-Sprint/actions/runs/38637473818) | Branch-qualified; six-article evidence mapping, not legal compliance or a `main` retest. |
| **Compliance Drift Detector** | **76** | 16 Oct · [cross-platform CI](https://github.com/RazorglintLabs/ComplianceDriftDetector/actions/runs/38898754185) | Current `main` source; 24 self-service tests are rerun **within** the 76—not extra unique cases. |
| **VEAC** | **66** | 14 Oct · [self-assurance CI](https://github.com/RazorglintLabs/viventia-veac/actions/runs/38639994394) | Independent examiner tests on a feature branch; no global product safety certificate. |

**2,325 distinct passing test cases are represented across these five selected, dated suite snapshots.** This is an **evidence subtotal, not the full Razorglint test inventory and not 2,325 tests re-executed today**. The Viventia row is a retained exact-branch acceptance record; the other four counts were recovered from GitHub Actions logs. Other assets are deliberately excluded until their current source/test receipts can be confirmed.

[Exact commit identities, command scopes, skip details and all 15 evidence states →](docs/CURRENT_TEST_EVIDENCE_2026-10-16.md)

## The architecture

```text
             HUMAN / EXPLICIT AUTHORITY
                       |
                 scoped policy
                       v
              GOVERN OR REFUSE
                       |
                bounded action
                       v
             OBSERVE AND PRESERVE
               evidence + time
                       |
                 source identity
                       v
              VERIFY THE RECORD
                       |
              independent challenge
                       v
             EXPLAIN THE BOUNDARY
           proven | missing | denied
```

| Architecture layer | Representative technology | Boundary that matters |
| --- | --- | --- |
| **Authority** | SAR, policy decision mechanisms | An AI suggestion is not authorization. |
| **Controlled action** | OpenClaw, Voidlock, Command Guardian, FleetSim | Test scope and implementation determine what is actually constrained. |
| **Evidence** | Blackiron, ProofChain, SealVault, Viventia | A hash or receipt is not necessarily an authenticated account of external reality. |
| **Evaluation** | Prestige-Reforged, Compliance Drift Detector | An evaluation cannot silently fill missing evidence or prove the source data was true. |
| **Independent challenge** | VEAC, hostile and receiver gates | An examiner evaluates propositions, not universal product safety. |

This is a **reference architecture**. Components do not share one authority, production runtime or completed integration merely because they appear together. The candidate Governed AI Control & Assurance (GCA) Stack remains separately source/IP-gated.

[Architecture and trust boundaries →](docs/ARCHITECTURE_LAYERS_2026-10-16.md)

## The systems

| # | Engineering asset | Focus | Current verification state |
| ---: | --- | --- | --- |
| 01 | **Prestige-Reforged** | Evidence, claim validity and proof handoff | **644** in bounded 16 Oct private Receiver CI; Windows G2 product acceptance remains gated |
| 02 | **SAR** | Explicit policy authority and audit receipts | Private source; no recent comparable GitHub CI suite total established |
| 03 | **Viventia** | Local-first customer / incident-response evidence | **1,453** in exact-branch retained Python qualification; latest product-`main` retest not established |
| 04 | **VEAC** | Independent adversarial assurance | **66** in 14 Oct branch CI, four OS/Python combinations |
| 05 | **[Compliance Drift Detector](https://github.com/RazorglintLabs/ComplianceDriftDetector)** | Policy-to-observation checkpoint drift | **76** on current `main`, 16 Oct Windows/Linux CI |
| 06 | **OpenClaw** | Governed agent/action model | Source/test state not independently reconciled with a current standalone GitHub repository |
| 07 | **Voidlock** | Capability attenuation and execution constraints | Current standalone source/test receipt not established |
| 08 | **Blackiron** | Rust cryptographic evidence primitives | Repository accessible; no recent Actions-based suite count found |
| 09 | **ProofChain** | Hash-linked history and accumulator design | Current standalone source/test receipt not established |
| 10 | **SealVault** | Evidence sealing, Rust / Go / TypeScript mechanisms | Repository accessible; no recent Actions-based suite count found |
| 11 | **Command Guardian** | Terminal policy guardrails and hash-chained receipts | Last accessible CI is older than this refresh; **no new count claimed** |
| 12 | **FleetSim** | Fleet trust-plane simulation | Current standalone source/test receipt not established |
| 13 | **EU AI Act Evidence Readiness Sprint** | Read-only six-article gap/evidence mapping | **86** in 14 Oct feature-branch CI |
| 14 | **ReasonForge** | LLM dataset quality, leakage and evaluation | [12 Oct smoke CI](https://github.com/RazorglintLabs/rdl-showroom/actions/runs/38229965533) PASS; no full-suite numeric count established |
| 15 | **CalledIt** | Sealed predictions, PWA and native wrapper concepts | Private source exists; no recent Actions-based numeric test receipt found |

**No blanks, no invented green badges:** “not established” is an evidence status, not a verdict that a system has no tests. Each missing total requires its own exact-head result, not borrowed counts from adjacent products.

[Full 15-system engineering profiles →](docs/SYSTEM_PROFILES_2026-10-16.md) · [Current qualification matrix →](docs/CURRENT_TEST_EVIDENCE_2026-10-16.md)

## Engineering, not theatre

- **Local-first where qualified.** Scoped operator control; not a claim that no component ever downloads dependencies or uses an API.
- **Proof with non-claims.** Signed, hash-chained, hashed-only and unverified records are different trust levels.
- **Human authority stays explicit.** No implicit policy approval by a model, frontend, or research demo.
- **Separate product maturity.** A passing component suite does not mean a customer installer, subscription, operational integration or product license is ready.
- **Independent examiner discipline.** VEAC must never turn its own successful tests into certification of Viventia.
- **IP boundaries matter.** Prestige-Reforged retained core rights stay outside candidate acquisition packages without a separate negotiated license.

## Independent verification

To reproduce a statement, record **repository, exact SHA, test command, platform, passing/failing/skipped counts and the meaning of the assertion**. A successful CI run on a feature branch does not qualify another branch. A repeated subset does not create additional unique test cases. Private repositories require authorized access; architecture documentation is not a clone permission.

[Read the test audit and qualification gaps](docs/CURRENT_TEST_EVIDENCE_2026-10-16.md) · [Verification method](docs/VERIFICATION_PLAYBOOK.md) · [Public claim and licensing boundaries](docs/IP_AND_DELIVERY_BOUNDARIES.md)

---

<p align="center"><strong>Razorglint Labs</strong> · Systems engineering, governance, provenance and verifiable automation<br/>
Damian G. L. Ketting · Founder · TCOG Collective LLC<br/>
<a href="mailto:razorglint.ops@protonmail.com">razorglint.ops@protonmail.com</a> · <a href="https://github.com/RazorglintLabs/damian-ketting-ai-systems-portfolio">Founder's portfolio</a> · <a href="https://github.com/RazorglintLabs/razorglint-pain-to-proof-map">Problems to proof</a>
</p>
