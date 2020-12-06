from collections import Counter
import sys

data = sys.stdin.read()
groups = data.split('\n\n')
count = 0
for group in groups:
	group = group.strip()
	n = len(group.split('\n'))
	group = group.replace('\n', '')
	counts = Counter(group)
	for c in counts:
		if (counts[c] == n):
			count += 1

print(count)
