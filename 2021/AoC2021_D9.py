import numpy as np

with open("D9_Data.txt", 'r') as f:
	data = np.array([[int(n) for n in l] for l in f.read().splitlines()])

total = 0
basins = []
_len = range(len(data[0]))

with np.nditer(data, flags=["multi_index"]) as it:
	for i in it:
		y, x = it.multi_index
		nums = [
			(y-1, x),
			(y+1, x),
			(y, x-1),
			(y, x+1)
		]
		nums = np.array([data[j] if all([k in _len for k in j]) else 99 for j in nums])
		if all(i < nums):
			total += i + 1
			basins += [(y, x),]

for basin in basins:
	

print(total, basins)
