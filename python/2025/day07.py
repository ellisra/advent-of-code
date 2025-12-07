#!/usr/bin/env python3


if __name__ == '__main__':
    with open('2025/example.txt') as file:
    # with open('../inputs/2025/day07.txt') as file:
        grid: list[list[str | int]] = [list(line) for line in file.read().splitlines()]
        # grid[0] = ['|' if x == 'S' else x for x in grid[0]]
        grid[0] = [1 if x == 'S' else x for x in grid[0]]

    part1 = 0
    for i, row in enumerate(grid[1:]):
        for j, char in enumerate(row):
            if grid[i][j] not in ('.', '^'):
                if grid[i+1][j] == '^':
                    part1 += 1

                    if grid[i+1][j+1] == '.':
                        grid[i+1][j+1] = grid[i][j]
                    elif isinstance(grid[i+1][j+1], int):
                        grid[i+1][j+1] += grid[i][j]  # type: ignore

                    if grid[i+1][j-1] == '.':
                        grid[i+1][j-1] = grid[i][j]
                    elif isinstance(grid[i+1][j-1], int):
                        grid[i+1][j-1] += grid[i][j]  # type: ignore
                else:
                    if grid[i+1][j] == '.':
                        grid[i+1][j] = grid[i][j]
                    elif isinstance(grid[i+1][j], int):
                        grid[i+1][j] += grid[i][j]  # type: ignore

        print(''.join(map(str, [f"{x:x}" if isinstance(x, int) else x for x in row])))

    print(f"Part 1: {part1}")
    print(f"Part 2: {sum([x if isinstance(x, int) else 0 for x in grid[-1]])}")
