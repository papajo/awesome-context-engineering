# Graph Report - .  (2026-06-08)

## Corpus Check
- Corpus is ~2,897 words - fits in a single context window. You may not need a graph.

## Summary
- 38 nodes · 47 edges · 11 communities (6 shown, 5 thin omitted)
- Extraction: 66% EXTRACTED · 34% INFERRED · 0% AMBIGUOUS · INFERRED: 16 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Repo Foundation & Governance|Repo Foundation & Governance]]
- [[_COMMUNITY_Initial PRD & Probe Suite|Initial PRD & Probe Suite]]
- [[_COMMUNITY_Agent Context & Examples|Agent Context & Examples]]
- [[_COMMUNITY_Context Engineering Ecosystem|Context Engineering Ecosystem]]
- [[_COMMUNITY_Memory Systems|Memory Systems]]
- [[_COMMUNITY_Repository Scaffold|Repository Scaffold]]
- [[_COMMUNITY_Context Compression & Ranking|Context Compression & Ranking]]
- [[_COMMUNITY_Security & Advisories|Security & Advisories]]
- [[_COMMUNITY_PRD Checklist|PRD Checklist]]
- [[_COMMUNITY_Probe Suite|Probe Suite]]

## God Nodes (most connected - your core abstractions)
1. `Context Engineering` - 8 edges
2. `Awesome Context Engineering Repository` - 4 edges
3. `sections/README.md` - 3 edges
4. `Memory Systems` - 3 edges
5. `Agent Context Management` - 3 edges
6. `Context Compression` - 3 edges
7. `Context Pruning` - 3 edges
8. `examples/README.md` - 2 edges
9. `customer-support-agent/architecture.md` - 2 edges
10. `patterns/README.md` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Rolling Memory Pattern` --conceptually_related_to--> `Memory Systems`  [INFERRED]
  patterns/rolling-memory.md → initial-prd.md
- `Customer Support Agent` --conceptually_related_to--> `Agent Context Management`  [INFERRED]
  examples/customer-support-agent/architecture.md → initial-prd.md
- `examples/README.md` --references--> `customer-support-agent/architecture.md`  [EXTRACTED]
  examples/README.md → examples/customer-support-agent/architecture.md
- `patterns/README.md` --references--> `patterns/rolling-memory.md`  [EXTRACTED]
  patterns/README.md → patterns/rolling-memory.md
- `sections/README.md` --references--> `sections/context-windows.md`  [EXTRACTED]
  sections/README.md → sections/context-windows.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Repository Governance** — code_of_conduct_md, contributing_md, security_md, changelog_md [EXTRACTED 1.00]
- **Repository Scaffold** — readme_md, contributing_md, code_of_conduct_md, security_md, changelog_md, roadmap_md, initial_prd_md, sections_readme_md, patterns_readme_md, examples_readme_md [EXTRACTED 1.00]
- **Probe and Checklist Suite** — existing_repo_probe_md, full_prd_checklist_md, full_repo_scope_probe_md, prd_scaffold_probe_md [EXTRACTED 1.00]

## Communities (11 total, 5 thin omitted)

### Community 0 - "Repo Foundation & Governance"
Cohesion: 0.29
Nodes (4): Core Principles (Modularity, Scalability, Maintainability, Security), sections/context-windows.md, sections/foundations.md, sections/README.md

### Community 2 - "Agent Context & Examples"
Cohesion: 0.50
Nodes (4): Agent Context Management, Customer Support Agent, customer-support-agent/architecture.md, examples/README.md

### Community 3 - "Context Engineering Ecosystem"
Cohesion: 0.50
Nodes (4): Context Engineering, Long Context Strategies, MCP Ecosystem, RAG Architectures

### Community 4 - "Memory Systems"
Cohesion: 0.50
Nodes (4): Memory Systems, Rolling Memory Pattern, patterns/README.md, patterns/rolling-memory.md

### Community 6 - "Context Compression & Ranking"
Cohesion: 0.67
Nodes (3): Context Compression, Context Pruning, Context Ranking

## Knowledge Gaps
- **9 isolated node(s):** `sections/context-windows.md`, `Repository Scaffold`, `Memory Layering`, `Context Observability`, `Core Principles (Modularity, Scalability, Maintainability, Security)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Awesome Context Engineering Repository` connect `Repository Scaffold` to `Initial PRD & Probe Suite`, `Context Engineering Ecosystem`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Why does `Memory Systems` connect `Memory Systems` to `Initial PRD & Probe Suite`, `Context Engineering Ecosystem`?**
  _High betweenness centrality (0.055) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `Context Engineering` (e.g. with `Agent Context Management` and `Awesome Context Engineering Repository`) actually correct?**
  _`Context Engineering` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Awesome Context Engineering Repository` (e.g. with `Repository Scaffold` and `Context Engineering`) actually correct?**
  _`Awesome Context Engineering Repository` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Memory Systems` (e.g. with `Context Engineering` and `Rolling Memory Pattern`) actually correct?**
  _`Memory Systems` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Agent Context Management` (e.g. with `Context Engineering` and `Customer Support Agent`) actually correct?**
  _`Agent Context Management` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `sections/context-windows.md`, `Repository Scaffold`, `Memory Layering` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._