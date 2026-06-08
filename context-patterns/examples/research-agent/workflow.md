# Research Agent Workflow

Systematic investigation process from question to synthesized report.

## Core Research Loop

```mermaid
sequenceDiagram
    actor User
    participant Plan as Research Planner
    participant Gather as Evidence Gatherer
    participant Anal as Analysis Engine
    participant Mem as Research Memory
    participant Synth as Synthesis Engine

    User->>Plan: "Research: How does MCP compare to Function Calling?"
    Plan->>Plan: Decompose into sub-questions
    Plan-->>User: Proposed research plan (4 sub-questions, 3 sources each)

    User-->>Plan: Execute plan

    loop For each sub-question
        Gather->>Gather: Query sources (web, papers, docs)
        Gather->>Gather: Extract & chunk content
        Gather->>Anal: Raw evidence chunks
        Anal->>Anal: Score relevance & quality
        Anal->>Anal: Check for contradictions
        Anal->>Mem: Store processed evidence
    end

    loop Deepen if needed
        Anal->>Anal: Identify knowledge gaps
        Anal->>Gather: Targeted follow-up queries
        Gather->>Anal: Additional evidence
    end

    Anal->>Synth: All evidence packages
    Synth->>Synth: Cross-reference & merge
    Synth->>Synth: Generate structured report
    Synth->>Synth: Build citation graph
    Synth-->>User: Research report with 12 citations

    alt User requests deeper investigation
        User->>Plan: Drill into section 3
        Plan->>Gather: Refine query
        Gather->>Anal: Additional sources
        Anal->>Synth: Updated analysis
        Synth-->>User: Revised report
    end
```

## Question Decomposition Strategy

```mermaid
flowchart TD
    Q["How does MCP compare to Function Calling?"] --> D1["What is MCP's protocol design?"]
    Q --> D2["What is Function Calling's architecture?"]
    Q --> D3["How do they handle tool discovery?"]
    Q --> D4["What are performance/scaling differences?"]
    Q --> D5["What do production users report?"]

    D1 --> S1_1["Source: MCP Specification"]
    D1 --> S1_2["Source: Anthropic Blog"]
    D1 --> S1_3["Source: MCP GitHub Repo"]

    D2 --> S2_1["Source: OpenAI API Docs"]
    D2 --> S2_2["Source: Comparison articles"]
    D2 --> S2_3["Source: Technical analysis"]

    D3 --> S3_1["Source: MCP vs FC analyses"]
    D4 --> S4_1["Source: Benchmarks"]
    D5 --> S5_1["Source: Community discussions"]
```

## Quality Scoring Heuristics

| Signal | Weight | Description |
|--------|--------|-------------|
| Source authority | 0.30 | Official docs > peer-reviewed > blog > forum |
| Recency | 0.20 | < 6 months = 1.0, 6-12 mo = 0.7, > 12 mo = 0.4 |
| Relevance | 0.25 | Semantic similarity to research question |
| Fact density | 0.15 | Ratio of claims to total word count |
| Contradiction score | 0.10 | Agreement across multiple sources |

## Iteration Termination Criteria

| Condition | Action |
|-----------|--------|
| All sub-questions have ≥ 3 high-quality sources | Move to synthesis |
| No new evidence after 2 rounds of targeted queries | Accept current evidence and flag gaps |
| Contradiction detected without resolution | Flag contradiction in report |
| Token budget reached | Summarize remaining gaps for extension |
