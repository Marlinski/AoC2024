import re
puzzle = 'day-4/puzzle'
matrix = []

with open(puzzle, 'r') as file:
    for line in file:
        matrix.append(line.replace('\n',''))

y_bound = len(matrix)    
x_bound = len(matrix[0])

def xmas(_x, _y, _ix, _iy, word):
    for i in range(0, len(word)):
        if (_x >= x_bound):
            return False
        if (_x < 0):
            return False
        if (_y >= y_bound):
            return False
        if (_y < 0):
            return False
        if not matrix[_y][_x] == word[i]:
            return False
        _x += _ix
        _y += _iy
    return True

res = 0
for y in range(0,len(matrix)):
    for x in range(0,len(matrix[y])):
        if matrix[y][x] == 'A':
            if (xmas(x-1, y-1, 1, 1, "MAS") or xmas(x-1, y-1, 1, 1, "SAM")) and (xmas(x+1, y-1, -1, 1, "MAS") or xmas(x+1, y-1, -1, 1, "SAM")):
                res += 1
print(res)