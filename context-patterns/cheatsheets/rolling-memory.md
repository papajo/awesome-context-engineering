# Rolling Memory — Cheatsheet

## Concept
Manage context as a sliding window: recent items verbatim, older items summarized, oldest items archived with search.

## Quick Reference

```
┌─────────────────────────────────────────────────────────────┐
│                    ROLLING MEMORY                           │
├──────────────┬──────────────────┬──────────────────────────┤
│ Active Window │  Summary Layer   │     Archival Store       │
│ (verbatim)    │  (compressed)    │     (searchable)         │
│ Recent N msgs │  N→1 summaries   │     Vector / KV index    │
└──────────────┴──────────────────┴──────────────────────────┘
```

## Eviction Policies

| Policy | How | Best For |
|---|---|---|
| FIFO | Drop oldest when full | Simple chat |
| Importance | Score + drop lowest | Complex agents |
| Summarize-then-evict | Compress batch before drop | Production |

## Token Budget Allocation

| Layer | Default % |
|---|---|
| Active Window | 60% |
| Summary Chain | 25% |
| Retrieved Archives | 15% |

## Key Code Snippet

```python
class RollingMemory:
    def __init__(self, window_size=20):
        self.window = deque(maxlen=window_size)
        self.summaries = []

    def add(self, role, content):
        if len(self.window) == self.window.maxlen:
            oldest = self.window[0]
            self.summaries.append(f"[Summary: {oldest['content'][:80]}]")
        self.window.append({"role": role, "content": content})

    def assemble(self, max_tokens=4000):
        parts = []
        # 25% budget for summaries
        summary_budget = int(max_tokens * 0.25)
        summary_text = "\n".join(self.summaries)
        if len(summary_text) // 4 > summary_budget:
            summary_text = summary_text[:summary_budget * 4]
        parts.append("=== SUMMARY ===\n" + summary_text)
        # 75% for recent window
        window_budget = max_tokens - (len(summary_text) // 4)
        window_chars = window_budget * 4
        window_lines = []
        for m in reversed(self.window):
            entry = f"{m['role']}: {m['content']}"
            if sum(len(l) for l in window_lines) + len(entry) > window_chars:
                break
            window_lines.insert(0, entry)
        parts.append("=== RECENT ===\n" + "\n".join(window_lines))
        return "\n\n".join(parts)
```

## Common Pitfalls

- ❌ **No summary layer** → hard cutoff loses all old context
- ❌ **Too-deep summary chain** → recursive summary drift
- ❌ **Blocking eviction** → user waits for memory bookkeeping
- ✅ **Async eviction** — run after response is sent
- ✅ **Cap summary depth** — max 3 levels of recursive summarization

## Related

- Full pattern: [patterns/rolling-memory.md](../patterns/rolling-memory.md)
- Recipe: [COOKBOOK.md#1](../COOKBOOK.md#1-basic-rolling-memory-sliding-window)
