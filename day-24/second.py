import re
from itertools import combinations
import copy

puzzle = "day-24/puzzle"

content = open(puzzle, "r").read()

wires = {wire: int(input) for (wire, input) in re.findall(r'(\w+): (\w+)', content)}
gates = [(op,left,right,output) for (left,op,right,output) in re.findall(r'(\w+) (\w+) (\w+) -> (\w+)', content)]


def generate_adder_graph(gates):
     with open("day-24/gates.dot", "w") as f:
        f.write("digraph AdderGraph {\n")
        f.write("  rankdir=LR;\n")  # Left-to-right layout

        for left, op, right, output in gates:
            f.write(f'  "{left}" -> "{output}" [label="{op}"];\n')
            f.write(f'  "{right}" -> "{output}" [label="{op}"];\n')
        f.write("}\n")

graph = generate_adder_graph(gates)

# I tried to bruteforce but this approach did not work
# vvvvv XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX vvvvv 

# se the default value (wire unset) 
for (op,left,right,output) in gates:
    if output not in wires:
        wires[output] = -1

# simulate until all z wire are set
def sim(wires,gates):
    while any(v == -1 for k,v in wires.items() if k.startswith("z")):
        for (op,left,right,output) in gates:
            if wires[left] == -1 or wires[right] == -1:
                continue
            match op:
                case "AND":
                    wires[output] = wires[left] and wires[right]
                case "XOR":
                    wires[output] = wires[left] ^ wires[right]
                case "OR":
                    wires[output] = wires[left] or wires[right]
                case _:
                    raise(Exception("unknown logical gate"))
    return wires


def swap(gates, swapped):
    for (x,y) in swapped:
        (xop,xleft,xright,xoutput) = gates[x]
        (yop,yleft,yright,youtput) = gates[y]
        gates[x] = (xop,xleft,xright,youtput)
        gates[y] = (yop,yleft,yright,xoutput)
    return gates


# print z_num
def num(wires,register):
    z_wire = [(zk,zv) for (zk,zv) in wires.items() if zk.startswith(register)]
    z_ordered = sorted(z_wire, key=lambda item: item[0], reverse=True)
    z_str = "".join([str(wv) for (_,wv) in z_ordered])
    print(z_str)
    return int(z_str, 2)


pairs = combinations(range(len(gates)), 2)
squads = combinations(pairs, 4)

def valid_squads():
    for squad in squads:
        nodes = set(node for pair in squad for node in pair)
        if len(nodes) == 8:
            yield squad


for squad in valid_squads():
    gates = swap(copy.deepcopy(gates), squad)
    wires = sim(wires, gates)
    x,y,z = num(wires,"x"), num(wires,"y"), num(wires,"z")
    print(f"{x} + {y} = {x+y} ({z})")
    if x+y == z:
        print(squad)
        input()