import tqdm

with open("2023/Day 5/day5_data.txt", 'r') as f:
    lines: list[str] = f.read()

# Clean input
seeds, *almanac = lines.split('\n\n')
seeds: list[int] = [int(s) for s in seeds.lstrip("seeds: ").split(' ')]
# Turn almanac into a list of lists, with each list having multiple sets of three numbers
# (Destination range, source range, range length)
almanac = [a.split(':')[1:][0].split('\n')[1:] for a in almanac]

almanac: list[list[tuple[int, int, int]]] = [
    [
        tuple(int(i) for i in entry.split(' '))
        for entry in maps
    ]
    for maps in almanac
]

def seed_map(_seeds: list[int], location: int = float("inf")) -> int: 
    for seed in _seeds:
        # Check each entry in each map
        for maps in almanac:
            for entry in maps:
                end, start, steps = entry

                if seed in range(start, start+steps):
                    # seed = destination value + (number of steps taken plus entry value - original entry value)
                    seed = end+(seed-start)
                    break
        # After changing the value of seed via the map, the value *should* be the location value...
        if location > seed:
            location = seed

    return location

# Sebby's solution: Iterate backwards, duh
def rev_seed_map(_seeds: list[tuple[int, int]]) -> int:
    _alm = almanac.copy()
    _seeds.sort()
    loc_maps: list[dict[int, int]] = []

    # Creates a dict of int, int
    # For each corresponding value in each map of almanac
    for maps in tqdm.tqdm(reversed(_alm)):
        loc_map: dict[int, int] = {}
        for entry in tqdm.tqdm(maps):
            start, end, steps = entry
            loc_map.update({i: end+i for i in tqdm.trange(start, start+steps)}) 
        loc_maps.append(loc_map)

    

    # for start, steps in _seeds.pop():
    #     for k, v in loc_map.items():
    #         if start <= v <= start+steps:
    #             return k

        
# Part 1
print(seed_map(seeds))

# Part 2
print(rev_seed_map([(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]))
