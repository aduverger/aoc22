import numpy as np
from itertools import product, permutations
from collections import defaultdict


G = []
for line in open("X.txt"):
    line = line.strip()
    G.append(line)
depth = len(G)
width = len(G[0])
