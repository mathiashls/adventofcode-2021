import argparse

DIRECTION_FORWARD = 'forward'
DIRECTION_UP = 'up'
DIRECTION_DOWN = 'down'

"""
All information and context was taken from https://adventofcode.com/2021/day/1
"""


def calculate_x_final_position(directions: list[tuple]) -> int:
    x_position = 0
    for direction, value in directions:
        if direction == DIRECTION_FORWARD:
            x_position += int(value)

    print(f"The horizontal final position is {x_position}")
    return x_position


def calculate_y_final_position(directions: list[tuple]) -> int:
    y_position = 0
    for direction, value in directions:
        if direction == DIRECTION_UP:
            y_position -= int(value)
        elif direction == DIRECTION_DOWN:
            y_position += int(value)

    print(f"The depth final position is {y_position}")
    return y_position


parser = argparse.ArgumentParser()
parser.add_argument("input")
args = parser.parse_args()

directions = None
with open(args.input) as file:
    directions = file.read().splitlines()
    directions = [direction.split() for direction in directions]

if directions:
    x_position = calculate_x_final_position(directions)
    y_position = calculate_y_final_position(directions)
    result = x_position * y_position
    print(f"The product from x and y is {result}")
