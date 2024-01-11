from typing import Iterator
from collections import Counter

with open("2023/Day 8/day8_data.txt", 'r') as f:
    lines: list[str] = f.readlines()

# Parse input
lines = [l.strip() for l in lines if l.strip() != '']
dir: str = lines.pop(0)

desert_map: dict[str, tuple[str, str]] = {
    k: tuple(v.strip('()').split(', ')) 
    for k, v in [
        [_ for _ in l.split(' = ')] 
        for l in lines
    ]
}


# Part 1
current_node: str = "AAA"
steps: int = 0

while current_node != "ZZZ":
    for d in dir:
        current_node = desert_map[current_node][d=='R']
    steps += len(dir)

print(steps)


# Part 2
def least_common_multiple(num: int) -> dict[int, int]:
    def prime_gen() -> Iterator[int]:
        yield 2
        n: int = 3
        while True:
            if not any([n%i==0 for i in range(2, n)]):
                yield n
            n += 1

    multiples: Counter = Counter()

    for i in prime_gen():
        if num == 1:
            return multiples
        while num != 1:
            if num % i == 0:
                multiples[i] += 1
                num /= i
            else:
                break
        

steps = 0
current_nodes: set[str] = set(filter(lambda n: n[2] == 'A', desert_map))
ending_nodes: set[str] = set(filter(lambda n: n[2] == 'Z', desert_map))

node_lcm: list[dict[int, int]] = []
node_steps: list[int] = []

# Find least common multiples of all nodes
for node in current_nodes:
    steps = 0
    while node not in ending_nodes:
        for d in dir:
            node = desert_map[node][d=='R']
        steps += len(dir)
    node_lcm += [tuple(i) for i in least_common_multiple(steps).items()]
    node_steps += [steps]

prod: int = 1
for lcm, i in set(node_lcm):
    prod *= lcm**i

print(prod)

# # Part 2, alternative
# import math
# print(math.lcm(*node_steps))

