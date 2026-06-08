# RAG System Workflow

End-to-end document processing and query-answering pipeline.

## Document Ingestion Flow

```mermaid
sequenceDiagram
    participant User
    participant Load as Doc Loader
    participant Chunk as Chunker
    participant Embed as Embedding Service
    participant Index as Vector Index

    User->>Load: Upload 100 documentation PDFs
    Load->>Load: Detect format, extract text & metadata
    Load-->>Chunk: Parsed documents with metadata

    loop For each document
        Chunk->>Chunk: Apply chunking strategy
        alt Semantic chunking
            Chunk->>Chunk: Split at sentence boundaries, min 50 tokens
        else Recursive
            Chunk->>Chunk: Split at 512 tokens, 10% overlap
        end
        Chunk-->>Embed: Text chunks
        Embed->>Embed: Generate embeddings
        Embed-->>Index: Chunk + embedding + metadata
        Index->>Index: Store with metadata filters
    end

    Index-->>User: Indexed 2,847 chunks from 100 docs
    Note over User,Index: Ingestion complete. Ready for queries.
```

## Query Processing Flow

```mermaid
sequenceDiagram
    actor User
    participant QProc as Query Processor
    participant Search as Search Engine
    participant Rerank as Reranker
    participant Fuse as Fusion Engine
    participant LLM as LLM
    participant Check as Quality Checker

    User->>QProc: "How do I configure Prometheus for high availability?"
    QProc->>QProc: Rewrite query (2 variants)
    QProc->>QProc: Generate HyDE document
    QProc-->>Search: 3 query variants + HyDE doc

    par Dense Search
        Search->>Search: Vector similarity search
    and Sparse Search
        Search->>Search: BM25 keyword search
    end

    Search-->>Rerank: Top-20 from each strategy
    Rerank->>Rerank: Cross-encoder reranking
    Rerank-->>Fuse: Top-10 reranked results

    Fuse->>Fuse: Apply fusion strategy
    Fuse->>Fuse: Filter by metadata (recency)
    Fuse->>Fuse: Select diverse cover
    Fuse-->>LLM: 5 selected chunks with citations

    LLM->>LLM: Generate answer with chunk context
    LLM-->>Check: Response + citations

    Check->>Check: Faithfulness check
    Check->>Check: Citation verification

    alt All checks pass
        Check-->>User: Answer with citations
    else Hallucination detected
        Check->>User: Answer with warning
        Check->>User: Re-verify suggested
    end
```

## Fusion Strategy Decision

```mermaid
flowchart TD
    Q[Query + Chunks] --> DIVERSITY{Chunk Diversity?}
    DIVERSITY -->|High overlap| CONCAT[Simple Concatenation
Rank by relevance]
    DIVERSITY -->|Complementary| MAP[MAP-REDUCE
Process each chunk
independently then merge]
    DIVERSITY -->|Contradictory| DEBATE[MULTI-LLM DEBATE
Generate answers per chunk
cross-validate]

    CONCAT --> TOKEN_LIMIT{Token Budget?}
    TOKEN_LIMIT -->|Under limit| DIRECT[Direct prompt]
    TOKEN_LIMIT -->|Exceeded| SUMMARIZE[Summarize each
chunk first]
```

## Quality Check Gates

| Check | Method | Threshold | Action on Failure |
|-------|--------|-----------|------------------|
| **Faithfulness** | Claim extraction → verify against chunks | < 30% unverified claims | Return with warning |
| **Citation accuracy** | Citation → match chunk source | Exact source match | Remove unverified citations |
| **Answer relevance** | Embedding similarity to query | > 0.7 | Generate more focused answer |
| **Token efficiency** | Response tokens / retrieved tokens | < 50% wastage | Hint to optimize retrieval |
| **Safety check** | Toxicity/safety classifier | < 0.1 | Block response |
