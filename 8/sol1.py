import fileinput

instr = []
for line in fileinput.input():
	op_arg = line.split(' ')
	instr.append((op_arg[0], int(op_arg[1])))

executed = [False] * len(instr)
i = 0
acc = 0
while (not executed[i]):
	executed[i] = True
	if instr[i][0] == 'nop':
		i += 1
		continue
	elif instr[i][0] == 'acc':
		acc += instr[i][1]
		i += 1
	elif instr[i][0] == 'jmp':
		i += instr[i][1]
print(acc)
