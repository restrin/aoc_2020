import fileinput
import math

def rot_mat(lr, deg):
	if lr == 'L':
		deg *= -1
	deg = deg * (math.pi / 180.)
	return [[math.cos(deg), -math.sin(deg)], [math.sin(deg), math.cos(deg)]]

def turn(wp, lr, deg):
	r = rot_mat(lr, deg)
	wpt = wp[:]
	wp[0] = r[0][0] * wpt[0] + r[0][1] * wpt[1]
	wp[1] = r[1][0] * wpt[0] + r[1][1] * wpt[1]

def update_wp(wp, heading, d):
	if heading == 'N':
		wp[0] += d
	elif heading == 'E':
		wp[1] += d
	elif heading == 'S':
		wp[0] -= d
	elif heading == 'W':
		wp[1] -= d

nav = []
for line in fileinput.input():
	nav.append((line[0], int(line[1:])))

pos = [0, 0]
wp = [1, 10]
heading = 'E'
for instr in nav:
	if instr[0] == 'R' or instr[0] == 'L':
		turn(wp, instr[0], instr[1])
	elif instr[0] == 'F':
		pos[0] += instr[1] * wp[0]
		pos[1] += instr[1] * wp[1]
	else:
		update_wp(wp, instr[0], instr[1])

print(pos)
print(abs(pos[0]) + abs(pos[1]))
