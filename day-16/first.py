puzzle = 'day-16/puzzle'

map = []
start = (0,0)
end=(0,0)
position=(0,0)
facing=(1,0)

# load puzzle
with open(puzzle, 'r') as file:
    for y,line in enumerate(file):
        map.append(list(line.strip()))
        start = (map[-1].index("S"),y) if "S" in map[-1] else start
        end = (map[-1].index("E"),y) if "E" in map[-1] else end
(rows,cols) = (len(map), len(map[0]))
map[start[1]][start[0]] = "."
map[end[1]][end[0]] = "."

def display(position, dir):
    for y,row in enumerate(map):
        for x,cell in enumerate(row):
            if (x,y) == position:
                match dir:
                    case (1,0) : print(">",end="")
                    case (0,-1) : print("^",end="")
                    case (-1,0) : print("<",end="")
                    case (0,1) : print("v",end="")
            elif (x,y) == end:
                print("E",end="")
            else:
                print(cell,end="")
        print()

display(start, facing)

def turn(start, target):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    start_index = directions.index(start)
    target_index = directions.index(target)
    clockwise = (target_index - start_index) % 4
    counterclockwise = (start_index - target_index) % 4
    return min(clockwise, counterclockwise)


def dijkstra():
    shortest = { start: 0  }
    to_visit = [ (0, start, facing) ]

    while(to_visit):
        (d, (x,y), (vx,vy)) = to_visit.pop(0)

        if (x,y) == end:
            continue
        
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            rotate = turn((vx,vy),(dx,dy))
            (next_x, next_y) = (x+dx, y+dy)

            if map[next_y][next_x] == "#":
                continue
            
            next_d = d + 1 + 1000*rotate
            if (next_x, next_y) not in shortest or next_d < shortest[(next_x, next_y)]:
                shortest[(next_x, next_y)] = next_d
                to_visit.append((next_d, (next_x, next_y), (dx,dy)))
    return shortest

shortest = dijkstra()
print(shortest[end])