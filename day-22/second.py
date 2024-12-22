def highest_bid(secret, n): 
    window = [0]*4
    spread = {}
    for i in range(n):
        prev = secret
        secret = (secret ^ (secret * 64))   % 16777216
        secret = (secret ^ (secret // 32))  % 16777216
        secret = (secret ^ (secret * 2048)) % 16777216
        window[i % 4] = ((secret % 10) - (prev % 10))
        if i > 3:
            key = ",".join(str(window[j % 4]) for j in range(i+1, i+5, 1))
            if key not in spread:
                spread[key] = secret % 10
    return spread

seeds = [seed for seed in open("day-22/puzzle", "r").read().split()]
spreads = [highest_bid(int(seed), 2000) for seed in seeds]
all_unique_seq = {s for seq in spreads for s in set(seq.keys()) }
max_seq, max_score = max(
    ((seq, sum(spread.get(seq, 0) for spread in spreads)) for seq in all_unique_seq),
    key=lambda x: x[1],
)

print(max_seq,max_score)