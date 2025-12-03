#!/usr/bin/env python3

TEST = [
    [9,8,7,6,5,4,3,2,1,1,1,1,1,1,1],
    [8,1,1,1,1,1,1,1,1,1,1,1,1,1,9],
    [2,3,4,2,3,4,2,3,4,2,3,4,2,7,8],
    [8,1,8,1,8,1,9,1,1,1,1,2,1,1,1],
]


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
        bank_slice = bank
        for i in range(11, -1, -1):
            j, n = max(enumerate(bank_slice), key=lambda x: x[1])
            digits.append(n)
            bank_slice = bank[j+1:-i]
            print(digits)
        total += sum(bank_slice)

    return total


if __name__ == '__main__':
    with open('../inputs/2025/day03.txt') as file:
        banks = [[int(d) for d in line] for line in file.read().splitlines()]

    # print(highest_joltage_pairs(banks))
    print(highest_joltage_twelves(TEST))
