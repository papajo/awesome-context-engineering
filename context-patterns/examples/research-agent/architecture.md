# Research Agent Architecture

An AI research assistant that performs deep investigation across multiple sources, synthesizes findings, and produces structured reports with citations.

## System Architecture

```mermaid
flowchart TB
    subgraph Input["Research Input"]
        Q["Research Question"]
        FOCUS["Focus Areas"]
        DEPTH["Depth Parameter"]
        FORMAT["Output Format"]
    end

    subgraph Orchestrator["Research Orchestrator"]
        DECOMP["Question Decomposition"]
        PLAN["Research Plan Generator"]
        GATHER["Evidence Gathering"]
        ANALYZE["Cross-Source Analysis"]
        SYNTH["Synthesis Engine"]
        CITE["Citation Manager"]
    end

    subgraph Sources["Information Sources"]
        WEB["Web Search / Scrape"]
        DOCS["Document Store"]
        DB["Structured DB"]
        PAPER["Academic Papers (ArXiv)"]
        CODE["Code Repos (GitHub)"]
    end

    subgraph Processing["Processing Pipeline"]
        EXTRACT["Content Extraction"]
        RANK["Relevance Ranking"]
        DEDUP["Deduplication"]
        CONTRA["Contradiction Detection"]
        QUAL["Quality Scoring"]
    end

    subgraph Output["Output Generation"]
        REPORT["Research Report"]
        BRIEF["Executive Brief"]
        MAP["Knowledge Map"]
        CITE_DOC["Citation List"]
    end

    subgraph Memory["Research Memory"]
        VISITED["Visited Sources"]
        NOTES["Extracted Notes"]
        THREAD["Reasoning Threads"]
    end

    Input --> Orchestrator
    Orchestrator --> Sources
    Sources --> Processing
    Processing --> Orchestrator
    Orchestrator <--> Memory
    Orchestrator --> Output

    style Input fill:#e1f5fe
    style Orchestrator fill:#f3e5f5
    style Sources fill:#fff3e0
    style Processing fill:#e8f5e9
    style Output fill:#ffebee
    style Memory fill:#fce4ec
```

## Research Strategy: Breadth vs. Depth

| Strategy | Use Case | Source Coverage | Iterations | Token Budget |
|----------|----------|----------------|------------|-------------|
| **Quick Scan** | Initial landscape overview | 5-10 sources | 1 round | 8K |
| **Focused Deep Dive** | Specific technical question | 3-5 high-quality sources | 2-3 rounds | 32K |
| **Comprehensive Survey** | Literature review / competing analysis | 20-50 sources | 4-6 rounds | 100K+ |
| **Contradiction Hunt** | Finding disagreements in evidence | 10-20 sources | 3-4 rounds | 16K |

## Extensibility

- **Custom source adapters**: Add new information sources via uniform scraper/API interface
- **Output templates**: Extensible template engine for report formats (markdown, PDF, HTML, slides)
- **Quality rules**: Custom quality scoring criteria for domain-specific relevance
