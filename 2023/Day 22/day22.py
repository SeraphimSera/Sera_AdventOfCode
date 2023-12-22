with open("2023/Day 22/day22_data.txt", 'r') as f:
    lines: list[str] = f.readlines()

brick_grid: dict[int, dict[int, tuple[int, int]]] = {}
brick_grid_zyx: dict[int, list[tuple[int, int, int]]] = {}
brick_grid_collapsed: list[list[list[int]]] = []


# Lay bricks down by coordinate
for i, l in enumerate(lines):
    l = l.strip().split('~')
    x1, y1, z1 = [int(c) for c in l[0].split(',')]
    x2, y2, z2 = [int(c) for c in l[1].split(',')]

    z_range = range(z1, z2) if z1 != z2 else [z1]
    y_range = range(y1, y2) if y1 != y2 else [y1]
    x_range = range(x1, x2) if x1 != x2 else [x2]

    for z in z_range:
        if not brick_grid.get(z):
            brick_grid[z] = {}

        for y in y_range:
            for x in x_range:
                brick_grid[z][i] = (y, x)
        
        if not brick_grid_zyx.get(i):
            brick_grid_zyx[i] = [(z, y, x)]
        else:
            brick_grid_zyx[i].append((z, y, x))

x_max = max([yx[0] for b in brick_grid.values() for yx in b.values()])
y_max = max([yx[1] for b in brick_grid.values() for yx in b.values()])

# Place bricks in grid
for i in sorted(brick_grid):
    brick_yx = list(sorted(brick_grid[i].items(), key=lambda y: y[1][0]))
    brick, yx = brick_yx.pop(0)
    layer: list[list[int]] = []

    for y in range(1, y_max+1):
        row: list[int] = []
        for x in range(1, x_max+1):
            if yx != (y, x):
                row.append(0)
            else:
                row.append(brick)
                brick, yx = brick_yx.pop(0) if len(brick_yx) != 0 else (0, 0)
        layer.append(row)
    brick_grid_collapsed.append(layer)


# Simulate disintegrations
disint: int = 0
vert_bricks: set[int] = set([b for b, zyx in brick_grid_zyx.items() if not all([zyx[0][0]==z for z, *_ in zyx])])
one_brick_sup: set[int] = set()

for z in range(len(brick_grid_collapsed)):
    for y in range(y_max):
        for x in range(x_max):
            b = brick_grid_collapsed[z][y][x]
            # Check if vertical brick is supporting anything
            if b in vert_bricks:
                _, _y, _x = brick_grid_zyx[b][0]
                if brick_grid_collapsed[max([z for z, *_ in brick_grid_zyx[b]])+1][_y][_x] == 0:
                    disint += 1
                    vert_bricks.remove(b)
            elif b in brick_grid_zyx:
                for brick in brick_grid_zyx[b]:
                    if all([brick_grid_collapsed[z+1][y][x]==0 for z, y, x in brick_grid_zyx[b]]):
                        disint += 1
                    
            
            del brick_grid_zyx[b]