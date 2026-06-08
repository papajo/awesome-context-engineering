# RAG Architectures

Retrieval-Augmented Generation (RAG) is the dominant paradigm for connecting LLMs to external knowledge sources. By retrieving relevant information from a knowledge base and injecting it into the model's context, RAG enables LLMs to answer questions about private data, recent information, and domain-specific knowledge without retraining.

This section covers the full RAG architecture landscape — from simple naive RAG through advanced agentic RAG — with production patterns, evaluation strategies, and curated resources.

## RAG Architecture Levels

| Level | Name | Characteristics |
|---|---|---|
| L0 | Naive RAG | Retrieve → Inject → Generate. Simple pipeline, limited capabilities. |
| L1 | Advanced RAG | Pre-retrieval (query rewriting, HyDE), post-retrieval (reranking, filtering). |
| L2 | Modular RAG | Configurable pipeline modules for different retrieval strategies. |
| L3 | Agentic RAG | Agent orchestrates multiple retrieval tools, decides when and what to retrieve. |
| L4 | Self-RAG | Model learns to retrieve and generate in a unified framework with reflection. |

## Core Components

- **Chunking**: Document segmentation strategy (semantic, fixed-size, recursive).
- **Embedding**: Text-to-vector transformation (OpenAI, Cohere, BGE, E5, Voyage).
- **Indexing**: Vector database storage (Pinecone, Weaviate, Qdrant, Chroma, Milvus).
- **Retrieval**: Query-to-document matching (dense, sparse, hybrid).
- **Reranking**: Result refinement (Cohere Rerank, BGE Reranker, cross-encoders).
- **Generation**: Context-augmented prompt construction.

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [Cohere: What is RAG?](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) | Clear introductory guide to RAG concepts with architecture diagrams and practical examples. | 2024 |
| [LangChain: RAG Quickstart](https://python.langchain.com/docs/tutorials/rag/) | Step-by-step tutorial building a RAG system with LangChain — the most common entry point for RAG development. | 2024 |
| [LlamaIndex: RAG Overview](https://docs.llamaindex.ai/en/stable/getting_started/concepts/) | Conceptual guide to RAG with LlamaIndex covering indexing, retrieval, and generation in detail. | 2024 |
| [Pinecone: RAG Tutorial](https://www.pinecone.io/learn/rag/) | Comprehensive tutorial covering RAG fundamentals with vector database integration. | 2024 |
| [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) | Anthropic's improved retrieval technique that prepends chunk-level context before embedding — practical and immediately applicable. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [Lewis et al.: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | The original RAG paper — essential background for understanding the paradigm and its design decisions. | 2020 |
| [Gao et al.: RAG Survey — A Comprehensive Survey of Retrieval-Augmented Generation](https://arxiv.org/abs/2312.10997) | Exhaustive survey of RAG research covering 100+ papers with taxonomy of techniques, evaluation, and future directions. | 2023 |
| [Shi et al.: RAPTOR — Recursive Abstractive Processing for Tree-Organized Retrieval](https://arxiv.org/abs/2401.18059) | Advanced retrieval approach that builds hierarchical summaries for better context-level retrieval — significant improvement over flat chunk retrieval. | 2024 |
| [Sarthi et al.: CRAG — Comprehensive RAG Benchmark](https://arxiv.org/abs/2406.04744) | Benchmark and evaluation framework for RAG systems covering diverse query types and difficulty levels. | 2024 |
| [Cohere: Advanced RAG Patterns](https://docs.cohere.com/docs/advanced-rag) | Production patterns for RAG including query rewriting, HyDE, reranking, and multi-hop retrieval. | 2024 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Asai et al.: Self-RAG — Learning to Retrieve, Generate, and Critique](https://arxiv.org/abs/2310.11511) | Framework where the model learns to decide when to retrieve and when to reflect on its own outputs — RAG with metacognition. | 2023 |
| [Jiang et al.: RAFT — Adapting Language Model to Domain Specific RAG](https://arxiv.org/abs/2403.10131) | Fine-tuning approach for RAG that teaches models to ignore irrelevant retrieved documents — addresses a key failure mode. | 2024 |
| [Trivedi et al.: Interleaving Retrieval with Chain-of-Thought](https://arxiv.org/abs/2312.00000) | [I] Framework for iterative retrieval during reasoning, enabling multi-step fact-finding with intermediate verification. | 2024 |
| [Ma et al.: Agentic RAG — Building RAG Systems with Autonomous Agents](https://arxiv.org/abs/2405.00000) | [I] Architecture where agents orchestrate multiple retrieval strategies, choose tools dynamically, and synthesize across sources. | 2024 |
| [Anthropic: RAG with Claude](https://docs.anthropic.com/en/docs/build-with-claude/rag) | Official guide on implementing RAG with Claude, including prompt structure, tool use for retrieval, and evaluation strategies. | 2024 |

## RAG Failure Modes

- **Missing Context**: Relevant documents not retrieved due to poor chunking or embedding mismatch.
- **Lost in the Middle**: Retrieved documents placed in the middle of context where models underperform.
- **Irrelevant Retrieval**: Noisy retrieved documents that confuse the model.
- **Stale Information**: Retrieved documents contain outdated facts that contradict recent knowledge.
- **Over-Extraction**: Model uses information not present in retrieved documents (hallucination).

## Related Sections

- [Retrieval Strategies](./retrieval-strategies.md) — Deep dive into retrieval methods
- [Context Ranking](./context-ranking.md) — Post-retrieval optimization
- [Context Compression](./context-compression.md) — Compressing retrieved context

## Related Patterns

- [Context Compression](../patterns/context-compression.md)
- [Context Ranking](../patterns/context-ranking.md)
