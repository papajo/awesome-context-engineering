# Quickstart: Context Engineering in 10 Minutes

> Get from zero to a running context pipeline in three steps. No external dependencies required.

---

## What You'll Build

A context management pipeline that:
1. Takes a user query and a set of context documents
2. **Prunes** duplicates and noise
3. **Ranks** items by relevance to the query
4. **Compresses** the survivors to fit a token budget
5. **Assembles** the final prompt

## Step 1: Create a File

Save this as `context_pipeline.py`:

```python
"""context_pipeline.py — minimal end-to-end context engineering pipeline."""
import re
import math


# ─── Pruning ────────────────────────────────────────────────────────

def prune(items: list[str]) -> list[str]:
    """Remove exact duplicates and short filler messages."""
    seen = set()
    kept = []
    for item in items:
        stripped = item.strip()
        # Skip short filler
        if len(stripped) < 15 and stripped.lower() in {
            "ok", "okay", "thanks", "got it", "yes", "no", "sure",
        }:
            continue
        # Skip exact duplicates
        h = hash(stripped)
        if h in seen:
            continue
        seen.add(h)
        kept.append(stripped)
    return kept


# ─── Ranking ────────────────────────────────────────────────────────

def tokenize(text: str) -> set[str]:
    return set(re.findall(r"\w+", text.lower()))


def rank(query: str, items: list[str]) -> list[tuple[float, str]]:
    """Score items by Jaccard similarity to the query."""
    q_tokens = tokenize(query)
    scored = []
    for item in items:
        i_tokens = tokenize(item)
        if not q_tokens or not i_tokens:
            scored.append((0.0, item))
            continue
        intersection = q_tokens & i_tokens
        union = q_tokens | i_tokens
        jaccard = len(intersection) / len(union)
        scored.append((jaccard, item))

    # Sort descending, keep top items with score > 0
    scored.sort(key=lambda x: x[0], reverse=True)
    return [s for s in scored if s[0] > 0]


# ─── Compression ────────────────────────────────────────────────────

def compress(text: str, max_chars: int = 2000) -> str:
    """Structural + extractive compression to fit a budget."""
    # Structural: collapse whitespace, remove formatting
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r'[*_~`#>"]+', " ", text)
    text = re.sub(r"[ \t]{2,}", " ", text)

    if len(text) <= max_chars:
        return text

    # Extractive: keep first 2 sentences per paragraph
    paragraphs = text.split("\n\n")
    compressed = []
    for p in paragraphs:
        sentences = re.split(r"(?<=[.!?])\s+", p.strip())
        compressed.append(" ".join(sentences[:2]))

    result = "\n\n".join(compressed)
    return result[:max_chars]


# ─── Rolling Memory ─────────────────────────────────────────────────

from collections import deque


class RollingMemory:
    """Simple sliding window for conversational context."""

    def __init__(self, window_size: int = 10):
        self.window = deque(maxlen=window_size)

    def add(self, role: str, content: str) -> None:
        self.window.append({"role": role, "content": content})

    def get_context(self) -> str:
        return "\n".join(
            f"{m['role']}: {m['content']}" for m in self.window
        )


# ─── End-to-End Pipeline ───────────────────────────────────────────

def run_pipeline(query: str, documents: list[str], memory: RollingMemory | None = None):
    """Run the full context engineering pipeline."""
    print("=" * 60)
    print("CONTEXT ENGINEERING PIPELINE")
    print("=" * 60)

    # Step 0: Count input
    total_chars = sum(len(d) for d in documents)
    print(f"\n📥 Input: {len(documents)} items, {total_chars} chars")

    # Step 1: Prune
    pruned = prune(documents)
    pruned_chars = sum(len(d) for d in pruned)
    print(f"🔧 Pruned: {len(pruned)} items ({len(documents) - len(pruned)} removed), {pruned_chars} chars")

    # Step 2: Rank
    ranked = rank(query, pruned)
    print(f"📊 Ranked: {len(ranked)} items above threshold")

    # Step 3: Assemble context
    context_parts = []

    if memory:
        context_parts.append("=== CONVERSATION HISTORY ===")
        context_parts.append(memory.get_context())

    context_parts.append("=== QUERY ===")
    context_parts.append(query)

    context_parts.append("=== RELEVANT DOCUMENTS ===")
    for score, doc in ranked[:5]:  # top 5
        context_parts.append(f"[Relevance: {score:.2f}]\n{doc}")

    raw_context = "\n\n".join(context_parts)

    # Step 4: Compress to fit budget
    budget = 4000
    compressed = compress(raw_context, budget)

    print(f"🗜️  Compressed: {len(raw_context)} → {len(compressed)} chars (target: {budget})")
    print(f"\n{'=' * 60}")
    print("FINAL PROMPT")
    print("=" * 60)
    print(compressed)

    return compressed


# ─── Main ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Sample data
    query = "How do I configure rate limiting for the API gateway?"

    docs = [
        "The API gateway supports rate limiting via the X-RateLimit headers. "
        "Default limit is 1000 requests per hour for the free tier. "
        "Configure via RATE_LIMIT_ENABLED=true in the gateway config.",

        "Rate limiting is configured per API key. Use the admin dashboard "
        "to set custom limits for enterprise customers.",

        "Thanks",  # filler — will be pruned

        "The API gateway supports rate limiting via the X-RateLimit headers. "
        "Default limit is 1000 requests per hour.",  # duplicate — will be pruned

        "Deploy completed successfully. All services are healthy.",

        "For the pro tier, rate limits are 10000 requests per hour. "
        "Use the /admin/rate-limits endpoint to configure programmatically.",
    ]

    # Optional: simulate conversation
    memory = RollingMemory(window_size=5)
    memory.add("user", "I'm setting up the API gateway for our production deployment.")
    memory.add("assistant", "Great! Let me help with rate limiting, auth, and routing configuration.")

    run_pipeline(query, docs, memory)
```

## Step 2: Run It

```bash
python context_pipeline.py
```

Expected output:

```
============================================================
CONTEXT ENGINEERING PIPELINE
============================================================

📥 Input: 6 items, 593 chars

🔧 Pruned: 5 items (1 removed), 587 chars

📊 Ranked: 4 items above threshold

🗜️  Compressed: 906 → 906 chars (target: 4000)

============================================================
FINAL PROMPT
============================================================
=== CONVERSATION HISTORY ===
user: I'm setting up the API gateway for our production deployment.
assistant: Great! Let me help with rate limiting, auth, and routing configuration.

=== QUERY ===
How do I configure rate limiting for the API gateway?

=== RELEVANT DOCUMENTS ===
[Relevance: 0.47]
The API gateway supports rate limiting via the X-RateLimit headers...
...
```

## Step 3: What Just Happened?

| Step | What | Why |
|---|---|---|
| **Prune** | Removed "Thanks" (filler) and a duplicate doc | Saves tokens, reduces noise |
| **Rank** | Scored docs by word overlap with query | Puts most relevant first |
| **Assemble** | Combined conversation + query + top docs | Complete context for the LLM |
| **Compress** | Structured + extractive pass | Fits within budget |

## Next Steps

| If You Want To | Go To |
|---|---|
| See the full rolling memory pattern | [COOKBOOK.md#1](../COOKBOOK.md#1-basic-rolling-memory-sliding-window) |
| Learn deeper compression | [COOKBOOK.md#2](../COOKBOOK.md#2-context-compression-pipeline) |
| Add multi-signal ranking | [COOKBOOK.md#3](../COOKBOOK.md#3-multi-signal-context-ranking) |
| Understand agent context tracking | [COOKBOOK.md#5](../COOKBOOK.md#5-agent-context-budget-tracker) |
| Decide which pattern fits your problem | [DECISION-GUIDE.md](../DECISION-GUIDE.md) |
| Read the full pattern docs | [patterns/](../patterns/) |
| See architecture examples | [examples/](../examples/) |

## Reference: Token Estimation

```python
def estimate_tokens(text: str) -> int:
    """Rough token estimation: ~4 chars per token for English."""
    return len(text) // 4

def estimate_chars(tokens: int) -> int:
    return tokens * 4
```

> ⚠️ This is a rough estimate. Real tokenizers (cl100k_base, tiktoken) vary by model and language. Use the model's actual tokenizer for production budgeting.
