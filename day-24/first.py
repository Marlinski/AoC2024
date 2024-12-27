import re

puzzle = "day-24/puzzle"

content = open(puzzle, "r").read()

wires = {wire: int(input) for (wire, input) in re.findall(r'(\w+): (\w+)', content)}
gates = {(op,left,right,output) for (left,op,right,output) in re.findall(r'(\w+) (\w+) (\w+) -> (\w+)', content)}

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

# print z_num
def z_num(wires):
    z_wire = [(zk,zv) for (zk,zv) in wires.items() if zk.startswith("z")]
    z_ordered = sorted(z_wire, key=lambda item: item[0], reverse=True)
    z_str = "".join([str(wv) for (_,wv) in z_ordered])
    return int(z_str, 2)

wires = sim(wires, gates)
print(z_num(wires))