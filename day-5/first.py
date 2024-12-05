from collections import defaultdict

puzzle = 'day-5/puzzle'
rules = defaultdict(list)

def valid(update):
    for (i, after) in enumerate(update):
        for before in update[0:i]:
            if after not in rules[before]:
                return False
    return True

res=0
with open(puzzle, 'r') as file:
    for line in file:
        if "|" in line:
            rule = line.strip().split("|")
            rules[rule[0]].append(rule[1])
        if "," in line:
            update = line.strip().split(",")
            if not valid(update):
                continue
            res += int(update[len(update)//2])

print(res)

