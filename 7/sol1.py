from collections import defaultdict 
import fileinput
import re

def dfs(g, node, visited):
	for neighbour in g[node]:
		if neighbour in visited:
			continue
		visited.append(neighbour)
		dfs(g, neighbour, visited)
	return visited

pattern = re.compile(r'[\d+] (.+?) bags?')

graph = defaultdict(lambda : [])
for line in fileinput.input():
	node_edges = line.split('bags contain')
	node = node_edges[0].strip()
	match = re.findall(pattern, node_edges[1])
	for m in match:
		graph[m.strip()].append(node)

reach = dfs(graph, 'shiny gold', [])
print(len(reach))
