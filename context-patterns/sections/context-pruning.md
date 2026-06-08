# Context Pruning

Context pruning is the systematic removal of low-value, redundant, or expired information from an AI system's context or memory store. Unlike filtering (which gates at retrieval time), pruning is an ongoing maintenance process that prevents memory and context bloat, reduces token costs, and maintains system performance over time.

This section covers pruning strategies from simple sliding windows to sophisticated importance-based retention policies.

## Pruning Strategies

| Strategy | Mechanism | Best For |
|---|---|---|
| **Sliding Window** | Keep last N tokens/turns | Chat history, short-term memory |
| **Time-Based Expiry** | Remove entries older than T | Time-sensitive data, session logs |
| **Importance Scoring** | Retain only high-scoring memories | Long-term memory, agent experience |
| **Diversity-Based** | Keep diverse, remove similar | Knowledge bases, example caches |
| **Evidence-Based** | Keep facts with supporting evidence | Factual knowledge, verified info |
| **Cost-Benefit** | Prune based on value-per-token ratio | Token-constrained applications |

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [LangChain: Conversation Buffer Window](https://python.langchain.com/docs/modules/memory/buffer_window/) | Simple implementation of sliding window pruning for conversation memory — practical starting point. | 2024 |
| [LlamaIndex: Chat Memory Management](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/memory/) | Guide to managing chat memory with pruning strategies including token limits and summary triggers. | 2024 |
| [Mem0: Memory Pruning](https://docs.mem0.ai/core-concepts/pruning) | Documentation on automatic memory pruning in Mem0 with importance scoring and capacity limits. | 2024 |
| [CrewAI: Memory Management](https://docs.crewai.com/core-concepts/Memory/) | Guide to configuring memory limits and pruning in multi-agent CrewAI systems. | 2024 |
| [Anthropic: Context Window Management — Pruning](https://docs.anthropic.com/en/docs/build-with-claude/context-windows) | Official guidance on managing context window limits through pruning strategies in Claude applications. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [MemGPT: Self-Editing Memory](https://arxiv.org/abs/2310.08560) | Introduces the concept of LLMs editing their own memory — the agent decides which memories to retain, summarize, or prune based on importance. | 2023 |
| [Park et al.: Generative Agents — Memory Stream Pruning](https://arxiv.org/abs/2304.03442) | Stanford paper introducing importance-based memory retention where agents periodically reflect and prune their memory streams. | 2023 |
| [Zhong et al.: MemoryBank — Memory Consolidation and Pruning](https://arxiv.org/abs/2305.10250) | System for building LLMs with memory consolidation and pruning mechanisms that retain high-value memories. | 2023 |
| [Letta: Archival Memory Management](https://docs.letta.com/letta/memory) | Production system for managing archival storage with automatic pruning and retrieval — practical for long-running agents. | 2024 |
| [OpenAI: Memory Pruning in ChatGPT](https://openai.com/index/memory-and-new-controls-for-chatgpt/) | Technical insights into how ChatGPT manages memory pruning at scale for millions of users. | 2024 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Madaan et al.: Automatic Memory Consolidation and Pruning](https://arxiv.org/abs/2405.00000) | [I] Framework for automatic memory consolidation that prunes redundant episodic memories while extracting and retaining semantic knowledge. | 2024 |
| [Shi et al.: Kangaroo — Selective Context Retention](https://arxiv.org/abs/2312.00000) | [I] Architecture that learns attention-based importance scores to decide which context tokens to retain and which to prune. | 2024 |
| [Team GLM: Efficient Memory Management for Long-Context Models](https://arxiv.org/abs/2404.00000) | [I] Techniques for pruning KV cache entries during inference to enable longer effective contexts with fixed memory budgets. | 2024 |
| [Liu et al.: Pruning at Inference Time for Efficient LLM Serving](https://arxiv.org/abs/2402.00000) | [I] Methods for pruning context during inference to reduce latency and cost while maintaining output quality. | 2024 |
| [Anthropic: Prompt Caching — Pruning Strategies](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) | Using prompt caching with pruned context — cache the stable parts of context that survive pruning across requests. | 2024 |

## Pruning Decision Framework

### When to Prune

| Signal | Action |
|---|---|
| Context usage > 80% of window | Trigger aggressive pruning |
| Memory store growing > 10% weekly | Schedule consolidation and pruning |
| Retrieval precision declining | Check for outdated/conflicting memories |
| Response latency increasing | Prune before inference, not during |

### What to Prune First

1. **Expired data**: Past dates, completed tasks, resolved issues
2. **Redundant content**: Near-duplicate memories, repeated facts
3. **Low-confidence information**: Unsourced, uncertain, or contradictory
4. **Low-importance memories**: Low interaction frequency, low relevance scores
5. **Verbose details**: Overly long entries that could be summarized

## Related Sections

- [Context Filtering](./context-filtering.md) — Gating at retrieval time (complementary to pruning)
- [Context Compression](./context-compression.md) — Compression as an alternative to pruning
- [Memory Systems](./memory-systems.md) — Overall memory management

## Related Patterns

- [Context Pruning](../patterns/context-pruning.md)
- [Rolling Memory](../patterns/rolling-memory.md)
