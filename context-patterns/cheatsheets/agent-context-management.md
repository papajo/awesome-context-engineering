# Agent Context Management — Cheatsheet

## Concept
Track context budget across multi-step agent execution: core (system + tools) never evicted, working (recent steps) bounded, archive (old steps) summarized.

## Architecture

```
┌─────────────────────────────────────────────────┐
│              AGENT CONTEXT                       │
├──────────┬──────────────┬────────────────────────┤
│  CORE    │   WORKING    │       ARCHIVE          │
│ System   │  Recent      │  Old steps + summaries │
│ Prompt   │  steps       │  + tool results        │
│ Tools    │  (bounded)   │  (retrievable)         │
└──────────┴──────────────┴────────────────────────┘
```

## Budget Tracking

```
total_budget = model_max_tokens - output_tokens - safety_margin

core_usage = system_prompt_tokens + tools_tokens
working_usage = sum(recent_step_tokens)
archive_usage = sum(summary_tokens)

trigger_archival = (core + working + archive) > total_budget * 0.85
```

## Trigger Points

| Event | Action |
|---|---|
| Usage > 85% of budget | Archive oldest 30% of working events |
| Tool result > 2000 tokens | Store as reference, insert pointer (`See [ref_003]`) |
| Every 10 steps | Generate intermediate summary of work done |
| Archive > 50 items | Recursively summarize oldest summaries |

## Key Code Snippet

```python
class AgentContextManager:
    def __init__(self, max_tokens=8000):
        self.max_tokens = max_tokens
        self.core = []    # never evicted
        self.working = [] # bounded window
        self.summaries = []

    def add_event(self, event_type, content):
        tokens = len(content) // 4  # rough estimate
        self.working.append({"type": event_type,
                            "content": content,
                            "tokens": tokens})
        self._check_budget()

    def _check_budget(self):
        total = sum(e["tokens"] for e in self.core) \
              + sum(e["tokens"] for e in self.working) \
              + sum(len(s) for s in self.summaries) // 4
        if total > self.max_tokens * 0.85:
            self._archive_oldest()

    def _archive_oldest(self):
        cutoff = max(1, len(self.working) // 3)
        batch = self.working[:cutoff]
        summary = f"[Archived {len(batch)} steps: " \
                  + "; ".join(e["content"][:60] for e in batch[:3]) \
                  + "...]"
        self.summaries.append(summary)
        self.working = self.working[cutoff:]

    def format_prompt(self):
        parts = []
        for e in self.core:
            parts.append(f"<{e['type']}>{e['content']}</{e['type']}>")
        if self.summaries:
            parts.append("<history>" + "\n".join(self.summaries) + "</history>")
        if self.working:
            parts.append("<recent>" + "\n".join(
                f"[{e['type']}] {e['content']}" for e in self.working
            ) + "</recent>")
        return "\n\n".join(parts)
```

## Common Pitfalls

- ❌ **No budget tracking** → context silently grows until OOM or truncation
- ❌ **Blocking archival** → agent pauses mid-step to wait for summarization
- ❌ **No tool output limits** → single search result can blow the budget
- ✅ **Async archival** — summarize after response, never before
- ✅ **Tool output truncation** — store full output as reference, insert summary
- ✅ **Pre-flight token check** — estimate before every LLM call
- ✅ **Context pressure signal** — include usage % in prompt so model can self-regulate

## Tool Output Strategy

| Tool Result Size | Strategy |
|---|---|
| < 500 tokens | Keep verbatim in working |
| 500–2000 tokens | Keep verbatim, mark as truncatable |
| 2000–10000 tokens | Extract key facts, store raw as reference |
| > 10000 tokens | Summarize to <500 tokens, store raw externally |

## Related

- Full pattern: [patterns/agent-context-management.md](../patterns/agent-context-management.md)
- Recipe: [COOKBOOK.md#5](../COOKBOOK.md#5-agent-context-budget-tracker)
