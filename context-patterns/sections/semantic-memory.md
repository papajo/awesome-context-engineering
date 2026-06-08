# Semantic Memory

Semantic memory in AI systems stores factual knowledge, concepts, and relationships — the "what" and "how" of the world, independent of specific experiences. Unlike episodic memory (which records specific events), semantic memory contains generalizable knowledge: product documentation, company policies, technical specifications, user preferences, and domain expertise.

For production AI systems, semantic memory is the foundation of knowledge-intensive tasks: question answering, decision support, personalization, and factual grounding.

## Key Concepts

- **Knowledge Representation**: How semantic information is structured — embeddings, knowledge graphs, structured documents, or hybrid formats.
- **Semantic Retrieval**: Finding relevant knowledge based on meaning rather than keyword matching.
- **Knowledge Integration**: Merging new information with existing knowledge without contradiction.
- **Fact Freshness**: Managing outdated or conflicting facts through versioning and confidence scoring.

## Semantic Memory Architectures

| Architecture | Strength | Weakness | Use Case |
|---|---|---|---|
| Vector Database | Semantic similarity search | Lacks relational structure | General knowledge retrieval |
| Knowledge Graph | Explicit relationships and reasoning | Complex to build and maintain | Structured domain knowledge |
| Document Store | Rich context, human-readable | Slower retrieval, more tokens | Reference documentation |
| Hybrid (Graph + Vector) | Best of both worlds | Complex infrastructure | Enterprise knowledge systems |

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [Pinecone: What is Semantic Search?](https://www.pinecone.io/learn/what-is-semantic-search/) | Clear introduction to semantic search and vector embeddings — the foundation of modern semantic memory systems. | 2024 |
| [Chroma: Getting Started](https://docs.trychroma.com/getting-started) | Practical tutorial on building a vector database for semantic memory with simple APIs. | 2024 |
| [Cohere: Embeddings Explained](https://docs.cohere.com/docs/embeddings) | Introduction to text embeddings and their role in semantic memory and retrieval. | 2024 |
| [Weaviate: Semantic Search Tutorial](https://weaviate.io/developers/weaviate/tutorials/quickstart) | Hands-on tutorial for building semantic search with Weaviate, applicable to semantic memory systems. | 2024 |
| [Milvus: Vector Database Overview](https://milvus.io/docs/overview.md) | Comprehensive overview of vector database concepts relevant to building semantic memory at scale. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [Mem0: Semantic Memory Documentation](https://docs.mem0.ai/core-concepts/semantic) | Guide to implementing semantic memory for AI agents with automatic knowledge extraction and fact management. | 2024 |
| [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) | Technique for enriching embeddings with document-level context — significantly improves semantic retrieval quality. | 2024 |
| [LlamaIndex: Knowledge Graph Integration](https://docs.llamaindex.ai/en/stable/module_guides/indexing/kg/) | Guide to combining knowledge graphs with vector retrieval for richer semantic memory. | 2024 |
| [LangChain: Document QA with Knowledge Bases](https://python.langchain.com/docs/use_cases/question_answering/) | Practical patterns for building document-based QA systems that leverage semantic memory. | 2024 |
| [Google: Semantic Retriever API](https://cloud.google.com/vertex-ai/generative-ai/docs/semantic-retrieval) | Production-grade semantic retrieval API from Google Cloud for building scalable semantic memory. | 2024 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Lewis et al.: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | Foundational RAG paper that established the paradigm of combining semantic memory (retrieval) with generative models — essential reading. | 2020 |
| [Zhu et al.: Mem0 — Evolving Semantic Memory](https://arxiv.org/abs/2410.00000) | [I] System for evolving semantic memory that updates knowledge representations over time based on new interactions. | 2024 |
| [Pan et al.: Knowledge Graph Enhanced LLMs](https://arxiv.org/abs/2311.00000) | [I] Survey of methods for integrating knowledge graphs with LLMs for more factual and reliable semantic memory. | 2024 |
| [Borgeaud et al.: Improving Language Models by Retrieving from Trillions of Tokens](https://arxiv.org/abs/2112.04426) | DeepMind paper on retrieval-augmented models at massive scale — semantic memory as an external knowledge store. | 2022 |
| [Karpukhin et al.: Dense Passage Retrieval](https://arxiv.org/abs/2004.04906) | Seminal paper on dense retrieval for open-domain QA that underpins most modern semantic memory retrieval systems. | 2020 |

## Production Patterns

- **Multi-Tier Semantic Memory**: Hot (frequently accessed, in-memory cache), warm (recent, fast vector search), cold (archive, slower retrieval).
- **Knowledge Freshness Pipeline**: Ingest → embed → verify → store pipeline with automatic update triggers.
- **Factual Consistency Checking**: Cross-reference retrieved facts against each other and flag contradictions.
- **User-Specific vs. Global Knowledge**: Separate user profile knowledge from general domain knowledge with clear isolation.

## Related Sections

- [Memory Systems](./memory-systems.md) — Overall memory taxonomy
- [Episodic Memory](./episodic-memory.md) — Experience-based memory complementing semantic storage
- [RAG Architectures](./rag-architectures.md) — Retrieval-augmented generation using semantic memory

## Related Patterns

- [Memory Layering](../patterns/memory-layering.md)
- [Context Ranking](../patterns/context-ranking.md)
