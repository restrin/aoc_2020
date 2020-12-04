import fileinput

terrain = []
for line in fileinput.input():
  terrain.append(line.strip())

width = len(terrain[0])
tree = '#'

num_trees = 0
x = 0
for y in range(1, len(terrain)):
	x += 3
	if (terrain[y][x % width] == tree):
		num_trees += 1

print(num_trees)
