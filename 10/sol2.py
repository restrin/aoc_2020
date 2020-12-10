import fileinput

jolts = [0]
for line in fileinput.input():
	jolts.append(int(line.strip()))

jolts = sorted(jolts)

comb = [0] * len(jolts)
comb[0] = 1
for j in range(len(comb)):
	d = 1
	while ((j - d >= 0) and (jolts[j] - jolts[j - d] <= 3)):
		comb[j] += comb[j - d]
		d += 1

print(comb[-1])
