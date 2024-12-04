#! /usr/bin/python
import re

vald_mul = "mul\\([0-9]+,[0-9]+\\)"
valid_do = "do\\(\\)"
valid_dont = "don\\'t\\(\\)"

text = ""
with open("input", "r") as fp:
    text = fp.read()

muls = re.finditer(vald_mul, text)
dos = re.finditer(valid_do, text)
donts = re.finditer(valid_dont, text)

program = list(muls) + list(dos) + list(donts)
program.sort(key=lambda val: val.start())

do = True
solves = []
for instruction in program:
    if instruction[0] == "do()":
        do = True
    elif instruction[0] == "don't()":
        do = False
    else:
        if do:
            mults = [int(i) for i in instruction[0][4:-1].split(",")]
            solves.append(mults[0] * mults[1])

print(sum(solves))
