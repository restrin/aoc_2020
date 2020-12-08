from collections import defaultdict 
import fileinput
import re

def num_bags(g, node, memo):
	if node in memo:
		return memo[node]
	bags = 0
	for (neighbour, n) in g[node]:
		bags += n * (1 + num_bags(g, neighbour, memo))
	
	memo[node] = bags
	return bags

pattern = re.compile(r'((\d+) (.+?)) bags?')

graph = defaultdict(lambda : [])
for line in fileinput.input():
	node_edges = line.split('bags contain')
	node = node_edges[0].strip()
	match = re.findall(pattern, node_edges[1])
	for m in match:
		graph[node].append((m[2].strip(), int(m[1])))

print(num_bags(graph, 'shiny gold', {}))
