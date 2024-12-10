from memoization import cached

puzzle = 'day-10/puzzle'
map = []

with open(puzzle, 'r') as file:
    for line in file:
        map.append([int(i) for i in list(line.strip())])
(rows,cols) = (len(map), len(map[0]))


def is_inside(x,y):
    return x >= 0 and x < cols and y >= 0 and y < rows


@cached
def explore(x,y):
    if map[y][x] == 9:
        return 1
    
    ends = 0
    sides = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    for (next_x, next_y) in sides:
        if is_inside(next_x, next_y) and map[next_y][next_x] == map[y][x] + 1:
            ends += explore(next_x, next_y)
    return ends


trailheads = []
for (y, row) in enumerate(map):
    for (x, height) in enumerate(map[y]):
        if height == 0:
            trailheads.append(explore(x,y))
    
print(sum(trailheads))