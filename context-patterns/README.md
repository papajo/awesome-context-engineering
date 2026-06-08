# Context Patterns — Reference Layer

This is the **reference catalog** for the [Swaha](../README.md) recipe collection. Use it when you need the full picture — deep-dive patterns, curated resources, and architecture examples.

> 🔧 **Need code first?** Start with the [Recipes](./recipes/) — 6 standalone Python files with zero dependencies. Or the [Quickstart](./quickstart/README.md) — 10 minutes, real pipeline.

---

## Practical Layer

| Resource | What You Get |
|---|---|
| [Recipes](./recipes/) | 6 standalone Python files — rolling memory, compression, ranking, pruning, budget tracking, memory layering |
| [Cookbook Index](./COOKBOOK.md) | Table of contents linking to each recipe with problem + savings summary |
| [Decision Guide](./DECISION-GUIDE.md) | Mermaid decision tree + comparison tables + anti-patterns |
| [Cheatsheets](./cheatsheets/) | One-page quick references: rolling memory, compression, ranking, agent context management |
| [Quickstart](./quickstart/README.md) | Build a full context pipeline (prune → rank → compress → assemble) in 10 minutes |

---

## Patterns

Eight deep-dive implementation guides. Each includes Problem, Solution, Architecture (Mermaid), Tradeoffs, Failure Modes, and Production Considerations.

| Pattern | Problem |
|---------|---------|
| [Rolling Memory](./patterns/rolling-memory.md) | Sliding window + summaries + archival |
| [Context Compression](./patterns/context-compression.md) | Multi-stage compression pipeline |
| [Context Ranking](./patterns/context-ranking.md) | Multi-signal relevance scoring |
| [Context Pruning](./patterns/context-pruning.md) | Three-pass deterministic dedup |
| [Memory Layering](./patterns/memory-layering.md) | Four-tier cognitive memory |
| [Agent Context Management](./patterns/agent-context-management.md) | Lifecycle context for autonomous agents |
| [Context Observability](./patterns/context-observability.md) | Full pipeline telemetry |
| [Long Context Strategies](./patterns/long-context-strategies.md) | Techniques for 128K–2M token windows |

## Examples

Seven architecture examples with Mermaid diagrams and context flow docs:

[Customer Support Agent](./examples/customer-support-agent/) · [Coding Agent](./examples/coding-agent/) · [Research Agent](./examples/research-agent/) · [Sales Agent](./examples/sales-agent/) · [Autonomous Workflow Agent](./examples/autonomous-workflow-agent/) · [RAG System](./examples/rag-system/) · [MCP-Powered Agent](./examples/mcp-powered-agent/)

## Sections

Curated resource lists across 28 topics, each annotated by difficulty and production relevance.

[Foundations](./sections/foundations.md) · [Context Windows](./sections/context-windows.md) · [Attention Mechanisms](./sections/attention-mechanisms.md) · [Long Context Models](./sections/long-context-models.md) · [Memory Systems](./sections/memory-systems.md) · [Episodic Memory](./sections/episodic-memory.md) · [Semantic Memory](./sections/semantic-memory.md) · [Agent Memory](./sections/agent-memory.md) · [RAG Architectures](./sections/rag-architectures.md) · [Retrieval Strategies](./sections/retrieval-strategies.md) · [Context Compression](./sections/context-compression.md) · [Context Ranking](./sections/context-ranking.md) · [Context Filtering](./sections/context-filtering.md) · [Context Pruning](./sections/context-pruning.md) · [MCP Ecosystem](./sections/mcp-ecosystem.md) · [Agent Context Management](./sections/agent-context-management.md) · [Multi-Agent Context Sharing](./sections/multi-agent-context-sharing.md) · [Evaluation](./sections/evaluation.md) · [Benchmarks](./sections/benchmarks.md) · [Observability](./sections/observability.md) · [Production Patterns](./sections/production-patterns.md) · [Research Papers](./sections/research-papers.md) · [Open Source Tools](./sections/open-source-tools.md) · [Frameworks](./sections/frameworks.md) · [Tutorials](./sections/tutorials.md) · [Courses](./sections/courses.md) · [Blogs](./sections/blogs.md)

## Getting Started

1. **New?** Start with the [Quickstart](./quickstart/README.md).
2. **Have a specific problem?** Use the [Decision Guide](./DECISION-GUIDE.md).
3. **Want code?** Open a [Recipe](./recipes/).
4. **Need the full picture?** Browse [patterns](./patterns/) or [sections](./sections/).

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).
