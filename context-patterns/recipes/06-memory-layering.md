# Memory Layering with Consolidation

**Problem:** A single memory store conflates working context, episodic experiences, semantic knowledge, and procedural skills. Use separate tiers with different retention and access patterns.

**Pattern:** [Memory Layering](../patterns/memory-layering.md)

```python
import time
import json
from collections import deque
from dataclasses import dataclass, field


@dataclass
class EpisodicMemory:
    """What happened: chronological experience traces."""
    events: list[dict] = field(default_factory=list)
    max_events: int = 100

    def record(self, event_type: str, description: str, metadata: dict | None = None) -> None:
        self.events.append({
            "type": event_type,
            "description": description,
            "metadata": metadata or {},
            "timestamp": time.time(),
        })
        if len(self.events) > self.max_events:
            self.events.pop(0)

    def recall(self, query: str, limit: int = 5) -> list[dict]:
        q = query.lower()
        matches = [e for e in self.events if q in e["description"].lower()]
        return matches[-limit:]


@dataclass
class SemanticMemory:
    """What I know: consolidated knowledge, facts, concepts."""
    facts: dict[str, dict] = field(default_factory=dict)

    def store(self, key: str, fact: dict) -> None:
        self.facts[key] = {**fact, "updated_at": time.time()}

    def retrieve(self, key: str) -> dict | None:
        return self.facts.get(key)

    def search(self, query: str) -> list[tuple[str, dict]]:
        q = query.lower()
        return [(k, v) for k, v in self.facts.items() if q in k.lower() or q in json.dumps(v).lower()]


@dataclass
class ProceduralMemory:
    """How I do things: skills, recipes, action sequences."""
    skills: dict[str, list[str]] = field(default_factory=dict)

    def teach(self, skill_name: str, steps: list[str]) -> None:
        self.skills[skill_name] = steps

    def recall(self, skill_name: str) -> list[str] | None:
        return self.skills.get(skill_name)


class LayeredMemory:
    """Four-tier cognitive memory architecture.

    Layers:
    1. Working — current conversation (volatile, stored externally)
    2. Episodic — chronological experience traces
    3. Semantic — consolidated facts and knowledge
    4. Procedural — skills and action sequences
    """

    def __init__(self):
        self.working: deque = deque(maxlen=20)
        self.episodic = EpisodicMemory()
        self.semantic = SemanticMemory()
        self.procedural = ProceduralMemory()
        self._consolidation_count = 0

    def add_interaction(self, role: str, content: str) -> None:
        self.working.append({"role": role, "content": content, "timestamp": time.time()})
        self.episodic.record(f"{role}_message", content[:200])

    def consolidate(self) -> None:
        """Extract semantic facts from recent episodic memory."""
        if len(self.episodic.events) < 5:
            return
        recent = self.episodic.events[-5:]
        for event in recent:
            desc = event["description"].lower()
            if " is " in desc:
                parts = desc.split(" is ", 1)
                key = parts[0].strip().replace("the ", "").replace("a ", "")
                value = parts[1].strip().rstrip(".")
                if len(key) > 2 and len(value) > 2:
                    existing = self.semantic.retrieve(key)
                    if existing:
                        existing["value"] = value
                        existing["confidence"] = min(existing.get("confidence", 0.5) + 0.1, 1.0)
                        existing["consolidations"] = existing.get("consolidations", 1) + 1
                    else:
                        self.semantic.store(key, {
                            "value": value,
                            "confidence": 0.5,
                            "consolidations": 1,
                            "source_events": [event["description"]],
                        })
        self._consolidation_count += 1

    def search_all(self, query: str) -> dict:
        return {
            "episodic": self.episodic.recall(query, limit=3),
            "semantic": self.semantic.search(query),
            "procedural": [(k, v) for k, v in self.procedural.skills.items() if query.lower() in k.lower()],
        }

    def get_working_summary(self) -> str:
        return "\n".join(f"{m['role']}: {m['content']}" for m in list(self.working)[-5:])


if __name__ == "__main__":
    mem = LayeredMemory()
    mem.add_interaction("user", "How do I configure the database connection in my FastAPI app?")
    mem.add_interaction("assistant", "Use SQLAlchemy async with a DATABASE_URL environment variable.")
    mem.add_interaction("user", "Should I use Alembic for migrations?")
    mem.add_interaction("assistant", "Yes, Alembic is the standard migration tool for SQLAlchemy.")
    mem.add_interaction("user", "How do I handle database migrations in production?")
    mem.add_interaction("assistant", "Use Alembic with one migration per change, run as release step.")
    mem.consolidate()
    mem.procedural.teach("database_setup", [
        "Install SQLAlchemy and asyncpg",
        "Set DATABASE_URL environment variable",
        "Create SQLAlchemy async engine",
        "Set up Alembic with `alembic init`",
        "Run migrations as part of deployment",
    ])
    print("=== WORKING MEMORY ===")
    print(mem.get_working_summary())
    print("\n=== SEMANTIC FACTS ===")
    for k, v in mem.semantic.facts.items():
        print(f"  {k}: {v['value']} (confidence: {v['confidence']:.1f})")
    print("\n=== SEARCH 'alembic' ===")
    results = mem.search_all("alembic")
    print(f"  Episodic: {len(results['episodic'])} matches")
    print(f"  Semantic: {len(results['semantic'])} matches")
    print(f"  Procedural: {len(results['procedural'])} matches")
```

## Key Takeaways

- **Working**: volatile, current conversation only (deque, max 20)
- **Episodic**: chronological trace, capped at 100 events
- **Semantic**: consolidated facts extracted via "X is Y" pattern, confidence-weighted
- **Procedural**: explicit skills with step-by-step instructions
- **Consolidation**: episodic → semantic runs periodically (here every 5 interactions)

## Production Notes

- Replace the "X is Y" heuristic with an LLM-based fact extractor
- Add embedding-based retrieval for semantic memory (vector DB)
- Implement forgetting: decay semantic confidence over time without reinforcement
- Add hierarchical procedural skills (sub-skills, prerequisites)

## Related

- [Decision Guide: which pattern?](../DECISION-GUIDE.md)
