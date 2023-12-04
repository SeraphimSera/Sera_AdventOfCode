import re

with open("2023/Day 1/day1_data.txt", 'r') as f:
    lines = f.readlines()

# Part 1
# Hold sum of all numbers
numsum: int = 0

for line in lines:
    # First, find all the numbers in the given line
    nums = [n for n in line if n.isnumeric()]
    # If there is only one number, assume it is both start and end
    if len(nums) == 1:
        numsum += int(nums[0]*2)
    # Otherwise, return first and last numbers
    else:
        numsum += int(nums[0] + nums[-1])

# Return final sum
print(numsum)


# Part 2
numsum: int = 0
strnums: dict[str, int] = {
    k: v for v, k in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
}

for line in lines:
    # Splits line into numbers and strings
    re.split(r"(\d)", line)[:-1]
    
    

print(numsum)