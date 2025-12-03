#!/usr/bin/env python3


def highest_joltage_pairs(banks: list[list[int]]) -> int:
    total = 0
    for bank in banks:
        i, n1 = max(enumerate(bank[:-1]), key=lambda x: x[1])
        n2 = max(bank[i+1:])
        total += 10 * n1 + n2

    return total


def highest_joltage_twelves(banks: list[list[int]]) -> int:
    total = 0
    for bank in banks:
        digits = []
        for i in range(11, -1, -1):
            j, n = max(enumerate(bank[:len(bank)-i]), key=lambda x: x[1])
            digits.append(n)
            bank = bank[j+1:]
        total += int(''.join(str(d) for d in digits))

    return total


if __name__ == '__main__':
    with open('../inputs/2025/day03.txt') as file:
        banks = [[int(d) for d in line] for line in file.read().splitlines()]

    print(f"Part 1: {highest_joltage_pairs(banks)}")
    print(f"Part 2: {highest_joltage_twelves(banks)}")
