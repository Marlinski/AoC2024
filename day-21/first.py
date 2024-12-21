puzzle = 'day-21/puzzle-test'
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
r_num_pad = {v: k for k, v in num_pad.items()}

key_pad = {
    (0,1): "<",
    (1,0): "^",
    (1,1): "v",
    (2,0): "A",
    (2,1): ">",
}
r_key_pad = {v: k for k, v in key_pad.items()}

dir_to_key_pad = {
    (1,0): ">",
    (-1,0): "<",
    (0,1): "v",
    (0,-1): "^",
    (0,0): "A"
}

def map_seq(rpad, start, seq):
    seq = [start] + [rpad[pos] for pos in seq]
    seq = [(seq[i], seq[i+1]) for i in range(len(seq) - 1)]
    seq = [(x2-x1,y2-y1) for ((x1,y1),(x2,y2)) in seq]
    atomic = []
    for move in seq:
        (dx,dy) = move
        for _ in range(abs(dx)):
            atomic += [(dx//abs(dx),0)]
        for _ in range(abs(dy)):
            atomic += [(0,dy//abs(dy))]
        atomic += [(0,0)]
    seq = [dir_to_key_pad[move] for move in atomic]
    print("".join(seq))
    return seq


def conundrum(seq):
    print(seq)
    key_pad_0 = map_seq(r_num_pad, (2,3), seq)
    key_pad_1 = map_seq(r_key_pad, (2,0), key_pad_0)
    key_pad_2 = map_seq(r_key_pad, (2,0), key_pad_1)
    print(int(seq[:-1]),len(key_pad_2),"".join(key_pad_2))
    return int(seq[:-1])*len(key_pad_2)


print(sum([conundrum(code) for code in codes]))