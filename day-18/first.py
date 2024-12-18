import re

puzzle = 'day-18/puzzle'

start = (0,0)
end=(7,7)
bytes = []
step=1024
(rows,cols) = (71,71)

for (x,y) in re.findall(r'(\d+),(\d+)', open(puzzle).read()):
    bytes.append((int(x),int(y)))

def is_outside(x,y):
    return x < 0 or x >= cols or y < 0 or y >= rows

def dijkstra():
    shortest = { start: 0  }
    to_visit = [ (0, start) ]

    while(to_visit):
        (d, (x,y)) = to_visit.pop(0)

        if (x,y) == end:
            continue
        
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            (next_x, next_y) = (x+dx, y+dy)

            if (next_x,next_y) in bytes[:step]:
                continue

            if is_outside(next_x,next_y):
                continue
            
            next_d = d + 1
            if (next_x, next_y) not in shortest or next_d < shortest[(next_x, next_y)]:
                shortest[(next_x, next_y)] = next_d
                to_visit.append((next_d, (next_x, next_y)))
    return shortest

shortest = dijkstra()
print(shortest[(70,70)])