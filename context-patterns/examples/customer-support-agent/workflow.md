# Customer Support Agent Workflow

End-to-end flow from user message to resolution, with decision branches for automation vs. escalation.

## Core Message Processing Flow

```mermaid
sequenceDiagram
    actor User
    participant GW as Gateway
    participant NLU as Intent Engine
    participant DM as Dialogue Manager
    participant RAG as RAG Pipeline
    participant LLM as LLM
    participant ACT as Action Service

    User->>GW: Send message (chat/email/api)
    GW->>GW: Authenticate & normalize
    GW->>NLU: Forward parsed message
    NLU->>NLU: Classify intent & extract entities
    NLU->>DM: Intent + entities + raw text

    alt Known intent with KB context needed
        DM->>RAG: Retrieve relevant documents
        RAG->>RAG: Embed query & search
        RAG-->>DM: Top-K document chunks
    end

    DM->>DM: Build context window
    Note over DM: Session history + profile + retrieved chunks

    DM->>LLM: Generate response with context
    LLM-->>DM: Response candidate

    DM->>DM: Policy check & guardrails

    alt Escalation required
        DM->>ACT: Create support ticket
        ACT->>ACT: Route to human agent
        ACT-->>User: "Transferring to agent"
    else Auto-resolve
        DM->>ACT: Update CRM / trigger action
        ACT-->>User: Final response
    end

    DM->>DM: Update session memory
```

## Decision Flow: Auto-resolve vs. Escalate

```mermaid
flowchart TD
    START([User Message]) --> INTENT{Intent Known?}
    INTENT -->|Yes| CONF{Confidence > 0.85?}
    INTENT -->|No| CLARIFY[Ask Clarifying Question]
    CLARIFY --> INTENT

    CONF -->|Yes| RETRIEVE[Retrieve KB Context]
    CONF -->|No| ESCALATE[Escalate to Human]

    RETRIEVE --> RELEVANT{Relevant Results?}
    RELEVANT -->|Yes| GEN[Generate Response]
    RELEVANT -->|No| ESCALATE

    GEN --> SENTIMENT{Positive Sentiment?}
    SENTIMENT -->|Yes| RESOLVE[Mark Resolved]
    SENTIMENT -->|No| ESCALATE

    RESOLVE --> LOG[Log & Update Memory]
    ESCALATE --> TICKET[Create Ticket]
    TICKET --> LOG
```

## Context Window Assembly

```mermaid
flowchart LR
    subgraph Input["Input Sources"]
        MSG["Current Message"]
        HIST["Session History<br/>(last N turns)"]
        PROF["Customer Profile"]
        KB["KB Chunks"]
    end

    subgraph Assembly["Context Assembly"]
        TRIM["Truncate History"]
        PRIORITY["Priority Sort"]
        TEMPLATE["Prompt Template"]
    end

    subgraph Output["Composed Context"]
        SYS["System Instructions"]
        CHAT["Conversation So Far"]
        FACTS["Relevant Facts"]
        QUERY["Current Query"]
    end

    MSG --> Assembly
    HIST --> TRIM --> Assembly
    PROF --> Assembly
    KB --> PRIORITY --> Assembly

    Assembly --> SYS
    Assembly --> CHAT
    Assembly --> FACTS
    Assembly --> QUERY
```

## Resource Allocation by Scenario

| Scenario | History Depth | KB Chunks | Profile Included | LLM Call Type |
|----------|--------------|-----------|-----------------|---------------|
| Simple FAQ | 0-2 turns | 3 chunks | No | Direct generation |
| Troubleshooting | 3-5 turns | 5 chunks | Yes (plan) | Structured response |
| Complaint | Full session | 3 chunks | Yes (full) | Sentiment + generation |
| Account change | 1 turn | 0 chunks | Yes (full) | Tool call |
| Multi-intent | 2 turns | 5 chunks | Yes | Decompose + generate |
