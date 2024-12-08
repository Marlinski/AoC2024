from collections import defaultdict

puzzle = 'day-8/puzzle'
matrix = []

with open(puzzle, 'r') as file:
    for line in file:
        matrix.append(list(line.strip()))
(rows,cols) = (len(matrix), len(matrix[0]))

def is_outside(x,y):
    return x < 0 or x >= cols or y < 0 or y >= rows

fr_loc = defaultdict(list)
for y, _ in enumerate(matrix):
    for x, value in enumerate(matrix[y]):
        if value in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            fr_loc[value].append((x,y))


antinodes = []
for frequency in fr_loc:
    for i,(x1,y1) in enumerate(fr_loc[frequency]):
        for (x2,y2) in fr_loc[frequency][i+1:]:
            antinodes.append((x1,y1))
            antinodes.append((x2,y2))
            (vx,vy) = (x2-x1,y2-y1)
        
            (ax,ay) = (x1,y1)
            while(True):
                (ax,ay) = (ax-vx, ay-vy)
                if is_outside(ax,ay):
                    break
                #matrix[ay][ax] = "#"
                antinodes.append((ax,ay))

            (ax,ay) = (x2,y2)
            while(True):
                (ax,ay) = (ax+vx, ay+vy)
                if is_outside(ax,ay):
                    break
                #matrix[ay][ax] = "#"
                antinodes.append((ax,ay))


#for y,row in enumerate(matrix):
#    for elem in matrix[y]:
#        print(elem,end='')
#    print()
print(len(set(antinodes)))