# Frameworks

Frameworks provide structured abstractions for building context engineering systems — handling the boilerplate of retrieval, memory, agent reasoning, and tool integration so engineers can focus on application logic. The framework landscape has matured rapidly, with specialized frameworks emerging for different use cases.

This section covers the major frameworks, their design philosophies, strengths, and weaknesses for context engineering.

## Framework Landscape

| Framework | Focus | Language | Key Strength |
|---|---|---|---|
| **LangChain** | General LLM applications | Python/JS | Broadest ecosystem, agent support |
| **LlamaIndex** | Data/RAG | Python | Best RAG abstractions, data connectors |
| **Haystack** | NLP pipelines | Python | Production NLP, search focus |
| **Semantic Kernel** | Enterprise AI | C#/Python | Microsoft ecosystem, planning |
| **CrewAI** | Multi-agent systems | Python | Multi-agent orchestration |
| **AutoGen** | Multi-agent conversations | Python | Microsoft's agent framework |
| **LangGraph** | Agent workflows | Python | LangChain's graph-based agents |

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [LangChain: Quickstart Guide](https://python.langchain.com/docs/tutorials/) | The most popular entry point for LLM application development — essential for context engineering beginners. | 2024 |
| [LlamaIndex: Getting Started](https://docs.llamaindex.ai/en/stable/getting_started/) | Comprehensive introduction to building RAG applications — best framework for data-intensive context systems. | 2024 |
| [Haystack: Introduction](https://docs.haystack.deepset.ai/docs/intro) | NLP pipeline framework with strong production pedigree — good for search-focused context engineering. | 2024 |
| [CrewAI: Getting Started](https://docs.crewai.com/getting-started/Introduction/) | Quick introduction to multi-agent systems with CrewAI — easiest way to experiment with agent teams. | 2024 |
| [AutoGen: Quickstart](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/quickstart.html) | Microsoft's multi-agent conversation framework — strong for complex agent interactions. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [LangChain: RAG Implementation Patterns](https://python.langchain.com/docs/tutorials/rag/) | Deep dive into RAG implementations with LangChain covering advanced retrieval, compression, and generation patterns. | 2024 |
| [LlamaIndex: Advanced RAG Patterns](https://docs.llamaindex.ai/en/stable/module_guides/querying/retrievers/advanced_retrieval/) | Advanced retrieval patterns in LlamaIndex including hybrid search, reranking, and recursive retrieval. | 2024 |
| [LangGraph: Agent Architecture](https://langchain-ai.github.io/langgraph/tutorials/) | Tutorials on building agent workflows with LangGraph — the state-of-the-art for agentic context management. | 2024 |
| [Semantic Kernel: AI Orchestration](https://learn.microsoft.com/en-us/semantic-kernel/overview/) | Microsoft's enterprise AI orchestration framework with planning and memory capabilities. | 2024 |
| [CrewAI: Advanced Collaboration](https://docs.crewai.com/core-concepts/Collaboration/) | Advanced multi-agent collaboration patterns with CrewAI including context sharing and task delegation. | 2024 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [LangChain: Custom Agent Architectures](https://python.langchain.com/docs/how_to/custom_agent/) | Building custom agents with LangChain — advanced patterns for context routing and tool management. | 2024 |
| [LlamaIndex: Agentic RAG with Tool Use](https://docs.llamaindex.ai/en/stable/examples/agent/) | Examples of agentic RAG where agents decide retrieval strategies based on context needs. | 2024 |
| [Haystack: Custom Pipeline Components](https://docs.haystack.deepset.ai/docs/custom-components) | Building custom components for Haystack pipelines — advanced pattern for production context pipelines. | 2024 |
| [AutoGen: Multi-Agent with Shared Context](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/groupchat.html) | Group chat and shared context patterns in AutoGen for complex multi-agent coordination. | 2024 |
| [Google: Vertex AI Agent Builder](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder) | Google's managed framework for building agents with context management, search, and tool integration. | 2024 |

## Framework Comparison by Context Engineering Requirements

| Requirement | LangChain | LlamaIndex | Haystack | CrewAI |
|---|---|---|---|---|
| **Retrieval flexibility** | ★★★★ | ★★★★★ | ★★★★ | ★★ |
| **Memory management** | ★★★ | ★★★★ | ★★ | ★★★★ |
| **Agent complexity** | ★★★★★ | ★★★★ | ★★★ | ★★★★★ |
| **Multi-agent support** | ★★★ | ★★ | ★ | ★★★★★ |
| **Production tooling** | LangSmith | Limited | deepset Cloud | Limited |
| **Learning curve** | Moderate | Moderate | Easy | Easy |

## Related Sections

- [Open Source Tools](./open-source-tools.md) — Individual tools used within frameworks
- [Tutorials](./tutorials.md) — Framework-specific tutorials
- [Agent Context Management](./agent-context-management.md) — Context patterns with frameworks

## Related Patterns

- [Agent Context Management](../patterns/agent-context-management.md)
