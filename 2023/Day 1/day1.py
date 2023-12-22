import re

with open("2023/Day 1/day1_data.txt", 'r') as f:
    lines: list[str] = f.readlines()

strnums: dict[str, int] = {
    k: v for v, k in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
}

sum1 = sum2 = 0

def first_last(p: list[int]) -> int:
    if len(p) == 1:
        return p[0]*11
    return p[0]*10 + p[-1]

for l in lines:
    # Find all numbers
    results: list[str] = [
        r for r in re.findall(
            fr"(?=(\d|{'|'.join(strnums)}))",
            l
        ) if r not in ['', '\n']
    ]

    # Filter results into part 1 and 2 answers
    part1: list[int] = [int(r) for r in results if r.isnumeric()]
    part2: list[int] = [int(r) if r.isnumeric() else strnums[r] for r in results]

    # Sum for part 1 and 2
    sum1 += first_last(part1)
    sum2 += first_last(part2)
        
print(sum1)
print(sum2)
