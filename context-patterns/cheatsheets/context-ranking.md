# Context Ranking — Cheatsheet

## Concept
Score each context item, then filter (drop low-scoring), order (best positions), and budget-allocate (more tokens to high-value items).

## Scoring Formula

```
score = w1·embedding_sim(query, item)
      + w2·recency_factor(age)
      + w3·authority_score(source)
      + w4·specificity(rare_terms)
```

## Typical Weights

| Use Case | Embedding | Recency | Authority | Specificity |
|---|---|---|---|---|
| Chat with history | 0.25 | 0.40 | 0.15 | 0.20 |
| RAG pipeline | 0.50 | 0.15 | 0.25 | 0.10 |
| Tool output | 0.30 | 0.35 | 0.20 | 0.15 |
| Research synthesis | 0.35 | 0.10 | 0.35 | 0.20 |

## Position Optimization

```
Best positions: [BEGINNING]  [END]
Worst position: [MIDDLE]

Strategy:
- Top 1-2 items → prompt beginning
- Next best items → prompt end
- Everything else → middle (or drop)
```

## Key Code Snippet

```python
def score_item(query_tokens: set, item_text: str,
               age_hours: float, source: str) -> float:
    """Compute multi-signal relevance score."""
    import math
    item_tokens = set(item_text.lower().split())

    # Embedding similarity proxy (Jaccard)
    jaccard = (len(query_tokens & item_tokens) /
               len(query_tokens | item_tokens)) if query_tokens else 0

    # Recency decay (λ=0.01 → 50% at ~69h)
    recency = math.exp(-0.01 * age_hours)

    # Authority lookup
    authority = {"doc": 1.0, "chat": 0.6, "forum": 0.4}.get(source, 0.3)

    # Specificity: fraction of non-stopword tokens
    stopwords = {"the", "a", "an", "is", "are", "in", "on", "at", "to", "for"}
    rare = [t for t in item_tokens if t not in stopwords and len(t) > 3]
    specificity = len(rare) / max(len(item_tokens), 1)

    return 0.4*jaccard + 0.3*recency + 0.15*authority + 0.15*specificity
```

## Cascade Strategy (Cost Optimization)

```
Stage 1 (cheap): filter with recency + authority → reduces candidate pool 60-80%
Stage 2 (expensive): rank survivors with embedding similarity
```

## Common Pitfalls

- ❌ **Score saturation** → all items score 0.9+; no filtering happens → normalize or use percentile threshold
- ❌ **Recency dominance** → old but critical docs always filtered → use task-specific decay λ
- ❌ **Fixed threshold** → score distribution shifts over time → use top-K or top-30% instead
- ✅ **Two-stage cascade** → 60-80% fewer embedding calls
- ✅ **Pre-compute static doc embeddings** → only score dynamic items in real-time
- ✅ **Log per-item scores** → debug ranking quality regressions

## Related

- Full pattern: [patterns/context-ranking.md](../patterns/context-ranking.md)
- Recipe: [COOKBOOK.md#3](../COOKBOOK.md#3-multi-signal-context-ranking)
