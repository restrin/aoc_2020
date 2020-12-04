import fileinput
import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def is_valid_passport(passport):
	for f in required_fields:
		if f not in passport:
			return False
	return True

pattern = re.compile(r'([a-zA-Z]+):([\S]+)')

valid = 0
passport = {}
for line in fileinput.input():
	if (line.strip() == ''):
		if (is_valid_passport(passport)):
			valid += 1
		passport = {}
		continue
	match = re.findall(pattern, line)
	for m in match:
		passport[m[0]] = m[1]

if (is_valid_passport(passport)):
	valid += 1

print(valid)
