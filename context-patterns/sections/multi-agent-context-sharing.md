# Multi-Agent Context Sharing

Multi-agent context sharing is the architecture and protocol layer that enables multiple AI agents to share information, coordinate actions, and maintain a coherent shared state. As agent systems scale from single agents to teams of specialized agents — each with their own context and memory — the challenge of sharing context while maintaining consistency becomes critical.

This section covers shared memory architectures, agent communication protocols, context synchronization strategies, and production patterns for multi-agent systems.

## Sharing Architectures

| Architecture | Description | Best For |
|---|---|---|
| **Shared Memory** | All agents access the same knowledge store | Simple coordination, common facts |
| **Message Passing** | Agents communicate via structured messages | Loose coupling, distributed teams |
| **Blackboard Pattern** | Shared workspace where agents post and read updates | Complex problem decomposition |
| **Broadcast/Subscribe** | Agents publish to topics and subscribe to relevant updates | Event-driven coordination |
| **Hierarchical** | Parent agent delegates and synthesizes | Task orchestration with oversight |

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [CrewAI: Collaboration Concepts](https://docs.crewai.com/core-concepts/Collaboration/) | Introduction to multi-agent collaboration patterns with shared context and communication. | 2024 |
| [LangGraph: Multi-Agent Systems](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/) | Tutorial on building multi-agent systems with shared state and communication channels. | 2024 |
| [AutoGen: Multi-Agent Conversations](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/framework/overview.html) | Microsoft's framework for multi-agent conversations with context sharing patterns. | 2024 |
| [OpenAI: Multi-Agent Patterns](https://platform.openai.com/docs/guides/agents#multi-agent) | OpenAI's guide to multi-agent patterns with context isolation and sharing strategies. | 2024 |
| [CrewAI: Memory Sharing](https://docs.crewai.com/core-concepts/Memory/) | Guide to shared memory between agents in CrewAI systems with short-term and long-term options. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [CrewAI: Crews and Processes](https://docs.crewai.com/core-concepts/Crews/) | Deep dive into CrewAI's agent orchestration with sequential and hierarchical context sharing patterns. | 2024 |
| [LangGraph: Agent Team with Supervisor](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/) | Tutorial on building agent teams with a supervisor agent that manages context distribution. | 2024 |
| [AutoGen: GroupChat Patterns](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/groupchat.html) | Group chat patterns for multi-agent context sharing with speaker selection and message routing. | 2024 |
| [Anthropic: Multi-Agent Patterns with Claude](https://docs.anthropic.com/en/docs/build-with-claude/agents#multi-agent) | Official guidance on building multi-agent systems with Claude, including context sharing and delegation patterns. | 2024 |
| [Google: Multi-Agent Systems with Gemini](https://ai.google.dev/gemini-api/docs/agents#multi-agent) | Google's guide to multi-agent systems with context sharing and role-based agent design. | 2024 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Park et al.: Generative Agents — Shared Memory Streams](https://arxiv.org/abs/2304.03442) | Stanford's seminal work on multi-agent systems where agents share a memory stream, reflect together, and coordinate behavior through shared context. | 2023 |
| [Li et al.: CAMEL — Communicative Agents for Mind Exploration](https://arxiv.org/abs/2303.17760) | Framework for role-playing agent communication with context sharing between specialized agents — practical for complex task decomposition. | 2023 |
| [Wu et al.: AutoGen — Enabling Next-Gen LLM Applications](https://arxiv.org/abs/2308.08155) | Academic paper behind AutoGen with detailed discussion of multi-agent conversation patterns and context management. | 2023 |
| [Hong et al.: MetaGPT — Multi-Agent Framework for Software Engineering](https://arxiv.org/abs/2308.00352) | Framework where multiple agents with shared context simulate a software company — demonstrates sophisticated context routing. | 2023 |
| [Qian et al.: AgentVerse — Facilitating Multi-Agent Collaboration](https://arxiv.org/abs/2307.00000) | [I] Platform for multi-agent collaboration with shared context, dynamic role assignment, and coordination protocols. | 2024 |

## Context Isolation in Multi-Agent Systems

A critical design decision is how much context to share:

| Strategy | Sharing Level | Risk |
|---|---|---|
| **Full Transparency** | All agents see all context | Information overload, token waste |
| **Role-Based Isolation** | Agents see only relevant context | Missing shared information |
| **On-Demand Sharing** | Agents request specific context | Latency, coordination overhead |
| **Summarized Sharing** | Shared summaries, private details | Best balance for most systems |

## Related Sections

- [Agent Context Management](./agent-context-management.md) — Single-agent context management
- [Agent Memory](./agent-memory.md) — Agent memory systems
- [MCP Ecosystem](./mcp-ecosystem.md) — MCP for standardized context interfaces

## Related Patterns

- [Agent Context Management](../patterns/agent-context-management.md)
- [Memory Layering](../patterns/memory-layering.md)
