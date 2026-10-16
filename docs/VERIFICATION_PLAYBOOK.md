# Verification Playbook — Source, Tests and Claims

This repository is an **architecture/evidence index**, not a universal executable test harness.

## Source-bound verification checklist

1. Record the **canonical repository and immutable commit** (and tree/build/artifact SHA-256 where applicable).
2. Check license, dependency and scope boundaries *before* attempting the workflow.
3. Identify exactly one testable proposition with defined platform, command, fixtures and expected results.
4. Run the source repository's **own** documented command, not generic `pytest` against a different tree.
5. Record **passed, failed, errored, skipped, environment N/A**, and artifacts.
6. Verify receipts/JSON with the verifier for that **specific version**; do not conflate consistency, provenance and signatures.
7. Write an explicit **WHAT THIS DOES NOT PROVE** section.
8. Before a public claim, obtain a separate exact-source review. Historical “approved” language does not automatically authorize new claims.

## Current demonstrable public route

[Compliance Drift Detector](https://github.com/RazorglintLabs/ComplianceDriftDetector) was accepted as an unsigned Windows x64 v0.2 **controlled evaluation preview** on 16 October 2026, with source `662f84caa2ed372abde6a83245c58b466e52ce94`. The [cross-platform test workflow 38893214199](https://github.com/RazorglintLabs/ComplianceDriftDetector/actions/runs/38893214199) and [native Windows build 38893213993](https://github.com/RazorglintLabs/ComplianceDriftDetector/actions/runs/38893213993) both report **completed/success on that exact SHA**. The [product release record](https://github.com/RazorglintLabs/ComplianceDriftDetector/blob/main/docs/RELEASE_STATUS.md) reports **76 passes** and includes ZIP/EXE digests.

Use the [published CLI quickstart](https://github.com/RazorglintLabs/ComplianceDriftDetector/blob/main/SELF_SERVICE_QUICKSTART.md) to reproduce supported source workflows. The currently tagged older v0.1.x GitHub release must **not** be represented as the accepted v0.2 native binary.

This architecture document **checked metadata**, and did not independently rerun the suite or execute the Windows binary.

## Historical result policy

[April 26, 2026 audit](../assets/proof/PROOF_AUDIT_2026-04-26.md): 3,505 reported passes across 10 distinct rows, some with environment failures/skips. The source includes legacy Prestige-Forge; those counts are not current Prestige-Reforged. Images remain historical rather than being mislabeled as current October proof.

## Wording gate

- **Current linked CI:** identify exact SHA, run, environment, result and limits.
- **Private staged tests:** quote only cleared exact-source receipts, no public reproduction promise.
- **Historical test record:** preserve date, untested changes and failures/skips.
- **Candidate integration:** call it planned/under admission, never complete.
- **Certification:** do not claim one unless an actual independent certification exists.

[Overview](../README.md).
