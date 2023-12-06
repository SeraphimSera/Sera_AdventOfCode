# I give up.
with open("D6_Data.txt") as f:
	data = tuple(map(int, f.read().split(',')))

fish = [data.count(i) for i in range(9)]
for i in range(256):
    num = fish.pop(0)
    fish[6] += num
    fish.append(num)
    assert len(fish) == 9

print(sum(fish))

"""
from __future__ import annotations
from functools import lru_cache

with open("D6_Data.txt") as f:
	nums = tuple(map(int, f.read().split(',')))


Deprecated due to inefficacy.

num_range = range(8)

def countdown(days: int, _nums) -> list:
    if days:
        return countdown(days - 1, [n-1 if n-1 in num_range else 6 for n in _nums] + [8] * len(tuple(filter(lambda n: n == 0, _nums))))
    return _nums 


# First, figure out state of fish after n days.
# start = num_range.index(n)
# num_range[(days+start)%len(num_range)]

# Then, figure out days where fish has produced new animals.
# range(start, days+start, len(num_range))

# Finally,?
num_range = list(reversed(range(7)))
nums = (3,4,3,1,2)

def countdown(days: int, _nums: list): -> list
	l1 = []
	l2 = []

	for i in nums:
		start = num_range.index(i)

		# Append the mutated number
		l1.append(num_range[(days+start)%len(num_range)])

		# If the number will mutate at least once
		if days+start // len(num_range):
			for j in range(start, days+start, len(num_range)):
				l2.append([])


#print(f"After 80 days, there would be {countdown(80, nums)} lanternfish.")
#print(f"After 256 days, there would be {countdown(256, nums)} lanternfish.")"""