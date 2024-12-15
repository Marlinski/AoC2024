puzzle = 'day-15/puzzle'

map = []
moves = []
robot = (0,0)

# load puzzle
with open(puzzle, 'r') as file:
    for line in file:
        if '#' in line:
            map.append(list(line.strip()))
        else: 
            moves.append(line.strip())
(rows,cols) = (len(map), len(map[0]))
moves = ''.join(moves)

# find starting position
for y in range(rows):
    for x in range(cols):
        if map[y][x] == "@":
            robot = (x,y)
            
def display():
    for y in range(rows):
        [print(map[y][x],end='') for x in range(cols)]
        print()
    print()

# let's go
def next(x,y, dir):
    match(dir):
        case "^":
            return (x,y-1) 
        case ">":
            return (x+1,y) 
        case "v":
            return (x,y+1) 
        case "<":
            return (x-1,y) 

def move_to(x,y,a,b):
    global robot
    map[b][a] = map[y][x]
    map[y][x] = "."
    if map[b][a] == "@":
        robot = (a,b) 

def update(position,dir):
    (x,y) = position
    (a,b) = next(x,y,dir)
    if map[b][a] == "#":
        return False
    if map[b][a] == ".":
        move_to(x,y,a,b)
        return True
    if map[b][a] == "O":
        has_moved = update((a,b),dir)
        if has_moved:
            move_to(x,y,a,b)
        return has_moved
            
for dir in moves:
    print(dir, robot)
    update(robot,dir)
    display()
    input()

res = 0
for y in range(rows):
    for x in range(cols):
        if map[y][x] == "O":
            res += 100*y + x
print(res)