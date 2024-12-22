from itertools import product
from memoization import cached

puzzle = 'day-21/puzzle'
codes = [code.strip() for code in open(puzzle,"r").readlines()]

num_pad = {
    (0,0): "7",
    (0,1): "4",
    (0,2): "1",
    (1,0): "8",
    (1,1): "5",
    (1,2): "2",
    (1,3): "0",
    (2,0): "9",
    (2,1): "6",
    (2,2): "3",
    (2,3): "A",
}
key_pad = {
    (0,1): "<",
    (1,0): "^",
    (1,1): "v",
    (2,0): "A",
    (2,1): ">",
}
r_num_pad = {v: k for k, v in num_pad.items()}
r_key_pad = {v: k for k, v in key_pad.items()}

# for part 2, I started from scratch.

# find the "path" from one key to another, avoiding the forbidden one
def atomic_move(rpad, start, end):
    (x1, y1) = rpad[start]
    (x2, y2) = rpad[end]
    (dx, dy) = (x2-x1,y2-y1)

    h = ">" * abs(dx) if dx > 0 else "<" * abs(dx)
    v = "v" * abs(dy) if dy > 0 else "^" * abs(dy)

    if (x2,y1) not in rpad.values():
        return {v+h+"A"}
    if (x1,y2) not in rpad.values():
        return {h+v+"A"}
    return {v+h+"A", h+v+"A"}

# find all the moves for a given code
def code_move(rpad, code):
    seq = [c for c in "A" + code]
    seq = [(seq[i], seq[i+1]) for i in range(len(seq) - 1)]
    seq = [atomic_move(rpad, i, j) for (i,j) in seq]
    seq = {s for s in product(*seq)} # I discovered itertools.product on reddit, neat tool !
    seq = {"".join(s) for s in seq}
    return seq


# return the min len for inputing the code with n successive robot arms
@cached
def min_len(code, n):
    if n == 0:
        return len(code)

    # given a set of move like "<A^A^^>AvvvA" we can find the shortest move for each sub-problems
    seq = code.split("A")
    seq = [code_move(r_key_pad, s+"A") for s in seq]
    
    seq_min_len = 0
    for choices in seq[:-1]:
        # go deeper
        seq_min_len += min(min_len(choice, n-1) for choice in choices)
    
    return seq_min_len


def conundrum(code):
    num_pad_moves = code_move(r_num_pad, code)
    l =  min([min_len(c, 25) for c in num_pad_moves])
    print(int(code[:-1]), l)
    return int(code[:-1]) * l


print(sum([conundrum(code) for code in codes]))