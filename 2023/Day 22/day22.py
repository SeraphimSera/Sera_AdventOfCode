with open("2023/Day 22/day22_data.txt", 'r') as f:
    lines: list[str] = f.readlines()

# Outer list is indexed by z,
# Second list is indexed by y,
# Third list is indedex by x
brick_grid: dict[str, dict[str, dict[str, str]]] = dict()


# Lay bricks down
for l in lines:
    l = l.strip().split('~')
    x1, y1, z1 = [int(c) for c in l[0].split(',')]
    x2, y2, z2 = [int(c) for c in l[1].split(',')]

    z_range = range(z1, z2)
    y_range = range(y1, y2)
    x_range = range(x1, x2)
    if z1 == z2:
        z_range = [z1]
    if y1 == y2:
        y_range = [y1]
    if x1 == x2:
        x_range = [x1]
    
    for z in z_range:
        if not brick_grid.get(z):
            brick_grid[z] = {}
        for y in y_range:
            if not brick_grid[z].get(y):
                brick_grid[z][y] = {}
            for x in x_range:
                brick_grid[z][y][x] = 'B'

# Fill in gaps
z_max = max(brick_grid.keys())
y_max = max(brick_grid.values().keys())
x_max = max(brick_grid.values().values().keys())
