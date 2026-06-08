# Coding Agent Workflow

Step-by-step flow from user request to code change, with verification gates.

## Full Task Lifecycle

```mermaid
sequenceDiagram
    actor User
    participant Agent as Agent Core
    participant Index as Codebase Index
    participant LLM as LLM
    participant Tools as Tool Executor
    participant Git as Git Integration

    User->>Agent: "Add pagination to user list"
    Agent->>Index: Query relevant files
    Index-->>Agent: File paths & signatures

    Agent->>LLM: Understand context + propose plan
    LLM-->>Agent: Plan: 1) Find list view 2) Add component 3) Wire routes

    Agent->>User: Show plan, request approval
    User-->>Agent: Proceed

    loop For each step
        Agent->>Tools: Read current file
        Tools-->>Agent: File content
        Agent->>LLM: Generate change
        LLM-->>Agent: Proposed edit
        Agent->>Tools: Apply change
        Tools-->>Agent: Result
    end

    Agent->>Tools: Run tests
    Tools-->>Agent: 14 pass, 0 fail
    Agent->>Tools: Run linter
    Tools-->>Agent: No issues

    Agent->>LLM: Review diff for edge cases
    LLM-->>Agent: Review OK

    Agent->>Git: Stage and commit
    Git-->>Agent: Commit abc123 created
    Agent->>Git: Push branch
    Git-->>Agent: Branch pushed

    Agent-->>User: Done! Branch ready for PR
```

## Decision Flow: When to Delegate vs. Direct Edit

```mermaid
flowchart TD
    START([User Request]) --> SCOPE{Change Scope?}

    SCOPE -->|"Single file, <20 lines"| DIRECT[Direct Edit
    No plan needed]
    SCOPE -->|"2-3 files, familiar"| PLAN[Light Plan
    Quick approval]
    SCOPE -->|"4+ files or new pattern"| DEEP[Deep Plan
    Full analysis]
    SCOPE -->|"Architecture change"| ARCH[Architecture Review
    Multi-agent]

    DIRECT --> VERIFY[Auto-verify]
    PLAN --> VERIFY
    DEEP --> VERIFY
    ARCH --> VERIFY

    VERIFY --> PASS{Tests pass?}
    PASS -->|Yes| DONE[Present diff]
    PASS -->|No| FIX[Auto-fix & retry]
    FIX --> VERIFY

    DONE --> APPROVE{User approves?}
    APPROVE -->|Yes| COMMIT[Commit & push]
    APPROVE -->|No| REVISE[Revise per feedback]
    REVISE --> PLAN
```

## Verification Gates

```mermaid
flowchart LR
    P[Plan Ready] --> C[Changes Applied]
    C --> L1{Lint Check}
    L1 -->|Pass| T1{Type Check}
    L1 -->|Fail| C
    T1 -->|Pass| T2{Unit Tests}
    T1 -->|Fail| C
    T2 -->|Pass| T3{Integration Tests}
    T2 -->|Fail| C
    T3 -->|Pass| R[Review Diff]
    T3 -->|Fail| C
    R -->|OK| D[Done]
    R -->|Issues| C
```

## Context Budget per Phase

| Phase | Token Budget | Context Sources |
|-------|-------------|-----------------|
| Understand | 8K | User query, file signatures, symbol index |
| Plan | 4K | Analysis results, dependency hints |
| Implement | 12K | Full target file, relevant imports |
| Verify | 2K | Test output, lint results |
| Review | 8K | Full diff, related files |
