with open("2023/Day 6/day6_data.txt", 'r') as f:
    lines: list[str] = f.readlines()

times: list[int] = lines[0].split()[1:]
dists: list[int] = lines[1].split()[1:]

# Part 1
def record_wins(t: int, d: int) -> int:
    """
    Finds number of different ways you can win
    based on total time and minimum distance.
    """
    wins: int = 0

    for i in range(1, t):
        if i*(t-i) > d:
            wins += 1

    return wins


win_prod: int = 1
for t, d in zip(times, dists):
    win_prod *= record_wins(int(t), int(d))
    
print(win_prod)
# Part 2
print(record_wins(int(''.join(times)), int(''.join(dists))))
