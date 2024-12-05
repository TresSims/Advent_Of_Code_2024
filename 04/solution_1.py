#! /usr/bin/python

# Welcome to vector math hell


# Takes a 2D vector array for the origin, a 2D vector array for the direction
# the length of the ray to return, and the grid to search
def get_ray(x, y, direction, length, matrix):
    ray = []

    for i in range(length):
        # Start at the origin
        target = [x, y]

        # offset by the direction scaled by the character we are looking for
        target[0] += i * direction[0]
        target[1] += i * direction[1]

        # If the character is in the array, add it to the list
        if (0 <= target[0] < len(matrix)) and (0 <= target[1] < len(matrix[0])):
            ray.append(matrix[target[0]][target[1]])

    return ray


# take a puzzle map, and the origin (vector 2D array) of a goal list and find the words
# in all cardinal directions around that origin, and return however many words are goals
def solve_start(puzzle_map, x, y, goal):
    solutions = 0

    directions = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]

    for direction in directions:
        word = get_ray(x, y, direction, len(goal), puzzle_map)
        if word == goal:
            solutions += 1

    return solutions


### Entry Point ###

goals = ["XMAS"]
goals = list(map(list, goals))

puzzle_map = []
with open("input", "r") as fp:
    for line in fp:
        puzzle_map.append(list(line))


solutions = 0
for x in range(len(puzzle_map)):
    for y in range(len(puzzle_map[x])):
        for goal in goals:
            if goal[0] == puzzle_map[x][y]:
                solutions += solve_start(puzzle_map, x, y, list(goal))

print(solutions)
