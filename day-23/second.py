import re
from collections import defaultdict
from colorama import Fore

puzzle = "day-23/puzzle"

links = re.findall(r'(\w+)-(\w+)', open(puzzle).read())
lookup = defaultdict(set)
for c1, c2 in links:
    lookup[c1].add(c2)
    lookup[c2].add(c1)

# quickly realized that bruteforcing my way into it would yield no result
# I knew I had to find the largest clique but I found the algorithm on wikipedia
# https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
# pretty nice !
def bron_kerbosch(current, candidates, excluded):
    print(f"{Fore.RED}{current} {Fore.YELLOW}{candidates} {Fore.GREEN}{excluded}{Fore.RESET}")
    if not candidates and not excluded:
        yield current
    while candidates:
        candidate = candidates.pop()
        yield from bron_kerbosch(current | {candidate}, candidates & lookup[candidate], excluded & lookup[candidate])
        excluded.add(candidate)

all_cliques = bron_kerbosch(set(), set(lookup.keys()), set())
print(",".join(sorted(max(all_cliques, key=len))))