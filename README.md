<p align="center">
  <code>Systems Architecture</code> · <code>AI Integration</code> · <code>Governance Infrastructure</code> · <code>Verifiable Automation</code>
</p>

> Systems architecture portfolio by **Damian Ketting** — founder of **Razorglint Labs**.
>
> Focused on building **AI integration platforms, governance infrastructure, and verifiable automation systems** that remain controllable, deterministic, and auditable.

---

<h1 align="center">Razorglint Systems Architecture</h1>

<p align="center">
  <em>Controllable automation. Verifiable systems. Architecture that proves itself.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=flat-square" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-async-009688?style=flat-square" alt="FastAPI">
  <img src="https://img.shields.io/badge/React-18-61DAFB?style=flat-square" alt="React">
  <img src="https://img.shields.io/badge/Ed25519-signed-critical?style=flat-square" alt="Ed25519">
  <img src="https://img.shields.io/badge/SHA--256-hash--chained-orange?style=flat-square" alt="SHA-256">
  <img src="https://img.shields.io/badge/AES--256--GCM-encrypted-blueviolet?style=flat-square" alt="AES-256">
  <img src="https://img.shields.io/badge/design-local--first-lightgrey?style=flat-square" alt="Local-First">
</p>

---

## Why This Portfolio Matters

This portfolio is not a collection of isolated code experiments.
It documents a systems-level body of work where AI integration, governance, verification, and operational control are treated as separate architectural concerns.

The result is infrastructure designed to support real-world automation without sacrificing traceability, safety boundaries, or operator control.

---

## Overview

This repository documents the architecture of the systems developed under **Razorglint Labs** — an independent systems engineering effort exploring how automation and AI systems can operate inside real environments while remaining **auditable, deterministic, and controllable**.

The portfolio consists of multiple independent but cooperating systems organized into a layered architecture. Each layer separates a distinct concern — orchestration, governance, verification, execution — so that **no system defines its own rules and no output exists without traceable evidence**.

The broader Razorglint portfolio currently spans **15 interconnected systems** across AI infrastructure, runtime governance, cryptographic verification, and automation platforms.

This repository documents the architectural relationships between multiple systems built to explore how automation and AI can operate in controlled environments without sacrificing operator authority, auditability, or deterministic safety boundaries.

---

## Architecture Layers

```
┌─────────────────────────────────────────────────────┐
│            OPERATIONAL INTERFACES                    │  ← Human control
│       Cockpits · CLIs · Approval Surfaces            │
├─────────────────────────────────────────────────────┤
│            CONTROL / ORCHESTRATION                   │  ← System coordination
│       State Machines · Agent Routing · Scheduling    │
├─────────────────────────────────────────────────────┤
│            GOVERNANCE INFRASTRUCTURE                 │  ← Safety rules & execution control
│       Policy Enforcement · Command Gating · Signing  │
├─────────────────────────────────────────────────────┤
│            VERIFICATION / LEDGER SYSTEMS             │  ← Audit & proof
│       Hash Chains · Append-Only Records · Proofs     │
├─────────────────────────────────────────────────────┤
│            EXECUTION SYSTEMS                         │  ← Automation / AI
│       AI Reasoning · Content Generation · Crypto Ops │
└─────────────────────────────────────────────────────┘
```

Each layer produces records that can be validated independently. Authority flows downward. Evidence flows upward. **Execution engines never define their own rules.**

---

## Core Systems

### SAR — Safety Automation Readiness

Governance infrastructure for automation systems — a **control layer that enforces operational rules and safety boundaries**.

```
Operator ──► Governance Console ──► Policy Enforcement ──► Execution
                    │                       │
                    ▼                       ▼
              Ed25519 Signing        Fail-Closed Denial
                    │                       │
                    └───────► Receipt Chain ◄┘
                             (append-only)
```

| Capability | What It Does |
|---|---|
| Execution policy enforcement | Signed YAML doctrine bundles evaluated before every operation |
| Append-only operational records | Hash-linked receipt chains — each entry contains the hash of the previous |
| Deterministic command evaluation | Gated command execution with explicit pass/deny rules, no ambiguity |
| Fail-closed safety boundaries | Invalid policy state = system refuses all requests. No override. |

SAR is intentionally **non-AI infrastructure**. It remains deterministic so that operators can predict system behavior and maintain safety guarantees.

---

### CTLM — Controlled Thinking Layer Model

AI memory and reasoning orchestration — infrastructure that separates **AI reasoning from execution authority**.

| Capability | What It Does |
|---|---|
| Controlled reasoning chains | Multi-phase structured reasoning (warm-up, main, verification, diagnostics) |
| Memory retrieval systems | Vector-based semantic search over embedded knowledge (384-dimensional space) |
| Structured decision flows | Reasoning produces traceable outputs — not freeform generation |
| Traceable reasoning pipelines | Every reasoning step logged, every decision auditable |

The AI layer generates recommendations and analysis. It never executes actions directly. Governance and execution remain separate systems.

---

### Phantom Ledger

Cryptographic verification for system events.

```
Event ──► Hash(event + prev_hash) ──► Append to Chain ──► Verifiable History
```

| Capability | What It Does |
|---|---|
| Append-only event chains | Events are recorded permanently — no deletion, no modification |
| Hash-linked records | Each entry includes the hash of the previous, creating a tamper-evident sequence |
| Independent verification | Any party can verify the chain without trusting the system that produced it |
| Tamper-evident system history | Altering any record breaks the hash chain and is immediately detectable |

This ensures system operations can be **verified after the fact without trusting the system itself**.

---

### Truthpack Engine

Proof-driven revenue automation — a system that converts cryptographic governance evidence into **verifiable marketing and closed deals**.

```
Proof Artifacts ──► Claim Validation ──► Content Generation ──► Approval Gate
                         │                      │                     │
                    Evidence Link           Proof-Linked          Human Review
                    (SHA-256)              (per channel)          (mandatory)
```

| Capability | What It Does |
|---|---|
| Claim validation | Every marketing claim linked to a specific cryptographic proof artifact |
| Evidence aggregation | Proof freshness enforced (≤24h) — stale evidence blocks all downstream publishing |
| Structured output pipelines | Deterministic agent orchestration across 9 bounded agents with single-owner task routing |
| Proof-gated distribution | No output reaches any channel without verified, traceable supporting evidence |

The objective is to prevent automation systems from producing claims **without traceable supporting evidence**.

---

### CalledIt

Prediction sealing and verifiable forecasting.

```
Prediction ──► AES-256-GCM Seal ──► Time-Locked ──► Reveal ──► Verify Integrity
                    │                                    │
              Encrypted at rest                   Decrypted on schedule
              (per-seal keys)                     (proof of timestamp)
```

| Capability | What It Does |
|---|---|
| Cryptographic prediction sealing | AES-256-GCM encryption with per-seal random keys — predictions locked at creation time |
| Time-horizon classification | Structured tiers across precision levels and time windows (hours to months) |
| Privacy-first verification | Anonymous authentication — no identity required to prove prediction accuracy |
| Cross-platform delivery | PWA + native wrappers (Android via Capacitor, Windows via Tauri/Rust) |

This allows the system to demonstrate **prediction integrity without relying on trust in the operator**.

---

## Architectural Principles

### Separation of Authority

Execution engines must not define their own rules. Governance layers enforce operational boundaries. The system that runs the operation is never the system that approves the operation.

### Deterministic Control

Systems that control automation behave deterministically. Same inputs produce same outputs. Operators can predict system behavior and maintain safety guarantees without relying on probabilistic reasoning.

### Verifiability

System events produce records that can be independently verified. Cryptographic techniques — hash chains, digital signatures, sealed proofs — ensure tamper resistance without requiring trust in the producing system.

### Local-First Operation

Systems operate locally by default. No cloud dependencies at runtime. No external infrastructure required for core functions. Operator maintains full control of data and execution.

### Fail-Closed Design

When safety checks fail, systems deny execution rather than continue operating. Invalid policy, stale proof, broken hash chain — any of these result in a hard stop, not a warning.

---

## Selected Technologies

**Languages:** Python, TypeScript, PowerShell
**Frameworks:** FastAPI, React, Electron
**Storage / Infra:** SQLite, Docker
**Security / Verification:** Ed25519, SHA-256, AES-256-GCM, append-only ledgers
**AI / Retrieval:** FAISS, sentence-transformers

---

## System Interaction

```
┌──────────────────────────────────────────────────────────────┐
│                    OPERATOR INTERFACE                         │
│              Cockpits · CLI · Approval Surface               │
└──────────────────────────┬───────────────────────────────────┘
                           │
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
      ┌──────────┐  ┌───────────┐  ┌───────────┐
      │Truthpack │  │ CalledIt  │  │  Control  │
      │ Engine   │  │  Platform │  │  Cockpit  │
      └────┬─────┘  └───────────┘  └─────┬─────┘
           │                              │
           └──────────────┬───────────────┘
                          ▼
              ┌───────────────────────┐
              │   SAR Governance      │
              │   Policy Enforcement  │
              │   Command Gating      │
              └───────────┬───────────┘
                          │
                ┌─────────┼─────────┐
                ▼                   ▼
        ┌──────────────┐   ┌──────────────┐
        │    CTLM      │   │   Phantom    │
        │  Reasoning   │   │   Ledger     │
        │  & Memory    │   │ Verification │
        └──────────────┘   └──────────────┘
```

Each layer produces records that can be validated independently. Authority flows down. Evidence flows up.

---

## Purpose of This Repository

This repository documents **architectural relationships between systems**.

Individual repositories contain implementation details. This repository focuses on system design, interaction patterns, and the principles that govern how components cooperate.

---

## About

**Razorglint Labs** is an independent systems engineering effort exploring new approaches to automation governance and verifiable AI systems.

The work focuses on how complex automated systems can remain **controllable, transparent, and auditable** — proving their behavior through cryptographic evidence rather than compliance assertions.

---

## Open To

- AI integration and systems architecture roles
- Infrastructure and governance engineering work
- Consulting or contract collaboration through **Razorglint Labs**

**Contact:** razorglint.ops@protonmail.com
**GitHub:** [@RazorglintLabs](https://github.com/RazorglintLabs)

---

<p align="center"><sub>Razorglint Labs — TCOG Collective LLC · All rights reserved</sub></p>
