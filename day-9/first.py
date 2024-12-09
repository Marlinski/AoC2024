puzzle = 'day-9/puzzle'
with open(puzzle, 'r') as file:
    hdd = [int(i) for i in file.read().strip()]

res = 0
id = 0
i = 0
j = len(hdd) if len(hdd) % 2 == 0 else len(hdd)-1
pos = 0
n = 0
while i <= j:
    if i % 2 == 0:
        n = hdd[i]
        id = i // 2
        i += 1
    else:
        id = j // 2
        if hdd[j] > hdd[i]:
            n = hdd[i]
            hdd[j] = hdd[j] - hdd[i]
            i = i + 1
        else:
            n = hdd[j]
            hdd[i] = hdd[i] - hdd[j]
            j = j - 2
    
    # given an ID, a starting pos and N number of blocks
    # we compute the sum of the arithmetic series:
    # S= Number of terms × (First term + Last term) / 2
    # print(f"id={id} n={n} pos={pos}")
    res += id * n * (pos + pos + n - 1) // 2
    pos += n
print(res)
