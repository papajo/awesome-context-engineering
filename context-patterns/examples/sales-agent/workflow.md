# Sales Agent Workflow

End-to-end lead-to-meeting pipeline with AI-driven outreach and human-in-the-loop gates.

## Lead Engagement Flow

```mermaid
sequenceDiagram
    actor SDR as Sales Rep
    participant Agent as Sales Agent
    participant CRM as CRM System
    participant Intel as Intelligence Engine
    participant Prospect

    SDR->>Agent: Set campaign: "Q3 Enterprise Outreach"
    Agent->>CRM: Fetch leads matching ICP
    CRM-->>Agent: 250 leads

    loop Batch process (50 leads)
        Agent->>Intel: Enrich lead data
        Intel-->>Agent: Tech stack, recent news, decision makers
        Agent->>Agent: Score & segment each lead
        Agent->>Agent: Generate personalized message
    end

    Agent-->>SDR: Campaign preview (50 leads, 3 segments)
    SDR-->>Agent: Approve segment A & B

    par Email outreach
        Agent->>Prospect: Personalized email (Segment A)
    and LinkedIn outreach
        Agent->>Prospect: Connection request + note (Segment B)
    end

    alt Prospect replies
        Prospect->>Agent: "Interested, tell me more"
        Agent->>Agent: Classify intent (positive)
        Agent->>Prospect: Follow-up with case study
        Agent->>Agent: Update lead score +20
    else Prospect ignores
        Agent->>Agent: Schedule reminder (Day 3)
        Agent->>Prospect: Follow-up #1
    end

    alt Positive engagement
        Prospect->>Agent: "Let's schedule a call"
        Agent->>CRM: Create meeting slot
        Agent->>Prospect: Calendar invite
        Agent-->>SDR: Meeting booked!
    else Objection raised
        Prospect->>Agent: "Not now, budget frozen"
        Agent->>Agent: Classify objection (budget)
        Agent->>Agent: Queue for next quarter nurture
    end
```

## Lead Scoring Model

```mermaid
flowchart LR
    subgraph Signals["Scoring Signals"]
        FIT["Fit Score
- ICP match: 0-30
- Company size: 0-10
- Industry: 0-10
- Tech stack: 0-10"]
        ENGAGE["Engagement Score
- Email opens: 0-15
- Link clicks: 0-15
- Replies: 0-20
- Meeting: 0-30"]
        INTENT["Intent Score
- Job change: 0-10
- Funding: 0-15
- Hiring: 0-10
- Competitor usage: 0-15"]
    end

    FIT --> TOTAL{Total Score
0-100}
    ENGAGE --> TOTAL
    INTENT --> TOTAL

    TOTAL --> TIER{Lead Tier}
    TIER -->|80-100| HOT[Hot: Immediate contact]
    TIER -->|60-79| WARM[Warm: Sequence start]
    TIER -->|40-59| COOL[Cool: Nurture track]
    TIER -->|0-39| COLD[Cold: Long-term nurture]
```

## Outreach Cadence

```mermaid
gantt
    title Outreach Sequence
    dateFormat  D
    axisFormat  %a

    section Email
    Email 1 (Intro)          :a1, 0, 1d
    Email 2 (Value Prop)      :a2, after a1, 1d
    Email 3 (Case Study)      :a3, after a2, 1d
    Email 4 (Breakup)         :a4, after a3, 1d

    section Social
    LinkedIn Request          :b1, 0, 1d
    LinkedIn Follow-up        :b2, after b1, 2d

    section Phone
    Call Attempt 1            :c1, after a2, 1d
    Call Attempt 2            :c2, after a3, 1d
```

## Decision Gates

| Gate | Condition | Action |
|------|-----------|--------|
| Reply received | Any positive signal | Switch to conversational mode |
| Bounce detected | Email hard bounce | Remove from list, flag CRM |
| Unsubscribe | Opt-out event | Remove immediately, suppress forever |
| Meeting booked | Calendar event created | Transfer to SDR queue, pause outreach |
| Negative sentiment | Angry/negative reply | Flag for human review, pause sequence |
