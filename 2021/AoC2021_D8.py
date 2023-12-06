with open("D8_Data.txt", 'r') as f:
	data = f.read().splitlines()

total_1 = total_2 = 0
for d in data:
	p2, p1 = [p.split() for p in d.split('|')]

	# Part 2
	# Find 1, 7, 4, 8
	p2 = set(''.join(sorted(n)) for n in p2)
	nums = {2: 1, 3: 7, 4: 4, 7: 8}
	nums = {nums[len(n)]: n for n in p2 if len(n) in nums}

	# Find the rest
	for n in p2 - set(nums.values()):
		if len(n) == 5:
			if len(set(n) & set(nums[1])) == 2:
				nums[3] = n
			elif len(set(n) & set(nums[4])) == 3:
				nums[5] = n
			else:
				nums[2] = n
		else:
			if len(set(n) & set(nums[1])) == 1:
				nums[6] = n
			elif len(set(n) & set(nums[4])) == 4:
				nums[9] = n
			else:
				nums[0] = n

	# If I set the key to the words themselves it'll be a PITA to use, 
	# Which is why I didn't reverse it in the first place 
	nums = {k: v for v, k in nums.items()}

	# Part 1 and 2
	for i, n in enumerate(reversed([n for n in p1])):
		if len(n) in (2,3,4,7):
			total_1 += 1
		total_2 += 10**i*nums[''.join(sorted(n))]


print(f"There are a total of {total_1} 1, 4, 7 and 8s.")
print(f"All numbers tally up to {total_2}.")
