import fileinput

def in_bounds(x, y, X, Y):
	return x >= 0 and x < X and y>= 0 and y < Y

def occ_neighbors(x, y, occ):
	c = 0
	Y = len(occ)
	X = len(occ[0])
	for dx in [-1, 0, 1]:
		for dy in [-1, 0, 1]:
			if (dx != 0 or dy != 0):
				px = x + dx
				py = y + dy
				while (in_bounds(px, py, X, Y)):
					if (occ[py][px] == '.'):
						px += dx
						py += dy
						continue
					if (occ[py][px] == 'L'):
						break
					c += 1
					break
	return c

def new_state(x, y, occ):
	if (occ[y][x] == 'L' and occ_neighbors(x, y, occ) == 0):
		return '#'
	if (occ[y][x] == '#' and occ_neighbors(x, y, occ) >= 5):
		return 'L'
	return occ[y][x]

def update(new_occ, occ):
	for y in range(len(occ)):
		for x in range(len(occ[y])):
			new_occ[y][x] = new_state(x, y, occ)

def print_seats(occ):
	for row in occ:
		print("".join(row))
	print('\n')

seats = []
for line in fileinput.input():
	s = []
	s[:0] = line.strip()
	seats.append(s)

occ = seats
new_occ = [row[:] for row in occ]
update(new_occ, occ)

while (new_occ != occ):
	tmp = occ
	occ = new_occ
	new_occ = tmp
	update(new_occ, occ)

cnt = 0
for y in range(len(occ)):
	for x in range(len(occ[y])):
		if (occ[y][x] == '#'):
			cnt += 1

print(cnt)
