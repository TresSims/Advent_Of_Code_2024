from typing import List
from functools import reduce
import numpy as np


def solve(list_a: List[int], list_b: List[int]) -> int:
    return reduce(
        lambda a, b: a + b,
        [abs(a - b) for a, b in zip(sorted(list_a), sorted(list_b))],
    )


input = []
with open("input") as fp:
    for line in fp:
        print(f"{line}")
        input.append([int(i) for i in line.split("   ")])

input = np.rot90(input)
print(solve(input[0], input[1]))
