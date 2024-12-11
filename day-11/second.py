from memoization import cached

puzzle = 'day-11/puzzle'
with open(puzzle, 'r') as file:
    stones = file.read().strip().split(' ')

@cached
def blink_individual_stone(stone, times):
    if times == 0:
        return 1
    if stone == '0':
        return blink_individual_stone('1', times-1)
    elif len(stone) % 2 == 0:
        return blink_individual_stone(stone[:len(stone)//2], times-1) + blink_individual_stone(stone[len(stone)//2:], times-1)
    else: 
        return blink_individual_stone(str(int(stone)*2024), times-1)

print(sum([blink_individual_stone(stone, 75) for stone in stones]))
        