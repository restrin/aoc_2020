from collections import Counter
import sys

data = sys.stdin.read()
groups = data.split('\n\n')
count = 0
for group in groups:
	group = group.replace('\n', '')
	counts = Counter(group)
	count += len(counts.keys())

print(count)
