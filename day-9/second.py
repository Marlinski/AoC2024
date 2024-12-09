puzzle = 'day-9/puzzle'
with open(puzzle, 'r') as file:
    hdd = [(int(size), i // 2, i % 2 == 1) for (i,size) in enumerate(file.read().strip())]

# print("".join([f"{str(id)}"*size if not free else "."*size for (size,id,free) in hdd]))
res = 0
j = len(hdd) if len(hdd) % 2 == 0 else len(hdd)-1

# we consider all block (non-free cells) moving from right to left
while j > 0:
    try:
        (block_size, block_id, j_free) = hdd[j]
        if j_free:
            continue

        # let's try to insert in the first free cell that fits, from left to right
        for i in range(0, j):
            (free_size, free_id, i_free) = hdd[i]
            if not i_free:
                continue
            
            if free_size >= block_size:
                hdd[i] = (free_size-block_size, free_id, True) # update length of free cell
                hdd[j] = (block_size, block_id, True)          # moved block now is free memory
                hdd.insert(i, (block_size, block_id, False))   # insert moved block in front of free cell
                break
    finally:
        j -= 1
# print("".join([f"{str(id)}"*size if not free else "."*size for (size,id,free) in hdd]))

pos = 0
res = 0
for (n,id,is_free) in hdd:
    res += (id * n * (pos + pos + n - 1) // 2) if not is_free else 0
    pos += n
print(res)