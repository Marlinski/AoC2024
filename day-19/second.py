import re
from memoization import cached

puzzle = 'day-19/puzzle'

with open(puzzle) as f:
    patterns = re.findall(r'(\w+)', f.readline().strip())
    f.readline()
    designs =  [design.strip() for design in f.readlines()]

@cached
def is_valid(design):
    return 1 if not design else sum(is_valid(design[len(pattern):]) for pattern in patterns if design.startswith(pattern))

print(sum(is_valid(design) for design in designs))
