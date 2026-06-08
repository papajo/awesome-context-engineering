import json
from networkx.readwrite import json_graph
import networkx as nx
from pathlib import Path
data = json.loads(Path("graphify-out/graph.json").read_text())
G = json_graph.node_link_graph(data, edges="links")
nid = "concept_awesome_context_engineering_repo"
print("NODE:", G.nodes[nid].get("label", nid))
print("  source:", G.nodes[nid].get("source_file",""))
print("  degree:", G.degree(nid))
print()
print("ALL CONNECTIONS:")
for neighbor in G.neighbors(nid):
    edge = G.edges[nid, neighbor]
    nlabel = G.nodes[neighbor].get("label", neighbor)
    print("  --" + edge.get("relation","") + " [" + str(edge.get("confidence","")) + " " + str(edge.get("confidence_score","")) + "]--> " + nlabel)
    print("     src: " + str(G.nodes[neighbor].get("source_file","")))
