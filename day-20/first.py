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


def inside(coord):
    (x,y) = coord
    return x >= 0 and x < cols and y >= 0 and y < rows


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
cheats = defaultdict(int)

# I search for every wall that sits right in between two cells in my shortest path
# if I remove the wall, the distance I saved by cheating is the difference between the 
# two cells.
for x,y in walls:
    left,right,top,bottom = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    if left not in walls and right not in walls and inside(left) and inside(right):
        save = abs(shortest[left]-shortest[right])-2
        cheats[save] += 1

    if top not in walls and bottom not in walls and inside(top) and inside(bottom):
        save = abs(shortest[top]-shortest[bottom])-2
        cheats[save] += 1
        

print(sum(v for k,v in cheats.items() if k >= 100))
    
