import argparse

"""
All information and context was taken from https://adventofcode.com/2021/day/1
"""


def count_measurement_increment(values):
    increment_count = 0
    previous_value = None
    for value in values:
        value = int(value)
        if not previous_value:
            previous_value = value
            continue
        if previous_value < value:
            increment_count += 1
        previous_value = value

    return increment_count



parser = argparse.ArgumentParser()
parser.add_argument("input")
args = parser.parse_args()

with open(args.input) as file:
    lines = file.read().splitlines()
    count = count_measurement_increment(lines)
    print(f"There is [{count}] measurements larger than the previous one.")
