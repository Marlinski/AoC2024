puzzle = 'day-12/puzzle'

map = []
with open(puzzle, 'r') as file:
    for line in file:
        map.append(list(line.strip()))
(rows,cols) = (len(map), len(map[0]))


def is_inside(x,y):
    return x >= 0 and x < cols and y >= 0 and y < rows
def is_outside(x,y):
    return not is_inside(x,y)


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

# compute area and sides
area =  [0] * id
sides = [0] * id
def is_diff(X,Y):
    (x1,y1) = X
    (x2,y2) = Y
    if is_outside(x2,y2):
        return True
    return tag[y1][x1] != tag[y2][x2]

def is_same(X,Y):
    return not is_diff(X,Y)

for y, row in enumerate(tag):
    for x, region in enumerate(row):
        (X, t,b,l,r,tl,tr,bl,br) = ((x,y),(x,y-1),(x,y+1),(x-1,y),(x+1,y),(x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1))
        area[region] += 1
        if is_diff(X,t) and (is_diff(X,l) or (is_same(X,l) and is_same(X,tl))):
            sides[region] += 1

        if is_diff(X,b) and (is_diff(X,l) or (is_same(X,l) and is_same(X,bl))):
            sides[region] += 1

        if is_diff(X,l) and (is_diff(X,t) or (is_same(X,t) and is_same(X,tl))):
            sides[region] += 1

        if is_diff(X,r) and (is_diff(X,t) or (is_same(X,t) and is_same(X,tr))):
            sides[region] += 1

print(sum(area[i] * sides[i] for i in range(id)))

