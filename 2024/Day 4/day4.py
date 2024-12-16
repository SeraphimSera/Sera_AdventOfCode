KEY: str = "XMAS"

with open("day4_data.txt") as f:
    data: list[str] = f.read().splitlines()

# Find length of array, 
# Then flatten to 1D
line_len: int = len(data[0])
data: str = ''.join(data)
data_len: int = len(data)
key_len: int = len(KEY)


def check_dirs(x: int) -> int:
    dirs: list[slice] = [
        data[x:x+key_len], # Right
        data[x:x+(key_len*line_len):line_len], # Down
        data[x:x+key_len+(key_len*line_len):line_len+1], # Right down diag
        data[x:x+key_len-(key_len*line_len):-line_len+1] # Right up diag
    ]

    words: int = 0

    # NOTE: Assumes that key is not a palindrome
    for direction in dirs:
        if KEY in [direction, ''.join(reversed(direction))]:
            words += 1

    return words


total: int = 0
for i in range(data_len):
    total += check_dirs(i)

print(total)