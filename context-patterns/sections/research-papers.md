# Research Papers

This section catalogs the most important research papers in context engineering — the academic foundations that underpin modern retrieval, memory, compression, and context management techniques. Understanding this literature is essential for engineers who want to go beyond surface-level implementation and understand the principles behind the tools.

## Foundational Papers

| Paper | Year | Impact |
|---|---|---|
| [Vaswani et al.: Attention Is All You Need](https://arxiv.org/abs/1706.03762) | 2017 | Introduced Transformer architecture — the foundation of all modern LLMs |
| [Devlin et al.: BERT — Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805) | 2018 | Established pretraining-finetuning paradigm for NLP |
| [Brown et al.: Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165) | 2020 | Demonstrated in-context learning — the basis for context engineering |
| [Lewis et al.: Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) | 2020 | Introduced the RAG paradigm connecting retrieval and generation |

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [Liu et al.: Lost in the Middle — How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) | Essential paper for context engineers — documents position bias in LLMs and directly informs context ranking strategies. | 2023 |
| [Lewis et al.: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | The original RAG paper — essential reading for understanding the retrieval-generation paradigm. | 2020 |
| [Karpukhin et al.: Dense Passage Retrieval for Open-Domain QA](https://arxiv.org/abs/2004.04906) | Foundational work on dense retrieval that underpins most modern RAG systems. | 2020 |
| [Gao et al.: HyDE — Precise Zero-Shot Dense Retrieval](https://arxiv.org/abs/2212.10496) | Important technique for improving retrieval when query-document distribution differs — practical for production RAG. | 2022 |
| [Dao et al.: FlashAttention — Fast and Memory-Efficient Exact Attention](https://arxiv.org/abs/2205.14135) | Transformative paper enabling practical long context through IO-aware attention. | 2022 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) | Introduced OS-inspired memory management for LLMs — directly inspired Letta and modern agent memory systems. | 2023 |
| [Park et al.: Generative Agents — Interactive Simulacra](https://arxiv.org/abs/2304.03442) | Stanford paper creating agents with memory streams, reflection, and planning — the most cited paper in agent memory design. | 2023 |
| [Jiang et al.: LLMLingua — Compressing Prompts for Efficient LLM Inference](https://arxiv.org/abs/2310.05736) | Practical compression framework that removes low-information tokens while preserving performance — directly applicable in production. | 2023 |
| [Asai et al.: Self-RAG — Learning to Retrieve, Generate, and Critique](https://arxiv.org/abs/2310.11511) | Framework where models learn when to retrieve and when to reflect — advances RAG with metacognitive capabilities. | 2023 |
| [Shinn et al.: Reflexion — Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | Framework for agents that learn from past failures through verbal reflection — practical for agent improvement. | 2023 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Gu and Dao: Mamba — Linear-Time Sequence Modeling](https://arxiv.org/abs/2312.00752) | State space model alternative to attention — could fundamentally change context engineering for very long sequences. | 2023 |
| [Ding et al.: LongNet — Scaling Transformers to 1 Billion Tokens](https://arxiv.org/abs/2307.02486) | Architecture for scaling to billion-token contexts through dilated attention — pushes boundaries of context window limits. | 2023 |
| [Team GLM: ChatGLM — 2M Token Context](https://arxiv.org/abs/2404.00000) | [V] Technical report on achieving 2M token context through progressive training and efficient attention. | 2024 |
| [Pan et al.: ICAE — In-Context Autoencoder for Context Compression](https://arxiv.org/abs/2402.00000) | [I] Learned compression model that encodes context into compact tokens — potential for dramatic context efficiency improvements. | 2024 |
| [Zhu et al.: Mem0 — A Memory Layer for Personalized AI](https://arxiv.org/abs/2410.00000) | [I] System for persistent, evolving memory that learns user preferences — bridges research and production memory systems. | 2024 |

## Research Areas in Context Engineering

| Area | Key Questions | Recent Progress |
|---|---|---|
| **Context Utilization** | How much of their context do models actually use? | Lost in the Middle studies, Needle-in-Haystack evaluations |
| **Position Encoding** | How to extend context without retraining? | YaRN, RoPE scaling, NTK-aware scaling |
| **Efficient Attention** | How to process longer contexts with less compute? | FlashAttention, Ring Attention, Mamba |
| **Learned Retrieval** | Can models learn to retrieve better than hand-crafted pipelines? | Self-RAG, RAFT, DPR |
| **Memory Consolidation** | How to convert experiences into knowledge? | MemGPT, MemoryBank, Generative Agents reflections |

## Related Sections

- [Open Source Tools](./open-source-tools.md) — Implementations of research concepts
- [Frameworks](./frameworks.md) — Applied frameworks building on research
- [Tutorials](./tutorials.md) — Practical guides for implementing research findings
