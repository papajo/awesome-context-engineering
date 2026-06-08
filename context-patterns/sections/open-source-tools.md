# Open Source Tools

Open source tools are the backbone of the context engineering ecosystem. From vector databases and embedding models to retrieval frameworks and evaluation platforms, the open source community has produced production-quality infrastructure that powers most context engineering systems.

This section catalogs the most important open source tools for context engineering, organized by category, with annotations on production readiness and ecosystem fit.

## Tools by Category

### Vector Databases

| Tool | Description | Production Ready |
|---|---|---|
| **Chroma** | Embedded vector database, simple API | Yes — prototyping to small production |
| **Qdrant** | High-performance vector search with filtering | Yes — production at scale |
| **Weaviate** | Vector + hybrid search with GraphQL | Yes — enterprise production |
| **Milvus** | Distributed vector database for billion-scale | Yes — large-scale production |
| **Pgvector** | PostgreSQL vector extension | Yes — integrates with existing SQL |

### Embedding Models

| Model | Size | Languages | Quality |
|---|---|---|---|
| **BGE (BAAI)** | Small-Large | 100+ | Top-tier open embeddings |
| **E5 (Microsoft)** | Small-Large | English | Strong multilingual |
| **GTE (Alibaba)** | Small-Large | 100+ | Excellent retrieval quality |
| **Jina Embeddings** | Small-Large | 100+ | Good general purpose |
| **Nomic Embed** | Various | English | Strong with RAG focus |

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [Chroma: Getting Started](https://docs.trychroma.com/getting-started) | Simplest vector database to start with — ideal for learning context retrieval basics. | 2024 |
| [LangChain: Open Source Tools Guide](https://python.langchain.com/docs/integrations/providers/) | Comprehensive catalog of open source tool integrations in LangChain — practical starting point. | 2024 |
| [LlamaIndex: Tool Integrations](https://docs.llamaindex.ai/en/stable/community/integrations/) | Guide to integrating open source tools with LlamaIndex for context engineering. | 2024 |
| [Hugging Face: Open Source Models](https://huggingface.co/models) | Largest hub of open source models including embedding, reranking, and generation models for context systems. | 2024 |
| [Ollama: Local LLM Runner](https://ollama.com/) | Run open source LLMs locally — essential for local development of context engineering systems. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [Qdrant: Production Deployment Guide](https://qdrant.tech/documentation/guides/distributed_deployment/) | Guide to deploying Qdrant at scale for production vector search — practical for high-load retrieval. | 2024 |
| [Weaviate: Hybrid Search Configuration](https://weaviate.io/developers/weaviate/search/hybrid) | Configuring hybrid search in Weaviate — critical for achieving high retrieval quality. | 2024 |
| [Milvus: Billion-Scale Vector Search](https://milvus.io/docs/clustering.md) | Architecture guide for billion-scale vector search with Milvus — for large-scale memory systems. | 2024 |
| [Pgvector: PostgreSQL Vector Search](https://github.com/pgvector/pgvector) | Open-source vector extension for PostgreSQL — production pattern for teams already on Postgres. | 2024 |
| [FlagEmbedding: BGE Model Suite](https://github.com/FlagOpen/FlagEmbedding) | BAAI's open-source embedding, reranking, and retrieval model suite — production-quality and widely used. | 2024 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [LanceDB: Serverless Vector Database](https://lancedb.github.io/lancedb/) | Columnar vector database designed for ML workflows with zero-copy access — emerging production pattern. | 2024 |
| [Jina: CLIP-as-Service and Embeddings](https://jina.ai/embeddings/) | Production-grade embedding service with multi-modal support — important for rich media context engineering. | 2024 |
| [Qdrant: Custom Quantization for Vector Search](https://qdrant.tech/documentation/guides/quantization/) | Advanced quantization techniques for reducing memory footprint in production vector search. | 2024 |
| [Weaviate: Multi-Tenancy Configuration](https://weaviate.io/developers/weaviate/configuration/multi-tenancy) | Multi-tenancy patterns for vector databases — essential for SaaS context engineering platforms. | 2024 |
| [Mem0: Open Source Memory Layer](https://github.com/mem0ai/mem0) | Open source memory layer for AI agents with automatic memory extraction, consolidation, and retrieval. | 2024 |

## Tool Selection Guide

### Vector Database Selection

| Criterion | Chroma | Qdrant | Weaviate | Milvus | Pgvector |
|---|---|---|---|---|---|
| Ease of setup | ★★★★★ | ★★★★ | ★★★★ | ★★★ | ★★★★★ |
| Scalability | ★★ | ★★★★★ | ★★★★ | ★★★★★ | ★★★ |
| Hybrid search | ✓ | ✓ | ✓ | ✓ | Limited |
| Filtering | Basic | Advanced | Advanced | Advanced | Full SQL |
| Managed cloud | — | ✓ | ✓ | ✓ | — |

### Framework Selection

| Criterion | LangChain | LlamaIndex | Haystack |
|---|---|---|---|
| Flexibility | ★★★★ | ★★★ | ★★★★ |
| RAG components | ★★★★ | ★★★★★ | ★★★★ |
| Agent support | ★★★★★ | ★★★★ | ★★★ |
| Memory support | ★★★ | ★★★★ | ★★ |
| Production tooling | LangSmith | — | deepset Cloud |

## Related Sections

- [Frameworks](./frameworks.md) — Full frameworks for context engineering
- [Tutorials](./tutorials.md) — Tutorials for using open source tools
- [RAG Architectures](./rag-architectures.md) — Building RAG with open source tools

## Related Patterns

- [Context Observability](../patterns/context-observability.md)
