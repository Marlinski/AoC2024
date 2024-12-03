import re
puzzle = 'day-3/puzzle'

res = 0
with open(puzzle, 'r') as file:
    for line in file:
        p = re.compile(r'mul\((\d+),(\d+)\)+')
        matches = p.findall(line)
        muls = [(int(a), int(b)) for a, b in matches]
        for a,b in muls:
            res += a*b
print(res)