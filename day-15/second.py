from enum import Enum
puzzle = 'day-15/puzzle'

map = []
moves = []
robot = (0,0)
walls = {}
boxes = []
debug = False

class Item(Enum):
    EMPTY = "."
    WALL = "#"
    ROBOT = "@"
    BOX_LEFT = "["
    BOX_RIGHT = "]"

# load puzzle
with open(puzzle, 'r') as file:
    for y,line in enumerate(file):
        if '#' in line:
            for x, c in enumerate(list(line.strip())):
                if c == "O":
                    boxes.append((2*x,y))
                if c == "@":
                    robot = (2*x,y)
                if c == "#":
                    walls[(2*x,y)] = True
                    walls[(2*x+1,y)] = True
            map.append(line.strip())
        else: 
            moves.append(line.strip())

(rows,cols) = (len(map), 2*len(map[0]))
moves = ''.join(moves)

def at(x,y):
    if (x,y) == robot:
        return (Item.ROBOT, None)
    if (x,y) in walls:
        return (Item.WALL, None)
    if (x,y) in boxes:
        return (Item.BOX_LEFT, boxes.index((x,y)))
    if (x-1,y) in boxes:
        return (Item.BOX_RIGHT, boxes.index((x-1,y)))
    else:
        return (Item.EMPTY, None)

def display():
    for y in range(rows):
        for x in range(cols):
            print(at(x,y)[0].value, end="")
            #print(at(x,y).value if at(x,y) is not Item.BOX_LEFT else boxes.index((x,y)), end="")
        print()
    print()

# let's go
def next_single(x,y, dir):
    match(dir):
        case "^":
            return (x,y-1) 
        case ">":
            return (x+1,y) 
        case "v":
            return (x,y+1) 
        case "<":
            return (x-1,y) 
        

def push_box_vertically(box,dir,do=True,depth=0):
    #if debug:
    #    print(f"pbv-{box}",">"*depth,dir,do)
    (x,y) = boxes[box]
    ((a,b),(c,d)) = ((x,y-1),(x+1,y-1)) if dir == "^" else ((x,y+1),(x+1,y+1))
    (li, lb)  = at(a,b)
    (ri, rb)  = at(c,d)
    checkleft = push_box_vertically(lb, dir, False,depth+1) if lb is not None else li is Item.EMPTY
    checkright = push_box_vertically(rb, dir, False,depth+1) if rb is not None else ri is Item.EMPTY
    #if debug:
    #    print(f"pbv-{box}",">"*depth, checkleft and checkright, "(",checkleft, checkright,")")

    if checkleft and checkright and do:
        push_box_vertically(lb, dir, True,depth+1) if lb is not None else ()
        push_box_vertically(rb, dir, True,depth+1) if rb is not None and not lb == rb else ()
        boxes[box] = (x,y-1) if dir == "^" else (x,y+1)
    return checkleft and checkright


def push_box_horizontally(box,dir, do=True):
    (x,y) = boxes[box]
    (a,b) = (x-1,y) if dir == "<" else (x+2,y)
    (ni, nb) = at(a,b)
    check = push_box_horizontally(nb, dir, False) if nb is not None else ni is Item.EMPTY
    if check and do:
        push_box_horizontally(nb, dir, True) if nb is not None else ()
        boxes[box] = (x-1,y) if dir == "<" else (x+1,y)
    return check


def push_box(box, dir):
    if dir == "<" or dir == ">":
        return push_box_horizontally(box,dir)
    else:
        return push_box_vertically(box,dir)


def update_robot(position, dir):
    global robot
    (x,y) = position
    (a,b) = next_single(x,y,dir)
    match at(a,b):
        case (Item.EMPTY, _):
            robot = (a,b)
        case (Item.BOX_LEFT | Item.BOX_RIGHT, box):
            if push_box(box, dir):
                robot = (a,b)
        case _: 
            pass
            
for i,dir in enumerate(moves):
    #debug = True if i > 193 else False
    if debug:
        print(i, ":", dir, robot)
        display()
        #input()
    update_robot(robot,dir)

display()

# The puzzle said: 
# For these larger boxes, distances are measured from the edge of the map to the closest edge of the box in question.
# So this should have been the correct answer
print(sum([100*(min(y, rows-y+1)) + (min(x,cols-x)) for (x,y) in boxes]))

# However this got me the second star, same gps as part 1
print(sum([100*y + x for (x,y) in boxes]))