import fileinput

terrain = []
for line in fileinput.input():
  terrain.append(line.strip())

width = len(terrain[0])
tree = '#'

def trees_hit(dx, dy):
	num_trees = 0
	x = 0
	for y in range(dy, len(terrain), dy):
		x += dx
		if (terrain[y][x % width] == tree):
			num_trees += 1
	return num_trees

h1 = trees_hit(1, 1)
h2 = trees_hit(3, 1)
h3 = trees_hit(5, 1)
h4 = trees_hit(7, 1)
h5 = trees_hit(1, 2)
print(h1 * h2 * h3 * h4 * h5)
