import re
puzzle = 'day-4/puzzle'
matrix = []

with open(puzzle, 'r') as file:
    for line in file:
        matrix.append(line.replace('\n',''))

y_bound = len(matrix)    
x_bound = len(matrix[0])
print(">>", x_bound, y_bound)

def search(_x, _y, _ix, _iy):
    word = "XMAS"
    for i in range(0, len(word)):
        if (_x >= x_bound):
            return 0
        if (_x < 0):
            return 0
        if (_y >= y_bound):
            return 0
        if (_y < 0):
            return 0
        if not matrix[_y][_x] == word[i]:
            return 0
        _x += _ix
        _y += _iy
    return 1

res = 0
for y in range(0,len(matrix)):
    for x in range(0,len(matrix[y])):
        if matrix[y][x] == 'X':
            for ix in (-1,0,1):
                for iy in (-1, 0 ,1):
                    res += search(x,y,ix,iy)
print(res)