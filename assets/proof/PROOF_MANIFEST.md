# Proof Manifest — Systems Architecture

Index of proof images in `assets/proof/`. Each entry records what the image proves and what it does not.

---

## Command Guardian — Hardened Prototype

| Field | Value |
|-------|-------|
| **Filename** | `proof_command_guardian_131_pass_hardened.jpg` |
| **Command used** | `python -m pytest tests/ -q --tb=no` |
| **Timestamp** | 2026-04-26T13:54:45Z |
| **Test count** | 131 passed, 0 failed, 0 skipped |
| **Version** | 0.2.0 |
| **AV active** | Bitdefender (bdagent + 4× bdservicehost) |

### What it proves

- All 131 tests pass after emergency security remediation (Pass 1 + Pass 2)
- 7 test suites cover: classifier, policy, receipts, runner enforcement, verification, adversarial bypasses, receipt sanitization
- Version 0.2.0 is consistent across package metadata
- AV was active during the test run (Bitdefender)
- Critical classifier bypass classes are closed
- DENY receipts are sanitized (no raw dangerous command strings)
- Token issuance is audit-receipted

### What it does NOT prove

- Production readiness
- SAR integration
- Receipt signing
- External AV quarantine-log confirmation (observation-based only)
- Absence of all possible bypass vectors (only the tested adversarial patterns are covered)
- Certification or compliance with any standard
- v1.0.0 maturity
