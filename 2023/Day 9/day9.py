with open("2023/Day 9/day9_data.txt", 'r') as f:
    lines: list[str] = f.readlines()


# Part 1
extra_total: int = 0

for l in lines:
    nums: list[int] = [int(n) for n in l.split(' ')]
    extra_nums: list[list[int]] = [nums]
    diff_nums: list[int] = []

    while True:
        # Find difference in list values
        for i in range(len(nums)-1):
            diff_nums.append(nums[i+1] - nums[i])
        extra_nums.append(diff_nums)

        # If all numbers are 0
        if len(set(diff_nums)) == 1 and 0 in set(diff_nums):
            break
        
        nums = diff_nums
        diff_nums = []
    
    # Extrapolate
    # TODO: make it so that the numbers are stored before adding them
    rev_extra = list(reversed(extra_nums))
    for i in range(len(rev_extra)-1):
        extra_total += rev_extra[i][-1] + rev_extra[i+1][-1]


print(extra_total)
    