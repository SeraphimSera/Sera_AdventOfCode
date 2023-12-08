import re

with open("2023/Day 2/day2_data.txt", 'r') as f:
    lines: list[str] = f.readlines()

red_limit = 12
green_limit = 13
blue_limit = 14

id_sum = power_sum = 0

for i, l in enumerate(lines, start=1):
    # Turn text into a list of dictionaries, containing data per set
    game: list[dict[str, int]] = [
        {k: int(v) for v, k in re.findall(r"(\d+) (red|green|blue)", s)}
        for s in l.split(';')
    ]
    
    # Find highest value of any colored cube in all given sets
    red = green = blue = 0
    for g in game:
        game_red = g.get("red", 1)
        game_green = g.get("green", 1)
        game_blue = g.get("blue", 1)

        red = (game_red if game_red > red else red)
        green = (game_green if game_green > green else green)
        blue = (game_blue if game_blue > blue else blue)

    # Part 1
    # Find out which games are possible from given limit of number of cubes
    # Then sum game ID
    if not any([
        red_limit < red,
        green_limit < green,
        blue_limit < blue
    ]):
        id_sum += i

    # Part 2
    # Find which value is the highest in each game
    # After finding all highest values, multiply and add to total sum
    power_sum += red * green * blue
    
print(id_sum)
print(power_sum)
