puzzle = 'day-12/puzzle'

map = []
with open(puzzle, 'r') as file:
    for line in file:
        map.append(list(line.strip()))
(rows,cols) = (len(map), len(map[0]))

def is_inside(x,y):
    return x >= 0 and x < cols and y >= 0 and y < rows

def is_outside(x,y):
    return x < 0 or x >= cols or y < 0 or y >= rows


# tag all regions
id = 0
tag = [[None for _ in row] for row in map]
def visit(x,y,region):
    tag[y][x] = region
    for (nextx, nexty) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if (is_inside(nextx, nexty) and tag[nexty][nextx] is None and map[y][x] == map[nexty][nextx]):
            visit(nextx, nexty,region)


for y, row in enumerate(tag):
    for x, region in enumerate(row):
        if tag[y][x] is None:
            visit(x,y,id)    
            id += 1


# compute area and perimeter for each region
area =  [0] * id
perimeter = [0] * id
for y, row in enumerate(tag):
    for x, region in enumerate(row):
        area[region] += 1
        for (nextx, nexty) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if (is_outside(nextx,nexty) or region != tag[nexty][nextx]):
                perimeter[region] += 1

print(sum(area[i] * perimeter[i] for i in range(id)))

