import numpy as np
import queue
from itertools import product, permutations
from collections import defaultdict

stacks = [[] for _ in range(9)]
moves_time = False

for line in open("5.txt"):
    if line.strip() == "":
        moves_time = True
        for idx in range(len(stacks)):
            stacks[idx] = stacks[idx][::-1]
        continue
    if not moves_time:
        crates = []
        for idx in range(9):
            crate = line[1 + 4 * idx]
            crates.append(crate)
        for idx, crate in enumerate(crates):
            if crate != " ":
                stacks[idx].append(crate)
    else:
        move_cnt = int(line[5:].split(" from ")[0])
        start_stack_idx, end_stack_idx = line.split(" to ")
        start_stack_idx, end_stack_idx = int(start_stack_idx[-1]), int(end_stack_idx)
        # for _ in range(move_cnt):
        # stacks[end_stack_idx - 1].append(stacks[start_stack_idx - 1].pop())
        move_idx = len(stacks[start_stack_idx - 1]) - move_cnt
        stacks[end_stack_idx - 1] += stacks[start_stack_idx - 1][move_idx:]
        stacks[start_stack_idx - 1] = stacks[start_stack_idx - 1][:move_idx]


for stack in stacks:
    print(stack[-1], end="")
