import fileinput

h2d = {'N' : 0, 'E' : 90, 'S' : 180, 'W' : 270}
d2h = {0 : 'N', 90 : 'E', 180 : 'S', 270 : 'W'}

def turn(heading, lr, deg):
	if lr == 'L':
		deg *= -1
	return d2h[(h2d[heading] + deg) % 360]

def update_pos(pos, heading, d):
	if heading == 'N':
		pos[0] += d
	elif heading == 'E':
		pos[1] += d
	elif heading == 'S':
		pos[0] -= d
	elif heading == 'W':
		pos[1] -= d

nav = []
for line in fileinput.input():
	nav.append((line[0], int(line[1:])))

pos = [0, 0]
heading = 'E'
for instr in nav:
	if instr[0] == 'R' or instr[0] == 'L':
		heading = turn(heading, instr[0], instr[1])
	elif instr[0] == 'F':
		update_pos(pos, heading, instr[1])
	else:
		update_pos(pos, instr[0], instr[1])

print(pos)
print(abs(pos[0]) + abs(pos[1]))
