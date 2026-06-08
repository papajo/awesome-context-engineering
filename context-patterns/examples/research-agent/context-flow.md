# Research Agent Context Flow

Context management across a multi-turn, multi-source research session.

## Research Context Architecture

```mermaid
flowchart TD
    subgraph Phase1["Phase 1: Question Context"]
        Q["Research Question"]
        SCOPE["Scope Boundaries"]
        BIAS["Known Biases & Positions"]
        METADATA["User Metadata (expertise level)"]
    end

    subgraph Phase2["Phase 2: Discovery Context"]
        SOURCES["Source Credibility Scores"]
        VISITED["Visited URLs"]
        QUERIES["Search Query History"]
        SUB_Q["Sub-Question Status"]
    end

    subgraph Phase3["Phase 3: Evidence Context"]
        EXTRACTS["Extracted Passages"]
        RANKING["Relevance Rankings"]
        CONTRA["Contradiction Log"]
        CONF["Confidence Scores"]
    end

    subgraph Phase4["Phase 4: Synthesis Context"]
        TEMPLATE["Output Template"]
        CITING["Citation Graph"]
        DRAFT["Draft Sections"]
        GAPS["Unresolved Gaps"]
    end

    Phase1 --> Phase2
    Phase2 --> Phase3
    Phase3 --> Phase4

    style Phase1 fill:#e1f5fe
    style Phase2 fill:#fff3e0
    style Phase3 fill:#e8f5e9
    style Phase4 fill:#f3e5f5
```

## Context Budget by Phase

```mermaid
flowchart LR
    subgraph Budget["Token Budget Allocation (32K total)"]
        SYS["System & Instructions: 1K"]
        PHASE1["Question Context: 2K"]
        PHASE2["Discovery Context: 3K"]
        PHASE3["Active Evidence: 12K"]
        PHASE4["Working Synthesis: 8K"]
        HISTORY["Session History: 4K"]
        OUTPUT["Response Buffer: 2K"]
    end
```

## Evidence Chunk Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Raw: Source discovered
    Raw --> Extracted: Content parsed
    Extracted --> Scored: Relevance scored
    Scored --> Selected: Above threshold (≥0.7)
    Scored --> Rejected: Below threshold
    Selected --> Contextualized: Placed in research context
    Contextualized --> CrossReferenced: Compared with other evidence
    CrossReferenced --> Cited: Included in output
    CrossReferenced --> Contradicted: Conflict with stronger evidence
    Contradicted --> Flagged: Flagged for user review
    Cited --> [*]
    Flagged --> [*]
```

## Context Hierarchy by Research Stage

| Stage | Active Context | Token Weight | Eviction Policy |
|-------|---------------|-------------|-----------------|
| Decomposition | Question + Scope | Light (1K) | Static for session |
| First pass discovery | Query history + visited URLs | Medium (3K) | Evict low-relevance queries |
| Deep evidence extraction | Active evidence chunks | Heavy (12K) | Rank → keep top-K per sub-question |
| Cross-analysis | Comparison matrices | Heavy (10K) | Merge duplicate findings |
| Synthesis | Draft + citations | Medium (8K) | Keep until output delivered |

## Failure Modes

| Mode | Symptom | Mitigation |
|------|---------|------------|
| **Source saturation** | Same article cited by multiple paths | Dedup by canonical URL + content hash |
| **Context drift** | Agent forgets original question | Pin question to system prompt; re-anchor after each N iterations |
| **Citation hallucination** | Cites plausible-sounding but false sources | Source verification step: require direct quote extraction |
| **Recency bias** | Overweighs most recently retrieved content | Explicit position bias correction in aggregation |

## Example Research Context State

```json
{
  "research_id": "res_mcp_fc_01",
  "question": "How does MCP compare to OpenAI Function Calling?",
  "sub_questions": [
    {"id": "sq1", "question": "Protocol design differences", "status": "completed", "sources": 4},
    {"id": "sq2", "question": "Tool discovery mechanisms", "status": "completed", "sources": 3},
    {"id": "sq3", "question": "Performance benchmarks", "status": "in_progress", "sources": 2},
    {"id": "sq4", "question": "Production adoption", "status": "pending", "sources": 0}
  ],
  "active_evidence": {
    "total_chunks": 45,
    "selected": 18,
    "rejected": 27,
    "contradictions": [
      {
        "claim": "MCP is faster than FC",
        "sources": ["blog_a", "paper_x"],
        "confidence": 0.6
      }
    ]
  },
  "tokens_used": 14500,
  "budget_remaining": 17500
}
```
