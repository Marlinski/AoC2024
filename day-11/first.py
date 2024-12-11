puzzle = 'day-11/puzzle'

with open(puzzle, 'r') as file:
    stones = file.read().strip().split(' ')

def blink(stones):
    next = []
    for stone in stones:
        if stone == '0':
            next.append('1')
            continue
        if len(stone) % 2 == 0:
            next.append(str(int(stone[:len(stone)//2])))
            next.append(str(int(stone[len(stone)//2:])))
            continue
        next.append(str(int(stone)*2024))
    return next

for i in range(0,25):
    stones = blink(stones)
print(len(stones))