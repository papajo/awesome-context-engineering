# Documentation Sections

This directory contains the main documentation sections for Context Engineering — covering the full landscape from foundational concepts through production patterns and resources.

Each section includes:
- Introductory explanation of the topic
- Curated resources categorized by difficulty (Beginner / Intermediate / Advanced)
- Annotations explaining why each resource matters
- Production relevance highlights
- Links to related sections and patterns

## Core Concepts

| Section | Description | Topics |
|---|---|---|
| [Foundations](./foundations.md) | Core principles, evolution, and fundamental concepts | Context window, utilization, architecture, information density |
| [Context Windows](./context-windows.md) | Window mechanics, model capabilities, position bias | Token budgeting, RoPE scaling, lost in the middle |
| [Attention Mechanisms](./attention-mechanisms.md) | Transformer attention, efficient variants, implications | FlashAttention, sliding window, Mamba, sparse attention |
| [Long Context Models](./long-context-models.md) | Model landscape, architectures, vs RAG tradeoffs | Gemini 1.5, Claude 3, Llama 3.1, YaRN |

## Memory Systems

| Section | Description | Topics |
|---|---|---|
| [Memory Systems](./memory-systems.md) | Taxonomy, architecture patterns, design decisions | Working, episodic, semantic, procedural, hybrid |
| [Episodic Memory](./episodic-memory.md) | Experience-based memory for agents | Event storage, episodic retrieval, consolidation |
| [Semantic Memory](./semantic-memory.md) | Knowledge-based memory systems | Embeddings, knowledge graphs, fact freshness |
| [Agent Memory](./agent-memory.md) | Full memory architecture for autonomous agents | Self-managing, reflection-based, hierarchical |

## Retrieval & Generation

| Section | Description | Topics |
|---|---|---|
| [RAG Architectures](./rag-architectures.md) | Retrieval-augmented generation levels and components | Naive, advanced, modular, agentic RAG |
| [Retrieval Strategies](./retrieval-strategies.md) | Technical retrieval methods and pipelines | Dense, sparse, hybrid, multi-hop, HyDE |

## Context Optimization

| Section | Description | Topics |
|---|---|---|
| [Context Compression](./context-compression.md) | Reducing token count while preserving meaning | Extractive, abstractive, learned compression |
| [Context Ranking](./context-ranking.md) | Ordering information for optimal utilization | Position bias, reranking, structured prioritization |
| [Context Filtering](./context-filtering.md) | Removing irrelevant or low-quality information | Relevance, recency, redundancy, safety filtering |
| [Context Pruning](./context-pruning.md) | Ongoing maintenance removal of low-value content | Sliding window, importance scoring, cost-benefit |

## Agents & Multi-Agent

| Section | Description | Topics |
|---|---|---|
| [MCP Ecosystem](./mcp-ecosystem.md) | Model Context Protocol architecture and tools | MCP servers, clients, protocol, ecosystem |
| [Agent Context Management](./agent-context-management.md) | Context architecture for autonomous agents | State management, context pressure, tool integration |
| [Multi-Agent Context Sharing](./multi-agent-context-sharing.md) | Shared context across agent teams | Shared memory, message passing, blackboard, isolation |

## Quality & Operations

| Section | Description | Topics |
|---|---|---|
| [Evaluation](./evaluation.md) | Measuring context system effectiveness | RAGAS, faithfulness, component vs end-to-end |
| [Benchmarks](./benchmarks.md) | Standardized tests for comparison | Needle-in-Haystack, LongBench, CRAG, MTEB |
| [Observability](./observability.md) | Monitoring context pipelines in production | Tracing, metrics, drift detection, alerting |
| [Production Patterns](./production-patterns.md) | Battle-tested approaches for production | Caching, budgeting, staged retrieval, A/B testing |

## Resources

| Section | Description | Topics |
|---|---|---|
| [Research Papers](./research-papers.md) | Academic foundations of context engineering | Lost in the Middle, FlashAttention, MemGPT, Self-RAG |
| [Open Source Tools](./open-source-tools.md) | Production-quality open source infrastructure | Chroma, Qdrant, Weaviate, Milvus, BGE, Mem0 |
| [Frameworks](./frameworks.md) | Development frameworks for context systems | LangChain, LlamaIndex, Haystack, CrewAI, AutoGen |
| [Tutorials](./tutorials.md) | Hands-on practical guides | RAG building, memory implementation, MCP development |
| [Courses](./courses.md) | Structured learning paths | DeepLearning.AI, Stanford CS224N, Hugging Face |
| [Blogs](./blogs.md) | Timely practitioner insights | Anthropic Blog, Cohere Blog, Latent Space |

## Explore Further

- **Patterns** — Practical implementation guides in [/patterns](../patterns/README.md)
- **Examples** — Architecture, workflow, and context flow docs in [/examples](../examples/README.md)
- **Full Repository Guide** — [README.md](../README.md)
