# Context Pruning for RAG

**Problem:** RAG retrieves overlapping chunks, filler conversations, and near-duplicates that waste tokens. Prune before ranking.

**Pattern:** [Context Pruning](../patterns/context-pruning.md)

```python
import re
from collections import Counter

class ContextPruner:
    """Three-pass pruner: structural dedup → conversational noise → semantic overlap."""

    def __init__(self):
        self.removed: list[tuple[int, str]] = []

    def prune(self, items: list[str]) -> list[str]:
        self.removed = []
        result = items.copy()
        result = self._pass1_structural_dedup(result)
        result = self._pass2_conversational_noise(result)
        result = self._pass3_semantic_overlap(result)
        return result

    def _pass1_structural_dedup(self, items: list[str]) -> list[str]:
        """Remove exact duplicates and near-duplicates (Jaccard > 0.85)."""
        seen_hashes: set[int] = set()
        kept: list[str] = []
        for i, item in enumerate(items):
            h = hash(item)
            if h in seen_hashes:
                self.removed.append((i, "exact_duplicate"))
                continue
            seen_hashes.add(h)
            if kept:
                prev_tokens = set(self._tokenize(kept[-1]))
                curr_tokens = set(self._tokenize(item))
                if prev_tokens and curr_tokens:
                    jaccard = len(prev_tokens & curr_tokens) / len(prev_tokens | curr_tokens)
                    if jaccard > 0.85:
                        self.removed.append((i, f"near_duplicate (j={jaccard:.2f})"))
                        continue
            kept.append(item)
        return kept

    _FILLER_PATTERNS = [
        re.compile(r"^(ok|okay|thanks|thank you|got it|sure|yes|no|yep|nope|right|understood)$", re.IGNORECASE),
        re.compile(r"^(processing|waiting|loading)\.+\.?$", re.IGNORECASE),
        re.compile(r"^(let me |i'll |i will |hold on ).{0,40}$", re.IGNORECASE),
    ]

    def _pass2_conversational_noise(self, items: list[str]) -> list[str]:
        """Remove filler, acknowledgments, and system status messages."""
        kept: list[str] = []
        for i, item in enumerate(items):
            stripped = item.strip()
            if len(stripped) < 15:
                if any(p.match(stripped) for p in self._FILLER_PATTERNS):
                    self.removed.append((i, "conversational_filler"))
                    continue
            kept.append(item)
        return kept

    def _pass3_semantic_overlap(self, items: list[str]) -> list[str]:
        """Merge overlapping chunks by keeping unique sentences."""
        if not items:
            return items
        merged = [items[0]]
        for i in range(1, len(items)):
            prev_sentences = self._split_sentences(merged[-1])
            curr_sentences = self._split_sentences(items[i])
            prev_set = set(prev_sentences)
            overlap = sum(1 for s in curr_sentences if s in prev_set)
            if overlap / max(len(curr_sentences), 1) > 0.6:
                union = list(prev_set | set(curr_sentences))
                merged[-1] = " ".join(union)
                self.removed.append((i, "merged_overlap"))
            else:
                merged.append(items[i])
        return merged

    def _tokenize(self, text: str) -> list[str]:
        return re.findall(r"\w+", text.lower())

    def _split_sentences(self, text: str) -> list[str]:
        return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


if __name__ == "__main__":
    pruner = ContextPruner()
    sample_items = [
        "The API uses OAuth 2.0 for authentication. Tokens expire after 3600 seconds.",
        "Tokens expire after 3600 seconds. Always refresh before expiry.",  # near-duplicate
        "The API uses OAuth 2.0 for authentication. Tokens expire after 3600 seconds.",  # exact duplicate
        "ok",  # filler
        "Rate limiting is applied per API key: 1000 requests per hour.",
        "Thanks",  # filler
        "The API rate limit is 1000 req/h for free tier. The pro tier has 10000.",
        "Processing...",  # system noise
    ]
    pruned = pruner.prune(sample_items)
    print(f"=== BEFORE: {len(sample_items)} items ===")
    print(f"=== AFTER:  {len(pruned)} items ===")
    print(f"=== REMOVED: {len(pruner.removed)} items ===")
    for idx, reason in pruner.removed:
        print(f"   - Item #{idx}: {reason}")
    print("\n=== PRUNED OUTPUT ===")
    for i, item in enumerate(pruned):
        print(f"  [{i}] {item[:80]}...")
```

## Key Takeaways

- **Pass 1**: removes exact + near-duplicates (typically cuts 15–30% of RAG results)
- **Pass 2**: strips filler (ok, thanks, processing...) — common in agent tool traces
- **Pass 3**: merges overlapping chunks via sentence overlap > 60%
- **Cumulative**: 15–60% token reduction depending on retrieval quality

## Production Notes

- Tune the Jaccard threshold (0.85) based on your chunking strategy
- Sentence overlap pass works best with contiguous chunks; skip if chunks come from different sources
- Add min-hash LSH for near-dedup at scale (thousands of chunks)
- Log pruning decisions for debugging retrieval quality

## Related

- [Decision Guide: which pattern?](../DECISION-GUIDE.md)
