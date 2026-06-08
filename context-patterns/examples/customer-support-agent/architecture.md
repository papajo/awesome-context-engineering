# Customer Support Agent Architecture

A context-rich multi-channel customer support system that uses LLMs with RAG, session memory, and escalation orchestration.

## System Architecture

```mermaid
flowchart TB
    subgraph Channels["User Channels"]
        WEB["Web Chat"]
        EMAIL["Email"]
        MOBILE["Mobile App"]
        API["API / Webhook"]
    end

    subgraph Gateway["Ingress Gateway"]
        LB["Load Balancer"]
        AUTH["Auth & Rate Limit"]
        ROUTE["Message Router"]
    end

    subgraph Orchestrator["Conversation Orchestrator"]
        NLU["Intent & Entity Extraction"]
        DM["Dialogue Manager"]
        POL["Policy Engine"]
        MEM["Session Memory Store"]
    end

    subgraph Context["Context & Knowledge"]
        RAG["RAG Pipeline"]
        KB["Knowledge Base"]
        PROF["Customer Profile DB"]
        HIST["Interaction History"]
    end

    subgraph Actions["Action Layer"]
        TICKET["Ticket System"]
        CRM["CRM Update"]
        ESCALATE["Human Escalation"]
        NOTIFY["Notification Service"]
    end

    subgraph LLM["LLM Inference"]
        COMPL["Response Generation"]
        SUMM["Summarization"]
        SENT["Sentiment Analysis"]
    end

    Channels --> Gateway
    Gateway --> Orchestrator
    Orchestrator <--> Context
    Orchestrator --> LLM
    LLM --> Orchestrator
    Orchestrator --> Actions
    MEM <--> Orchestrator

    style Channels fill:#e1f5fe
    style Gateway fill:#fff3e0
    style Orchestrator fill:#f3e5f5
    style Context fill:#e8f5e9
    style Actions fill:#ffebee
    style LLM fill:#e0f7fa
```

## Component Responsibilities

| Component | Responsibility |
|-----------|----------------|
| **Ingress Gateway** | Authentication, rate limiting, message normalization across channels |
| **NLU Engine** | Intent classification, entity extraction, language detection |
| **Dialogue Manager** | Turn tracking, response policy, escalation triggers |
| **Session Memory** | Sliding-window conversation history with summarization |
| **RAG Pipeline** | Retrieval-augmented generation from knowledge base |
| **Policy Engine** | Business rules for routing, escalation, and fallback |

## Design Decisions

- **Stateless gateway + stateful orchestrator**: Gateway scales horizontally; orchestrator maintains session affinity via session ID
- **Separate memory store**: Enables hot-swapping memory strategies (sliding window → summarization → hybrid) without touching other components
- **RAG as plugin**: Knowledge base is swappable (FAISS, Pinecone, pgvector) via adapter interface
- **Async escalation**: Human handoff uses a message queue — agent never blocks on ticket creation

## Extensibility

- Add new channel via Gateway adapter
- Add new LLM provider via model abstraction layer
- Add new knowledge source via RAG connector interface
- Custom escalation policies via Policy Engine rules DSL
