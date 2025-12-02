#!/usr/bin/env python3

import re


def part_one(ranges: list[list[int]]) -> int:
    total = 0
    for start, end in ranges:
        for i in range(start, end + 1):
            i_str = str(i)
            i_len = len(i_str)
            if i_str[:i_len//2] == i_str[i_len//2:]:
                total += i

    return total


def part_two(ranges: list[list[int]]) -> int:
    total = 0
    pattern = re.compile(r"^(.+)\1+$")
    for start, end in ranges:
        for i in range(start, end + 1):
            if pattern.match(str(i)):
                total += i

    return total


if __name__ == '__main__':
    with open('../inputs/2025/day02.txt') as file:
        ranges = [list(map(int, x.split('-'))) for x in file.read().rstrip().split(',')]

    print(f"Part 1: {part_one(ranges)}")
    print(f"Part 2: {part_two(ranges)}")
