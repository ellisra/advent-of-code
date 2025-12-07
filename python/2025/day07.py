#!/usr/bin/env python3


def propagate(grid: list[list[str | int]], i: int, j: int, value: int):
    target = grid[i+1][j]
    if target == '.':
        grid[i+1][j] = value
    elif isinstance(target, int):
        grid[i+1][j] = target + value


def solve(grid: list[list[str | int]]) -> tuple[int, int]:
    n_splits = 0
    grid_max_len = len(grid[0]) - 1
    for i in range(len(grid) - 1):
        for j, cell in enumerate(grid[i]):
            if cell in ('.', '^'):
                continue

            value = cell if isinstance(cell, int) else 0
            if grid[i+1][j] == '^':
                n_splits += 1

                propagate(grid, i, j-1, value)
                if j < grid_max_len:
                    propagate(grid, i, j+1, value)
            else:
                propagate(grid, i, j, value)

        print(''.join(map(str, [f"{x:x}" if isinstance(x, int) else x for x in grid[i]])))

    return n_splits, sum(x if isinstance(x, int) else 0 for x in grid[-1])


if __name__ == '__main__':
    with open('2025/example.txt') as file:
        grid: list[list[str | int]] = [list(line) for line in file.read().splitlines()]

    grid[0] = [1 if x == 'S' else x for x in grid[0]]
    part1, part2 = solve(grid)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
