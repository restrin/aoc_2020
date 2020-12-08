import fileinput

def halts(instr):
	executed = [False] * len(instr)
	i = 0
	acc = 0
	while (i < len(instr)) and (not executed[i]):
		executed[i] = True
		if instr[i][0] == 'nop':
			i += 1
			continue
		elif instr[i][0] == 'acc':
			acc += instr[i][1]
			i += 1
		elif instr[i][0] == 'jmp':
			i += instr[i][1]
	return (i == len(instr), acc)

instr = []
for line in fileinput.input():
	op_arg = line.split(' ')
	instr.append([op_arg[0], int(op_arg[1])])

for i in range(len(instr)):
	if instr[i][0] == 'nop':
		instr[i][0] = 'jmp'
		halt, acc = halts(instr)
		if halt:
			print(acc)
			break
		instr[i][0] = 'nop'

	if instr[i][0] == 'jmp':
		instr[i][0] = 'nop'
		halt, acc = halts(instr)
		if halt:
			print(acc)
			break
		instr[i][0] = 'jmp'
