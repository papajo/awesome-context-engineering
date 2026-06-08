# Context Compression — Cheatsheet

## Concept
Reduce token count before prompt assembly using three complementary stages: structural (lossless), extractive (selection), abstractive (summarization).

## Pipeline

```
Raw Input → Structural → Extractive → Abstractive → Compressed Context
             1.2-2×        2-8×          3-15×          Combined: 5-40×
```

## Stage Details

| Stage | Lossy? | Typical Ratio | Cost |
|---|---|---|---|
| Structural | No | 1.2–2× | Free |
| Extractive | Low | 2–8× | Embedding call |
| Abstractive | Medium | 3–15× | LLM call |
| Combined | Depends | 5–40× | Medium+ |

## Key Code Snippet

```python
def strip_formatting(text: str) -> str:
    """Structural: remove Markdown, collapse whitespace."""
    import re
    text = re.sub(r"```[\s\S]*?```", "[CODE]", text)
    text = re.sub(r'[*_~`#>"]+', " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def extract_top_k(text: str, k: int = 3) -> str:
    """Extractive: keep first K sentences per paragraph."""
    import re
    paragraphs = text.split("\n\n")
    compressed = []
    for p in paragraphs:
        sentences = re.split(r"(?<=[.!?])\s+", p.strip())
        compressed.append(" ".join(sentences[:k]))
    return "\n\n".join(compressed)
```

## When to Use Which

| Content Type | Recommended Stage | Reason |
|---|---|---|
| Logs | Structural only | Mostly formatting waste |
| Web pages | Extractive → Abstractive | High noise, low signal density |
| Research papers | Abstractive only | Need condensation, not selection |
| API docs | Extractive only | Exact phrasing matters for params/endpoints |
| Tool outputs | Structural + Extractive | Mixed boilerplate + unique content |

## Budget-Aware Strategy

```python
def compress_to_budget(text: str, budget_chars: int) -> str:
    """Compress iteratively until under budget."""
    if len(text) <= budget_chars:
        return text
    text = strip_formatting(text)          # stage 1
    if len(text) <= budget_chars:
        return text
    text = extract_top_k(text, 3)          # stage 2
    if len(text) <= budget_chars:
        return text
    return abstractive_summary(text, budget_chars)  # stage 3
```

## Common Pitfalls

- ❌ **Over-compression** → model misses specific numbers, names, versions
- ❌ **Same ratio for all content** → JSON needs different treatment than prose
- ❌ **No caching** → re-compressing the same document for every query
- ✅ **Preserve critical fields** (versions, endpoints, error codes)
- ✅ **Cache by (source_hash + target_budget)**
- ✅ **Quality gate** — verify compressed output still contains named entities
- ✅ **Tier by content type** — different strategies per source

## Related

- Full pattern: [patterns/context-compression.md](../patterns/context-compression.md)
- Recipe: [COOKBOOK.md#2](../COOKBOOK.md#2-context-compression-pipeline)
