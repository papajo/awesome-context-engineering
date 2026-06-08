# Multi-Signal Context Ranking

**Problem:** You have many candidate context items but limited token budget. Score, filter, and order them optimally.

**Pattern:** [Context Ranking](../patterns/context-ranking.md)

```python
import math
import time
from dataclasses import dataclass, field


@dataclass
class ContextItem:
    text: str
    source: str = ""
    timestamp: float = 0.0
    metadata: dict = field(default_factory=dict)


@dataclass
class ScoredItem:
    item: ContextItem
    score: float
    signals: dict = field(default_factory=dict)


class ContextRanker:
    """Multi-signal ranker with configurable weights."""

    def __init__(self, weights: dict[str, float] | None = None):
        self.weights = weights or {
            "embedding_sim": 0.4,
            "recency": 0.3,
            "authority": 0.15,
            "specificity": 0.15,
        }
        self.authority_scores: dict[str, float] = {
            "official_docs": 1.0,
            "api_spec": 0.95,
            "code_example": 0.85,
            "team_chat": 0.6,
            "forum": 0.4,
            "unknown": 0.3,
        }
        self._query_tokens: set[str] = set()

    def set_query(self, query: str) -> None:
        self._query_tokens = set(self._tokenize(query.lower()))

    def _tokenize(self, text: str) -> list[str]:
        return text.split()

    def _embedding_similarity(self, item: ContextItem) -> float:
        """Jaccard overlap as cheap proxy for embedding similarity."""
        if not self._query_tokens:
            return 0.0
        item_tokens = set(self._tokenize(item.text.lower()))
        if not item_tokens:
            return 0.0
        intersection = self._query_tokens & item_tokens
        union = self._query_tokens | item_tokens
        return len(intersection) / len(union) if union else 0.0

    def _recency_score(self, item: ContextItem) -> float:
        age = time.time() - item.timestamp
        lam = 0.01 / 3600  # per-second decay (~50% at 69h)
        return math.exp(-lam * age)

    def _authority_score(self, item: ContextItem) -> float:
        return self.authority_scores.get(item.source, self.authority_scores["unknown"])

    def _specificity(self, item: ContextItem) -> float:
        """Score based on rare terms (inverse DF proxy)."""
        tokens = self._tokenize(item.text.lower())
        if not tokens:
            return 0.0
        stop_words = {"the", "a", "an", "is", "are", "in", "on", "at", "to", "for", "of", "and", "or"}
        rare_tokens = [t for t in tokens if t not in stop_words and len(t) > 3]
        return min(len(rare_tokens) / max(len(tokens), 1), 1.0)

    def score(self, item: ContextItem) -> ScoredItem:
        signals = {
            "embedding_sim": self._embedding_similarity(item),
            "recency": self._recency_score(item),
            "authority": self._authority_score(item),
            "specificity": self._specificity(item),
        }
        total = sum(signals[k] * self.weights[k] for k in signals)
        return ScoredItem(item=item, score=total, signals=signals)

    def rank(self, items: list[ContextItem], threshold: float = 0.15, top_k: int | None = None) -> list[ScoredItem]:
        scored = [self.score(item) for item in items]
        scored = [s for s in scored if s.score >= threshold]
        scored.sort(key=lambda s: s.score, reverse=True)
        if top_k:
            scored = scored[:top_k]
        return scored


if __name__ == "__main__":
    ranker = ContextRanker()
    ranker.set_query("How do I configure rate limiting for the API gateway?")

    items = [
        ContextItem(
            text="Rate limiting is configured via the X-RateLimit headers. Default is 1000 req/h.",
            source="official_docs", timestamp=time.time() - 3600,
        ),
        ContextItem(
            text="I had issues with rate limiting on the gateway too. Try setting RATE_LIMIT_ENABLED=true.",
            source="forum", timestamp=time.time() - 86400 * 2,
        ),
        ContextItem(
            text="Deploy finished successfully. All services green.",
            source="team_chat", timestamp=time.time() - 300,
        ),
        ContextItem(
            text="The API gateway supports both token bucket and sliding window algorithms.",
            source="official_docs", timestamp=time.time() - 86400 * 30,
        ),
    ]

    results = ranker.rank(items, threshold=0.2)
    print("\n=== RANKED CONTEXT ITEMS ===")
    for i, scored in enumerate(results, 1):
        print(f"\n#{i} Score: {scored.score:.3f}")
        print(f"   Text: {scored.item.text[:80]}...")
        print(f"   Source: {scored.item.source}")
        print(f"   Signals: ", end="")
        for k, v in scored.signals.items():
            print(f"{k}={v:.2f} ", end="")
        print()
```

## Key Takeaways

- **Four signals**: embedding similarity (0.4), recency (0.3), authority (0.15), specificity (0.15)
- **Filter threshold**: items below 0.15 are dropped before sorting
- **Top-K limit**: optional cap to fit token budget

## Production Notes

- Replace Jaccard similarity with real embeddings (OpenAI, Cohere, BGE)
- Tune weights for your domain using a held-out eval set
- Add diversity penalty to avoid selecting 3 nearly-identical chunks
- Cache embedding vectors to avoid recomputation

## Related

- [Decision Guide: which pattern?](../DECISION-GUIDE.md)
- [Cheatsheet: Ranking](../cheatsheets/context-ranking.md)
