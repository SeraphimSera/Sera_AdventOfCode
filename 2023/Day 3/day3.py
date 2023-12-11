import re

with open("2023/Day 3/day3_data.txt", 'r') as f:
    lines = f.read()

symbols: set[str] = set(re.findall(r"[^\d.\n]", lines))
lines: list[str] = lines.split('\n')

symbol_sum: int = 0
gear_nums: dict[tuple[int, int], list[int]] = {}

# Part 1 and 2
def check_symbol(match: re.Match) -> tuple[int, int] | bool:
    """
    Checks if a number at a given location has symbols next to it.

    If the symbol is an asterisk, return a tuple of (row, index) instead.
    """

    col_start: int = max(match.start(0)-1, 0)
    row_start: int = max(i-1, 0)

    _lines: list = [
        l[col_start:min(match.end(0)+1, len(l))] 
        for l in lines[row_start:min(i+2, len(lines))]
    ]

    # Check if asterisk in lines
    for row, l in enumerate(_lines, start=row_start):
        if '*' in l:
            return (row, col_start + l.find('*'))

    return any([s in ''.join(_lines) for s in symbols])

for i, line in enumerate(lines):
    for m in re.finditer(r"\d+", line):
        if (s := check_symbol(m)):
            symbol_sum += int(m[0])
            if isinstance(s, tuple):
                gear_nums[s] = [*gear_nums.get(s, [])] + [int(m[0])] 

print(symbol_sum)
print(sum(i*j for i, j in filter(lambda x: len(x) == 2, gear_nums.values())))
