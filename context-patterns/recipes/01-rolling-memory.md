# Rolling Memory (Sliding Window)

**Problem:** Your LLM conversation or agent trace exceeds the context window. Keep recent items verbatim and compress older ones into summaries.

**Pattern:** [Rolling Memory](../patterns/rolling-memory.md)

```python
import json
from collections import deque

class RollingMemory:
    """Tiered rolling memory: active window + summary layer + archival store."""

    def __init__(self, window_size: int = 20, summary_interval: int = 10):
        self.window = deque(maxlen=window_size)
        self.summaries: list[str] = []
        self.archive: list[dict] = []
        self.summary_interval = summary_interval
        self._since_last_summary = 0

    def add(self, role: str, content: str) -> None:
        if len(self.window) == self.window.maxlen:
            oldest = self.window[0]
            self._maybe_summarize_batch([oldest])
        self.window.append({"role": role, "content": content})
        self._since_last_summary += 1

    def _maybe_summarize_batch(self, batch: list[dict]) -> None:
        if not batch:
            return
        texts = [m["content"][:80] for m in batch]
        summary = f"[Summary: {' | '.join(texts)}]"
        self.summaries.append(summary)
        self.archive.extend(batch)
        self._since_last_summary = 0

    def assemble_context(self, max_tokens: int = 4000) -> str:
        parts: list[str] = []
        budget = max_tokens
        summary_budget = int(budget * 0.25)
        summary_text = "\n".join(self.summaries)
        if len(summary_text) // 4 > summary_budget:
            trimmed = []
            char_budget = summary_budget * 4
            for s in reversed(self.summaries):
                if sum(len(x) for x in trimmed) + len(s) <= char_budget:
                    trimmed.insert(0, s)
                else:
                    break
            summary_text = "\n".join(trimmed)
        if summary_text:
            parts.append(f"=== SUMMARY CHAIN ===\n{summary_text}")
        window_budget = budget - (len(summary_text) // 4)
        window_chars = window_budget * 4
        window_text = ""
        for msg in reversed(self.window):
            entry = f"{msg['role']}: {msg['content']}"
            if len(window_text) + len(entry) > window_chars:
                break
            window_text = f"{entry}\n" + window_text
        if window_text:
            parts.append(f"=== ACTIVE WINDOW ===\n{window_text.strip()}")
        return "\n\n".join(parts)

    def search_archive(self, keyword: str) -> list[dict]:
        return [m for m in self.archive if keyword.lower() in m["content"].lower()]


if __name__ == "__main__":
    mem = RollingMemory(window_size=5, summary_interval=3)
    for i in range(12):
        mem.add("user", f"Message number {i}: how do I optimize my RAG pipeline?")
        mem.add("assistant", f"Response to message {i}: consider chunk overlap and reranking.")
    context = mem.assemble_context(max_tokens=500)
    print("\n=== ASSEMBLED CONTEXT ===")
    print(context[:800] + "..." if len(context) > 800 else context)
    print("\n=== ARCHIVE SEARCH ===")
    results = mem.search_archive("RAG")
    print(f"Found {len(results)} archived messages mentioning 'RAG'")
```

## Key Takeaways

- **Active window** keeps recent items verbatim (configurable size)
- **Summary layer** compresses older items (25% of token budget)
- **Archive** stores everything for later keyword search
- **Eviction policy**: oldest items are summarized before eviction

## Production Notes

- Replace the extractive summary with an LLM call for better quality
- Use a vector DB for archive search instead of keyword matching
- Cap summary depth to 3 levels to avoid recursive drift
- Run eviction asynchronously after response is sent

## Related

- [Decision Guide: which pattern?](../DECISION-GUIDE.md)
- [Cheatsheet: Rolling Memory](../cheatsheets/rolling-memory.md)
