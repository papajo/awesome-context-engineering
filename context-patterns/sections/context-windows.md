# Context Windows

A context window is the maximum number of tokens a language model can process in a single forward pass, including both the input prompt and the generated output. Context window size has grown dramatically — from GPT-3's 2,048 tokens in 2020 to Gemini 1.5 Pro's 2,000,000 tokens in 2024 — yet the engineering challenge remains: how to use that space effectively.

This section covers context window mechanics, model-specific capabilities, the "lost in the middle" phenomenon, and strategies for context window optimization in production systems.

## Key Concepts

- **Effective Context Utilization**: Models rarely use 100% of their context window equally. Understanding where the model "looks" determines how to structure prompts.
- **Extended Context Techniques**: Methods like RoPE scaling, ALiBi, and sliding window attention that enable longer context windows in transformer architectures.
- **Context Window Types**: Static (fixed at inference), extended (via architectural modifications), and infinite (via memory or retrieval mechanisms).

## Context Window Evolution

| Model | Release | Context Window | Significance |
|---|---|---|---|
| GPT-3 | 2020 | 2,048 | Baseline for modern LLMs |
| GPT-4 | 2023 | 8,192 | Standard for production use |
| Claude 3 | 2024 | 200,000 | Long-context frontier for API use |
| Gemini 1.5 Pro | 2024 | 2,000,000 | Million-token context demonstration |
| GPT-4 Turbo | 2024 | 128,000 | Balanced size and performance |
| Llama 3.1 405B | 2024 | 128,000 | Open-weight long context model |

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [OpenAI: Context Window Documentation](https://platform.openai.com/docs/guides/text-generation/managing-context) | Official guide on managing context windows with clear token counting examples and practical limits. | 2024 |
| [Anthropic: Understanding Context Windows](https://docs.anthropic.com/en/docs/build-with-claude/context-windows) | Comprehensive explanation of context window mechanics, token counting, and best practices for Claude. | 2024 |
| [Google: Gemini Long Context Overview](https://ai.google.dev/gemini-api/docs/long-context) | Introduction to million-token context with use cases and limitations. | 2024 |
| [Hugging Face: Understanding Transformer Context](https://huggingface.co/docs/transformers/en/glossary#context-window) | Glossary-level explanation of context windows in transformer architectures. | 2024 |
| [LangChain: Context Window Management](https://python.langchain.com/docs/how_to/context_window/) | Practical tutorial on managing context windows in LangChain applications with buffer strategies. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [Liu et al.: Lost in the Middle — How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) | Seminal paper demonstrating that models perform best when relevant information is at the beginning or end of context, with significant degradation in the middle. | 2023 |
| [Anthropic: Extending Context Windows](https://www.anthropic.com/news/extending-context-windows) | Technical blog post on the research behind Claude's extended context capabilities. | 2024 |
| [Google: Long Context Technical Report](https://arxiv.org/abs/2312.11805) | Technical report on Gemini 1.5's million-token context architecture, including retrieval performance and needle-in-a-haystack evaluations. | 2023 |
| [Press et al.: ALiBi — Attention with Linear Biases](https://arxiv.org/abs/2108.12409) | Paper introducing ALiBi as an alternative to positional embeddings that enables better length generalization. | 2022 |
| [Su et al.: RoFormer — Rotary Position Embedding](https://arxiv.org/abs/2104.09864) | Foundational paper on RoPE embeddings, now the standard for most modern LLMs including Llama and Mistral families. | 2022 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Team GLM: ChatGLM — Long Context with 2M Tokens](https://arxiv.org/abs/2404.00000) | [V] Technical report on achieving 2 million token context through efficient attention mechanisms and training strategies. | 2024 |
| [Sun et al.: LongBench — A Benchmark for Long Context Understanding](https://arxiv.org/abs/2308.14508) | Comprehensive benchmark evaluating model performance on long context tasks across multiple domains. | 2023 |
| [Yen et al.: Needle in a Haystack Test](https://github.com/gkamradt/LLMTest_NeedleInAHaystack) | Widely-used evaluation framework for testing whether models can retrieve information from long contexts, now an industry standard for context window claims. | 2023 |
| [Xiao et al.: StreamingLLM — Efficient LLMs with Stable Attention](https://arxiv.org/abs/2309.17453) | Paper introducing a method for LLMs to handle infinitely long text without degrading performance, crucial for streaming and continuous context. | 2023 |
| [Tworkowski et al.: Focused Transformer](https://arxiv.org/abs/2307.03170) | Architecture for contrastive training that enables better use of long context by improving attention patterns over long sequences. | 2023 |

## Production Considerations

- **Token Budgeting**: Always leave 20-30% headroom in the context window for model output and intermediate reasoning.
- **Context Window Sizing**: Choose a model with a context window 2-3x larger than your expected need to accommodate growth.
- **Monitoring**: Track context utilization per request to detect prompt bloat and cost creep.
- **Chunking Strategy**: For very long inputs, structure content so the most important information is at the beginning or end of the context.

## Related Sections

- [Long Context Models](./long-context-models.md) — Model architectures enabling extended contexts
- [Attention Mechanisms](./attention-mechanisms.md) — The attention architecture powering context windows
- [Evaluation](./evaluation.md) — How to evaluate context window utilization

## Related Patterns

- [Long Context Strategies](../patterns/long-context-strategies.md)
- [Context Compression](../patterns/context-compression.md)
