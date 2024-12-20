from collections import defaultdict

puzzle = 'day-20/puzzle'

walls=[]
start = (0,0)
end=(0,0)

with open(puzzle, 'r') as file:
    for y,line in enumerate(file):
        for x,c in enumerate(line.strip()):
            match c:
                case "S": start = (x,y)
                case "E": end = (x,y)
                case "#": walls.append((x,y))
        cols = x
    rows = y


def dijkstra(walls):
    shortest = { start: 0  }
    to_visit = [ (0, start) ]

    while(to_visit):
        (d, (x,y)) = to_visit.pop(0)

        if (x,y) == end:
            continue
        
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            (next_x, next_y) = (x+dx, y+dy)

            if next_x < 0 or next_x >= cols or next_y < 0 or next_y >= rows:
                continue

            if (next_x, next_y) in walls:
                continue
            
            next_d = d + 1
            if (next_x, next_y) not in shortest or next_d < shortest[(next_x, next_y)]:
                shortest[(next_x, next_y)] = next_d
                to_visit.append((next_d, (next_x, next_y)))
    return shortest


shortest = dijkstra(walls)
path = list(shortest.keys())
cheats = defaultdict(int)

# This cheat can basically lets us roam free within a distance of 20 cells.
# This time I compare all unique pair of cells in the shortest path.
# if their distance is less than 20 then we can cheat. 
for i,(x1,y1) in enumerate(path):
    for (x2,y2) in path[i:]:
        distance = abs(x1 - x2) + abs(y1 - y2)
        save = abs(shortest[(x1,y1)]-shortest[(x2,y2)])-distance
        if distance <= 20 and save >= 50:
            cheats[save] += 1 

print(sum(v for k,v in cheats.items() if k >= 100))
    
