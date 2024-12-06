import numpy as np

puzzle = 'day-6/puzzle-test'
matrix = []

with open(puzzle, 'r') as file:
    matrix = [list(line.strip()) for line in file]
matrix = np.array(matrix)
(rows,cols) = matrix.shape


def is_outside(x,y):
    return x < 0 or x >= cols or y < 0 or y >= rows


def next_step(x,y,dir):
    match(dir):
        case "^":
            return (x,y-1,">") 
        case ">":
            return (x+1,y,"v") 
        case "v":
            return (x,y+1,"<") 
        case "<":
            return (x-1,y,"^") 
        

def walk(x,y,dir):
    visited = {}
    while True:
        visited[(x,y)] = True
        (x2,y2,dir2) = next_step(x,y,dir)
        if is_outside(x2,y2):
            return len(visited)
        (x,y,dir) = (x,y,dir2) if matrix[y2][x2] == "#" else (x2,y2,dir)

res = 0
for (y, x), value in np.ndenumerate(matrix):
    if value in ["^",">","<","v"]:
        res = walk(x,y,value)
        break
print(res)
