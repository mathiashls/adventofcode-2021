import argparse

DIRECTION_FORWARD = 'forward'
DIRECTION_UP = 'up'
DIRECTION_DOWN = 'down'

"""
All information and context was taken from https://adventofcode.com/2021/day/1
"""


def calculate_final_position(directions: list[tuple]) -> tuple[int, int]:
    horizontal = 0
    aim = 0
    depth = 0
    for direction, value in directions:
        if direction == DIRECTION_FORWARD:
            horizontal += int(value)
            depth += aim * int(value)
        elif direction == DIRECTION_UP:
            aim -= int(value)
        elif direction == DIRECTION_DOWN:
            aim += int(value)

    print(
        f"The horizontal final position is {horizontal} and depth is {depth}"
    )
    return (horizontal, depth)


parser = argparse.ArgumentParser()
parser.add_argument("input")
args = parser.parse_args()

directions = None
with open(args.input) as file:
    directions = file.read().splitlines()
    directions = [direction.split() for direction in directions]

if directions:
    position = calculate_final_position(directions)
    result = position[0] * position[1]
    print(f"The product from x and y is {result}")
