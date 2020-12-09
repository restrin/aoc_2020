import fileinput

def is_pair_sum(n, lon):
	for i in lon:
		if n - i in lon:
			return True
	return False

nums = []
for line in fileinput.input():
	nums.append(int(line.strip()))

for i in range(25, len(nums)):
	if not is_pair_sum(nums[i], nums[(i - 25):i]):
		print(nums[i])
		break
