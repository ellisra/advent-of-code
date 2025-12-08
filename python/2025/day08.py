#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass
class Point:
    x: int
    y: int
    z: int

    @classmethod
    def from_line(cls, line: str) -> Point:
        x, y, z = map(int, line.strip().split(','))

        return cls(x, y, z)


if __name__ == '__main__':
    with open('2025/example.txt') as file:
    # with open('../inputs/2025/day08.txt') as file:
        points = [Point.from_line(line) for line in file]

    get_distance: Callable[[Point, Point], int] = lambda a, b: (a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2
    flatmap: dict[tuple[int, int], int] = {
        (i, j): get_distance(points[i], points[j])
        for i in range(len(points))
        for j in range(i + 1, len(points))
    }
    sorted_flatmap = sorted(flatmap.items(), key=lambda x: x[1])

    print(sorted_flatmap[:10])
