
with open("day2_data.txt") as f:
    lines: list[str] = f.read().splitlines()

def check_safe(line: list[int], dampen: bool = False) -> bool:
    i: int = 0

    # Increment 3 at most
    while i < len(line)-1:
        safe = range(line[i+1]-3, line[i+1]+4)
        if line[i] == line[i+1] or line[i] not in safe:
            if dampen:
                return attempt_dampen(line)
            return False
        i += 1

    # Check if all increasing or decreasing
    if not line in [sorted(line), sorted(line, reverse=True)]:
        if dampen:
            return attempt_dampen(line)
        return False

    return True

def attempt_dampen(line: list[int]) -> bool: 
    for i in range(len(line)):
        l: list = line.copy()
        l.pop(i)
        
        if check_safe(l):
            return True
    
    return False


# Part 1 and 2
safe_1: int = 0
safe_2: int = 0

for l in lines:
    l = [int(i) for i in l.split()]
    safe_1 += check_safe(l)
    safe_2 += check_safe(l, dampen=True)

print(safe_1)
print(safe_2)