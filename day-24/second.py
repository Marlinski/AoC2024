import re
from itertools import combinations
import copy
import os
import math

puzzle = "day-24/puzzle.modified"

content = open(puzzle, "r").read()

wires = {wire: int(input) for (wire, input) in re.findall(r'(\w+): (\w+)', content)}
gates = [(op,left,right,output) for (left,op,right,output) in re.findall(r'(\w+) (\w+) (\w+) -> (\w+)', content)]

# set the default value (wire unset) 
for (op,left,right,output) in gates:
    if output not in wires:
        wires[output] = -1



# 2nd TRY: Generates a graph and realized that it was merely an adder:
# https://en.wikipedia.org/wiki/Adder_(electronics)
# this gave me an idea...
# vvvvv XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX vvvvv 

def generate_adder_graph(gates):
     with open("day-24/gates.dot", "w") as f:
        f.write("digraph AdderGraph {\n")
        f.write("  rankdir=LR;\n")  # Left-to-right layout

        for op, left, right, output in gates:
            f.write(f'  "{output}" [shape=diamond, label="{op}"];\n')
            f.write(f'  "{left}" -> "{output}" [label={left}]\n')
            f.write(f'  "{right}" -> "{output}" [label={right}]\n')
            if output[0] == "z":
                f.write(f'  "z{output}" [shape=box, style=filled, label={output}];\n')
                f.write(f'  "{output}" -> "z{output}"\n')
        f.write("}\n")

graph = generate_adder_graph(gates)

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


# print z_num
def num(wires,register):
    z_wire = [(zk,zv) for (zk,zv) in wires.items() if zk.startswith(register)]
    z_ordered = sorted(z_wire, reverse=True)
    z_str = "".join([str(wv) for (_,wv) in z_ordered])
    print(z_str)
    return int(z_str, 2)

def set(wires,register,value):
    z_wires = {key: value for key,value in wires.items() if key[0] == register}
    bin_repr = list(bin(value)[2:].zfill(len(z_wires)))[::-1]
    for i, key in enumerate(sorted(z_wires.keys())):
        wires[key] = int(bin_repr[i]) if i < len(bin_repr) else 0
    return wires


# 3rd TRY: let's add two numbers and see which bit starts diverging
# I am adding 2^50 - 1 to only have 1s on X and adding 1 with y, I should normally get only 0s (except for MSB)

wires = set(wires, "x", int(math.pow(2,45)-1))
wires = set(wires, "y", 1)
wires = sim(wires, gates)
x,y,z = num(wires,"x"), num(wires,"y"), num(wires,"z")

#   111111111111111111111111111111111111111111111
#   000000000000000000000000000000000000000000001
#  0111111100000000000000000000000111100000000000
#                                    ^
#                                    z11
# >> diverging at z11 ! 
# indeed, looking at the graphviz the AND and XOR was swapped so I swapped rpv with z11
#
# I swapped them then run again and got this:
#   111111111111111111111111111111111111111111111
#   000000000000000000000000000000000000000000001
#  0111111100000000000000000000001000000000000000
#                                ^
# >> diverging at z15 ! 
# indeed, looking at the graphviz this time it was the internal gates rpb and ctg that was swapped
#
# I swapped then and run again:
#   111111111111111111111111111111111111111111111
#   000000000000000000000000000000000000000000001
#  0111111100000000000000000000000000000000000000
#         ^
# >> diverging at z38 ! 
# indeed, looking at the graphviz this time it was the internal gates dvq and z38 that was swapped
#
# I swapped then and run again:
#   111111111111111111111111111111111111111111111
#   000000000000000000000000000000000000000000001
#  1000000000000000000000000000000000000000000000
#
# looks okay to me! since I only have 3 pairs there must be another combination that somehow makes it ok.
# Since I was now used to what an adder should be expected to work, I decided to just look through all 
# the adder and see if anything sticked out, hopefully I quickly found out z31 and dmh was swapped!


# I just assembled the solution by hand at this point:
swapped = ["rpv","z11",   "ctg","rpb",    "dvq","z38",    "dmh","z31"]
print(",".join(sorted(swapped)))







os._exit(1)

# 1st TRY: I tried to bruteforce but this approach did not work
# vvvvv XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX vvvvv 

def swap(gates, swapped):
    for (x,y) in swapped:
        (xop,xleft,xright,xoutput) = gates[x]
        (yop,yleft,yright,youtput) = gates[y]
        gates[x] = (xop,xleft,xright,youtput)
        gates[y] = (yop,yleft,yright,xoutput)
    return gates

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
