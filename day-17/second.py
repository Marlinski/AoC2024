import os

# program is: 2,4, 1,3, 7,5, 4,0, 1,3, 0,3, 5,5, 3,0
# pseudo assembly:
#
# WHILE A != 0
#    B <- (A % 8)      2,4
#    B <- B ^ 3        1,3
#    C <- A / 2^B      7,5
#    B <- B ^ C        4,0
#    B <- B ^ 3        1,3
#    A <- A / 8        0,3
#    out B % 8         5,5
#                      3,0
#
# we want it to output 2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0
#
# let's simplify the program:
#
# WHILE A != 0
#    B = ((A % 8) XOR 3)
#    B = B XOR (A / pow(2, B))
#    B = B XOR 3
#    A <- A / 8
#    out B % 8 
# 
# even more
#
# WHILE A != 0
#   B = (((A % 8) XOR 3) XOR (A / pow(2,((A % 8) XOR 3)))) XOR 3
#   print(B)
#   A = A // 8



# I first brute forced the solution by looking for all values of A, breaking early as soon as the output diverged from the objective output
# I printed the value of A (in binary format) every time I had at least the first 3 elements of my objective output
#   that's when I noticed that all value of A had same binary suffix!!
# So I started again brute forcing from this value, and filtering for values that matched at least the 4 elements
#   I noticed they all share a similar binary suffix, this time longer!!
# So on until I got the solution :)
#
# Retrospectively, it is a sort of gradient descent with my loss being the number of matching element of the objective array
# Below is an automated version of this approach, in reality I printed the values and adjusted the suffix visually
def common_suffix(numbers):
    binary_repr = [format(num, f'0{128}b') for num in numbers]
    suffix = ""
    for i in range(1, 129):
        suffix = binary_repr[0][-i:]
        if not all(b.endswith(suffix) for b in binary_repr):
            break
    return suffix[1:]


program = [2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0]
suffix=""
score = 0
samples = []

while len(suffix) < 128:
    # I will only sample value of A that yields me at least "loss" first value of objective array
    # at each iteration I will increase my "loss" and the suffix should (hopefully) grow larger
    score += 1
    if len(samples) > 0:
        suffix = common_suffix(samples)
        print("suffix=> "+" "*(64-len(suffix)-10),suffix,end="\n\n")

    A = int(suffix, 2) if len(suffix) > 0 else 0
    samples = []
    print(f"starting search with score={score}")
    while True:
        # I have enough sample to find a common suffix
        if len(samples) > 5:
            break
        
        # bruteforcing the space, starting from the "suffix" value
        out = []
        B = 0
        C = A
        while not C == 0:
            B = (((int(C % 8) ^ 3) ^ (int(C) // pow(2, ((int(C) % 8) ^ 3)))) ^ 3) % 8
            out.append(B)
            C = C // 8

            # break out early
            if not program[:len(out)] == out:
                if len(out) >= score:
                    print(format(A, f'0{64}b'))
                    samples.append(A)
                break
            
            # we found it!
            if program == out:
                print("A=",A, out)
                os._exit(0)
        
        # As the suffix grow larger, I am narrowing down to the answer
        A += 2**len(suffix)

