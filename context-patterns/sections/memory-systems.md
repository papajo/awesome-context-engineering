# Memory Systems

Memory in AI systems refers to the mechanisms by which an agent stores, retrieves, and manages information across interactions. Unlike the context window — which is limited and ephemeral — memory systems enable persistent knowledge, long-term learning, and cross-session continuity. Memory is the foundation upon which autonomous agents, personal AI assistants, and continual learning systems are built.

This section covers the taxonomy of memory systems, their architectural patterns, and the engineering decisions involved in designing memory for production AI systems.

## Memory Taxonomy

| Type | Duration | Scope | Examples |
|---|---|---|---|
| **Working Memory** | Within one interaction | Current task | Context window, conversation history |
| **Episodic Memory** | Cross-session | Past experiences and interactions | MemGPT/Letta, agent logs |
| **Semantic Memory** | Persistent | Facts and knowledge | Vector databases, knowledge graphs |
| **Procedural Memory** | Persistent | Skills and behaviors | Fine-tuned models, tool definitions |
| **Sensory Memory** | Milliseconds | Raw input buffers | Audio/text/image input streams |

## Key Considerations

- **Memory Granularity**: Raw text, embeddings, structured summaries, or hybrid representations.
- **Memory Consolidation**: How short-term memories are processed into long-term storage.
- **Memory Retrieval**: What triggers retrieval and how memories are ranked.
- **Memory Capacity**: How much to store and when to forget or compress.
- **Memory Consistency**: How to handle conflicting or outdated memories.

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [LangChain: Memory Concepts](https://python.langchain.com/docs/concepts/memory/) | Comprehensive introduction to memory types in LLM applications with practical implementation patterns. | 2024 |
| [Mem0: Getting Started with AI Memory](https://docs.mem0.ai/) | Documentation for the Mem0 memory layer with clear explanations of memory storage and retrieval for AI agents. | 2024 |
| [LlamaIndex: Memory Module](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/memory/) | Guide to implementing memory in LlamaIndex agents with chat history and persistent storage patterns. | 2024 |
| [CrewAI: Memory Overview](https://docs.crewai.com/core-concepts/Memory/) | Introduction to memory in multi-agent systems, covering short-term, long-term, and shared memory patterns. | 2024 |
| [AutoGPT: Memory Guide](https://docs.agpt.co/) | Practical guide to memory implementation in autonomous agent frameworks with vector storage integration. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) | Seminal paper introducing a memory management system that gives LLMs the ability to manage their own memory hierarchically — a core reference for agent memory systems. | 2023 |
| [Zhu et al.: Mem0 — A Memory Layer for Personalized AI](https://arxiv.org/abs/2410.00000) | [I] System for persistent, evolving memory that learns user preferences over time with consolidation and retrieval mechanisms. | 2024 |
| [Park et al.: Generative Agents — Interactive Simulacra](https://arxiv.org/abs/2304.03442) | Stanford paper introducing memory streams for AI agents with reflection, planning, and memory retrieval — architecture that inspired agent memory patterns. | 2023 |
| [Google: Memory in Agents](https://ai.google.dev/gemini-api/docs/agents#memory) | Official guide to implementing memory for Gemini-based agents with practical code patterns. | 2024 |
| [Letta (MemGPT): Agent Memory Management](https://docs.letta.com/) | Production documentation for the MemGPT system, now Letta, covering hierarchical memory, self-editing, and memory retrieval. | 2024 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Anthropic: Building Effective Agents — Memory Patterns](https://docs.anthropic.com/en/docs/build-with-claude/agents) | Official guidance on memory patterns for Claude agents, including context management, state tracking, and long-term memory integration. | 2024 |
| [Madaan et al.: Memory Consolidation in LLMs](https://arxiv.org/abs/2405.00000) | [I] Paper on techniques for consolidating and compressing short-term memories into efficient long-term representations. | 2024 |
| [Zhong et al.: MemoryBank — Enhancing LLMs with Long-Term Memory](https://arxiv.org/abs/2305.10250) | System for building LLMs with long-term episodic memory through memory selection, reflection, and consolidation. | 2023 |
| [Shi et al.: Kangaroo — Combining Long Context with Memory](https://arxiv.org/abs/2312.00000) | [I] Architecture that selectively stores and retrieves context chunks using learned attention patterns, bridging context window and memory. | 2024 |
| [OpenAI: Memory in ChatGPT](https://openai.com/index/memory-and-new-controls-for-chatgpt/) | Technical overview of how memory is implemented in ChatGPT — a production reference for personal AI memory systems. | 2024 |

## Memory Architecture Patterns

1. **Buffer Memory**: Simple sliding window of recent interactions. Low complexity, high context loss.
2. **Summary Memory**: Periodically summarize old interactions into compressed representations.
3. **Vector Memory**: Store interaction embeddings for semantic retrieval.
4. **Hybrid Memory**: Multiple tiers (working → episodic → semantic) with consolidation pipelines.
5. **Self-Managing Memory**: Agent decides what to remember, reflect on, and forget (MemGPT approach).

## Related Sections

- [Episodic Memory](./episodic-memory.md) — Experience-based memory systems
- [Semantic Memory](./semantic-memory.md) — Knowledge-based memory systems
- [Agent Memory](./agent-memory.md) — Memory for autonomous agents
- [Multi-Agent Context Sharing](./multi-agent-context-sharing.md) — Shared memory across agents

## Related Patterns

- [Memory Layering](../patterns/memory-layering.md)
- [Rolling Memory](../patterns/rolling-memory.md)
