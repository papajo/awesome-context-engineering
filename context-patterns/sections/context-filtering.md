# Context Filtering

Context filtering removes irrelevant, redundant, or low-quality information from the context before it reaches the LLM. Unlike compression (which reduces size while preserving meaning) or ranking (which orders by importance), filtering makes binary or categorical decisions about inclusion — playing a critical gatekeeping role in production context pipelines.

This section covers filtering strategies from simple heuristic rules to learned relevance classifiers, with production patterns for maintaining context quality at scale.

## Filtering Dimensions

| Dimension | What It Removes | Method |
|---|---|---|
| **Relevance** | Documents unrelated to the query | Similarity threshold, classifier |
| **Recency** | Outdated or superseded information | Timestamp comparison |
| **Redundancy** | Duplicate or overlapping content | Deduplication (cosine, MinHash) |
| **Quality** | Low-quality or noisy content | Quality classifiers, perplexity scores |
| **Safety** | Harmful, toxic, or PII content | Content filters, PII scanners |
| **Authority** | Unreliable or contradictory sources | Source scoring, confidence thresholds |

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [LangChain: Document Filtering](https://python.langchain.com/docs/how_to/document_filtering/) | Practical guide to filtering documents in LangChain pipelines using relevance thresholds and metadata filtering. | 2024 |
| [LlamaIndex: Similarity Postprocessor](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/) | Guide to filtering nodes by similarity score in LlamaIndex — the simplest filtering approach. | 2024 |
| [Pinecone: Metadata Filtering](https://www.pinecone.io/learn/metadata-filtering/) | Tutorial on using metadata filtering in vector search to narrow results before similarity search. | 2024 |
| [Weaviate: Filtering in Vector Search](https://weaviate.io/developers/weaviate/search/filtering) | Guide to combining vector search with structured filtering for precise retrieval. | 2024 |
| [Qdrant: Payload Filtering](https://qdrant.tech/documentation/concepts/filtering/) | Documentation on filtering vector search results by payload conditions. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [Anthropic: Contextual Retrieval — Chunk-Level Filtering](https://www.anthropic.com/news/contextual-retrieval) | Anthropic's context-enrichment technique includes filtering signals that help distinguish relevant from irrelevant chunks. | 2024 |
| [Cohere: Relevance Threshold Tuning](https://docs.cohere.com/docs/relevance-tuning) | Guide on tuning relevance thresholds for filtering retrieved documents in production RAG systems. | 2024 |
| [Microsoft: Filtering for RAG Quality](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview) | Microsoft's guidance on filtering strategies in Azure AI Search for RAG quality improvement. | 2024 |
| [LlamaIndex: Recency Filtering](https://docs.llamaindex.ai/en/stable/module_guides/indexing/metadata_extraction/) | Techniques for extracting and filtering on temporal metadata to ensure context freshness. | 2024 |
| [Google: Data Quality Filtering for RAG](https://cloud.google.com/vertex-ai/generative-ai/docs/rag) | Google Cloud's approach to data quality filtering in Vertex AI RAG pipelines. | 2024 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Shani et al.: Multi-Step Retrieval with Filtering](https://arxiv.org/abs/2404.00000) | [I] Techniques for interleaving retrieval and filtering steps, where each retrieval round uses information from previous rounds to filter. | 2024 |
| [Adlakha et al.: Self-Filtering in RAG](https://arxiv.org/abs/2402.00000) | [I] Method where the LLM itself identifies and filters irrelevant information in context before generating — a form of self-consistency filtering. | 2024 |
| [Zhang et al.: Quality-Aware Content Filtering](https://arxiv.org/abs/2405.00000) | [I] Learned quality scores for documents that predict their usefulness for downstream tasks — enables quality-based filtering. | 2024 |
| [Wang et al.: Redundancy-Aware Filtering for RAG](https://arxiv.org/abs/2403.00000) | [I] Approach that identifies and removes redundant information across retrieved documents using embedding similarity and LLM-based detection. | 2024 |
| [Anthropic: Prompt Caching — Context Filtering Applications](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) | Using prompt caching with filtered context to avoid reprocessing unchanged filtered information — practical production optimization. | 2024 |

## Filtering Pipeline Design

```
Raw Retrieved Documents
         │
         ▼
┌─────────────────┐
│ Metadata Filter  │ ← Recency, source, domain filters
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Relevance Filter │ ← Similarity score threshold
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Deduplication   │ ← Remove near-duplicate content
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Quality Filter   │ ← Content quality / safety check
└────────┬────────┘
         │
         ▼
    Filtered Context
```

## Related Sections

- [Context Pruning](./context-pruning.md) — Removing low-value information (complementary to filtering)
- [Context Compression](./context-compression.md) — Compressing remaining context after filtering
- [Context Ranking](./context-ranking.md) — Ordering filtered content for optimal placement

## Related Patterns

- [Context Pruning](../patterns/context-pruning.md)
- [Context Compression](../patterns/context-compression.md)
