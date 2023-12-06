# Part 1 + P2 prep
inc = inc_2 = 0
with open("D1_Data.txt", "r") as f:
	depths = [int(n) for n in f.read().splitlines()]
depths_2 = depths.copy()
depth = depths.pop(0)

for n in depths:
	if n > depth:
		inc += 1
	depth = n

print(f"Part 1: increased {inc} times")

# Part 2
depth = sum(depths_2[0:3])
size = len(depths_2)

for n in range(size):
	if (total := sum(depths_2[n:min(n+3, size)])) > depth:
		inc_2 += 1
	depth = total

print(f"Part 2: increased {inc_2} times")
