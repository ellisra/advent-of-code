#!/usr/bin/env python3


from collections import defaultdict


if __name__ == '__main__':
    # with open('2025/example.txt') as file:
    with open('../inputs/2025/day09.txt') as file:
        data = [tuple(map(int, line.split(','))) for line in file.read().splitlines()]

    diffs = defaultdict(dict)
    for point in data:
        diffs[point] = {
            p2: abs(1 + point[0] - p2[0]) * abs(1 + point[1] - p2[1])
            for p2 in data
        }

    p1, p2, val = max(
        ((ok, ik, val) for ok, inner in diffs.items() for ik, val in inner.items()),
        key=lambda x: x[2]
    )

    print(val)
