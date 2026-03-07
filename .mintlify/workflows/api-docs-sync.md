---
name: "API Docs Sync"
on:
  push:
    - repo: "qwed-ai/qwed-verification"
    - repo: "qwed-ai/qwed-tax"
    - repo: "qwed-ai/qwed-legal"
context:
  - repo: "qwed-ai/qwed-finance"
  - repo: "qwed-ai/qwed-mcp"
  - repo: "qwed-ai/qwed-ucp"
  - repo: "qwed-ai/qwed-open-responses"
  - repo: "qwed-ai/qwed-learning"
---

When a PR is merged in any trigger repository, update the API documentation in `documentationai` (or your docs repo) to reflect the recent code changes.

Guidelines:
1. **Target:** Update the OpenAPI/Swagger specs, SDK reference pages, and relevant `.mdx` or `.json` API documentation files.
2. **Format:** Follow the existing structure of the DocumentationAI platform. Do not use unsupported components like `<TabItem>`. Use the native `<ParamField>`, `<ResponseField>`, and `<Tabs>` with `<Tab>` structure if modifying MDX files.
3. **Clarity:** Ensure parameter descriptions, response schemas, and endpoint paths strictly match the merged python code/schemas (e.g. from `qwed_finance/schemas.py`, etc).
4. **Scope boundary:** Do not invent or assume undocumented endpoints. Only document what was explicitly added or modified in the triggering PR.
