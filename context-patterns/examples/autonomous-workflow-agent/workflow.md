# Autonomous Workflow Agent Workflow

Goal-driven execution from decomposition through verification with dynamic adaptation.

## Core Execution Loop

```mermaid
sequenceDiagram
    actor User
    participant Plan as Planner
    participant Exec as Orchestrator
    participant Tools as Tool Registry
    participant Ref as Reflection Engine
    participant Mon as Monitor

    User->>Plan: "Deploy monitoring stack on K8s cluster"
    Plan->>Plan: Decompose into 12 tasks
    Plan->>Plan: Build dependency DAG
    Plan-->>User: Proposed plan (6 stages, 12 tasks)
    User-->>Exec: Execute

    loop Main execution
        Exec->>Exec: Pop next ready task from queue
        Exec->>Tools: Execute task with context
        Tools-->>Exec: Task result

        Exec->>Ref: Validate result
        Ref->>Ref: Self-critique quality

        alt Quality threshold met
            Ref-->>Exec: Accept result
            Exec->>Exec: Cache result, update DAG
        else Needs refinement
            Ref-->>Exec: Re-run with feedback
            Exec->>Tools: Retry with adjustments
        else Fatal error
            Ref-->>Exec: Cannot recover
            Exec->>Mon: Alert for human intervention
            Exec->>Exec: Pause workflow
        end

        Exec->>Mon: Log step metrics
    end

    Exec->>Exec: All tasks complete
    Exec->>Mon: Compile execution report
    Exec-->>User: Workflow complete

    alt Human intervention
        User->>Exec: Adjust parameter X
        Exec->>Exec: Resume from checkpoint
    end

    User->>Ref: Request post-mortem
    Ref-->>User: Analysis + recommendations
```

## Decision Flow: Self-Adaptation

```mermaid
flowchart TD
    START([Task Ready]) --> EXEC[Execute Task]
    EXEC --> STATUS{Status?}

    STATUS -->|Success| QUAL{Pass Quality?}
    STATUS -->|Retryable Error| RETRY{Retries Left?}
    STATUS -->|Fatal| BLOCKED{Can Skip?}

    QUAL -->|Yes| DONE[Mark Complete]
    QUAL -->|No| FEEDBACK[Refine with Feedback]
    FEEDBACK --> RETRY

    RETRY -->|Yes| EXEC
    RETRY -->|No| BLOCKED

    BLOCKED -->|Yes| SKIP[Skip & Log Warning]
    BLOCKED -->|No| HALT[Halt & Escalate]

    DONE --> CHECK{All Done?}
    SKIP --> CHECK
    CHECK -->|Yes| COMPLETE[Final Report]
    CHECK -->|No| START

    HALT --> APPROVAL{User Approval?}
    APPROVAL -->|Override| START
    APPROVAL -->|Abort| ABORT[Fail Workflow]
    APPROVAL -->|Modify| RECONFIG[Reconfigure & Restart]
    RECONFIG --> START
```

## Task Dependency DAG Example

```mermaid
flowchart TD
    T0[Provision Cluster] --> T1[Install Prometheus]
    T0 --> T2[Install Grafana]
    T1 --> T3[Configure Alert Rules]
    T1 --> T4[Set Up ServiceMonitors]
    T2 --> T5[Configure Dashboards]
    T3 --> T6[Test Alerting]
    T4 --> T6
    T5 --> T7[Validate End-to-End]
    T6 --> T7
    T7 --> T8[Generate Report]

    style T0 fill:#e1f5fe
    style T7 fill:#e8f5e9
    style T8 fill:#f3e5f5
```

## Execution Budget Controls

| Control | Limit | Action on Exceed |
|---------|-------|------------------|
| Max iterations | 50 per workflow | Escalate for approval |
| Step timeout | 5 min per task | Retry once, then escalate |
| Token budget | 100K per workflow | Pause, ask to continue |
| Cost cap | $5.00 per workflow | Pause, ask to increase budget |
| Failure threshold | 3 consecutive failures | Escalate to human |
