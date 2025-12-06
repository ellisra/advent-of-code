#!/usr/bin/env python3

from math import prod


def part_one(data: str) -> int:
    lines = data.splitlines()
    operators = lines[-1].split()
    digits = [line.split() for line in lines[:-1]]
    nums = [list(map(int, col)) for col in zip(*digits)]

    total = 0
    for i, row in enumerate(nums):
        if operators[i] == '+':
            total += sum(row)
        elif operators[i] == '*':
            total += prod(row)

    return total


def part_two(data: str) -> int:
    rows = [reversed(list(line)) for line in data.splitlines()]
    columns = list(zip(*rows))

    total = 0
    current_operator = ''
    current_numbers = []
    for i, column in enumerate(columns):
        is_empty = all(c == ' ' for c in column)
        is_last = (i + 1 == len(columns))

        if not is_empty:
            current_operator = column[-1] if column[-1] in ('+', '*') else current_operator
            current_numbers.append(int(''.join(column[:-1]).replace(' ', '')))
        if is_empty or is_last:
            if current_operator == '+':
                total += sum(current_numbers)
            elif current_operator == '*':
                total += prod(current_numbers)

            current_numbers = []
            current_operator = ''

    return total


if __name__ == '__main__':
    with open('../inputs/2025/day06.txt') as file:
        raw_data = file.read()

    print(f"Part 1: {part_one(raw_data)}")
    print(f"Part 2: {part_two(raw_data)}")
