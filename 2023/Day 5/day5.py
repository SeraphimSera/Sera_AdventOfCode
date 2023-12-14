with open("2023/Day 5/day5_data.txt", 'r') as f:
    lines: list[str] = f.read()

# Clean input
seeds, *almanac = lines.split('\n\n')
seeds: list[int] = [int(s) for s in seeds.lstrip("seeds: ").split(' ')]
# Turn almanac into a list of lists, with each list having multiple sets of three numbers
# (Destination range, source range, range length)
almanac: list[list[int, int, int]] = [a.split(':')[1:][0].split('\n')[1:] for a in almanac]

def seed_map(_seeds: list[int], location: int = float("inf")) -> int: 
    for seed in _seeds:
        # Check each entry in each map
        for maps in almanac:
            for entry in maps:
                dest, entry, steps = [int(i) for i in entry.split(' ')]

                if seed in range(entry, entry+steps):
                    # seed = destination value + (number of steps taken plus entry value - original entry value)
                    seed = dest+(seed-entry)
                    break
        # After changing the value of seed via the map, the value *should* be the location value...
        if location > seed:
            location = seed

    return location
    
# Part 1
print(seed_map(seeds))
# Part 2
seeds = [range(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
location = seed_map(seeds[0])
for seed_range in seeds[1:]:
    location = seed_map(seed_range, location)
print(location)

