# Design and Architecture Patterns

This directory contains detailed implementation guides for core Context Engineering patterns. Each pattern includes Problem, Solution, Architecture (with Mermaid diagram), Tradeoffs, Example Workflow, Example Prompt, Failure Modes, and Production Considerations.

## Patterns

| Pattern | Description | Key Topics |
|---|---|---|
| [Rolling Memory](./rolling-memory.md) | Sliding window memory with summary chains and archival retrieval | Token budget, summarization, archival, eviction |
| [Context Compression](./context-compression.md) | Multi-stage compression — structural, extractive, abstractive | Token reduction, semantic preservation, rate adaptation |
| [Context Ranking](./context-ranking.md) | Multi-signal relevance scoring with budget allocation | Position bias, reranking, freshness, diversity |
| [Context Pruning](./context-pruning.md) | Three-pass deterministic pruning — dedup, noise, overlap | Cost-benefit, safety filtering, sliding window |
| [Memory Layering](./memory-layering.md) | Four-tier cognitive memory architecture | Working, episodic, semantic, procedural memory |
| [Agent Context Management](./agent-context-management.md) | Lifecycle context for autonomous agents | State mgmt, context pressure, checkpoint summaries |
| [Context Observability](./context-observability.md) | Full pipeline telemetry with tracing and metrics | Spans, snapshots, drift detection, alerting |
| [Long Context Strategies](./long-context-strategies.md) | Techniques for 128K–2M token windows | Positional optimization, tiered loading, RoPE scaling |

## Cross-References

- **Sections** — Foundational knowledge in [/sections](../sections/README.md)
- **Examples** — Pattern implementations in [/examples](../examples/README.md)
