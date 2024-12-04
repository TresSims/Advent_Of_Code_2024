#! /usr/bin/python
import re

vald_mul = "mul\\([0-9]+,[0-9]+\\)"

text = ""
with open("input", "r") as fp:
    text = fp.read()

matches = re.findall(vald_mul, text)
matches = list(map(lambda match: match[4:-1].split(","), matches))
print(sum([int(i[0]) * int(i[1]) for i in matches]))
