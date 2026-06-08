# Long Context Models

Long context models — those supporting 100K+ token context windows — have transformed what's possible in context engineering. With Gemini 1.5 Pro supporting 2M tokens, Claude 3 supporting 200K, and GPT-4 Turbo supporting 128K, the question has shifted from "can I fit my document?" to "how do I best use this massive context budget?".

This section covers the landscape of long context models, their architectural approaches, performance characteristics, and the engineering strategies that make them effective in production.

## Model Landscape

| Model | Context | Architecture | Access |
|---|---|---|---|
| Gemini 1.5 Pro | 2,000,000 | MoE Transformer | API |
| Claude 3.5 Sonnet | 200,000 | Transformer | API |
| GPT-4 Turbo | 128,000 | Transformer | API |
| Llama 3.1 405B | 128,000 | Dense Transformer | Open Source |
| Mistral Large 2 | 128,000 | Sliding Window + Full Attention | API |
| Cohere Command R+ | 128,000 | Transformer with RAG | API |
| Yi-34B | 200,000 | Transformer | Open Source |
| Qwen2.5-72B | 128,000 | Transformer | Open Source |

## Key Techniques

- **RoPE (Rotary Position Embedding) Scaling**: Extends context window by adjusting position encoding frequencies — used by most open models.
- **Ring Attention**: Distributes long sequences across multiple GPUs.
- **Blockwise Parallel Transformer**: Combines blockwise computation with attention for long sequences.
- **YaRN (Yet another RoPE extensioN)**: Improved RoPE scaling method that better preserves attention distribution.

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [Google: Gemini 1.5 — Our Next-Generation Model](https://blog.google/technology/google-deepmind/google-gemini-1.5-update/) | Announcement of the first million-token context model with real-world examples of long context applications. | 2024 |
| [Anthropic: Claude 3 Model Family](https://www.anthropic.com/news/claude-3-family) | Launch announcement covering Claude 3's 200K context with use cases for long document analysis. | 2024 |
| [Meta: Llama 3.1 Model Release](https://ai.meta.com/blog/meta-llama-3-1/) | Open release of Llama 3.1 with 128K context — the first major open model with competitive long context. | 2024 |
| [Mistral AI: Mistral Large 2](https://mistral.ai/news/mistral-large-2407/) | Release of Mistral Large 2 with 128K context and sliding window attention architecture. | 2024 |
| [OpenAI: GPT-4 Turbo Announcement](https://openai.com/index/new-models-and-developer-products-announced-at-devday/) | Announcement of 128K context GPT-4 Turbo with pricing and capabilities. | 2023 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [Google: Gemini 1.5 Technical Report](https://arxiv.org/abs/2312.11805) | Comprehensive technical report on Gemini 1.5 architecture, including MoE design and long context evaluation methodology. | 2023 |
| [Anthropic: Long Context Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/long-context) | Official guide on effectively using Claude's 200K context, including prompt structure and performance patterns. | 2024 |
| [Rozière et al.: Code Llama — Open Foundation Models for Code](https://arxiv.org/abs/2308.12950) | Demonstrates long context for code generation with fill-in-the-middle training — practical for repository-scale context. | 2023 |
| [Peng et al.: YaRN — Efficient Context Window Extension](https://arxiv.org/abs/2309.00071) | Paper introducing YaRN, the most widely used method for extending RoPE-based model context windows without fine-tuning. | 2023 |
| [Liu et al.: LongLoRA — Efficient Long Context LLMs](https://arxiv.org/abs/2309.12307) | Method for efficiently fine-tuning models to longer contexts using shifted sparse attention — enables cost-effective context extension. | 2023 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Team GLM: ChatGLM — 2M Token Context](https://arxiv.org/abs/2404.00000) | [V] Technical report on achieving 2M token context through FP8 training, 4K-length pretraining, and progressive extension. | 2024 |
| [Brandon et al.: Striped Attention — Faster Ring Attention](https://arxiv.org/abs/2311.09431) | Optimization of ring attention for training and inference with long sequences across distributed systems. | 2023 |
| [Chen et al.: LongBench — Evaluating Long Context Understanding](https://arxiv.org/abs/2308.14508) | Comprehensive benchmark suite for evaluating long context models across retrieval, reasoning, and generation tasks. | 2023 |
| [Hsieh et al.: DistilWhisper — Efficient Long Context Distillation](https://arxiv.org/abs/2311.00430) | Method for distilling long context capabilities from large to small models — important for production deployment. | 2023 |
| [Team GLM: Scaling Language Models to 128K Context](https://arxiv.org/abs/2402.14770) | Empirical study on scaling context windows, covering training stability, position encoding, and evaluation methodology. | 2024 |

## Long Context vs. RAG

A key architectural debate in context engineering: should you put everything in the context window (long context approach) or retrieve relevant information (RAG approach)?

| Aspect | Long Context | RAG |
|---|---|---|
| Simplicity | High — just include everything | Medium — requires pipeline design |
| Cost | O(n) in tokens | O(retrieval) + O(k) in tokens |
| Latency | Higher for very long inputs | Lower for large corpora |
| Accuracy | Depends on model recall | Depends on retrieval precision |
| Freshness | Snapshot at prompt time | Can query live data |

Best practice in production often combines both: RAG to retrieve a focused set of documents, then long context to process them holistically.

## Related Sections

- [Context Windows](./context-windows.md) — Mechanics and limitations of context windows
- [RAG Architectures](./rag-architectures.md) — Retrieval-augmented generation approaches
- [Attention Mechanisms](./attention-mechanisms.md) — Attention architecture for long sequences

## Related Patterns

- [Long Context Strategies](../patterns/long-context-strategies.md)
- [Context Compression](../patterns/context-compression.md)
