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


def numpad_to_keypad(seq):
    num_pad_seq = [(2,3)] + [r_num_pad[pos] for pos in seq]
    num_pad_pairs = [(num_pad_seq[i], num_pad_seq[i+1]) for i in range(len(num_pad_seq) - 1)]
    num_pad_moves = [(x2-x1,y2-y1) for ((x1,y1),(x2,y2)) in num_pad_pairs]
    num_pad_moves_atomic = []
    for move in num_pad_moves:
        (dx,dy) = move
        if dy >= 0: # since we go down we should be careful to first adjust the X to avoid going into nogo zone
            num_pad_moves_atomic += [(dx//abs(dx),0)]*abs(dx) if dx != 0 else []
            num_pad_moves_atomic += [(0,dy//abs(dy))]*abs(dy) if dy != 0 else []
        else:  # since we go up we should be careful to first adjust the Y to avoid going into nogo zone
            num_pad_moves_atomic += [(0,dy//abs(dy))]*abs(dy) if dy != 0 else []
            num_pad_moves_atomic += [(dx//abs(dx), 0)]*abs(dx) if dx != 0 else []
        num_pad_moves_atomic += [(0,0)]
    next_key_pad_seq = [dir_to_key_pad[move] for move in num_pad_moves_atomic]
    #print("".join(next_key_pad_seq))
    return next_key_pad_seq


def keypad_to_keypad(seq):
    key_pad_seq = [(2,0)] + [r_key_pad[pos] for pos in seq]
    key_pad_pairs = [(key_pad_seq[i], key_pad_seq[i+1]) for i in range(len(key_pad_seq) - 1)]
    key_pad_moves = [(x2-x1,y2-y1) for ((x1,y1),(x2,y2)) in key_pad_pairs]
    key_pad_moves_atomic = []
    for move in key_pad_moves:
        (dx,dy) = move
        if dy <= 0: # since we go down we should be careful to first adjust the X to avoid going into nogo zone
            key_pad_moves_atomic += [(dx//abs(dx),0)]*abs(dx) if dx != 0 else []
            key_pad_moves_atomic += [(0,dy//abs(dy))]*abs(dy) if dy != 0 else []
        else:  # since we go up we should be careful to first adjust the Y to avoid going into nogo zone
            key_pad_moves_atomic += [(0,dy//abs(dy))]*abs(dy) if dy != 0 else []
            key_pad_moves_atomic += [(dx//abs(dx), 0)]*abs(dx) if dx != 0 else []
        key_pad_moves_atomic += [(0,0)]
    next_key_pad_seq = [dir_to_key_pad[move] for move in key_pad_moves_atomic]
    #print("".join(next_key_pad_seq))
    return next_key_pad_seq
    

def conundrum(seq):
    key_pad_0 = numpad_to_keypad(seq)
    key_pad_1 = keypad_to_keypad(key_pad_0)
    key_pad_2 = keypad_to_keypad(key_pad_1)
    print(int(seq[:-1]),len(key_pad_2),"".join(key_pad_2))
    return int(seq[:-1])*len(key_pad_2)

print(sum([conundrum(code) for code in codes]))