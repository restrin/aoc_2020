import fileinput

m = 0
for line in fileinput.input():
	line = line.replace('F', '0')
	line = line.replace('B', '1')
	line = line.replace('L', '0')
	line = line.replace('R', '1')
	idd = int(line, 2)
	if idd > m:
		m = idd

print(m)
