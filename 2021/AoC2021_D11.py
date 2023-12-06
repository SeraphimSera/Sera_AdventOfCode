import numpy as np

with open("D11_Data.txt", 'r') as f:
    data = f.read().splitlines()

array = np.array([[int(c) for c in l] for l in data])
flashes = steps = 0
flashed = set()

# Returns a clamped 3x3 slice of grid
def area(i: int) -> slice:
    def clamp(j): 
        return min(max(j, 0), len(data))
    return slice(clamp(i-1), clamp(i+2))

# Run until all flash
while len(array.flat) != len(flashed):
    array += 1
    flashed = set()
    while np.any(array > 9):        # While any number is above 9 in grid
        for y, x in zip(*np.where(array>9)):
            array[area(y), area(x)] += 1
            if steps < 100:         # Part 1
                flashes += 1
            flashed.add((y, x))     # Numbers flash once per step
        y, x = zip(*flashed)
        array[y, x] = 0
    steps += 1


print(f"After 100 steps, the octopuses flash {flashes} times.")
print(f"After {steps} steps, all octupuses flash.")
