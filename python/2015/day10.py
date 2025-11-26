#!/usr/bin/env python3

from itertools import groupby


with open('../inputs/2015/day10.txt') as f:
    data = f.read().strip()


def look_and_say(look: str) -> str:
    return ''.join(str(len(list(v))) + k for k, v in groupby(look))


def get_result_length(look: str, n_iter: int) -> int:
    for _ in range(n_iter):
        look = look_and_say(look)

    return len(look)


print(f"Part 1: {get_result_length(data, 40)}")
print(f"Part 2: {get_result_length(data, 50)}")
