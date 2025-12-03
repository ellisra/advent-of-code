#!/usr/bin/env python3

def solve(lines: list[int]):
    pos1, pos2 = 50, 50
    part1, part2 = 0, 0
    for step in lines:
        pos1 += step
        pos1 %= 100
        if pos1 == 0:
            part1 += 1

        for _ in range(abs(step)):
            pos2 += 1 if step > 0 else -1
            pos2 %= 100
            if pos2 == 0:
                part2 += 1

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == '__main__':
    with open('../inputs/2025/day01.txt') as file:
        data = [int(line.replace('R', '').replace('L', '-')) for line in file]

    solve(data)
