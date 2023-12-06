test = {'dark salmon': 5, 'test': 3}
rules = {'dark salmon': 2, 'test': 0}

# This should print 18: 5 + (5 * 2) + 3 + (3 * 0) = 18

def unnester(_dict):
    if isinstance(_dict, dict):
        for k, v in _dict.items():
    
    else: # Usually means _dict is an int



print(unnester(test))