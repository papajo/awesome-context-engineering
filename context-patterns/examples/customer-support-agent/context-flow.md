# Customer Support Agent Context Flow

How context is gathered, merged, prioritized, and evicted throughout a support conversation.

## Context Sources and Lifetimes

```mermaid
flowchart TD
    subgraph Sources["Context Sources"]
        SESS["Session Context<br/>- Conversation history<br/>- Current turn state<br/>- Language preference"]
        PROF["Customer Profile<br/>- Account info<br/>- Plan / tier<br/>- Past issues"]
        KB["Knowledge Base<br/>- FAQ articles<br/>- Troubleshooting guides<br/>- Policy documents"]
        LIVE["Live Signals<br/>- Sentiment drift<br/>- Escalation flags<br/>- Agent availability"]
    end

    subgraph Stage1["Stage 1: Context Gathering"]
        G1["Extract from message"]
        G2["Load session from store"]
        G3["Fetch profile by user_id"]
        G4["Query KB by intent"]
    end

    subgraph Stage2["Stage 2: Context Merging"]
        M1["Deduplicate facts"]
        M2["Resolve contradictions<br/>(profile > session > default)"]
        M3["Calculate token budget"]
    end

    subgraph Stage3["Stage 3: Context Prioritization"]
        P1["System instructions<br/>(always included)"]
        P2["Current query<br/>(always included)"]
        P3["Recent history<br/>(last ~3K tokens)"]
        P4["Relevant KB<br/>(top 3-5 chunks)"]
        P5["Profile summary<br/>(compressed)"]
        P6["Full history<br/>(summarized if needed)"]
    end

    subgraph Stage4["Stage 4: Context Eviction"]
        E1["Drop oldest turns"]
        E2["Summarize stale segments"]
        E3["Archive resolved sub-contexts"]
    end

    SESS --> G2
    PROF --> G3
    KB --> G4
    LIVE --> G1

    G1 --> Stage2
    G2 --> Stage2
    G3 --> Stage2
    G4 --> Stage2

    Stage2 --> Stage3
    Stage3 --> LLM[LLM Call]
    LLM --> Stage4
    Stage4 --> SESS
```

## Context Budget Allocation (token distribution per turn)

```mermaid
pie title Context Window Budget (4K tokens)
    "System Instructions" : 500
    "Customer Profile" : 300
    "Recent History (last 3 turns)" : 1200
    "KB Retrieved Chunks" : 1000
    "Current Query" : 200
    "Scratchpad / Reasoning" : 500
    "Reserved for Response" : 300
```

## Context Freshness Rules

| Context Item | TTL | Refresh Trigger | Eviction Policy |
|---|---|---|---|
| Session history | Per turn | Each new message | Drop oldest at token budget |
| Customer profile | Session-long | Explicit profile update | Carried whole session |
| KB chunks | Per intent | Intent change | Replaced entirely |
| Sentiment score | Per turn | Each response | Overwritten each turn |
| Escalation status | Until resolved | Escalation event | Archived on resolution |

## Failure Modes

| Mode | Symptom | Mitigation |
|------|---------|------------|
| **Context overflow** | Token budget exceeded, truncated response | Implement hierarchical summarization of older turns |
| **Stale profile** | Wrong account context | Check profile timestamp; re-fetch if > 5 min old |
| **KB hallucination** | Retrieved but irrelevant chunks | Add relevance threshold + fallback to clarification |
| **Context bleed** | Data from unrelated conversations | Strict session ID isolation in memory store |

## Example: Context Composition for Escalation

```json
{
  "session_id": "sess_abc123",
  "priority": "high",
  "context_stack": [
    {"source": "system", "tokens": 450},
    {"source": "profile", "summary": "Premium user, 3 previous escalations", "tokens": 200},
    {"source": "history", "turns": 5, "tokens": 1400, "summary": "User unable to cancel subscription via UI"},
    {"source": "kb", "chunks": 2, "tokens": 600, "relevance_scores": [0.92, 0.87]},
    {"source": "live_query", "text": "I want to speak to a supervisor now", "tokens": 30}
  ],
  "total_tokens": 2680,
  "budget_remaining": 1320
}
```
