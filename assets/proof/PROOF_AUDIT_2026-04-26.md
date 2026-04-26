# Proof Audit — 2026-04-26

Audited test counts across all Razorglint systems. Each row reflects live test execution, not inventory.

---

## Audit Table

| System | Passed | Failures / Skips | Command | Date | Notes |
|--------|--------|-------------------|---------|------|-------|
| OpenClaw | 1,578 | 0 failed, 156 skipped | `pytest tests/ -q` | 2026-04-26 | 45 test modules; dual-write + policy + trust + truthpack |
| Prestige-Forge (core) | 690 | 0 failed, 0 skipped | `pytest tests/core/ -q` | 2026-04-26 | 15 constitutional families, 19 core modules |
| SAR (Python) | 497 | 3 env-fail | `pytest governance/ -q` | 2026-04-26 | 86 inventoried endpoints; fail-closed |
| EU AI Act Sprint | 194 | 6 env-drift | `pytest tests/ -q` | 2026-04-26 | 147 excluding env-sensitive chain replay |
| Rust Modules | 132 | 0 failed, 24 env-skip | `cargo test` | 2026-04-26 | 6 crates: ironcache, ironledger, ironvec, irontext, pf_verify, sar_verify |
| Command Guardian | 131 | 0 failed, 0 skipped | `python -m pytest tests/ -q --tb=no` | 2026-04-26 | Hardened prototype; critical bypass classes closed; DENY receipts sanitized; token issuance audited |
| FleetSim | 103 | 0 failed, 0 skipped | `pytest tests/ -q` | 2026-04-26 | Trust plane, severity ladder, transition receipts |
| Prestige-Forge (UI) | 73 | 2 module-miss | `pytest tests/ui/ -q` | 2026-04-26 | Flask/Jinja local UI tests |
| Voidlock | 54 | 0 failed, 0 skipped | `pytest tests/ -q` | 2026-04-26 | stdlib-only, deny-by-default |
| Blackiron | 53 | 0 failed, 0 skipped | `cargo test` | 2026-04-26 | Rust, domain-separated, deterministic |

---

## Totals

| Metric | Value |
|--------|-------|
| **Total executed passing** | **3,505** |
| **Public headline** | **3,400+ executed passing tests** |
| **Systems counted** | 10 (across 15 sovereign systems; some share test suites) |

---

## Command Guardian Limitations

- Not production-ready
- Not SAR-integrated
- Receipt signing deferred
- AV no-quarantine is observation-based only, not externally confirmed through Bitdefender API
- Version: 0.2.0-security-hardening; earlier v1.0.0 release marked superseded

---

## Methodology

All counts are from direct `pytest` or `cargo test` execution on local machines. No CI aggregation. No inventory-only counts. Skipped tests are excluded from the passing count. Environment-sensitive failures are noted but not hidden.
