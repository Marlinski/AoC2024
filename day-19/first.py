import re

puzzle = 'day-19/puzzle'

with open(puzzle) as f:
    patterns = re.findall(r'(\w+)', f.readline().strip())
    f.readline()
    designs =  [design.strip() for design in f.readlines()]

def is_valid(design):
    return True if not design else any(design.startswith(pattern) and is_valid(design[len(pattern):]) for pattern in patterns)

print(sum([1 if is_valid(design) else 0 for design in designs]))

    
