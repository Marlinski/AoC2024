puzzle = "day-25/puzzle"

data = open(puzzle, "r").read()
schematics = data.split("\n\n")

keys = []
locks = []

for schematic in schematics:
    rows = schematic.splitlines()
    heights = [sum(row[idx] == "#" for row in rows) - 1 for idx in range(len(rows[0]))]
    (keys if rows[0][0] == "." else locks).append(heights)


print(sum(1 for l in locks for k in keys if all(a + b <= 5 for a, b in zip(l, k))))