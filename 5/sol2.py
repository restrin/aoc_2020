import fileinput

seats = []
for line in fileinput.input():
	line = line.replace('F', '0')
	line = line.replace('B', '1')
	line = line.replace('L', '0')
	line = line.replace('R', '1')
	seats.append(int(line, 2))

seats = sorted(seats)
prev = seats[0] - 1
for s in seats:
	if (s != prev + 1):
		print(s - 1)
		break
	prev = s
