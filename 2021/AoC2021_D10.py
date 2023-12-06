with open("D10_Data.txt", 'r') as f:
    data = f.read().splitlines()

total_1 = total_2 = 0
scores = []
patterns = ["()", "[]", "{}", "<>"]
left, right = zip(*patterns)    # Honestly, if I was smarter or less lazy, 
                                # I could do without this

for line in data:
    # Count valid/invalid bracketing
    # Part 1
    count = ""
    for c in line:
        if c in left:
            count += c
        elif count[-1] == {r: l for l, r in patterns}[c]:
            count = count[:-1]
        else:
            total_1 += {')': 3, ']': 57, '}': 1197, '>': 25137}[c]
            break
                
    # All brackets face left, line is not corrupted
    # Part 2
    else:
        for i in reversed([left.index(c) + 1 for c in count]):
            total_2 = (total_2 * 5) + i
        scores.append(total_2)
        total_2 = 0

print(f"In part 1, total SynError score tallies up to {total_1}.")
print(f"In part 2, the middle score is {sorted(scores)[len(scores)//2]}.")
