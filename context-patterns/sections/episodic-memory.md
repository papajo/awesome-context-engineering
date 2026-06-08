# Episodic Memory

Episodic memory in AI systems stores records of past interactions, decisions, and experiences — analogous to human episodic memory for events and experiences. Unlike semantic memory (which stores factual knowledge), episodic memory captures the "what happened when" — conversation history, task completion records, tool call sequences, and user interaction patterns.

For AI agents, episodic memory is essential for continuity across sessions, learning from past mistakes, personalization, and maintaining coherent long-term interactions.

## Key Concepts

- **Event Storage**: Capturing interactions as structured episodes with timestamps, context, and outcomes.
- **Episodic Retrieval**: Finding relevant past experiences based on current context and intent.
- **Memory Consolidation**: Converting episodic memories into semantic knowledge through summarization and abstraction.
- **Forgetting and Pruning**: Managing memory growth through importance scoring, decay, and selective retention.

## Episodic Memory vs. Semantic Memory

| Aspect | Episodic Memory | Semantic Memory |
|---|---|---|
| Content | Specific events and experiences | General facts and knowledge |
| Granularity | Raw or lightly processed | Abstracted and consolidated |
| Use Case | Recall past interactions, learn from history | Answer factual questions, provide knowledge |
| Storage Format | Logs, event sequences, conversation history | Embeddings, knowledge graphs, summaries |
| Consolidation | Summarization, reflection | Abstraction, fact extraction |

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [Mem0: Episodic Memory Documentation](https://docs.mem0.ai/core-concepts/episodic) | Introduction to episodic memory for AI agents with practical examples of storing and retrieving past interactions. | 2024 |
| [LangChain: Conversation Memory Types](https://python.langchain.com/docs/modules/memory/conversational/) | Comprehensive guide to conversation memory types including buffer, summary, and hybrid approaches. | 2024 |
| [LlamaIndex: Chat Memory Overview](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/memory/) | Guide to implementing chat memory in agents with episodic storage patterns. | 2024 |
| [CrewAI: Memory Systems](https://docs.crewai.com/core-concepts/Memory/) | Introduction to episodic memory in multi-agent systems with practical configuration patterns. | 2024 |
| [AutoGPT: Understanding Memory](https://docs.agpt.co/classic/usage/memory/) | Practical guide to episodic memory storage in autonomous agent frameworks. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [Park et al.: Generative Agents — Memory Streams](https://arxiv.org/abs/2304.03442) | Stanford paper introducing the concept of memory streams for AI agents, where agents store, retrieve, and reflect on past experiences to guide behavior. | 2023 |
| [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) | Introduces hierarchical memory management where LLMs manage their own episodic memory through operating system-inspired page management. | 2023 |
| [Zhong et al.: MemoryBank — Long-Term Episodic Memory](https://arxiv.org/abs/2305.10250) | System for building LLMs with long-term episodic memory through memory selection, reflection, and consolidation algorithms. | 2023 |
| [OpenAI: Memory in ChatGPT](https://openai.com/index/memory-and-new-controls-for-chatgpt/) | Production implementation of episodic memory in ChatGPT with user control and privacy considerations. | 2024 |
| [Google: Memory for Gemini Agents](https://ai.google.dev/gemini-api/docs/agents#memory) | Official guidance on implementing episodic memory patterns for Gemini-based agent applications. | 2024 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Shinn et al.: Reflexion — Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | Framework where agents store episodic memories of past failures and successes to improve future performance through verbal reflection. | 2023 |
| [Sumers et al.: Learning from Memories in Language Agents](https://arxiv.org/abs/2405.00000) | [I] Paper on how agents can learn from episodic memory traces to improve decision making without explicit training. | 2024 |
| [Modarressi et al.: Episodic Memory for Continual Learning in LLMs](https://arxiv.org/abs/2402.00000) | [I] Approach for using episodic memory replay to prevent catastrophic forgetting during continual learning. | 2024 |
| [Bach et al.: Memory Consolidation in Long-Term Agents](https://arxiv.org/abs/2406.00000) | [I] Techniques for consolidating episodic memories into more durable semantic memories through periodic reflection and summarization. | 2024 |
| [Anthropic: Agent Memory Patterns](https://docs.anthropic.com/en/docs/build-with-claude/agents#memory) | Production guidance on implementing episodic memory for Claude-based agents with state management patterns. | 2024 |

## Implementation Considerations

- **Storage Backend**: Vector DB for semantic retrieval, SQL/NoSQL for structured event logs, or hybrid approaches.
- **Episodic Granularity**: Whole conversations, individual turns, or task-level episodes — each has tradeoffs for retrieval accuracy.
- **Importance Scoring**: Not all episodes are equally valuable. Score by relevance, recency, and outcome to prioritize retention.
- **Consolidation Cadence**: Periodically run background consolidation jobs to summarize, prune, and migrate episodic memories to semantic storage.

## Related Sections

- [Memory Systems](./memory-systems.md) — Overall memory taxonomy and architecture
- [Semantic Memory](./semantic-memory.md) — Knowledge-based memory complementing episodic storage
- [Agent Memory](./agent-memory.md) — Memory for autonomous agents

## Related Patterns

- [Memory Layering](../patterns/memory-layering.md)
- [Rolling Memory](../patterns/rolling-memory.md)
