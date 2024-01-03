from typing import Literal, Iterable

with open("2023/Day 8/day8_data.txt", 'r') as f:
    lines: list[str] = f.readlines()

lines = [l.strip() for l in lines if l.strip() != '']
dir: str = lines.pop(0)

desert_map: dict[str, tuple[str, str]] = {k: tuple(v.strip('()').split(', ')) for k, v in [[_ for _ in l.split(' = ')] for l in lines]}

current_node: str = "AAA"
steps: int = 0

# Part 1
while current_node != "ZZZ":
    for d in dir:
        current_node = desert_map[current_node][d=='R']
        steps += 1

print(steps)

# Part 2
# steps = 0
# current_nodes: Iterable[str] = filter(lambda n: n[2] == 'A', desert_map)
# ending_nodes: Iterable[str] = set(filter(lambda n: n[2] == 'Z', desert_map))

# while current_nodes.difference(ending_nodes):
#     for d in dir:
#         current_nodes = {desert_map[n][d=='R'] for n in current_nodes}
#         steps += 1

# print(steps)
    
