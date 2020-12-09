import fileinput
import sys

nums = []
for line in fileinput.input():
	nums.append(int(line.strip()))

N = 90433990

start = 0
end = 0
curr = 0
while (curr != N):
	while (curr < N):
		curr += nums[end]
		end += 1
	while (curr > N):
		curr -= nums[start]
		start += 1

M = -sys.maxint - 1
m = sys.maxint
for i in range(start, end):
	m = min(m, nums[i])
	M = max(M, nums[i])

print(m + M)
