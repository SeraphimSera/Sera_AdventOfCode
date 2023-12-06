from collections import defaultdict

# Data sorting
with open("D12_Data.txt", 'r') as f:
    data: list[str] = f.read().splitlines()

routes: defaultdict[str, set[str]] = defaultdict(set)
for l in data:
    i, j = l.split('-')
    routes[i].add(j)
    routes[j].add(i)

for v in routes.values():
    v.discard("start")
routes.pop("end")

print(routes)

# Part 1
travel: list[str] = []          # List of all possible moves taken

def go(
    cave: set[str], 
    small: set[str] = set(), 
    move: list[str] = ["start", ]
):
    for r in cave.difference(small):        # Prevents being trapped by small cave
        if len(routes[r]) == 1:
            continue
        # Lookahead head reset
        elif r == "end":
            travel.append(f"{', '.join(move)}, end") 
            go(routes["start"])
            continue
        # Can only visit small cave once
        elif r.islower():
            small.add(r)
        go(routes[r], small, move + [r, ])

print()
go(routes["start"])
print(sorted(travel))
