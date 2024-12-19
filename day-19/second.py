import re
from memoization import cached

puzzle = 'day-19/puzzle'

with open(puzzle) as f:
    patterns = re.findall(r'(\w+)', f.readline().strip())
    f.readline()
    designs =  [design.strip() for design in f.readlines()]

@cached
def is_valid(design):
    if not design:
        return 1, True
    return (sum(is_valid(design[len(pattern):])[0] for pattern in patterns if design.startswith(pattern)), True)

print(sum(is_valid(design)[0] for design in designs if is_valid(design)[1]))
