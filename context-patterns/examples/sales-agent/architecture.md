# Sales Agent Architecture

An AI outbound/inbound sales agent that manages leads, personalizes outreach, and orchestrates multi-channel campaigns.

## System Architecture

```mermaid
flowchart TB
    subgraph Inputs["Sales Inputs"]
        LEAD["Lead Sources
- Website forms
- LinkedIn
- CRM imports
- Events"]
        TARGET["Targeting Criteria
- ICP definition
- Industry filters
- Company size
- Budget range"]
    end

    subgraph Orchestrator["Sales Orchestrator"]
        LEAD_SCORE["Lead Scoring Engine"]
        SEGMENT["Segmentation
- Industry / role
- Intent signals
- Stage in funnel"]
        PERSONAL["Personalization Engine
- Company research
- Prospect insights
- Pain point detection"]
        SEQ["Sequence Manager
- Timing optimization
- Channel mix
- A/B testing"]
    end

    subgraph Outreach["Multi-Channel Outreach"]
        EMAIL["Email Campaigns"]
        LI["LinkedIn DM"]
        CALL["Call Scripts"]
        WEBINAR["Webinar Invites"]
    end

    subgraph Intelligence["Sales Intelligence"]
        WEB_RESEARCH["Company Research
- Tech stack detection
- News monitoring
- Funding events"]
        CONTACT_RICH["Contact Enrichment"]
        SENTIMENT["Prospect Sentiment"]
        COMP_INTEL["Competitive Intel"]
    end

    subgraph Response["Response Handling"]
        INBOX["Unified Inbox"]
        REPLY["Reply Gen
- Objection handling
- FAQ answering
- Meeting booking"]
        FOLLOW["Follow-up Scheduler"]
    end

    subgraph Analytics["Analytics & Reporting"]
        PIPELINE["Pipeline Dashboard"]
        CONVERSION["Conversion Metrics"]
        ATTRIBUTION["Channel Attribution"]
        FORECAST["Forecasting"]
    end

    Inputs --> Orchestrator
    Orchestrator --> Outreach
    Orchestrator <--> Intelligence
    Outreach --> Response
    Response --> Orchestrator
    Orchestrator --> Analytics

    style Inputs fill:#e1f5fe
    style Orchestrator fill:#f3e5f5
    style Outreach fill:#fff3e0
    style Intelligence fill:#e8f5e9
    style Response fill:#ffebee
    style Analytics fill:#fce4ec
```

## Funnel Stages

| Stage | Activity | AI Role | Human Role |
|-------|----------|---------|------------|
| **Prospecting** | Lead identification & enrichment | Automated research & scoring | Define ICP |
| **Outreach** | First contact | Personalized message generation | Approve templates |
| **Nurturing** | Follow-ups & engagement | Sequence management, reply handling | Strategic intervention |
| **Qualification** | BANT/GPCT assessment | Automated qualification conversation | Review qualification |
| **Proposal** | Quote & demo scheduling | Proposal draft, calendar booking | Close deal |

## Extensibility

- **CRM adapters**: Pluggable connectors for Salesforce, HubSpot, Pipedrive
- **Channel modules**: Add new outreach channels via adapter interface
- **Scoring models**: Swappable ML models for lead scoring and intent detection
