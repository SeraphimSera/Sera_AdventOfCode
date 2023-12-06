from collections import Counter

# Parse directive and counts line, count occurances of line
def count_overlaps(dirs: str, diag=False) -> Counter:
	total_xy = Counter()
	total_diag = Counter()

	for _dir in dirs:
		x1, y1, x2, y2 = [int(d) for d in _dir.replace(" -> ", ",").split(',')]
		(x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])

		if (x1 == x2 or y1 == y2):	# Part 1
			total_xy += Counter([(x, y) for x in range(x1, x2+1) for y in range(y1, y2+1)])
		else:						# Part 2
			total_diag += Counter([(x, y) for x, y in zip(range(x1, x2+1), range(y1, y2 + (-1 if y1 > y2 else 1), -1 if y1 > y2 else 1))])

	return (total_xy, total_diag)

with open("D5_Data.txt", 'r') as f:
	lines = f.read().splitlines()

count_pt1, count_pt2 = count_overlaps(lines)

print(f"There are {sum([v > 1 for v in count_pt1.values()])} occurances where straight lines overlap more than once.")
print(f"There are {sum([v > 1 for v in (count_pt1 + count_pt2).values()])} occurances where straight and diagonal lines overlap more than once.")
