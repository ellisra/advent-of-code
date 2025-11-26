#!/usr/bin/env python3

from itertools import groupby

"""
Given an initial starting string, e.g. aaaaaaaa, it must be incremented (like binary - viginti-sex-ary??). I need to
find the first string which meets the following requirements:
    1. Must contain at least three consecutive letters, e.g. 'abc', 'xyz', 'hij', etc.
    2. May not contain the letters 'i', 'o', or 'l'
    3. Must contain at least two different, non-overlapping pairs of letters
"""


with open('../inputs/2015/day11.txt') as file:
    data = file.read().strip()

password = [ord(c) for c in data]
BANNED = { ord('i'), ord('o'), ord('l') }


def increment(password: list[int], idx: int) -> list[int]:
    if password[idx] == 123:
        password[idx] = 97
        password = increment(password, idx-1)
    else:
        password[idx] += 1

    return password


def is_valid(password: list[int]) -> bool:
    def _has_consecutive(password: list[int]) -> bool:
        for _, g in groupby(enumerate(password), lambda pair: pair[0] - pair[1]):
            if len([x for _, x in g]) >= 3:
                return True
        return False

    def _has_banned_letter(password: list[int]) -> bool:
        return any(c in password for c in BANNED)

    def _has_pairs(password: list[int]) -> bool:
        groups = [list(g) for _, g in groupby(password)]
        return any(len(g) >= 4 for g in groups) or sum(1 for g in groups if len(g) >=2) >= 2

    return _has_consecutive(password) and _has_pairs(password) and not _has_banned_letter(password)


while not is_valid(password):
    idx = -1
    password = increment(password, idx)


print(''.join(chr(d) for d in password))
