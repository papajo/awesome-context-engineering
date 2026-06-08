# Coding Agent Architecture

An AI-powered coding assistant that understands codebases, generates changes, runs tests, and manages git workflows.

## System Architecture

```mermaid
flowchart TB
    subgraph Interfaces["User Interfaces"]
        CLI["CLI Terminal"]
        IDE["VS Code Extension"]
        WEB["Web UI"]
        API["REST / MCP API"]
    end

    subgraph AgentLoop["Agent Core"]
        PLAN["Planner"]
        EXEC["Executor"]
        OBS["Observer"]
        MEM["Working Memory"]
    end

    subgraph Infrastructure["Code Intelligence"]
        INDEX["Codebase Indexer"]
        AST["AST Parser"]
        GREP["Semantic Search"]
        DEPS["Dependency Graph"]
    end

    subgraph Tools["Tool Execution"]
        FS["File System Ops"]
        BASH["Shell Executor"]
        GIT["Git Integration"]
        TEST["Test Runner"]
        LINT["Linter / Formatter"]
    end

    subgraph LLM["LLM Backends"]
        CLAUDE["Claude / Sonnet"]
        GPT["GPT-4o / o1"]
        LOCAL["Local (Llama/Mistral)"]
    end

    subgraph Memory["Persistent Memory"]
        PROJ["Project Context"]
        SESH["Session History"]
        LEARN["User Preferences"]
    end

    Interfaces --> AgentLoop
    AgentLoop <--> Infrastructure
    AgentLoop --> Tools
    AgentLoop <--> LLM
    AgentLoop <--> Memory
    Tools --> FS
    Tools --> BASH
    Tools --> GIT
    Tools --> TEST
    Tools --> LINT

    style Interfaces fill:#e1f5fe
    style AgentLoop fill:#f3e5f5
    style Infrastructure fill:#e8f5e9
    style Tools fill:#fff3e0
    style LLM fill:#e0f7fa
    style Memory fill:#fce4ec
```

## Agent Loop Phases

| Phase | Description | Tools Used |
|-------|-------------|------------|
| **Understand** | Map user request to codebase context | Indexer, Semantic Search |
| **Plan** | Decompose task into ordered steps | LLM, Planner |
| **Implement** | Execute file reads/writes/edits | File System, AST Parser |
| **Verify** | Run tests, linter, type check | Test Runner, Linter |
| **Review** | Self-review diff for correctness | LLM, Diff Analyzer |
| **Commit** | Stage, commit, push / PR | Git Integration |

## Extensibility

- **Custom tools**: Any CLI tool can be wrapped as an agent capability via a tool manifest
- **Language support**: AST parsers are language-agnostic via tree-sitter grammars
- **LLM backends**: Plugable model adapters for cloud, local, and hybrid inference
