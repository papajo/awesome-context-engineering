# Agent Memory

Agent memory encompasses the full memory architecture of autonomous AI agents — combining working, episodic, semantic, and procedural memory into a coherent system that enables an agent to operate across sessions, learn from experience, and maintain consistent behavior. Agent memory is the critical infrastructure that separates simple stateless LLM calls from truly autonomous AI agents.

This section covers the design patterns, implementation strategies, and production considerations for building memory systems that power autonomous agents.

## Agent Memory Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Agent Memory System                  │
├────────────┬────────────┬────────────┬───────────────┤
│  Working   │  Episodic   │  Semantic   │  Procedural    │
│  Memory    │  Memory     │  Memory     │  Memory        │
├────────────┼────────────┼────────────┼───────────────┤
│ Current    │ Past        │ Knowledge   │ Skills, tools  │
│ context    │ experiences │ facts, info │ behavior       │
│ (prompt)   │ (history)   │ (vector DB) │ (definitions)  │
└────────────┴────────────┴────────────┴───────────────┘
        │            │              │              │
        └────────────┴──────────────┴──────────────┘
                      │
              Memory Manager
         (consolidation, retrieval,
          importance scoring, GC)
```

## Key Patterns

- **Self-Managing Memory**: The agent decides what to remember and forget (MemGPT/Letta approach).
- **Reflection-Based Learning**: Agents periodically reflect on past episodes to extract insights (Generative Agents/Reflexion approach).
- **Hierarchical Memory**: Multiple tiers with automatic promotion and demotion based on importance and recency.
- **Tool-Mediated Memory**: Memory access and management exposed as tools the agent can call.

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [Anthropic: Building Effective Agents](https://docs.anthropic.com/en/docs/build-with-claude/agents) | Official guide on building Claude-based agents with memory patterns, tool use, and state management. | 2024 |
| [OpenAI: Agents Overview](https://platform.openai.com/docs/guides/agents) | Comprehensive guide to building OpenAI agents including memory management across conversations. | 2024 |
| [LangChain: Agent Memory Guide](https://python.langchain.com/docs/modules/agents/) | Practical patterns for implementing memory in LangChain agents with various storage backends. | 2024 |
| [LlamaIndex: Agent Memory Patterns](https://docs.llamaindex.ai/en/stable/understanding/agent/) | Guide to agent memory in LlamaIndex with working and long-term memory patterns. | 2024 |
| [CrewAI: Agent Memory Configuration](https://docs.crewai.com/core-concepts/Memory/) | Configuration guide for memory in multi-agent CrewAI systems. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) | Seminal paper establishing the OS-inspired approach to agent memory management with paging, contexts, and self-editing. | 2023 |
| [Park et al.: Generative Agents — Interactive Simulacra](https://arxiv.org/abs/2304.03442) | Stanford paper creating agents with memory streams, reflection, and planning — directly inspired leading agent memory frameworks. | 2023 |
| [Letta (MemGPT): Agent Memory Documentation](https://docs.letta.com/) | Production documentation for the MemGPT memory system with hierarchical memory, archival storage, and retrieval patterns. | 2024 |
| [Mem0: Agent Memory Layer](https://docs.mem0.ai/) | Open-source memory layer for AI agents with automatic memory extraction, consolidation, and retrieval. | 2024 |
| [Google: Agents with Memory](https://ai.google.dev/gemini-api/docs/agents#memory) | Official guidance on building Gemini-based agents with persistent memory patterns. | 2024 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Shinn et al.: Reflexion — Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | Framework where agents store and reflect on past experiences as verbal feedback, improving through self-critique rather than gradient updates. | 2023 |
| [Anthropic: Context Architecture for Agents](https://docs.anthropic.com/en/docs/build-with-claude/context-architecture) | Production architecture guide for structuring agent context including system prompts, tool definitions, and conversation management. | 2024 |
| [Wang et al.: Voyager — An Open-Ended Embodied Agent with Language Models](https://arxiv.org/abs/2305.16291) | Minecraft agent with sophisticated memory systems including skill library, interaction history, and self-guided learning. | 2023 |
| [Richards: Building Agent Memory Systems (Blog Series)](https://www.latent.space/p/agent-memory) | In-depth blog series on designing, implementing, and scaling memory systems for production AI agents. | 2024 |
| [OpenAI: Memory in ChatGPT — Technical Deep Dive](https://openai.com/index/memory-and-new-controls-for-chatgpt/) | Technical overview of how OpenAI implements memory at scale for millions of ChatGPT users — production reference architecture. | 2024 |

## Implementation Guide

### Minimal Agent Memory System

1. **Working Memory Buffer**: Keep last N turns of conversation in the prompt (sliding window).
2. **Episodic Storage**: Log completed tasks and session summaries to a vector database.
3. **Semantic Extraction**: Periodically extract facts and preferences from episodic storage into semantic memory.
4. **Memory Retrieval**: At the start of each session, retrieve relevant episodic and semantic memories.
5. **Importance Scoring**: Assign importance scores to memories to guide retention and garbage collection.

### Production Agent Memory Stack

```
1. Redis / In-memory cache → Working memory (fast, ephemeral)
2. PostgreSQL / SQLite → Structured episodic logs (durable, queryable)
3. Pinecone / Weaviate / Qdrant → Semantic vector storage (similarity search)
4. Neo4j / ArangoDB → Knowledge graph (relational facts)
5. S3 / GCS → Cold storage (compressed archives)
```

## Related Sections

- [Memory Systems](./memory-systems.md) — Overall memory taxonomy
- [Episodic Memory](./episodic-memory.md) — Experience-based memory for agents
- [Semantic Memory](./semantic-memory.md) — Knowledge-based memory for agents
- [Multi-Agent Context Sharing](./multi-agent-context-sharing.md) — Shared memory across agents

## Related Patterns

- [Memory Layering](../patterns/memory-layering.md)
- [Agent Context Management](../patterns/agent-context-management.md)
