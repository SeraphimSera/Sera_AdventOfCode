KEY: str = "XMAS"

with open("day4_data.txt") as f:
    data: list[str] = f.read().splitlines()

# Construct into 2D array
# NOTE: Assumes array is square
arr_len: int = len(data)
key_len: int = len(KEY)


def return_result(result: str) -> bool:
    return KEY in [result, ''.join(reversed(result))]

def check_right(x: int, y: int) -> bool:
    result: str = data[y][x:x+key_len]
    return return_result(result)

def check_down(x: int, y: int) -> bool:
    if y+key_len < arr_len:
        result: str = ''.join([data[i][x] for i in range(y, y+key_len)])
        return return_result(result)
    return False

def check_right_down(x: int, y: int) -> bool:
    if y+key_len < arr_len and x+key_len < arr_len:
        result: str = ''.join(
            [data[i][j] for i, j in zip(
                range(y, y+key_len), range(x, x+key_len)
            )])
        return return_result(result)
    return False

def check_right_up(x: int, y: int) -> bool:
    if y-key_len >= 0 and x+key_len < arr_len:
        result: str = ''.join(
            [data[i][j] for i, j in zip(
                range(y-key_len, y), range(x, x+key_len)
            )])
        return return_result(result)
    return False
    

# def check_dirs(x: int) -> int:
#     dirs: list[slice] = [
#         data[x:x+key_len], # Right
#         data[x:x+(key_len*line_len):line_len], # Down
#         data[x:x+key_len+(key_len*line_len):line_len+1], # Right down diag
#         data[x:x+key_len-(key_len*line_len):-line_len+1] # Right up diag
#     ]

#     words: int = 0

#     NOTE: Assumes that key is not a palindrome
#     for direction in dirs:
#         if KEY in [direction, ''.join(reversed(direction))]:
#             words += 1

#     return words


total: int = 0
for y in range(arr_len):
    for x in range(arr_len):
        total += check_right(x, y)
        total += check_down(x, y)
        total += check_right_down(x, y)
        total += check_right_up(x, y)

print(total)