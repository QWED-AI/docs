<div align="center">
  <h1>QWED Documentation</h1>
  <h3>Official Documentation for the QWED Verification Ecosystem</h3>

  > **Deterministic verification infrastructure for AI systems, agents, finance, legal, and compliance.**

  [![Docs](https://img.shields.io/badge/Docs-docs.qwedai.com-0f1117?style=flat&logo=mintlify&logoColor=white)](https://docs.qwedai.com)
  [![Powered by Mintlify](https://img.shields.io/badge/Powered_by-Mintlify-0f1117?style=flat&logo=mintlify&logoColor=white)](https://mintlify.com)
  [![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)
  [![GitHub Developer Program](https://img.shields.io/badge/GitHub_Developer_Program-Member-4c1?style=flat&logo=github)](https://github.com/QWED-AI)
</div>

---

## Overview

This repository contains the public documentation for [**QWED**](https://github.com/QWED-AI) — a deterministic verification ecosystem that proves, validates, and enforces trust boundaries for AI systems, agents, infrastructure, and computational workflows.

The documentation covers:

| Area | Description |
|------|-------------|
| **QWED Verification Protocol** | Core verification engines (Math, Logic, SQL, Code, Facts) and the Untrusted Translator architecture |
| **AI & Agent Security** | Agentic security guards — MCP Poison, RAG, Exfiltration, Process Determinism |
| **Finance Guards** | NPV/IRR verification, loan amortization, compound interest, ISO 20022, currency safety |
| **Legal Guards** | Deadline verification, clause consistency, citation validation, jurisdiction checks, statute of limitations |
| **SDK References** | Python, TypeScript, Go, and Rust SDK documentation and API references |
| **Architecture** | Deterministic verification design, fail-closed philosophy, verification boundaries |
| **Deployment** | Docker, Kubernetes, CI/CD integration, and operational guidance |

---

## Documentation Site

📖 **[docs.qwedai.com](https://docs.qwedai.com)**

---

## The QWED Ecosystem

| Package | Description | PyPI | npm | Repo |
|---------|-------------|------|-----|------|
| **qwed** | Core verification + security guards | [`qwed`](https://pypi.org/project/qwed/) | [`@qwed-ai/sdk`](https://www.npmjs.com/package/@qwed-ai/sdk) | [qwed-verification](https://github.com/QWED-AI/qwed-verification) |
| **qwed-finance** 🏦 | Banking, loans, NPV, ISO 20022 | [`qwed-finance`](https://pypi.org/project/qwed-finance/) | [`@qwed-ai/finance`](https://www.npmjs.com/package/@qwed-ai/finance) | [qwed-finance](https://github.com/QWED-AI/qwed-finance) |
| **qwed-legal** ⚖️ | Contracts, deadlines, citations, jurisdiction | [`qwed-legal`](https://pypi.org/project/qwed-legal/) | [`@qwed-ai/legal`](https://www.npmjs.com/package/@qwed-ai/legal) | [qwed-legal](https://github.com/QWED-AI/qwed-legal) |
| **qwed-tax** 💸 | Tax compliance & withholding verification | [`qwed-tax`](https://pypi.org/project/qwed-tax/) | — | [qwed-tax](https://github.com/QWED-AI/qwed-tax) |
| **qwed-infra** ☁️ | IaC verification (Terraform, IAM, Cost) | [`qwed-infra`](https://pypi.org/project/qwed-infra/) | — | [qwed-infra](https://github.com/QWED-AI/qwed-infra) |
| **qwed-ucp** 🛒 | E-commerce cart/transaction verification | [`qwed-ucp`](https://pypi.org/project/qwed-ucp/) | — | [qwed-ucp](https://github.com/QWED-AI/qwed-ucp) |
| **qwed-mcp** 🔌 | Claude Desktop MCP integration | [`qwed-mcp`](https://pypi.org/project/qwed-mcp/) | — | [qwed-mcp](https://github.com/QWED-AI/qwed-mcp) |
| **open-responses** 🤖 | OpenAI Responses API + QWED guards | [`qwed-open-responses`](https://pypi.org/project/qwed-open-responses/) | — | [qwed-open-responses](https://github.com/QWED-AI/qwed-open-responses) |

---

## Development

### Prerequisites

- [Node.js](https://nodejs.org/) (v18+)
- [Mintlify CLI](https://mintlify.com/docs/development)

### Install Mintlify CLI

```bash
npm i -g mintlify
```

### Run local development server

```bash
mintlify dev
```

Preview locally at: **http://localhost:3000**

---

## Repository Structure

```
/
├── legal/                # QWED-Legal guard documentation
├── finance/              # QWED-Finance guard documentation
├── tax/                  # QWED-Tax guard documentation
├── sdks/                 # SDK reference (Python, TypeScript, Go, Rust)
├── open-responses/       # OpenAI Responses API integration docs
├── specs/                # Verification specification documents
├── snippets/             # Shared reusable MDX snippets
├── images/               # Static assets
├── changelog.mdx         # Release changelog
├── architecture.mdx      # System architecture
├── faq.mdx               # Frequently asked questions
├── mint.json             # Mintlify configuration
├── LICENSE               # Apache License 2.0
└── README.md
```

---

## Philosophy

QWED is built around deterministic verification principles:

- **Fail closed by default** — unknown states are never treated as safe
- **Verification requires explicit evidence** — no silent assumptions, no fabricated defaults
- **Heuristics must not silently become proof** — LLM outputs are always marked `HEURISTIC` when symbolic verification is not possible
- **Auditability and reproducibility are first-class** — every verification is deterministic and inspectable
- **The LLM is the Untrusted Translator** — it converts natural language to formal DSLs; symbolic engines are the Trusted Verifiers

The documentation follows the same philosophy:

- **Precise over promotional**
- **Explicit over ambiguous**
- **Operational over hype**

> *Probabilistic systems should not be trusted with deterministic tasks. If it can't be verified, it doesn't ship.*

---

## Contributing

Contributions are welcome for:

- 📝 Documentation fixes and typo corrections
- 🔧 Broken code examples
- 💡 Clarification requests
- 🐛 Inaccurate guard behavior descriptions

Please open an issue or submit a pull request. For contribution guidelines, see the main [QWED Contributing Guide](https://github.com/QWED-AI/qwed-verification/blob/main/CONTRIBUTING.md).

---

## Security

If you discover a security issue related to QWED documentation, examples, or verification workflows, please follow the [repository security policy](https://github.com/QWED-AI/qwed-verification/security/policy).

---

## License

[Apache License 2.0](LICENSE)

```
Copyright 2025 QWED-AI

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
```
