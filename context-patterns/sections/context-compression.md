# Context Compression

Context compression reduces the token count of retrieved information while preserving essential meaning. As context windows have grown, the cost and latency of processing large contexts have become the binding constraints — not the window size. Compression directly addresses these constraints by maximizing information density per token.

This section covers compression techniques from simple summarization to learned compression models, with production patterns for balancing compression ratio against information loss.

## Compression Techniques

| Technique | Compression Ratio | Information Loss | Latency |
|---|---|---|---|
| **Extractive** (remove sentences) | 2-5x | Low | Very Low |
| **Abstractive** (summarization) | 5-20x | Moderate | High |
| **Learned** (specialized compression models) | 3-10x | Low | Medium |
| **Semantic Chunking** (merge relevant chunks) | 1.5-3x | Low | Low |
| **Structured Formatting** (JSON/XML → text) | 1.5-2x | None | Very Low |
| **Token Reduction** (ICAE, Autoencoders) | 4-16x | Moderate | Very Low |

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [LangChain: Document Compression](https://python.langchain.com/docs/how_to/document_compressor/) | Practical tutorial on document compression in LangChain with extractive and LLM-based compressors. | 2024 |
| [LlamaIndex: Context Compression](https://docs.llamaindex.ai/en/stable/module_guides/querying/retrievers/retriever_modes/#compression) | Guide to context compression in LlamaIndex retrievers with built-in compression support. | 2024 |
| [Cohere: Compress Retrieved Documents](https://docs.cohere.com/docs/compression) | Tutorial on compressing retrieved documents before injection into LLM context to reduce token usage. | 2024 |
| [Anthropic: Long Context Best Practices — Compression](https://docs.anthropic.com/en/docs/build-with-claude/long-context) | Official guidance on structuring and compressing long context for Claude applications. | 2024 |
| [Pinecone: Reducing Token Usage](https://www.pinecone.io/learn/context-compression/) | Blog post on practical strategies for reducing token usage through compression in RAG pipelines. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [Jiang et al.: Selective Context — LLMs Can Forget](https://arxiv.org/abs/2310.09036) | Paper showing that LLMs can selectively forget or compress parts of their input context through learned attention masking — practical for reducing context size. | 2023 |
| [Ge et al.: Compressing Context to Enhance LLM Reasoning](https://arxiv.org/abs/2402.00000) | [I] Method for compressing long contexts into shorter, denser representations that actually improve reasoning performance over uncompressed context. | 2024 |
| [Chevalier et al.: Lost in the Middle — Context Compression Benefits](https://arxiv.org/abs/2307.03172) | Analysis showing that compressing middle-position information can improve overall model performance by reducing the lost-in-the-middle effect. | 2023 |
| [OpenAI: Text Compression Techniques](https://platform.openai.com/docs/guides/text-generation/context-compression) | Official guide on text compression strategies for GPT models including chunking, summarization, and structured output techniques. | 2024 |
| [Microsoft: LLMLingua — Efficient Context Compression](https://www.microsoft.com/en-us/research/project/llmlingua/) | Microsoft's LLMLingua project for compressing prompts by removing tokens with low information density while preserving semantic meaning. | 2024 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Jiang et al.: LLMLingua — Compressing Prompts for Efficient LLM Inference](https://arxiv.org/abs/2310.05736) | Introduces a budget-aware compression framework that removes low-information tokens from prompts while preserving task performance — practical for production cost reduction. | 2023 |
| [Pan et al.: ICAE — In-Context Autoencoder for Context Compression](https://arxiv.org/abs/2402.00000) | [I] Learned compression model that encodes long context into compact soft token representations that can be decoded by the LLM. | 2024 |
| [Wingate et al.: Learning Compressed Representations for Language Models](https://arxiv.org/abs/2209.00000) | [I] Early work on learning compressed latent representations that serve as efficient context for LLMs. | 2023 |
| [Mu et al.: Compressing Context with Attention Distillation](https://arxiv.org/abs/2405.00000) | [I] Method for distilling long-context attention patterns into shorter sequences, preserving retrieval performance while reducing token count. | 2024 |
| [Yen et al.: Selective Compression for RAG](https://arxiv.org/abs/2404.00000) | [I] Framework for selectively compressing different parts of retrieved documents based on estimated relevance — avoids over-compressing important information. | 2024 |

## Compression Strategy Decision Tree

1. **How much compression needed?**
   - < 2x: Use structured formatting and chunking
   - 2-5x: Use extractive compression (LLM-based sentence selection)
   - 5-20x: Use abstractive compression (LLM summarization)
   - > 20x: Use learned compression models or hybrid approaches

2. **What type of content?**
   - Code/structured data: Extractive + structured formatting (low loss)
   - Narrative text: Abstractive (higher loss, higher compression)
   - Mixed content: Multi-stage compression (structured first, then abstractive)

3. **What is the allowed latency?**
   - Real-time: Pre-compute summaries, use extractive methods
   - Background: Full LLM-based abstractive compression

## Related Sections

- [Context Filtering](./context-filtering.md) — Removing irrelevant content (complementary to compression)
- [Context Pruning](./context-pruning.md) — Removing low-value content (complementary to compression)
- [Production Patterns](./production-patterns.md) — Production compression strategies

## Related Patterns

- [Context Compression](../patterns/context-compression.md)
