import fileinput
import re

pattern = re.compile(r'(\d+)\-(\d+) ([a-z]): ([a-z]+)')

valid = 0
for line in fileinput.input():
  match = re.findall(pattern, line)[0]
  lo = int(match[0])
  hi = int(match[1])
  letter = match[2]
  pw = match[3]
  first_eq = (pw[lo - 1] == letter)
  second_eq = (pw[hi - 1] == letter)
  if (first_eq ^ second_eq):
  	valid += 1

print(valid)
