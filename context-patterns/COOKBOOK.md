# Context Patterns — Cookbook

> 6 copy-paste recipes for context engineering. Each recipe solves a real problem, is written in Python with zero external dependencies, and links to the relevant pattern for deeper understanding.
>
> ⚠️ Requires Python 3.10+ (uses `dict | dict` merge and `type hint | union` syntax).

---

## Recipes

| # | Recipe | Problem | Savings | Link |
|---|--------|---------|---------|------|
| 1 | Rolling Memory | Conversation exceeds context window | Never lose context | [▶ Open](./recipes/01-rolling-memory.md) |
| 2 | Context Compression | Documents consume too many tokens | **2–10× reduction** | [▶ Open](./recipes/02-context-compression.md) |
| 3 | Multi-Signal Ranking | Too many candidates for limited budget | Filter low-signal items | [▶ Open](./recipes/03-context-ranking.md) |
| 4 | Context Pruning | RAG retrieves duplicates and noise | **15–60% fewer tokens** | [▶ Open](./recipes/04-context-pruning.md) |
| 5 | Agent Budget Tracker | Agent traces overflow context window | Auto-archive before overflow | [▶ Open](./recipes/05-agent-context-budget.md) |
| 6 | Memory Layering | Single store conflates different memory types | 4-tier cognitive architecture | [▶ Open](./recipes/06-memory-layering.md) |

---

## How to Use

1. **Pick a recipe** from the table above based on your problem.
2. **Open the individual file** — each is standalone with its own `__main__` block.
3. **Run it:** `python3 recipes/XX-recipe-name.md` won't work directly on `.md`, but copy the code block into a `.py` file.
4. **Read the full pattern** linked at the top of each recipe for production considerations, failure modes, and tradeoffs.
5. **Replace placeholders** — swap heuristic implementations (Jaccard similarity, keyword search, extractive summary) with real LLM calls, embedding models, and vector databases.

## Related

- [Decision Guide](./DECISION-GUIDE.md) — which pattern fits your problem?
- [Cheatsheets](./cheatsheets/) — one-page quick references
- [Quickstart](./quickstart/) — 10-minute walkthrough
