import re
from itertools import combinations
from collections import defaultdict

puzzle = "day-23/puzzle"
links = re.findall(r'(\w+)-(\w+)', open(puzzle).read())
lookup = defaultdict(set)
for c1, c2 in links:
    lookup[c1].add(c2)
    lookup[c2].add(c1)

# first we find all connected subgraphs to reduct the exploration space when finding cliques
# I thought I was being smart but it turns out the puzzle is just one big connected graph
# which is logical since it is a LAN party :')
lans = []
for c1, c2 in links:
    merged = {c1, c2}.union(*(lan for lan in lans if c1 in lan or c2 in lan))
    lans = [lan for lan in lans if lan.isdisjoint(merged)] + [merged]
print(f"there's {len(lans)} disjoint graphs")

# then for each subgraph, we find all the 3-degrees cliques that contains at leats one computer with "t"
# there's 23 299 640 3-degrees set
# there's 2 341 140 3-degrees set with at least one that starts with a "t"
# for all of them, we check if a link exists (using lookup table for efficiency)
cliques_3 = {frozenset(clique)
                for lan in lans 
                for clique in list(combinations(lan, 3))
                if any(c.startswith("t") for c in clique) and all(l2 in lookup[l1] for (l1,l2) in list(combinations(clique, 2)))}
print(f"there's {len(cliques_3)} 3-degrees clique")
