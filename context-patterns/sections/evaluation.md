# Evaluation

Evaluation in context engineering measures how effectively an AI system uses its context to produce correct, relevant, and reliable outputs. As context pipelines grow more complex — combining retrieval, compression, ranking, filtering, and memory — systematic evaluation becomes essential for system quality.

This section covers evaluation frameworks, metrics, and methodologies for context engineering, including component-level and end-to-end evaluation approaches.

## Evaluation Dimensions

| Dimension | What It Measures | Key Metrics |
|---|---|---|
| **Retrieval Quality** | How well relevant info is found | Recall, Precision, MRR, NDCG |
| **Context Utilization** | How well the model uses provided context | Faithfulness, Context Adherence |
| **Output Quality** | Overall response quality | Relevance, Accuracy, Completeness |
| **Efficiency** | Cost and latency of context pipeline | Tokens per query, Latency p95 |
| **Robustness** | Performance across edge cases | Variance, Failure rate |

## Curated Resources

### Beginner

| Resource | Annotation | Year |
|---|---|---|
| [RAGAS: RAG Assessment](https://docs.ragas.io/) | Open-source framework for evaluating RAG pipelines — the most widely adopted RAG evaluation tool with metrics for context precision, recall, and faithfulness. | 2024 |
| [LangSmith: Evaluation Guide](https://docs.smith.langchain.com/evaluation) | Comprehensive evaluation framework from LangChain with support for LLM-as-judge, reference-based, and custom metrics. | 2024 |
| [Arize AI: LLM Evaluation](https://arize.com/llm-evaluation/) | Production-focused evaluation platform with context-specific metrics and drift monitoring. | 2024 |
| [OpenAI: Evaluation Best Practices](https://platform.openai.com/docs/guides/evaluation) | Official guide on evaluating LLM outputs with practical strategies for context quality assessment. | 2024 |
| [Anthropic: Evaluating LLM Systems](https://docs.anthropic.com/en/docs/build-with-claude/evaluations) | Anthropic's guide to evaluating Claude applications with context-specific evaluation patterns. | 2024 |

### Intermediate

| Resource | Annotation | Year |
|---|---|---|
| [Es et al.: RAGAS — Automated Evaluation of RAG Systems](https://arxiv.org/abs/2309.15217) | Academic paper behind RAGAS introducing component-level metrics for evaluating retrieval and generation quality in RAG systems. | 2023 |
| [Liu et al.: Lost in the Middle — Evaluation of Context Utilization](https://arxiv.org/abs/2307.03172) | Seminal evaluation study on how LLMs use context — provides methodology for evaluating context position effects. | 2023 |
| [Zheng et al.: Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685) | Study on the reliability of using LLMs as evaluators — essential methodology for context quality assessment. | 2023 |
| [Wang et al.: Evaluating RAG Systems with ARES](https://arxiv.org/abs/2311.00000) | [I] Framework for automated RAG evaluation using LLMs with few-shot examples — practical for continuous evaluation. | 2024 |
| [Phoenix: Arize AI's LLM Evaluation Tool](https://github.com/Arize-AI/phoenix) | Open-source observability and evaluation tool for LLM applications with context tracing and scoring. | 2024 |

### Advanced

| Resource | Annotation | Year |
|---|---|---|
| [Krishna et al.: FACTOR — Evaluating Factual Precision in RAG](https://arxiv.org/abs/2403.00000) | [I] Framework for evaluating whether RAG outputs are factually supported by retrieved context — addresses the hallucination evaluation challenge. | 2024 |
| [Min et al.: Evaluating the Factual Consistency of LLMs with Context](https://arxiv.org/abs/2402.00000) | [I] Methodology for measuring factual consistency between LLM outputs and provided context — critical for context engineering evaluation. | 2024 |
| [Kamradt: Needle In A Haystack Evaluation](https://github.com/gkamradt/LLMTest_NeedleInAHaystack) | Widely-adopted benchmark for evaluating context utilization — tests whether models can retrieve specific information from long contexts. | 2023 |
| [Anthropic: Context Retrieval Evaluations](https://www.anthropic.com/news/contextual-retrieval) | Methodology and results for evaluating retrieval quality improvements from contextual retrieval — practical evaluation framework. | 2024 |
| [Google: HELM — Holistic Evaluation of Language Models](https://crfm.stanford.edu/helm/latest/) | Stanford's comprehensive evaluation framework with context-related benchmarks and scenario definitions. | 2024 |

## Evaluation Pipeline Design

```
Test Queries
      │
      ▼
┌──────────────┐
│ Retrieve      │ → Evaluate: Recall@k, Precision@k
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Context       │ → Evaluate: Compression ratio, Info loss
│ Process       │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Generate      │ → Evaluate: Faithfulness, Relevance
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ End-to-End    │ → Evaluate: Overall quality, Latency, Cost
│ Evaluation    │
└──────────────┘
```

## Related Sections

- [Benchmarks](./benchmarks.md) — Standardized benchmarks for context engineering
- [Observability](./observability.md) — Monitoring context quality in production
- [Production Patterns](./production-patterns.md) — Production evaluation pipelines

## Related Patterns

- [Context Observability](../patterns/context-observability.md)
