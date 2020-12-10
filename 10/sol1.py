import fileinput

jolts = [0]
for line in fileinput.input():
	jolts.append(int(line.strip()))

jolts = sorted(jolts)

diffs = [0, 0, 1]
for i in range(len(jolts) - 1):
	diffs[jolts[i + 1] - jolts[i] - 1] += 1

print(diffs[0] * diffs[2])
