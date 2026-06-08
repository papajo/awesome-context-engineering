# Attention Mechanisms

Attention mechanisms are the core architectural component that enables language models to process and understand context. The attention operation allows each token to "attend" to every other token in the context, weighting their influence based on relevance. The quality, efficiency, and scaling properties of attention directly determine what context engineering can achieve.

This section covers the evolution from full attention to modern efficient variants, the implications for context engineering, and the practical impact of attention architecture choices on system design.

## Key Attention Variants

- **Full (Self-)Attention**: O(n²) complexity — each token attends to all others. Used in GPT-4, Claude, Gemini. Provides maximum flexibility but scales poorly.
- **Sliding Window Attention**: O(n × w) where w is window size — tokens attend only to nearby tokens. Used in Mistral, Mixtral. Enables efficient streaming.
- **Sparse Attention**: Selectively attends to a subset of positions. Used in long-document models.
- **Flash Attention**: IO-aware exact attention algorithm. Hardware-efficient without approximation. Essential for long contexts.
- **Multi-Query / Grouped-Query Attention**: Shares key/value heads across query heads. Used in Llama 2/3, Mistral. Reduces memory bandwidth.
- **State Space Models (Mamba)**: Alternative to attention with linear-time inference. Emerging architecture for long sequences.

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [Vaswani et al.: Attention Is All You Need](https://arxiv.org/abs/1706.03762) | The original transformer paper that introduced the attention mechanism — essential reading for understanding context engineering fundamentals. | 2017 |
| [Jay Alammar: The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | Visual guide to attention mechanisms that remains the best introductory resource for understanding how attention works. | 2018 |
| [3Blue1Brown: Attention in Transformers](https://www.youtube.com/watch?v=eMlx5fFNoYc) | Animated visual explanation of attention mechanisms with clear intuition for how models weigh context. | 2024 |
| [Hugging Face: Attention Mechanisms Course](https://huggingface.co/learn/nlp-course/chapter1/1) | Free course module covering attention mechanisms with practical code examples. | 2024 |
| [Lilian Weng: The Transformer Family](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/) | Comprehensive survey of transformer variants and their attention mechanisms with clear comparisons. | 2023 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [Dao et al.: FlashAttention — Fast and Memory-Efficient Exact Attention](https://arxiv.org/abs/2205.14135) | Paper that fundamentally changed what's possible with long contexts by making attention IO-aware rather than computation-bound. Essential for context engineering. | 2022 |
| [Dao: FlashAttention-2 — Faster Attention with Better Parallelism](https://arxiv.org/abs/2307.08691) | Optimization of FlashAttention that doubled throughput, enabling practical million-token contexts. | 2023 |
| [Shazeer: Fast Transformer Decoding — One Write-Head is All You Need](https://arxiv.org/abs/1911.02150) | Introduced multi-query attention, the foundation for efficient decoding in production models like Llama and Mistral. | 2019 |
| [Ainslie et al.: GQA — Training Generalized Multi-Query Transformer Models](https://arxiv.org/abs/2305.13245) | Introduced grouped-query attention, balancing quality and efficiency — used in Llama 2 and 3. | 2023 |
| [Beltagy et al.: Longformer — The Long-Document Transformer](https://arxiv.org/abs/2004.05150) | Introduced sparse attention patterns for processing long documents, directly relevant to context engineering for lengthy inputs. | 2020 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Gu and Dao: Mamba — Linear-Time Sequence Modeling](https://arxiv.org/abs/2312.00752) | State space model alternative to attention that achieves linear-time inference — challenging the transformer paradigm for context engineering. | 2023 |
| [Piechocki et al.: MambaByte — Token-Free Language Modeling](https://arxiv.org/abs/2401.13660) | Extends Mamba to byte-level modeling, avoiding tokenization entirely — potential implications for context representation. | 2024 |
| [Ding et al.: LongNet — Scaling Transformers to 1 Billion Tokens](https://arxiv.org/abs/2307.02486) | Architecture for dilated attention that can theoretically scale to billion-token contexts through sparse communication patterns. | 2023 |
| [Child et al.: Generating Long Sequences with Sparse Transformers](https://arxiv.org/abs/1904.10509) | Early work on sparse attention patterns that enables processing of longer sequences with fixed compute budget. | 2019 |
| [Kitaev et al.: Reformer — The Efficient Transformer](https://arxiv.org/abs/2001.04451) | Introduced locality-sensitive hashing attention and reversible layers, reducing memory from O(n²) to O(n log n). | 2020 |

## Attention and Context Engineering

The choice of attention mechanism directly impacts context engineering strategy:

- **Full attention models** (GPT-4, Claude, Gemini): Context quality depends on prompt structure — put important info at ends, use XML tags, leverage structure.
- **Sliding window models** (Mistral, Mixtral): Information decays with distance. Structure context so related content stays within the window radius.
- **State space models** (Mamba): No quadratic penalty for long context, but may have different recall patterns for distant information.

## Related Sections

- [Context Windows](./context-windows.md) — How attention mechanisms determine context window behavior
- [Long Context Models](./long-context-models.md) — Full model-level approaches to extended context
- [Research Papers](./research-papers.md) — Foundational papers on attention mechanisms

## Related Patterns

- [Long Context Strategies](../patterns/long-context-strategies.md)
