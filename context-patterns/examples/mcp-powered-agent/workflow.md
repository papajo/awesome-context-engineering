# MCP-Powered Agent Workflow

End-to-end interaction between an MCP host, its servers, and the user, spanning capability discovery through execution.

## Full Interaction Flow

```mermaid
sequenceDiagram
    actor User
    participant Host as Host App
    participant Client as MCP Client
    participant FS as File System Server
    participant DB as Database Server
    participant MEM as Memory Server
    participant LLM as LLM

    User->>Host: "Review the database migration script"

    Note over Host,Client: Step 1: Capability Discovery
    Host->>Client: Discover capabilities
    Client->>FS: Request capability list
    Client->>DB: Request capability list
    Client->>MEM: Request capability list
    FS-->>Client: tools: read_file, search, grep
    DB-->>Client: tools: query, get_schema
    MEM-->>Client: resources: project_context, best_practices
    Client-->>Host: Unified capability map

    Note over Host,LLM: Step 2: Plan
    Host->>Host: Determine required tools
    Host->>FS: Read migration script
    FS-->>Host: migration_20260601.sql (12KB)
    Host->>DB: Get current schema
    DB-->>Host: schema dump
    Host->>MEM: Get project conventions
    MEM-->>Host: SQL best practices

    Host->>LLM: Analyze migration with context
    LLM-->>Host: Analysis + suggested changes

    Note over Host,User: Step 3: Present & Execute
    Host-->>User: Proposed migration review
    User-->>Host: Apply change #3

    Host->>FS: Write updated migration
    FS-->>Host: Done

    Host->>MEM: Save decision log
    MEM-->>Host: Stored

    Host-->>User: Changes applied. Summary saved to memory.
```

## Tool Selection Decision

```mermaid
flowchart TD
    START([User Intent]) --> ANALYZE{Requires
External Tool?}
    ANALYZE -->|No| LLM_Direct[Direct LLM Generation]
    ANALYZE -->|Yes| SERVER{Which Server?}

    SERVER -->|File access| FS{File Server?}
    SERVER -->|Data query| DB{DB Server?}
    SERVER -->|Web call| WEB{Web Server?}
    SERVER -->|Code run| CODE{Code Server?}
    SERVER -->|Knowledge| MEM{Memory Server?}

    FS -->|Connected| TOOL_READ[Tool: read_file]
    FS -->|Unavailable| FS_FALLBACK[Fallback: ask user to upload]
    DB -->|Connected| TOOL_QUERY[Tool: query]
    DB -->|Unavailable| DB_FALLBACK[Fallback: sample data prompt]
    WEB -->|Connected| TOOL_FETCH[Tool: fetch]
    WEB -->|Unavailable| WEB_FALLBACK[Fallback: use knowledge cutoff]
    CODE -->|Connected| TOOL_RUN[Tool: run_python]
    CODE -->|Unavailable| CODE_FALLBACK[Fallback: suggest local run]
    MEM -->|Connected| TOOL_MEM[Tool: recall]
    MEM -->|Unavailable| MEM_FALLBACK[Fallback: conversation context]
```

## Capability Negotiation Flow

```mermaid
sequenceDiagram
    participant Host as Host
    participant Server as MCP Server

    Host->>Server: initialize
    Note over Server: Server declares supported
                   protocol version
                   capabilities (tools, resources, prompts)
    Server-->>Host: initialized + server info

    Host->>Server: List capabilities

    par Query tools
        Host->>Server: tools/list
        Server-->>Host: [{name, description, inputSchema}]
    and Query resources
        Host->>Server: resources/list
        Server-->>Host: [{uri, name, description, mimeType}]
    and Query prompts
        Host->>Server: prompts/list
        Server-->>Host: [{name, description, arguments}]
    end

    Host->>Host: Build capability map
    Note over Host: For each tool/resource/prompt
                   validate against host requirements
                   register in capability registry

    Host->>Server: Notifications/initialized
    Note over Host,Server: Ready for interaction
```

## Execution Modes

| Mode | Tool Invocation | Error Strategy | Use Case |
|------|----------------|----------------|----------|
| **Eager** | Try all relevant tools in parallel | Roll back on any failure | Exploration & discovery |
| **Sequential** | One tool at a time, passing results | Retry with backoff | Data pipeline steps |
| **Conservative** | Confirm before each tool call | Ask user on error | Destructive operations |
| **Delegated** | Let server decide sub-tools | Server-level error handling | Complex multi-step operations |
