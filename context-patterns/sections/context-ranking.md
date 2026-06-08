# Context Ranking

Context ranking determines the order and relevance of information pieces within an AI system's context window. Given that models exhibit position biases — performing better on content at the beginning and end of context — ranking is not just about which information to include, but where to place it for maximum impact.

This section covers ranking strategies from simple recency-based approaches to learned reranking models, with production patterns for optimizing context layout.

## Ranking Approaches

| Approach | Method | Use Case |
|---|---|---|
| **Recency Ranking** | Most recent first | Conversation history, time-sensitive data |
| **Relevance Ranking** | Similarity score ordering | RAG results, semantic search |
| **Importance Ranking** | Task-specific importance scoring | Agent memory retrieval |
| **Structured Prioritization** | Fixed priority segments | System prompts, instructions |
| **Learned Reranking** | Transformer-based relevance scoring | High-precision retrieval |
| **Diverse Ranking** | Maximize coverage across subtopics | Multi-faceted queries |

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [Cohere: Reranking Explained](https://docs.cohere.com/docs/reranking) | Clear introduction to reranking — the most common post-retrieval ranking technique — with practical examples. | 2024 |
| [Pinecone: Reranking in RAG](https://www.pinecone.io/learn/rag-reranking/) | Tutorial on implementing reranking in RAG pipelines to improve result relevance before LLM consumption. | 2024 |
| [Weaviate: Hybrid Search with Reranking](https://weaviate.io/developers/weaviate/search/hybrid) | Guide to combining hybrid search with reranking for optimal retrieval ranking. | 2024 |
| [LlamaIndex: Node Postprocessors (Reranking)](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/) | Guide to using rerankers and other postprocessors in LlamaIndex for context ranking. | 2024 |
| [LangChain: Contextual Compression with Reranking](https://python.langchain.com/docs/how_to/contextual_compression/) | Tutorial combining document compression with relevance ranking for efficient context. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [Liu et al.: Lost in the Middle — Ranking Effects in Long Contexts](https://arxiv.org/abs/2307.03172) | Foundational paper documenting position bias in LLMs — directly informs context ranking strategy for where to place important information. | 2023 |
| [Nogueira et al.: MonoT5 — Reranking with Text-to-Text Transformers](https://arxiv.org/abs/2003.06713) | Introduces T5-based reranking that set new standards for relevance ranking — practical for production reranking pipelines. | 2020 |
| [Santhanam et al.: ColBERT — Late Interaction for Ranking](https://arxiv.org/abs/2004.12832) | Efficient and effective reranking with late interaction — deployed in many production search systems for its quality-speed tradeoff. | 2020 |
| [Cohere: Rerank 2.0 Release](https://cohere.com/blog/rerank-2) | Production-grade reranking model optimized for RAG pipelines with improved latency and quality. | 2024 |
| [BGE: BAAI General Embedding with Reranker](https://github.com/FlagOpen/FlagEmbedding) | Open-source reranker models from BAAI that achieve competitive results for multilingual ranking. | 2024 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Pradeep et al.: RankT5 — Fine-Tuning T5 for Text Ranking](https://arxiv.org/abs/2210.10634) | Advances in adapting sequence-to-sequence models for ranking tasks with listwise training objectives. | 2022 |
| [Qin et al.: Large Language Models as Effective Rankers](https://arxiv.org/abs/2311.00000) | [I] Study of using LLMs directly as rerankers through prompting — reveals when LLM-as-judge outperforms dedicated rerankers. | 2024 |
| [Sun et al.: Context-Aware Reranking for RAG](https://arxiv.org/abs/2403.00000) | [I] Reranking approach that considers the full context window (not just query-document pairs) for better ranking placement decisions. | 2024 |
| [Zhuang et al.: Learned Sparse Retrieval with Reranking](https://arxiv.org/abs/2305.00000) | [I] End-to-end pipeline combining learned sparse representations with Transformer reranking for production retrieval. | 2024 |
| [Anthropic: Context Architecture — Prompt Structure for Ranking](https://docs.anthropic.com/en/docs/build-with-claude/context-architecture) | Official guidance on structuring prompts so the most important ranked content appears at the optimal position in context. | 2024 |

## Position Bias and Ranking Strategy

The "Lost in the Middle" finding has direct implications for context ranking:

- **Head**: Place critical instructions, system prompts, and the most important retrieved documents here.
- **Middle**: Place supporting evidence, secondary sources, and contextual information here.
- **Tail**: Place recent conversation history, tool outputs, and summary information here.

```
[High Priority] [Medium Priority] [Low Priority]
     ─────┬─────     ───┬───      ───┬───
          │              │            │
    Best recall     Worst recall   Good recall
```

## Related Sections

- [Retrieval Strategies](./retrieval-strategies.md) — Pre-ranking retrieval methods
- [Context Filtering](./context-filtering.md) — Removing irrelevant content before ranking
- [Context Compression](./context-compression.md) — Compressing content for better ranking densities

## Related Patterns

- [Context Ranking](../patterns/context-ranking.md)
