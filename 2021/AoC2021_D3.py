from collections import Counter

# Count data
with open("D3_Data.txt", "r") as f:
	nums = f.read().splitlines()

# Iterates over each number top left, to bottom left to top right, to bottom right (I don't know the term for this LOL)
data = [Counter([n[i] for n in nums]) for i in range(len(nums[0]))]

# Part 1
# Find Gamma and Epsilon
gamma = "".join([data[i].most_common(1)[0][0] for i in range(len(nums[0]))])
epsilon = gamma.translate(str.maketrans({"0": "1", "1": "0"}))

# Part 2
def count_data(b: str, l: list = nums) -> str:
	nums = l.copy()

	for i in range(len(gamma)):
		if len(nums) == 1:
			return nums[0]

		# (Re)count list number occurances 
		data = Counter([n[i] for n in nums])

		# Check number occurances 
		check = data['0'] > data['1']
		if data['0'] == data['1']:
			n = b
		elif b == '1':
			n = ['1','0'][check]
		else:
			n = ['0','1'][check]

		nums = list(filter(lambda c: c[i] == n, nums))
	return nums[0]

o2 = count_data('1')
co2 = count_data('0')

print(f"The power consumption of the submarine is {int(gamma, 2) * int(epsilon, 2)}")
print(f"The life support rating of the submarine is {int(o2, 2) * int(co2, 2)}")
