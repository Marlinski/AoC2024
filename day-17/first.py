import re

puzzle = 'day-17/puzzle'

with open(puzzle, 'r') as file:
    data=file.read()
    registers = {match[0]: int(match[1]) for match in re.findall(r"Register (\w): (\d+)", data)}
    program = list(map(int, re.search(r"Program: ([\d,]+)", data).group(1).split(",")))

ip = 0

def read():
    global ip
    word = program[ip]
    ip += 1
    return word


def combo(operand):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return registers["A"]
        case 5:
            return registers["B"]
        case 6:
            return registers["C"]
        case 7:
            raise Exception("reserved")
        case _:
            return operand
    
out = []
while True:
    if ip >= len(program):
        break

    opcode = read()
    operand = read()

    match opcode:
        case 0:
            registers["A"] = registers["A"] // (2 ** combo(operand))
        case 1:
            registers["B"] = registers["B"] ^ operand
        case 2:
            registers["B"] = combo(operand) % 8
        case 3:
            print(registers, out)
            if not registers["A"] == 0:
                ip = operand
        case 4:
            registers["B"] = registers["B"] ^ registers["C"]
        case 5:
            out.append(combo(operand) % 8)
        case 6:
            registers["B"] = registers["A"] // pow(2,combo(operand))
        case 7:
            registers["C"] = registers["A"] // pow(2,combo(operand))

print("program halted: ",",".join([str(i) for i in out]))