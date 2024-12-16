from collections import defaultdict
puzzle = 'day-16/puzzle'

map = []
start = (0,0)
end=(0,0)
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


# count the minimum number of turns
def turn(start, target):
    if start == (0,0) or target == (0,0):
        return 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    start_index = directions.index(start)
    target_index = directions.index(target)
    clockwise = (target_index - start_index) % 4
    counterclockwise = (start_index - target_index) % 4
    return min(clockwise, counterclockwise)


# same dijkstra as first part except I am saving the cost depending on which way we face when we enter the cell
def dijkstra(map, end, start, facing):
    shortest = defaultdict(lambda: defaultdict(int))
    shortest[start][facing] = 0
    to_visit = [ (start, facing, 0) ]

    while(to_visit):
        ((x,y), (vx,vy), d) = to_visit.pop(0)

        if (x,y) == end:
            continue
        
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            rotate = turn((vx,vy),(dx,dy))
            (next_x, next_y) = (x+dx, y+dy)

            if map[next_y][next_x] == "#":
                continue
            
            next_d = d + 1 + 1000*rotate
            if (next_x, next_y) not in shortest or (dx,dy) not in shortest[(next_x, next_y)] or next_d < shortest[(next_x, next_y)][(dx,dy)]:
                shortest[(next_x, next_y)][(dx,dy)] = next_d
                to_visit.append(((next_x, next_y), (dx,dy), next_d))
    return shortest


# to find all the shortest path, I walk back from the end following the cost gradient, 
# accounting for the extra cost of turning.
def walk_back(map, end, shortest):
    visited = []
    kmin = min(shortest[end], key=lambda dir: shortest[end][dir], default=None)
    to_visit = [(end, kmin, shortest[end][kmin])]

    while(to_visit):
        ((x,y), (vx,vy), cost) = to_visit.pop()
        visited.append((x,y))

        for ((dx,dy),d_cost) in shortest[(x,y)].items():
            (next_x, next_y) = (x-dx, y-dy)

            if map[next_y][next_x] == "#":
                continue
            if (next_x, next_y) in visited:
                continue
            if d_cost+1000*turn((dx,dy),(vx,vy)) > cost:
                continue

            to_visit.append(((next_x, next_y), (dx,dy), d_cost))
    return visited


shortest = dijkstra(map, end, start, facing)
partof = walk_back(map, end, shortest)
print(len(partof))
