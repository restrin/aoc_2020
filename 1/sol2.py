import fileinput
import bisect

def sum3(N, numbers):
  numbers = sorted(numbers)
  l = len(numbers)
  for i in xrange(l):
  	m = numbers[i]
  	for j in xrange(i, l):
  	  n = numbers[j]
  	  p = N - n - m
	  k = bisect.bisect(numbers, p, j + 1, l)
	  if k - 1 < l and numbers[k - 1] == p:
	  	return m, n, p
  return None, None, None

numbers = []
for line in fileinput.input():
  numbers.append(int(line))

m, n, p = sum3(2020, numbers)

print(n * m * p)
