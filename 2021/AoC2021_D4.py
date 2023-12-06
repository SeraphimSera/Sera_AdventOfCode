with open("D4_Data.txt", 'r') as f:
    data = f.read().split("\n\n")

nums = data.pop(0).split(',')   # All winning nums
bingo = nums[:5]                # Slowly populate from nums, but start with first five
nums = nums[5:]
data = dict(enumerate(data))

def check(sheet: str) -> bool:
    # Turn each str sheet into a list of lists of nums
    sheet = [r.split() for r in sheet.split('\n')]

    def horizontal(_sheet: list) -> bool:
        return any([all([n in bingo for n in row]) for row in _sheet])
    def vertical(_sheet: list) -> bool:
        return any([all([row[i] in bingo for row in _sheet]) for i in range(len(_sheet))])

    return horizontal(sheet) or vertical(sheet)

# Part 1 & 2
# Run until find sheet
sheets = []
for i in nums:
    if not len(_data := data.copy()):
        break
    for j, sheet in _data.items():
        if check(sheet):
            sheets.append((sheet, bingo.copy()))
            data.pop(j)
    bingo.append(i)


# Find and return sheet as flat list of nums, then filter bingo nums
def sheet_score(s: int):
    return (filter(lambda x: x not in sheets[s][1], [n for r in sheets[s][0].split('\n') for n in r.split()]), sheets[s][1])

print(sheets)

sheet_1 = sheet_score(0)
sheet_2 = sheet_score(-1)

print(f"The total score of the first winning sheet is {sum([int(n) for n in sheet_1[0]]) * int(sheet_1[1][-1])}")
print(f"The total score of the last winning sheet is {sum([int(n) for n in sheet_2[0]]) * int(sheet_2[1][-1])}")
