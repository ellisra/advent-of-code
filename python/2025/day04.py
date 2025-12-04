#!/usr/bin/env python3

import numpy as np
from numpy.typing import NDArray


def get_accessible(
    grid: NDArray[np.str_],
    padded: NDArray[np.str_],
    offsets: list[tuple[int, int]],
) -> NDArray[np.bool]:
    num_neighbours = sum(padded[1+di:1+di+grid.shape[0], 1+dj:1+dj+grid.shape[1]] == '@' for di, dj in offsets)

    return (num_neighbours < 4) & (grid == '@')


def remove_rolls(accessible: NDArray[np.bool], grid: NDArray[np.str_]) -> NDArray[np.str_]:
    ...


if __name__ == '__main__':
    with open('../inputs/2025/day04.txt') as file:
        grid = np.array([list(line.strip()) for line in file], dtype=np.str_)

    padded = np.pad(grid, pad_width=1, mode='constant', constant_values='#')
    offsets = [(di, dj) for di in [-1, 0, 1] for dj in [-1, 0, 1] if (di, dj) != (0, 0)]

    print(f"Part 1: {get_accessible(grid, padded, offsets).sum()}")
