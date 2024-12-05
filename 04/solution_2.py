#! /usr/bin/python


def is_xmas(x, y, puzzle_map):

    # check TL MAS
    left_mas = (
        puzzle_map[x - 1][y - 1] == "M" and puzzle_map[x + 1][y + 1] == "S"
    ) or (puzzle_map[x - 1][y - 1] == "S" and puzzle_map[x + 1][y + 1] == "M")

    # check TR MAS
    right_mas = (
        puzzle_map[x + 1][y - 1] == "M" and puzzle_map[x - 1][y + 1] == "S"
    ) or (puzzle_map[x + 1][y - 1] == "S" and puzzle_map[x - 1][y + 1] == "M")

    return left_mas and right_mas


puzzle_map = []
with open("input", "r") as fp:
    for line in fp:
        puzzle_map.append(list(line))

solutions = 0
for x in range(1, len(puzzle_map) - 1):
    for y in range(1, len(puzzle_map[x]) - 1):
        if puzzle_map[x][y] == "A":
            if is_xmas(x, y, puzzle_map):
                solutions += 1

print(solutions)
