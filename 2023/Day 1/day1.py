import re

with open("2023/Day 1/day1_data.txt", 'r') as f:
    lines = f.readlines()

# NOTE: At this point it might just be easier to use RegEx for the whole thing...
"""
Alternative for program: 
- Construct dictionary of zero to nine
- re.split the line by f"(\d|{'|'.join(zero_nine_dict)}+)" or something
- Remove all blanks in returned results somehow
- Create copy with string version stripped (list comp)
- Number sum check
    - Check list length, if 1, return with * 11
    - Else, get [0] and [-1]
    - Do for both versions, copy or not
- Sum them separately
- Return both answers
"""

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
    nums: list[int] = []
    print(re.split(r"(\d|[a-z]+)", line)[:-1])
    # Splits line into numbers and strings
    for result in re.split(r"(\d)", line)[:-1]:
        if result.isnumeric():
            nums.append(int(result))
        elif (num := list(filter(lambda n: n in result, strnums))):
            nums.append(strnums[num[0]])

    # Now, perform check to list and then add to numsum
    if len(nums) == 1:
        numsum += nums[0]*11
    else:
        numsum += nums[0] + nums[-1]

print(numsum)

# TODO: Merge part 1 and part 2 together? 
