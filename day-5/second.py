from collections import defaultdict

puzzle = 'day-5/puzzle'
rules = defaultdict(list)

def valid(update):
    for (i, after) in enumerate(update):
        for before in update[0:i]:
            if after not in rules[before]:
                return False
    return True


def reorder(update):
    reordered = []
    for (i, to_insert) in enumerate(update):
        for (j,current) in enumerate(reordered[0:i]):
            if current in rules[to_insert]:
                reordered.insert(j, to_insert)
                break
        else:
            reordered.append(to_insert) 

    return reordered
        
res=0
with open(puzzle, 'r') as file:
    for line in file:
        if "|" in line:
            rule = line.strip().split("|")
            rules[rule[0]].append(rule[1])
        if "," in line:
            update = line.strip().split(",")
            if not valid(update):
                reordered = reorder(update)
                res += int(reordered[len(reordered)//2])
                continue
print(res)

