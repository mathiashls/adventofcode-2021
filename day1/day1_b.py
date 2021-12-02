import argparse

SLIDING_WINDOW_VALUE = 3

"""
All information and context was taken from https://adventofcode.com/2021/day/1
"""


def remove_noise(values):
    filtered_values = []
    for index, _ in enumerate(values):
        sliding_window = values[index:index+SLIDING_WINDOW_VALUE]
        new_value = sum(sliding_window)
        filtered_values.append(new_value)

    return filtered_values


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
    lines = [int(line) for line in lines]
    filtered_values = remove_noise(lines)
    count = count_measurement_increment(filtered_values)
    print(f"There is [{count}] measurements larger than the previous one.")
