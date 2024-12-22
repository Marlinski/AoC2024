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


# I struggled a lot doing a non-recursive approach but at the end I ended up going recursive...
def map_seq(rpad, target, hover=None, sequence = ""):
    if not target:
        return [sequence]
    
    if hover is None:
        hover = rpad["A"]

    if hover not in rpad.values():
        return []

    (x1,y1) = hover
    (x2,y2) = rpad[target[0]]
    (dx,dy) = (x2-x1,y2-y1)

    if (0,0) == (dx,dy):
        return map_seq(rpad, target[1:], hover, sequence + "A")
    
    res = []    
    if abs(dx) > 0:
        res += map_seq(rpad, target, (x1 + dx//abs(dx), y1), sequence + (">" if dx > 0 else "<"))
    if abs(dy) > 0:
        res += map_seq(rpad, target, (x1, y1 + dy//abs(dy)), sequence + ("v" if dy > 0 else "^"))
    return res



def conundrum(code):
    key_pad_0 = map_seq(r_num_pad, code)
    lens_0 = [len(s) for s in key_pad_0]

    key_pad_1 = [seq for s in key_pad_0 if len(s) == min(lens_0) for seq in map_seq(r_key_pad, s) ]
    lens_1 = [len(s) for s in key_pad_1]

    key_pad_2 = [seq for s in key_pad_1 if len(s) == min(lens_1) for seq in map_seq(r_key_pad, s) ]
    lens_2 = [len(s) for s in key_pad_2]
    
    print(int(code[:-1]),min(lens_2))
    return int(code[:-1])*min(lens_2)


print(sum([conundrum(code) for code in codes]))