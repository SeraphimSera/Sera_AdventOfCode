import collections

moves = collections.Counter()

with open("D2_Data.txt", "r") as f:
    for d, i in [d.split() for d in f.read().splitlines()]:
        i = int(i)
        
        moves[d] += i    # Part 1
        # Part 2
        if d == "forward":
            moves["depth"] += i * moves["aim"]
        if d in ("down", "up"):
            moves["aim"] += i * {"down": 1, "up": -1}[d]

print(f"Part 1: Final displacement is {moves['forward'] * (moves['down'] - moves['up'])}")
print(f"Part 2: Final displacement is {moves['forward'] * moves['depth']}")
