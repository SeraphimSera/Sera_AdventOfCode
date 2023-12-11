with open("2023/Day 4/day4_data.txt", 'r') as f:
    lines = f.readlines()

card_sum: int = 0
copies: dict[int, int] = {key: 1 for key in range(len(lines))}

for i, l in enumerate(lines):
    # Part 1
    win, nums = [set(s.split()) for s in l.split(':')[1].strip().split('|')]
    matches: int = len(win.intersection(nums))
    card_sum += int(2**(matches-1))

    # Part 2
    for j in range(i+1, i+1+matches):
        copies[j] += 1*copies[i]

print(card_sum)
print(sum(copies.values()))
