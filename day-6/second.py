import numpy as np

puzzle = 'day-6/puzzle'
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
        
        
def walk_in_circle(x,y,dir):
    been_there_done_that = {}
    while True:
        key = (x,y,dir)
        if key in been_there_done_that:
            return True
        been_there_done_that[key] = True

        (x2,y2,dir2) = next_step(x,y,dir)
        if is_outside(x2,y2):
            return False
        
        (x,y,dir) = (x,y,dir2) if matrix[y2][x2] == "#" else (x2,y2,dir)


# find starting position
(x_start,y_start,dir_start) = (0,0,"^")
for (y, x), value in np.ndenumerate(matrix):
    if value in ["^",">","<","v"]:
        (x_start,y_start,dir_start) = (x,y,value)
        break

# try all possibilities
res = 0
for (y, x), value in np.ndenumerate(matrix):
    if value in ["^",">","<","v","#"]:
        continue

    matrix[y][x] = "#"
    res += 1 if walk_in_circle(x_start, y_start, dir_start) else 0
    matrix[y][x] = "."
print(res)