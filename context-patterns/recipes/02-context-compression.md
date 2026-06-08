# Context Compression Pipeline

**Problem:** Raw documents, logs, and tool outputs consume too many tokens. Compress them before prompt assembly.

**Pattern:** [Context Compression](../patterns/context-compression.md)

```python
import re
import json
from typing import Callable

class CompressionPipeline:
    """Multi-stage context compression: structural → extractive → abstractive."""

    def __init__(self):
        self.stages: list[Callable[[str], str]] = []

    def add_stage(self, name: str, fn: Callable[[str], str]) -> None:
        self.stages.append((name, fn))

    def compress(self, text: str, verbose: bool = False) -> str:
        result = text
        for name, fn in self.stages:
            before = len(result)
            result = fn(result)
            after = len(result)
            if verbose:
                ratio = before / after if after > 0 else float("inf")
                print(f"  [{name}] {before}→{after} chars ({ratio:.1f}x)")
        return result


def strip_formatting(text: str) -> str:
    """Structural: remove Markdown, collapse whitespace."""
    text = re.sub(r"```[\s\S]*?```", "[CODE]", text)
    text = re.sub(r'[*_~`#>"]+', " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def minify_json(text: str) -> str:
    """Minify JSON blocks while preserving structure."""
    def _minify(match: re.Match) -> str:
        try:
            obj = json.loads(match.group())
            return json.dumps(obj, separators=(",", ":"))
        except json.JSONDecodeError:
            return match.group()
    return re.sub(r"\{[^{}]*\}", _minify, text)


def extract_top_k(text: str, k: int = 3) -> str:
    """Extractive: keep only first K sentences per paragraph."""
    paragraphs = text.split("\n\n")
    compressed = []
    for p in paragraphs:
        sentences = re.split(r"(?<=[.!?])\s+", p.strip())
        compressed.append(" ".join(sentences[:k]))
    return "\n\n".join(compressed)


def abstractive_summary(text: str, max_chars: int = 1000) -> str:
    """Abstractive: placeholder for LLM call. Keeps heading + first sentence per section."""
    sections = re.split(r"(?=^#{1,3}\s)", text, flags=re.MULTILINE)
    result = []
    for sec in sections:
        lines = [l.strip() for l in sec.split("\n") if l.strip()]
        if lines:
            result.extend(lines[:2])
    return "\n".join(result)[:max_chars]


if __name__ == "__main__":
    sample = """
# API Documentation

## Authentication

The API uses OAuth 2.0 for authentication. You must obtain a bearer token before making requests.

## Rate Limiting

Rate limiting is applied per API key: 1000 requests per hour for free, 10000 for pro.

## Endpoints

### GET /users
Returns a list of registered users. Supports pagination via `?page=` and `?limit=`.
"""

    pipeline = CompressionPipeline()
    pipeline.add_stage("structural", strip_formatting)
    pipeline.add_stage("minify", minify_json)
    pipeline.add_stage("extractive (top-2)", lambda t: extract_top_k(t, k=2))
    pipeline.add_stage("abstractive", lambda t: abstractive_summary(t, 500))

    result = pipeline.compress(sample, verbose=True)
    print(f"\n=== COMPRESSED ({len(result)} chars) ===")
    print(result)
```

## Key Takeaways

- **Structural** (lossless): strip formatting, collapse whitespace — typically 1.5–2× reduction
- **Extractive** (lossy): keep top-K sentences per paragraph — 2–5× reduction
- **Abstractive** (lossy): summarize with LLM — 5–20× reduction
- Compose stages: structural first (cheap), extractive next, abstractive last (expensive)

## Production Notes

- Replace the abstractive placeholder with a real LLM call (use a cheap model like Haiku or Mini)
- Measure compression ratio vs. downstream task quality to find your sweet spot
- Cache compressed versions of static documents
- For structured data (JSON, logs), use targeted templates instead of generic compression

## Related

- [Decision Guide: which pattern?](../DECISION-GUIDE.md)
- [Cheatsheet: Compression](../cheatsheets/context-compression.md)
