# Context Ranking Pattern

Assign relevance scores to each piece of context in the prompt assembly pipeline, ordering and filtering content so that the most salient information occupies the limited attention bandwidth of the model.

## Problem

In any context-rich system—RAG retrieval, multi-turn conversations, multi-source agentic workflows—not all context is equally important. When the assembled prompt exceeds optimal size (or the model's effective recall capacity), low-value context dilutes attention on critical information. Without principled ranking:

- **Lost-in-the-Middle:** Models consistently underperform when relevant information is placed in the middle of the prompt rather than at the beginning or end.
- **Retrieval Noise:** RAG pipelines retrieve chunks that are topically related but not actually useful for answering the specific query, wasting tokens.
- **Uneven Resource Allocation:** All context items consume the same token budget regardless of their actual utility for the current task.
- **User Frustration:** The model answers based on peripheral information while ignoring the central request.

## Solution

Context Ranking applies a multi-signal scoring function to each candidate context item and uses the resulting scores to:

1. **Filter:** Drop items below a relevance threshold.
2. **Order:** Place highest-scoring items at the beginning or end of the prompt (both positions show strongest recall).
3. **Allocate Budget:** Assign larger token budgets to higher-ranked items (e.g., full document vs. summary-only for low-ranked items).

The scoring function combines signals:

```text
score(context, query) = w1 · sim_emb(context, query)
                     + w2 · recency_factor(context)
                     + w3 · authority_score(source)
                     + w4 · specificity(context)
                     + w5 · recency_decay(timestamp)
```

Weights (w1–w5) are configurable per use case. For chat, recency and specificity dominate. For RAG, embedding similarity and authority dominate.

## Architecture

```mermaid
flowchart TB
    subgraph Candidates
        A[Retrieved Chunks]
        B[Conversation Turns]
        C[Tool Results]
        D[External Sources]
    end

    subgraph ScoringEngine
        E[Embedding Similarity<br/>cosine(emb_q, emb_d)]
        F[Recency Decay<br/>exp(-lambda * age)]
        G[Authority Signal<br/>source trust score]
        H[Specificity Penalty<br/>high IDF rare terms]
    end

    subgraph Aggregation
        I[Weighted Score<br/>sum(w_i * signal_i)]
    end

    subgraph ContextAssembly
        J{Score > Threshold?}
        K[Rank by Score]
        L[Allocate Token Budget<br/>per rank tier]
        M[Assemble Ordered Prompt<br/>best positions for top K]
    end

    A --> E
    B --> F
    C --> G
    D --> H
    E --> I
    F --> I
    G --> I
    H --> I
    I --> J
    J -- Yes --> K
    J -- No --> N[Discard]
    K --> L --> M
```

**Scoring signal details:**

| Signal | Implementation | Range | Notes |
|---|---|---|---|
| Embedding Similarity | cosine(embed_query, embed_doc) | [0, 1] | Requires embedding model; domain-tuned is better |
| Recency Decay | exp(-λ · Δt_hours) | (0, 1] | λ configurable; λ=0.01 gives ~50% decay at 69h |
| Authority | Pre-assigned per source (e.g., 0.9 for docs, 0.5 for forums) | [0, 1] | Maintain source registry |
| Specificity | Mean inverse document frequency of tokens | [0, +∞) | Rarer terms → more specific → higher score |

## Tradeoffs

| Approach | When to Use | Cost | Risk |
|---|---|---|---|
| **Single-signal (embedding only)** | Simple RAG, homogenous sources | Low | Misses recency-dependent needs; poor for conversations |
| **Multi-signal weighted** | Production systems with varied context types | Medium | Weight tuning requires eval feedback loop |
| **Learned scoring** | High-throughput systems with labeled relevance data | High (training) | Overfit to eval set; cold-start problem |
| **LLM-as-judge** | Small contexts where quality is paramount | High (LLM call per item) | Latency; cost; not suitable for real-time |

## Example Workflow

```text
1. User query: "What's the current deploy status for the auth service?"
2. Candidate context items:
   - [CI log] Last deploy output (2 min ago) → score: 0.92
   - [Chat] Deploy discussion from yesterday → score: 0.71
   - [Doc] Auth service architecture (6 months old) → score: 0.45
   - [Chat] General CI discussion (last week) → score: 0.31
   - [Doc] Auth service PR template → score: 0.12
3. Threshold: 0.4. Items 4 and 5 filtered.
4. Top 3 items placed: most recent deploy log first, architecture doc last.
5. Token budget: Item 1 gets 60%, item 2 gets 30%, item 3 gets 10%.
6. Assembled prompt fits in 6K tokens instead of 15K.
```

## Example Prompt

```text
Relevance Scoring Instructions:

Given the user query below, score each context item on a scale of 0.0 to 1.0.
Consider: (a) does this item directly answer the query? (b) is it recent?
(c) is it from an authoritative source?

Query: "How do I configure the rate limiter for the API gateway?"

Context items:
1. "API Gateway Configuration Guide (v2.3)"
2. "Community forum: rate limiting issues"
3. "Deploy logs from last Tuesday"

Output scores with brief justification:
```

## Failure Modes

| Mode | Symptom | Cause | Mitigation |
|---|---|---|---|
| **Score Saturation** | All items score 0.9+ → no filtering | Embedding space too dense; recency weights too low | Normalize scores; add specificity signal; increase authority weight |
| **Recency Dominance** | Old but critical context always dropped | λ too aggressive | Use task-specific λ (chat=0.05, RAG=0.001) |
| **Authority Blindness** | Low-authority source outranks canonical docs | Missing or stale authority registry | Audit source registry quarterly; bootstrap with manual assignments |
| **Cold Score** | New content with no recency or signal scores low | Not enough metadata to score | Assign default mid-score to new content; promote after first user interaction |

## Production Considerations

- **Pre-compute Where Possible:** Embeddings for static documents are pre-computed and cached. Only dynamic items (conversation turns, fresh tool outputs) need real-time scoring.
- **Weight Tuning via Eval:** Run an offline eval dataset with labeled relevance judgments. Optimize w1–w5 via grid search or Bayesian optimization. Re-tune monthly or when content sources change.
- **Threshold Adaptation:** Use a percentile-based threshold (keep top-K or top-30%) instead of an absolute score to handle score distribution shifts.
- **Cascading Ranking:** Two-stage: coarse filter (cheap signals: recency + authority) → fine rank (expensive signals: embedding similarity). Reduces embedding calls by 60–80%.
- **Observability:** Log per-item scores, final rank, and which items were filtered. Dashboard showing score distribution over time.
- **A/B Testing:** Run live A/B tests comparing ranking configurations on answer accuracy (LLM-as-judge or user feedback).
