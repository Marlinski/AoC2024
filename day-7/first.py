puzzle = 'day-7/puzzle'

def evaluate(result, partial, numbers):
    if len(numbers) == 0 and partial == result:
        return True
    if len(numbers) == 0 and not partial == result:
        return False
    return True if evaluate(result, partial + numbers[0], numbers[1:]) else evaluate(result, partial * numbers[0], numbers[1:])

res = 0
with open(puzzle, 'r') as file:
    for line in file:
        parts = line.strip().split(':')
        result = int(parts[0])
        numbers = [int(elem) for elem in parts[1].split(' ')[1:]]
        res += result if evaluate(result, numbers[0], numbers[1:]) else 0
print(res)
        
