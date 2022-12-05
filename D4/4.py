import numpy as np
from itertools import product, permutations
from collections import defaultdict


def is_overlaped_p1(range_a: tuple, range_b: tuple) -> bool:
    x_a, y_a = range_a
    x_b, y_b = range_b
    if (x_a >= x_b and y_a <= y_b) or (x_b >= x_a and y_b <= y_a):
        return True
    return False


def is_overlaped_p2(range_a: tuple, range_b: tuple) -> bool:
    x_a, y_a = range_a
    x_b, y_b = range_b
    if x_b > y_a or x_a > y_b:
        return False
    return True


p1_count, p2_count = 0, 0
for line in open("4.txt"):
    range_a, range_b = line.strip().split(",")
    range_a = [int(x) for x in range_a.split("-")]
    range_b = [int(x) for x in range_b.split("-")]
    if is_overlaped_p1(range_a, range_b):
        p1_count += 1
    if is_overlaped_p2(range_a, range_b):
        p2_count += 1

print(f"P1: {p1_count}")
print(f"P2: {p2_count}")
