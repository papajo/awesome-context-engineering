# Sales Agent Context Flow

Managing rich per-lead context across multi-channel, multi-touchpoint sales campaigns.

## Per-Lead Context Structure

```mermaid
flowchart TD
    subgraph LeadContext["Per-Lead Context"]
        PROFILE["Profile
- Name, title, company
- Industry, size
- Tech stack
- LinkedIn URL"]

        INTERACT["Interaction History
- Email thread
- LinkedIn DMs
- Call transcripts
- Website visits"]

        SIGNALS["Behavior Signals
- Email opens/clicks
- Replies & sentiment
- Page visits
- Intent keywords"]

        STAGE["Pipeline Stage
- Current stage
- Score history
- Previous actions
- Next recommended"]
    end

    subgraph CampaignContext["Campaign-Level Context"]
        CAMP["Campaign Config
- Target segments
- Message templates
- A/B variants
- Schedule rules"]

        PERFORMANCE["Campaign Performance
- Open rates by template
- Reply rates by channel
- Conversion by cohort"]

        COMP_INTEL["Competitive Context
- Competitor campaigns
- Market positioning
- Pricing intel"]
    end

    subgraph CompanyContext["Company-Level Context"]
        COMPANY["Account Profile
- Org structure
- Decision hierarchy
- Budget timeline
- Existing relationship"]
    end

    LeadContext --> Merge{Merge & Prioritize}
    CampaignContext --> Merge
    CompanyContext --> Merge
    Merge --> Prompt[Build Prompt Context]
    Prompt --> LLM[LLM Call]
    LLM --> Update[Update Lead Context]
    Update --> LeadContext

    style LeadContext fill:#e1f5fe
    style CampaignContext fill:#fff3e0
    style CompanyContext fill:#e8f5e9
    style Merge fill:#f3e5f5
```

## Token Budget by Interaction Type

```mermaid
pie title Context Budget per Outreach Event (8K tokens)
    "Lead Profile Summary" : 500
    "Interaction History (last 10)" : 2000
    "Company Research" : 1500
    "Campaign Context" : 1000
    "Personalization Guidelines" : 1000
    "Response Instructions" : 1000
    "Output Buffer" : 1000
```

## Context Sources and Refresh

| Context Layer | TTL | Refresh Event | Priority |
|--------------|-----|---------------|----------|
| Lead profile | Session-long | CRM sync | Critical |
| Interaction history | Per touchpoint | Each new email/call/link | High |
| Company research | 24 hours | Background refresh job | Medium |
| Campaign performance | 1 hour | Metric aggregation | Low |
| Competitive intel | Weekly | Intel refresh | Low |

## Context Prioritization Rules

1. **Recency**: Most recent interaction always included in full
2. **Sentiment flag**: Any negative sentiment interaction forces previous context to remain
3. **Objection tracking**: If an objection was raised, include how it was addressed
4. **Thread continuity**: For reply handling, include the last 5 messages of the thread fully, previous turns summarized
5. **Call context**: Call transcripts are summarized, not embedded raw (unless < 2K tokens)

## Failure Modes

| Mode | Symptom | Mitigation |
|------|---------|------------|
| **Context confusion** | Confuses two leads with similar names | Always include lead ID + company + role in context anchor |
| **Repetitive outreach** | Sending same message to same lead twice | Interaction dedup: check content hash before generation |
| **Stale company context** | References old funding/news | Tag company context with last update timestamp; refresh on trigger |
| **Channel bleed** | References LinkedIn DM in an email | Track per-channel context separately; merge only for summary |

## Example Lead Context Snapshot

```json
{
  "lead_id": "lead_789",
  "company": "Acme Corp",
  "contact": {
    "name": "Jane Chen",
    "title": "VP Engineering",
    "linkedin": "linkedin.com/in/jane-chen",
    "industry": "Fintech",
    "company_size": "500-1000"
  },
  "score": 82,
  "tier": "hot",
  "stage": "Active Outreach",
  "interactions": [
    {"type": "email", "direction": "sent", "date": "2026-06-01", "sentiment": "neutral"},
    {"type": "email_open", "date": "2026-06-02", "confirmed": true},
    {"type": "linkedin_message", "direction": "received", "date": "2026-06-03",
     "content": "Interesting, can you share a case study?", "sentiment": "positive"}
  ],
  "company_context": {
    "tech_stack": ["AWS", "Python", "Kubernetes"],
    "recent_funding": {"series": "C", "amount": "$50M", "date": "2026-03"},
    "key_initiatives": ["AI/ML infrastructure", "API platform v3"]
  },
  "next_action": "Send case study: ACME Corp + AI Infrastructure",
  "total_tokens": 4200
}
```
