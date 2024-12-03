import re
puzzle = 'day-3/puzzle'

res = 0
_do = True
with open(puzzle, 'r') as file:
    for line in file:
        p = re.compile(r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))')
        matches = re.findall(p, line)
        for m in matches:
            if m[0] == "do()":
                _do = True
            if m[0] == "don't()":
                _do = False
            if m[0].startswith("mul") and _do:
                res += int(m[1])*int(m[2])
print(res)