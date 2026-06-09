from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path("/mnt/data/agent-mri")
files = {}

files["README.md"] = """# Agent MRI

MRI for AI agents — inspect, trace, replay, and diagnose why an agent succeeded or failed.

## Install

```bash
pnpm install
pnpm dev

# Example
agent-mri analyze examples/simple-agent/trace.json
Outputs:

report.md
report.json
Architecture

Trace → Parser → Event Store → Analyzer → Reporter
"""

files["package.json"] = """{
"name":"agent-mri",
"private": true,
"version":"0.1.0",
"scripts":{
"dev":"tsx packages/cli/src/index.ts",
"build":"tsc",
"test":"vitest"
}
}
"""

files["packages/core/src/types.ts"] = """export type EventType =
| "input"
| "memory"
| "retrieve"
| "tool"
| "reason"
| "output";

export interface AgentEvent {
id: string;
timestamp: number;
type: EventType;
tokens: number;
payload: Record<string, unknown>;
}
"""

files["packages/parser/src/parser.ts"] = """import { AgentEvent } from "../../core/src/types";

export function parseTrace(input:string): AgentEvent[] {
return JSON.parse(input);
}
"""

files["packages/analyzers/src/contextLoss.ts"] = """import { AgentEvent } from "../../core/src/types";

export function detectContextLoss(events:AgentEvent){
const retrieval = events.filter(e=>e.type==="retrieve");
if(retrieval.length===0){
return {issue:"Context starvation", confidence:0.9};
}
return null;
}
"""

files["packages/reporter/src/report.ts"] = """export function render(result:any){
return `# Agent MRI Report

Root Cause: ${result?.issue ?? "None detected"}
Confidence: ${Math.round((result?.confidence ?? 0)*100)}%
`;
}
"""

files["packages/cli/src/index.ts"] = """#!/usr/bin/env node
import fs from "fs";
import { parseTrace } from "../../parser/src/parser";
import { detectContextLoss } from "../../analyzers/src/contextLoss";
import { render } from "../../reporter/src/report";

const file = process.argv[3];
if(!file){
console.log("usage: agent-mri analyze trace.json");
process.exit(1);
}

const events=parseTrace(fs.readFileSync(file,"utf8"));
const result=detectContextLoss(events);
console.log(render(result));
"""

files["examples/simple-agent/trace.json"] = """[
{"id":"1","timestamp":1,"type":"input","tokens":100,"payload":{"text":"fix bug"}},
{"id":"2","timestamp":2,"type":"output","tokens":300,"payload":{"text":"done"}}
]
"""

files["docs/roadmap.md"] = """# Roadmap

 CLI skeleton
 Trace normalization
 Replay
 HTML reports
 Visual timeline
"""

for rel, content in files.items():
p = root / rel
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(content)

zip_path = "/mnt/data/agent-mri-starter.zip"
with ZipFile(zip_path, "w", ZIP_DEFLATED) as z:
for p in root.rglob("*"):
z.write(p, p.relative_to(root.parent))

print(zip_path)

##started the repository as a **real scaffold instead of a spec**.



Included:

```text
agent-mri/
├── README.md
├── package.json
├── docs/
│   └── roadmap.md
├── examples/
│   └── simple-agent/
│       └── trace.json
├── packages/
│   ├── cli/
│   │   └── src/index.ts
│   ├── core/
│   │   └── src/types.ts
│   ├── parser/
│   │   └── src/parser.ts
│   ├── analyzers/
│   │   └── src/contextLoss.ts
│   └── reporter/
│       └── src/report.ts
```

Current flow:

```text
trace.json
↓
parse
↓
analyze
↓
diagnose
↓
report
```

Current command shape:

```bash
agent-mri analyze examples/simple-agent/trace.json
```

Current diagnosis implemented:

```text
No retrieval
→ Context starvation
```

Next milestone (what I’d build next, in order):

1. **Trace normalization**

   * OpenAI
   * LangGraph
   * CrewAI
   * generic JSON

2. **HTML report generation**

   * timeline
   * token attribution
   * root cause

3. **Replay mode**

   * step through events

4. **Visual context diff**

   * added / removed / compressed

5. **Plugin system**

   * custom analyzers

Once you unzip it, create the repo and commit:

```bash
git init
pnpm install
git add .
git commit -m "initial Agent MRI scaffold"
```

Then we can move to **Milestone 2: make it ingest real agent traces** instead of sample JSON.

