#! /usr/bin/python
from functools import reduce

input = {}

with open("input", "r") as fp:
    for line in fp:
        values = [int(i) for i in line.rstrip().split()]
        for i in range(len(values)):
            if values[i] not in input:
                input[values[i]] = [0, 0]

            input[values[i]][i] += 1

print(sum([key * reduce(lambda a, b: a * b, input[key]) for key in input]))
