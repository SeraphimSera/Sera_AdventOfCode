num_left: list[int] = []
num_right: list[int] = []
nums: dict[int, int] = {}
total: int = 0

# Part 1
with open("day1_data.txt") as f:
    while line := f.readline():
        left, right = line.split()
        num_left.append(int(left))
        num_right.append(int(right))

for i, j in zip(sorted(num_left), sorted(num_right)):
    total += abs(i-j)

print(total)

# Part 2
total = 0
for i in num_left:
    total += nums.setdefault(i, num_right.count(i))*i

print(total)
