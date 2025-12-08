#!/usr/bin/env python3

from __future__ import annotations

from collections import defaultdict
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


@dataclass
class Path:
    p1: Point
    p2: Point
    distance: int


def get_shortest_path(flatmap: dict[tuple[int, int], int], points: list[Point]) -> Path:
    key = min(flatmap, key=flatmap.__getitem__)
    value = flatmap[key]
    del flatmap[key]

    return Path(points[key[0]], points[key[1]], value)


if __name__ == '__main__':
    with open('2025/example.txt') as file:
    # with open('../inputs/2025/day08.txt') as file:
        points = [Point.from_line(line) for line in file]

    get_distance: Callable[[Point, Point], int] = lambda a, b: (a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2
    distance_map = defaultdict(dict)

    for i, point in enumerate(points):
        distance_map[i] = {
            i: get_distance(point, points[i])
            for i in range(len(points))
            if point != points[i]
        }

    flatmap: dict[tuple[int, int], int] = {(min(ok, ik), max(ok, ik)): v for ok, inner in distance_map.items() for ik, v in inner.items()}
    sorted_flatmap = sorted(flatmap.items(), key=lambda x: x[1])

    print(sorted_flatmap[:11])
