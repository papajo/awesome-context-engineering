# Agent Context Management

Agent context management is the discipline of designing, structuring, and maintaining the information environment in which autonomous AI agents operate. Unlike stateless LLM calls, agents persist across multiple turns, use tools, maintain state, and make autonomous decisions — requiring sophisticated context architecture.

This section covers the patterns, challenges, and best practices for managing context in autonomous agents, from simple conversational agents to complex multi-agent systems.

## Agent Context Architecture

```
┌──────────────────────────────────────────────────┐
│                 Agent Context                      │
├──────────────────────────────────────────────────┤
│  System Prompts  │  Tool Definitions  │  Safety   │
│  (Persona, rules)│  (schemas, docs)   │  (guard)  │
├──────────────────────────────────────────────────┤
│              Working Memory                        │
│  (current task state, intermediate reasoning)     │
├──────────────────────────────────────────────────┤
│           Retrieved Information                    │
│  (RAG results, memory recall, tool outputs)       │
├──────────────────────────────────────────────────┤
│           Conversation History                     │
│  (recent turns, compressed summaries)             │
└──────────────────────────────────────────────────┘
```

## Key Challenges

- **Context Window Pressure**: Agentic loops accumulate tool calls, outputs, and reasoning steps that rapidly fill the context window.
- **State Management**: Maintaining accurate agent state across long-running interactions.
- **Information Freshness**: Ensuring the agent has current information, not stale context.
- **Context Coherence**: Maintaining consistent behavior as context changes across turns.

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [Anthropic: Building Effective Agents](https://docs.anthropic.com/en/docs/build-with-claude/agents) | Official guide to building Claude-based agents with practical context management patterns. | 2024 |
| [OpenAI: Agents Overview](https://platform.openai.com/docs/guides/agents) | Comprehensive guide to building OpenAI agents with context management across conversations. | 2024 |
| [LangChain: Agent Concepts](https://python.langchain.com/docs/concepts/agents/) | Introduction to agent architectures in LangChain with context management fundamentals. | 2024 |
| [LlamaIndex: Agent Overview](https://docs.llamaindex.ai/en/stable/understanding/agent/) | Guide to building agents in LlamaIndex with working memory and tool context patterns. | 2024 |
| [Google: Agent Building Blocks](https://ai.google.dev/gemini-api/docs/agents) | Google's guide to building Gemini-based agents with context management and tool integration. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [Anthropic: Context Architecture for Agents](https://docs.anthropic.com/en/docs/build-with-claude/context-architecture) | Detailed architecture guide for structuring agent context including system prompts, tool definitions, and memory placement. | 2024 |
| [Google: Agent Context with Gemini](https://ai.google.dev/gemini-api/docs/agents#context) | Guide to managing agent context with Gemini, including system instructions, tool definitions, and conversation history. | 2024 |
| [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) | OS-inspired approach to agent context management with hierarchical memory, context paging, and automatic memory management. | 2023 |
| [Letta: Agent Memory Architecture](https://docs.letta.com/letta/architecture) | Production agent memory architecture documentation with context management patterns for long-running agents. | 2024 |
| [AutoGPT: Context Management](https://docs.agpt.co/) | Practical patterns for managing context in autonomous agent frameworks with looping and state tracking. | 2024 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Anthropic: Extended Thinking with Agents](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) | Guide on combining extended thinking (chain-of-thought) with agent context management — managing the interplay of reasoning traces and context. | 2024 |
| [Park et al.: Generative Agents — Context-Driven Behavior](https://arxiv.org/abs/2304.03442) | Stanford paper on context-driven agent behavior where memory streams, reflection, and planning all operate within a managed context framework. | 2023 |
| [Shinn et al.: Reflexion — Context from Past Experience](https://arxiv.org/abs/2303.11366) | Framework where agents use context from past experiences (stored in episodic memory) to improve decision making. | 2023 |
| [Wang et al.: Voyager — Context Management in Embodied Agents](https://arxiv.org/abs/2305.16291) | Demonstrates sophisticated context management in an embodied agent — skill library, task context, and environmental state. | 2023 |
| [MCP: Model Context Protocol for Agents](https://modelcontextprotocol.io/) | MCP provides standardized context and tool interfaces for agents — the emerging standard for agent-tool context management. | 2024 |

## Context Budget Management

For agentic loops, track context usage per turn:

```
Component               Typical Size    Priority
System Prompt           2-5K tokens     Highest
Tool Definitions        1-3K per tool   High
Working Memory          1-5K tokens     High
Retrieved Information   5-20K tokens    Medium
Recent History          2-10K tokens    Medium
Historical Summary      1-3K tokens     Low
```

## Related Sections

- [Agent Memory](./agent-memory.md) — Memory systems for agents
- [MCP Ecosystem](./mcp-ecosystem.md) — Standardized context interfaces via MCP
- [Multi-Agent Context Sharing](./multi-agent-context-sharing.md) — Context across multiple agents

## Related Patterns

- [Agent Context Management](../patterns/agent-context-management.md)
- [Memory Layering](../patterns/memory-layering.md)
