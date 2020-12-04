import fileinput
import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eye_clr = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_num(nstr, lo, hi):
	try:
		n = int(nstr)
		if (n < lo) or (n > hi):
			return False
	except:
		return False
	return True

def is_valid_passport(passport):
	for f in required_fields:
		if f not in passport:
			return False

	if not valid_num(passport['byr'], 1920, 2002):
		return False
	if not valid_num(passport['iyr'], 2010, 2020):
		return False
	if not valid_num(passport['eyr'], 2020, 2030):
		return False
	hgt = passport['hgt']
	try:
		unit = hgt[-2:]
		h = hgt[:-2]
		if unit == 'cm':
			if not valid_num(h, 150, 193):
				return False
		elif unit == 'in':
			if not valid_num(h, 59, 76):
				return False
		else:
			return False
	except:
		return False

	if not re.match(r'#[0-9a-f]{6}\Z', passport['hcl']):
		return False

	if passport['ecl'] not in eye_clr:
		return False

	if not re.match(r'\d{9}\Z', passport['pid']):
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
