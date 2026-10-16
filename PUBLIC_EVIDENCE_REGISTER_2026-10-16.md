# Public Evidence Register — 16 October 2026

**Purpose:** date- and source-bound claims for the public architecture landing page. This is a document review, **not** an execution of the private systems' full suites.

| Source/date | Observation | Verification basis | Limits |
| --- | --- | --- | --- |
| [CDD release status](https://github.com/RazorglintLabs/ComplianceDriftDetector/blob/main/docs/RELEASE_STATUS.md), 16 Oct 2026 | Windows x64 v0.2 **controlled-evaluation preview** accepted; 76 regressions passed on supported CI matrix | [source commit `662f84c`](https://github.com/RazorglintLabs/ComplianceDriftDetector/commit/662f84caa2ed372abde6a83245c58b466e52ce94), [Windows build](https://github.com/RazorglintLabs/ComplianceDriftDetector/actions/runs/38893213993), [cross-platform tests](https://github.com/RazorglintLabs/ComplianceDriftDetector/actions/runs/38893214199) | Binary unsigned; no general-availability enterprise release or authenticated original evidence. |
| [April portfolio audit](assets/proof/PROOF_AUDIT_2026-04-26.md), 26 Apr 2026 | **3,505 reported executed passing** across separately audited historical suites | Dated local audit, screenshots and [proof manifest](assets/proof/PROOF_MANIFEST.md) | Historical only; includes recorded environment-sensitive failures/skips; not a fresh combined run, not 3,505 independent certifications. |
| Prestige-Reforged staged engineering, Oct 2026 | Core / claim and evidence product work documented across frozen phases; UI, retrieval and Windows delivery continue in isolated review work | Private canonical repository and branch/PR records inspected 16 Oct 2026 | No public downloadable code or reproducible test invocation from this architecture repo; customer UI and installer **not** declared complete. |
| Viventia / VEAC, Oct 2026 | Local-first evidence cockpit and separate independent adversarial challenge are under active development | Private Viventia collaboration and VEAC project documents reviewed | Private evidence; no live customer deployment, universal adversarial PASS, SIEM/EDR equivalence or certification claimed. |
| GCA Stack, Oct 2026 | Acquisition-grade **candidate** integration project | Private Phase 0 repo, source/admission framework | Recovery, ownership and qualification gates remain; not a finished six-component integrated product. |

## Cross-checked GitHub Actions metadata — 16 October 2026

- [CDD Windows executable run 38893213993](https://github.com/RazorglintLabs/ComplianceDriftDetector/actions/runs/38893213993): completed / success, head `662f84caa2ed372abde6a83245c58b466e52ce94`.
- [CDD qualification run 38893214199](https://github.com/RazorglintLabs/ComplianceDriftDetector/actions/runs/38893214199): completed / success, **same source head**.
- CDD's [maintained release-status note](https://github.com/RazorglintLabs/ComplianceDriftDetector/blob/main/docs/RELEASE_STATUS.md) records the **76-pass** matrix and hashes. CI result metadata was checked separately; no local rerun is claimed.

## Historical image and claim policy

The April images in `assets/proof/` remain historical exhibits. They are **not** being re-dated or replaced with inferred October results. The 27/28 historical “approved claim” labels, where present, were assessments at their recorded dates; the current landing page supersedes them for current-facing statements.

The older architecture README made broader claims than the repository's own `CLAIMS_WITH_REQUIRED_QUALIFIERS.md` permitted. In particular, do not repeat:
- “15 independently deployed/sellable systems” as a current fact;
- “every number can be reproduced by running pytest/cargo test” without identifying accessible repos, exact refs and environments;
- “all systems prove it cryptographically or refuse to run”;
- “zero cloud dependence” across the entire portfolio;
- “all tests pass without exceptions”;
- “all receipts are signed”;
- “every component is buyer-ready or already integrated.”

## Proof-level vocabulary

**Historical execution** = dated pass evidence from a specific suite.  
**Repository documentation** = capability stated by a maintained source, not newly tested here.  
**Current CI result** = workflow result linked to a particular commit and configuration.  
**Owner walkthrough** = acceptance of a specific local scenario, not independent assurance.  
**Candidate / planned** = architecture or commercial scope awaiting qualification.  
**Certification** = not asserted anywhere by this register.

**Maintenance rule:** Each future current-facing count must carry a repository, exact commit, execution date, platform, test command, pass/fail/skip results and coverage boundary. Do not calculate a cross-product grand total from overlapping or noncontemporaneous suites.
