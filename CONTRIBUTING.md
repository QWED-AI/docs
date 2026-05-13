# Contributing to QWED Documentation

> **QWED** = **Q**uery with **E**vidence and **D**eterminism

Thank you for your interest in contributing to QWED Documentation.

This repository documents deterministic verification systems, security boundaries, and fail-closed verification workflows. Because documentation directly affects how users understand and implement QWED systems, contributions are reviewed carefully for technical accuracy, clarity, and consistency.

---

## 📚 Required Reading (Before Contributing)

| File | Why It Matters |
|------|----------------|
| [README.md](./README.md) | Understand the docs repository scope and ecosystem |
| [QWED Verification README](https://github.com/QWED-AI/qwed-verification/blob/main/README.md) | Core protocol philosophy and architecture |
| [QWED_RULES.md](https://github.com/QWED-AI/qwed-verification/blob/main/QWED_RULES.md) | Canonical enforcement rules — the source of truth |

When documentation content and enforcement rules appear to conflict, `QWED_RULES.md` is the authoritative source for boundary behavior.

---

## 🎯 Current Contribution Scope

At this stage, contributions are **intentionally limited** while the documentation architecture stabilizes.

### ✅ We Currently Welcome

- Typo and grammar fixes
- Broken link fixes
- Formatting and readability improvements
- Documentation clarification requests
- Code example corrections (must be reproducible)
- API reference corrections
- Small deterministic examples

### ❌ May Be Declined

- Large architectural rewrites
- Speculative or roadmap content
- Marketing-heavy or promotional edits
- Undocumented feature additions
- Content that weakens precision or introduces ambiguity
- Probabilistic framing without explicit `HEURISTIC` labeling

---

## 🧠 Core Documentation Principles

### 1. Deterministic Over Promotional

| Prefer | Avoid |
|--------|-------|
| Precise claims with explicit boundaries | Hype language or exaggerated guarantees |
| Operational details and verifiable behavior | Vague "AI magic" explanations |
| Concrete code examples with expected output | Hand-wavy descriptions |

### 2. Unknown States Must Be Explicit

Never describe uncertain behavior as guaranteed behavior.

If a workflow is partial, experimental, advisory, heuristic-based, or incomplete — it **must** be labeled clearly. Undeclared uncertainty is a documentation bug.

### 3. Verification Terminology Matters

Use terms consistently across all documentation:

| ✅ Preferred | ❌ Avoid |
|---|---|
| `verified` | smart |
| `deterministic` | intelligent |
| `fail-closed` | safe enough |
| `unverifiable` | probably valid |
| `advisory` | guaranteed |
| `HEURISTIC` (for LLM-dependent results) | accurate |

Do not blur the boundaries between:
- **validation** (input format checking)
- **parsing** (structural extraction)
- **simplification** (reduction)
- **heuristics** (probabilistic estimation)
- **verification** (deterministic proof)

### 4. Security Claims Must Be Accurate

Do not claim:
- ❌ Perfect security
- ❌ Guaranteed correctness beyond stated boundaries
- ❌ Impossible-to-bypass protection

Documentation must accurately represent the actual implemented behavior — nothing more, nothing less.

---

## 🚀 How to Contribute

### 1. Reporting Issues

Open an issue for:
- Incorrect or misleading documentation
- Broken code examples
- Unclear verification boundary descriptions
- Missing fail-closed behavior documentation

### 2. Submitting Pull Requests

```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/docs.git

# 2. Create a branch
git checkout -b fix/your-fix-description

# 3. Make changes

# 4. Preview locally
mintlify dev

# 5. Commit with conventional commits
git commit -m "docs: fix deadline guard example output"

# 6. Push and create PR
git push origin fix/your-fix-description
```

### Commit Message Format

```
type(scope): description

docs(legal): fix statute guard response fields table
docs(finance): correct NPV formula in example
fix(changelog): update broken PR link
docs: clarify fail-closed behavior for unknown jurisdictions
```

---

## ✅ Pull Request Expectations

### Good PRs

- Stay scoped to a single fix or improvement
- Explain **why** the change is needed
- Preserve deterministic terminology
- Keep examples minimal, reproducible, and explicit about assumptions
- Follow the existing writing style and MDX conventions

### PRs May Be Closed If They

- Introduce hype-oriented or marketing language
- Weaken precision of verification claims
- Add unverifiable or speculative claims
- Conflict with fail-closed philosophy
- Introduce probabilistic framing without explicit labeling
- Bypass the review process

### Review Standards

- All non-trivial changes require maintainer review
- Automated checks (Mintlify build, link validation) must pass
- Self-merging is restricted to typo fixes by maintainers

---

## ✍️ Style Guidelines

### Tone

| ✅ Preferred | ❌ Avoid |
|---|---|
| Technical, calm, direct | Aggressive marketing tone |
| Audit-friendly and precise | Exaggerated confidence |
| Operationally useful | Buzzword-heavy language |

### Code Examples

Examples must be:
- **Minimal** — shortest code that demonstrates the behavior
- **Deterministic** — same input always produces same output
- **Reproducible** — reader can copy-paste and run
- **Explicit** — state assumptions, expected output, and edge cases

If an example is incomplete or illustrative only, label it clearly:

```python
# ⚠️ Simplified example — production code should handle error cases
```

---

## ⚠️ What NOT to Contribute Here

These belong in their respective repositories, not in documentation PRs:

| Don't Add Here | Where It Belongs |
|----------------|-----------------|
| New guard implementations | [qwed-verification](https://github.com/QWED-AI/qwed-verification), [qwed-legal](https://github.com/QWED-AI/qwed-legal), [qwed-finance](https://github.com/QWED-AI/qwed-finance) |
| SDK code changes | Respective SDK repos |
| Enterprise features (audit, SSO, RBAC) | Separate enterprise repo |
| Telemetry / observability | Separate enterprise repo |

---

## 🔒 Security Reporting

If you discover:
- Unsafe or dangerous code examples
- Misleading verification claims that could cause operational risk
- Security-sensitive documentation issues
- Secret exposure in examples
- Incorrect operational guidance

**Do NOT open a public issue.** Use the [repository security policy](https://github.com/QWED-AI/qwed-verification/security/policy) instead.

---

## ⚖️ Governance & Legal

### Developer Certificate of Origin (DCO)

To contribute, you must sign off on your commits:

```
Signed-off-by: Your Name <your@email.com>
```

You can sign off automatically with `git commit -s`.

### Project Governance

This project is governed under a BDFL model. See the [QWED Governance](https://github.com/QWED-AI/qwed-verification/blob/main/GOVERNANCE.md) document for details.

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the [Apache License 2.0](./LICENSE).

---

## 💬 Questions?

- Open an issue with the `question` label
- Join discussions in [GitHub Discussions](https://github.com/QWED-AI/docs/discussions)
- Email: rahul@qwedai.com

---

> **QWED documentation is part of the trust boundary itself.** Ambiguous documentation creates operational risk, incorrect deployments, and false assumptions about verification guarantees. Clarity and correctness matter more than speed or volume.
