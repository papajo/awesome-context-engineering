# Agent Context Budget Tracker

**Problem:** Autonomous agents accumulate tool call traces, reasoning steps, and outputs that exceed context limits. Track budget and auto-archive before overflow.

**Pattern:** [Agent Context Management](../patterns/agent-context-management.md)

```python
import time
from dataclasses import dataclass, field


@dataclass
class ContextEvent:
    event_type: str  # "thought", "tool_call", "tool_result", "observation", "message"
    content: str
    token_estimate: int = 0
    timestamp: float = field(default_factory=time.time)


class AgentContextManager:
    """Three-tier agent context: core + working + archive."""

    def __init__(self, max_tokens: int = 8000, safety_margin: float = 0.85):
        self.max_tokens = max_tokens
        self.safety_margin = safety_margin
        self.max_working_tokens = int(max_tokens * safety_margin)
        self.core: list[ContextEvent] = []
        self.working: list[ContextEvent] = []
        self.archive: list[dict] = []
        self.summaries: list[str] = []

    def set_core(self, system_prompt: str, tools: list[str]) -> None:
        self.core = [
            ContextEvent("system", system_prompt, token_estimate=len(system_prompt) // 4),
            ContextEvent("tools", "\n".join(tools), token_estimate=sum(len(t) for t in tools) // 4),
        ]

    def add_event(self, event_type: str, content: str) -> None:
        tokens = len(content) // 4
        event = ContextEvent(event_type, content, token_estimate=tokens)
        self.working.append(event)
        self._check_budget()

    def _current_usage(self) -> int:
        core_tokens = sum(e.token_estimate for e in self.core)
        working_tokens = sum(e.token_estimate for e in self.working)
        summary_tokens = sum(len(s) for s in self.summaries) // 4
        return core_tokens + working_tokens + summary_tokens

    def _check_budget(self) -> None:
        if self._current_usage() > self.max_working_tokens:
            self._archive_oldest()

    def _archive_oldest(self) -> None:
        if len(self.working) < 3:
            return
        cutoff = max(1, len(self.working) // 3)
        batch = self.working[:cutoff]
        content_lines = [f"[{e.event_type}] {e.content[:100]}" for e in batch]
        summary = f"[Archived {cutoff} events: {'; '.join(content_lines[:3])}...]"
        self.summaries.append(summary)
        self.archive.append({"events": batch, "summary": summary, "count": cutoff})
        self.working = self.working[cutoff:]

    def get_context(self) -> dict:
        return {
            "usage": {
                "current": self._current_usage(),
                "max": self.max_tokens,
                "pct": round(self._current_usage() / self.max_tokens * 100, 1),
            },
            "core": [{"type": e.event_type, "content": e.content} for e in self.core],
            "working": [{"type": e.event_type, "content": e.content} for e in self.working],
            "summaries": self.summaries,
            "archived_events": sum(a["count"] for a in self.archive),
        }

    def format_prompt(self) -> str:
        parts = []
        for e in self.core:
            parts.append(f"<{e.event_type}>\n{e.content}\n</{e.event_type}>")
        if self.summaries:
            parts.append("<context_history>\n" + "\n".join(self.summaries) + "\n</context_history>")
        if self.working:
            steps = [f"[{e.event_type}] {e.content}" for e in self.working]
            parts.append("<recent_steps>\n" + "\n".join(steps) + "\n</recent_steps>")
        budget_pct = round(self._current_usage() / self.max_tokens * 100, 1)
        parts.append(f"<context_usage>{budget_pct}% of {self.max_tokens} tokens used</context_usage>")
        return "\n\n".join(parts)


if __name__ == "__main__":
    mgr = AgentContextManager(max_tokens=500)
    mgr.set_core(
        "You are a helpful coding assistant.",
        ["search_web(query)", "read_file(path)", "write_file(path, content)"],
    )
    for i in range(15):
        mgr.add_event("thought", f"Step {i}: find the auth module and check configuration.")
        mgr.add_event("tool_call", f"search_web('auth module config')")
        mgr.add_event("tool_result", f"Found auth at /src/auth/config.yaml")

    ctx = mgr.get_context()
    print("=== CONTEXT USAGE ===")
    print(f"  {ctx['usage']['pct']}% of {ctx['usage']['max']} tokens used")
    print(f"  Working events: {len(ctx['working'])}")
    print(f"  Archived events: {ctx['archived_events']}")
    print(f"  Summaries: {len(ctx['summaries'])}")
    print("\n=== PROMPT PREVIEW (first 500 chars) ===")
    prompt = mgr.format_prompt()
    print(prompt[:500] + "..." if len(prompt) > 500 else prompt)
```

## Key Takeaways

- **Core**: system prompt + tools, never evicted
- **Working**: recent steps, auto-archived when budget exceeds 85%
- **Archive**: summaries of oldest 30% of events preserved for context
- **Prompt format**: XML tags for core, history, and recent sections

## Production Notes

- Add fine-grained token counting (tiktoken, cl100k_base)
- Replace the placeholder summary with an LLM-generated one
- Add "pinned" events that never get archived (e.g., user goals)
- Log archive operations for debugging agent behavior

## Related

- [Decision Guide: which pattern?](../DECISION-GUIDE.md)
- [Cheatsheet: Agent Context Management](../cheatsheets/agent-context-management.md)
