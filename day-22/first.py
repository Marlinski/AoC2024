def round(secret, n):
    for i in range(n):
        secret = (secret ^ (secret * 64))   % 16777216
        secret = (secret ^ (secret // 32))  % 16777216
        secret = (secret ^ (secret * 2048)) % 16777216
    return secret

print(sum(round(int(secret), 2000) for secret in open("day-22/puzzle", "r").read().split()))