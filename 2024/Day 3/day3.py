import re
import math

with open("day3_data.txt") as f:
    data = f.read()

part1_result: list[re.Match] = re.findall(r"mul\((\d+,\d+)\)", data)
part2_result: list[re.Match] = re.findall(r"(do\(\)|don't\(\)|mul\((\d+,\d+)\))", data)

# Part 1
print(sum([math.prod([int(j) for j in i.split(',')]) for i in part1_result]))

# Part 2
do: bool = True
total: int = 0

for m in part2_result:
    if m[0] == "do()":
        do = True
        continue
    elif m[0] == "don't()":
        do = False
        continue
    
    if do:
        i, j = m[1].split(',')
        total += int(i) * int(j)

print(total)



    