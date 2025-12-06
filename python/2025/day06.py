#!/usr/bin/env python3

from math import prod


def part_one(data: str) -> int:
    lines = data.splitlines()
    operators = lines.pop(-1).split()
    raw_nums = [line.split() for line in lines]
    digits = [list(row) for row in zip(*raw_nums)]
    nums = [list(map(int, row)) for row in digits]
    total = 0
    for i, row in enumerate(nums):
        if operators[i] == '+':
            total += sum(row)
        elif operators[i] == '*':
            total += prod(row)

    return total


if __name__ == '__main__':
    # with open('2025/example.txt') as file:
    with open('../inputs/2025/day06.txt') as file:
        raw_data = file.read()

    print(f"Part 1: {part_one(raw_data)}")

    rows = [list(line) for line in raw_data.splitlines()]
    rows = [reversed(line) for line in rows]
    columns = [list(row) for row in zip(*rows)]

    total = 0
    operator = ''
    nums = []
    for i, col in enumerate(columns):
        if not all(x == ' ' for x in col):
            operator = col[-1] if col[-1] in ('+', '*') else operator
            nums.append(int(''.join(col[:-1]).replace(' ', '')))
        if all(x == ' ' for x in col) or i+1 == len(columns):
            if operator == '+':
                total += sum(nums)
            elif operator == '*':
                total += prod(nums)
            # print(operator, nums)
            nums = []
            operator = ''

    print(total)
