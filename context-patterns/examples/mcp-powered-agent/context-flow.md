# MCP-Powered Agent Context Flow

How context is managed across multiple MCP servers, capabilities, and session state.

## Multi-Server Context Architecture

```mermaid
flowchart TD
    subgraph ClientSide["Client-Side Context"]
        SESSION["Session State
- Active server connections
- Capability registry
- Authentication tokens
- Server health status"]
        COMPOSED["Composed Context
- Aggregated context from
  all connected servers
- Cross-server dedup
- Priority-ordered"]
        HISTORY["Interaction History
- Previous tool calls
- Resource fetches
- Prompt generations
- User feedback"]
    end

    subgraph PerServer["Per-Server Context"]
        FS_CTX["File System Server
- Current working dir
- Open file handles
- Recent file accesses"]
        DB_CTX["Database Server
- Active connection
- Current schema
- Query history"]
        MEM_CTX["Memory Server
- Active entities
- Recent recalls
- Write queue"]
        WEB_CTX["Web Server
- Rate limit state
- Cookie jar
- Session tokens"]
    end

    subgraph ContextFlows["Context Flow Patterns"]
        DIRECT["Direct Flow
Tool A → Tool B
Server A passes result
directly to Server B"]
        AGGREGATE["Aggregate Flow
Multiple server results
merged into single
context block"]
        COMPOSE["Compose Flow
Server A result becomes
resource URI for Server B
context composition"]
    end

    ClientSide <--> PerServer
    ContextFlows --> Composed
    Composed --> Prompt[LLM Prompt Assembly]

    style ClientSide fill:#e1f5fe
    style PerServer fill:#fff3e0
    style ContextFlows fill:#f3e5f5
```

## Context Aggregation Strategy

```mermaid
flowchart TD
    Q[Query / Task] --> DISCOVER{Which servers
provide relevant
context?}

    DISCOVER -->|File path needed| FS_GET[File Server: read_file]
    DISCOVER -->|Data needed| DB_GET[DB Server: query]
    DISCOVER -->|Knowledge needed| MEM_GET[Memory Server: recall]

    FS_GET --> RESULT{Has result?}
    DB_GET --> RESULT
    MEM_GET --> RESULT

    RESULT -->|Success| TOKEN_BUDGET{Fits token
budget?}
    RESULT -->|Error| FALLBACK[Fallback strategy]

    TOKEN_BUDGET -->|Yes| MERGE[Merge into context]
    TOKEN_BUDGET -->|No| TRIM[Trim & summarize]
    TRIM --> MERGE

    MERGE --> DEDUP[Deduplicate across servers]
    DEDUP --> PRIORITY[Priority rank]
    PRIORITY --> ASSEMBLE[Assemble final context]
    ASSEMBLE --> LLM[LLM Call]
```

## Token Budget per Context Source

```mermaid
pie title MCP Context Budget (16K tokens)
    "System Instructions & Protocol" : 500
    "Session & Connection State" : 500
    "Capability Registry Summary" : 500
    "Primary Tool Results" : 6000
    "Secondary Server Context" : 3000
    "Resource Content" : 3000
    "Interaction History" : 1500
    "Response Buffer" : 1000
```

## Server Context Lifecycle

| Server | Connection Init | Context Lifetime | Reconnect Strategy |
|--------|----------------|-----------------|-------------------|
| **File System** | On session start | Session-scoped | Auto-reconnect with backoff |
| **Database** | On first query | Connection pool (max 30 min) | Refresh on each query |
| **Memory** | On session start | Persistent with session ID | Cache locally, sync on reconnect |
| **Web** | On first fetch | Stateless (per request) | New connection each request |

## Context Flow Patterns in Detail

### Direct Flow
Server A output → Server B input → combined result

```json
{
  "pattern": "direct",
  "flow": [
    {"server": "file_system", "tool": "read_file", "result": "SELECT * FROM users;"},
    {"server": "database", "tool": "query",
     "input": {"sql": "FROM_PREVIOUS_STEP"},
     "result": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}
  ]
}
```

### Aggregate Flow
Multiple servers queried independently → results merged

```json
{
  "pattern": "aggregate",
  "sources": [
    {"server": "memory", "resource": "memory://project/context", "tokens": 1200},
    {"server": "file_system", "resource": "file://README.md", "tokens": 800},
    {"server": "web", "resource": "https://api.example.com/status", "tokens": 200}
  ],
  "merged_tokens": 2200
}
```

## Failure Modes

| Mode | Symptom | Mitigation |
|------|---------|------------|
| **Server disconnect** | Tool call timeout | Retry with backoff; if unavailable, use fallback |
| **Capability mismatch** | Server doesn't support requested tool | Re-query capability list; cache and version-check |
| **Context fragmentation** | Results scattered across servers without linkage | Maintain cross-reference map of server outputs |
| **Protocol version skew** | Initialize fails on version mismatch | Support multiple protocol versions; negotiate downgrade |
| **Resource leak** | Server connections not closed | Connection pool with TTL + health check pings |

## Example Aggregated Context

```json
{
  "session_id": "mcp_sess_789",
  "servers_connected": ["file_system", "database", "memory"],
  "capabilities": {
    "tools": ["read_file", "write_file", "search_files", "sql_query", "sql_execute", "store", "recall"],
    "resources": ["file://", "database://", "memory://"],
    "prompts": ["code_review", "sql_audit", "deploy_check"]
  },
  "context_stack": [
    {"source": "file_system", "type": "tool_result", "content": "PR #142 diff (450 lines)", "tokens": 3200},
    {"source": "database", "type": "tool_result", "content": "Schema migration check: 3 pending migrations", "tokens": 600},
    {"source": "memory", "type": "resource", "content": "Project conventions: SQL style guide", "tokens": 1500},
    {"source": "session", "type": "interaction", "content": "Previous review: approved migration #141", "tokens": 400}
  ],
  "total_tokens": 5700,
  "budget_remaining": 10300
}
```
