import re
import math
from collections import defaultdict

puzzle = 'day-14/puzzle-test'

with open(puzzle, 'r') as file:
    content=file.read()
    pattern = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")
    matches = pattern.findall(content)
    robots = [
        (int(x),int(y),int(vx),int(vy))
        for x,y,vx,vy in matches
    ]
    #cols = 101
    #rows = 103
    cols = 11
    rows = 7

counts = defaultdict(int)
def display():
    for y in range(rows):
        for x in range(cols):
            print(counts[(x,y)],end=" ")
        print()
    print()

for i in range(100):
    for j,(x,y,vx,vy) in enumerate(robots):
        counts[(x,y)] -= 1 if i > 0 else 0
        
        # update rule
        (x,y) = ((x+vx) % cols,(y+vy)%rows)
        robots[j] = (x,y,vx,vy)
        counts[(x,y)] += 1
    display()

quadrants = [0,0,0,0,0]
for x,y,vx,vy in robots:
    quadrant = (x > cols // 2) + 2 * (y > rows // 2) if not ((x == cols // 2) or (y == rows // 2)) else 4
    quadrants[quadrant] += 1

print(math.prod(quadrants[:4]))