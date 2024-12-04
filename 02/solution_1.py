#! /usr/bin/python

safe = 0

with open("input", "r") as fp:
    for line in fp:
        safe += 1

        data = [int(i) for i in line.rstrip().split()]

        p_val = data[0]
        ascending = False
        if p_val < data[1]:
            ascending = True

        for val in data[1:]:
            if abs(p_val - val) > 3:
                safe -= 1
                break

            if ascending and p_val >= val:
                safe -= 1
                break

            if not ascending and p_val <= val:
                safe -= 1
                break

            p_val = val


print(safe)
