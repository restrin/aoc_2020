import fileinput
import bisect

def sum_to(N, numbers):
  numbers = sorted(numbers)
  l = len(numbers)
  for i in xrange(len(numbers)):
  	n = numbers[i]
  	j = bisect.bisect(numbers, N - n, i + 1, l)
  	if j - 1 < l and numbers[j - 1] == N - n:
  		return n, N - n
  return None, None

numbers = []
for line in fileinput.input():
  numbers.append(int(line))

n, m = sum_to(2020, numbers)

print(n * m)
