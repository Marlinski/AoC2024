import re
import math
from collections import defaultdict

puzzle = 'day-14/puzzle'

with open(puzzle, 'r') as file:
    content=file.read()
    pattern = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")
    matches = pattern.findall(content)
    robots = [
        (int(x),int(y),int(vx),int(vy))
        for x,y,vx,vy in matches
    ]
    cols = 101
    rows = 103
    


counts = defaultdict(int)
def display():
    for y in range(rows):
        for x in range(cols):
            print(counts[(x,y)] if counts[(x,y)]  > 0 else " ",end="") 
        print()
    print("-"*cols)


def quadrant():
    quadrants = [0,0,0,0,0,0]
    for x,y,vx,vy in robots:
        if (x == cols // 2):
            quadrants[4] += 1
        elif (y == rows // 2):
            quadrants[5] += 1
        else:
            quadrants[(x > cols // 2) + 2 * (y > rows // 2)] += 1
    return quadrants


i = 0
while(True):
    q = quadrant()
    
    # if there's a christmas tree I would expect the quadrant to be "imbalanced"
    # meaning the difference with the mean would be big for one of the quadrant
    # I found the solution by filtering all steps to only keep the imbalanced one
    # hopefully I confirmed the solution using my EYES :-)
    mean = sum(q[:4])/4
    imbalance = max([abs(xi-mean) for xi in q[:4]])/mean
    if imbalance > 1:
        print(">",i,imbalance)
        display()
        input()

    for j,(x,y,vx,vy) in enumerate(robots):
        counts[(x,y)] -= 1 if i > 0 else 0
        (x,y) = ((x+vx) % cols,(y+vy)%rows)
        robots[j] = (x,y,vx,vy)
        counts[(x,y)] += 1

    i = i + 1
