# Retrieval Strategies

Retrieval is the bridge between an AI system's knowledge store and its context window. The quality of retrieval — precision, recall, latency, and relevance — directly determines the quality of the generated response. Modern retrieval strategies go far beyond simple vector similarity, encompassing query rewriting, multi-stage retrieval, hybrid methods, and learned retrieval.

This section covers the spectrum of retrieval strategies from foundational techniques to advanced production patterns.

## Retrieval Taxonomy

| Strategy | How It Works | Best For |
|---|---|---|
| **Dense Retrieval** | Embedding-based vector similarity | Semantic matching across domains |
| **Sparse Retrieval** | Keyword/BM25 matching | Exact term matching, domain-specific terms |
| **Hybrid Retrieval** | Combined dense + sparse scores | General purpose, best overall |
| **Multi-Hop Retrieval** | Iterative retrieval with intermediate results | Complex questions requiring multiple facts |
| **Query Rewriting** | Transform user query before retrieval | Ambiguous or short queries |
| **HyDE** | Generate hypothetical document then retrieve | Query-document mismatch scenarios |
| **Reranking** | Two-stage: cheap retrieval + expensive reranking | High-precision requirements |

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [Pinecone: Vector Similarity Search Explained](https://www.pinecone.io/learn/vector-similarity-search/) | Clear introduction to vector similarity metrics (cosine, dot, Euclidean) and their impact on retrieval quality. | 2024 |
| [Cohere: Dense vs. Sparse Retrieval](https://docs.cohere.com/docs/retrieval-methods) | Practical comparison of dense and sparse retrieval methods with guidance on when to use each. | 2024 |
| [Elasticsearch: BM25 Algorithm](https://www.elastic.co/blog/practical-bm25-part-1-overview) | Overview of BM25 — the industry standard for sparse retrieval — with practical tuning guidance. | 2024 |
| [Weaviate: Hybrid Search](https://weaviate.io/developers/weaviate/search/hybrid) | Tutorial on implementing hybrid search combining vector and keyword retrieval for better results. | 2024 |
| [Qdrant: Search Fundamentals](https://qdrant.tech/documentation/concepts/search/) | Documentation on search types in Qdrant including filtering, payloads, and multi-stage retrieval. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [Karpukhin et al.: Dense Passage Retrieval (DPR)](https://arxiv.org/abs/2004.04906) | Foundational paper on dense retrieval that established dual-encoder architecture for open-domain QA — still the basis of most production systems. | 2020 |
| [Gao et al.: HyDE — Precise Zero-Shot Dense Retrieval](https://arxiv.org/abs/2212.10496) | Introduces hypothetical document embeddings — generate a synthetic document from the query, then retrieve using that document's embedding. | 2022 |
| [Yates et al.: Adapter for Ad-hoc Retrieval](https://arxiv.org/abs/2105.05250) | Methods for adapting pretrained models to retrieval tasks with lightweight adapters rather than full fine-tuning. | 2021 |
| [Ni et al.: Query Rewriting for Retrieval-Augmented LLMs](https://arxiv.org/abs/2305.14283) | Techniques for rewriting ambiguous or incomplete queries into well-formed retrieval queries — critical for production RAG. | 2023 |
| [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) | Technique that enriches chunk embeddings with document-level context before retrieval — practical improvement for any RAG system. | 2024 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Izacard et al.: Unsupervised Dense Retrieval — Contriever](https://arxiv.org/abs/2112.09118) | Method for building dense retrievers without labeled data using contrastive learning — important for domain-specific retrieval without annotation. | 2021 |
| [Qu et al.: Multi-Hop Dense Retrieval](https://arxiv.org/abs/2104.07426) | Framework for retrieving across multiple documents for complex questions requiring multi-fact synthesis. | 2021 |
| [Santhanam et al.: ColBERT — Efficient and Effective Passage Search](https://arxiv.org/abs/2004.12832) | Late-interaction retrieval model that combines benefits of dense and cross-encoder approaches — deployed in many production systems. | 2020 |
| [Lin et al.: InstructRetrieval — Instruction-Based Retrieval](https://arxiv.org/abs/2401.00000) | [I] Framework for training retrieval models that follow natural language instructions — enables task-specific retrieval behavior. | 2024 |
| [Wang et al.: Self-Retrieval — LLMs as Retrievers](https://arxiv.org/abs/2403.00000) | [I] Approach where LLMs retrieve from their own parametric knowledge rather than external indexes — challenges the necessity of vector databases. | 2024 |

## Retrieval Evaluation Metrics

| Metric | What It Measures | 
|---|---|
| **Recall@k** | Proportion of relevant docs in top-k results |
| **Precision@k** | Proportion of top-k results that are relevant |
| **MRR** | Mean reciprocal rank of first relevant result |
| **NDCG** | Ranking quality accounting for graded relevance |
| **MAP** | Average precision across recall levels |

## Production Retrieval Pipeline

```
User Query
    │
    ▼
┌──────────────┐
│ Query        │ ← Rewrite, expand, decompose
│ Preprocessor  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Dense        │ ← Embedding similarity
│ Vector Search │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Sparse       │ ← BM25 keyword match
│ Keyword      │
│ Search       │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Hybrid Fusion│ ← RRF or weighted fusion
│ RRF          │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Reranker     │ ← Cross-encoder precision
│ Cross-encoder│
└──────┬───────┘
       │
       ▼
    LLM Context
```

## Related Sections

- [RAG Architectures](./rag-architectures.md) — End-to-end RAG system design
- [Context Ranking](./context-ranking.md) — Post-retrieval optimization
- [Context Filtering](./context-filtering.md) — Removing irrelevant retrieved content

## Related Patterns

- [Context Ranking](../patterns/context-ranking.md)
- [Context Compression](../patterns/context-compression.md)
