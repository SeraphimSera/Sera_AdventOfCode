with open("day5_data.txt") as f:
    data: list[str] = f.read().splitlines()

page_rule_raw: list[str] = data[:data.index('')]
page_order: list[str] = data[data.index('')+1:]
page_rule: dict[int, set[int]] = {}

for p in page_rule_raw:
    l, r = p.split('|')
    page_rule.setdefault(int(l), {int(r)}).add(int(r))

middle_num: int = 0
wrong_mid_num: int = 0

def check_page(i: int) -> bool:
    for j in page[i+1:]:
        if j not in page_rule[page[i]]:
            return False
    return True

# Put page into correct order then spit out middle page num
def fix_page(nums: list[int]) -> int:
    # - count occurances of other nums in each page num
    # - order in desc
    # - return mid num
    num_occ: dict[int, int] = {}

    for i in nums:
        total = 0
        for j in nums:
            total += j in page_rule[i]
        num_occ[i] = total
    
    num_order = sorted(num_occ.items(), key=lambda x: x[1], reverse=True)
    return num_order[int(len(num_order)/2)][0]
    

for page in page_order:
    page = [int(p) for p in page.split(',')]
    # Check all num after this index are in page rule
    for i in range(len(page)-1):
        if not check_page(i):
            # Part 2 goes here
            wrong_mid_num += fix_page(page)
            break     
    else:
        middle_num += page[int(len(page)/2)]

print(middle_num)
print(wrong_mid_num)
