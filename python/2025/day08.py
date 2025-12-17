#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from math import prod
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
class Connection:
    p1: int
    p2: int
    distance: int


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x: int) -> int:
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


def group_circuits(connected: list[Connection], n_points: int):
    # uf = UnionFind()
    # for conn in connected:
    #     uf.union(conn.p1, conn.p2)
    #
    # circuits: dict[int, set[int]] = {}
    # for point in uf.parent.keys():
    #     root = uf.find(point)
    #     if root not in circuits:
    #         circuits[root] = set()
    #     circuits[root].add(point)
    #
    # return list(circuits.values())

    circuits: list[set[int]] = []
    bridge = None

    for conn in connected:
        circuit_with_p1 = None
        circuit_with_p2 = None

        for circuit in circuits:
            if conn.p1 in circuit:
                circuit_with_p1 = circuit
            if conn.p2 in circuit:
                circuit_with_p2 = circuit

        if circuit_with_p1 is None and circuit_with_p2 is None:
            circuits.append({conn.p1, conn.p2})
        elif circuit_with_p1 is None:
            circuit_with_p2.add(conn.p1)
        elif circuit_with_p2 is None:
            circuit_with_p1.add(conn.p2)
        elif circuit_with_p1 is circuit_with_p2:
            pass
        else:
            circuit_with_p1.update(circuit_with_p2)
            circuits.remove(circuit_with_p2)

        n_circuits = len(circuits)
        all_points_in_circuits = set()
        for circuit in circuits:
            all_points_in_circuits.update(circuit)

        if n_circuits == 1 and len(all_points_in_circuits) == n_points:
            bridge = conn
            break

    return circuits, bridge


if __name__ == '__main__':
    # with open('2025/example.txt') as file:
    with open('../inputs/2025/day08.txt') as file:
        points = [Point.from_line(line) for line in file]

    get_distance: Callable[[Point, Point], int] = lambda a, b: (a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2

    flatmap: list[Connection] = sorted([
        Connection(i, j, get_distance(points[i], points[j]))
        for i in range(len(points))
        for j in range(i + 1, len(points))
    ], key=lambda x: x.distance)

    grouped, bridge = group_circuits(flatmap, len(points))
    grouped = sorted(grouped, key=lambda x: len(x), reverse=True)

    # print(prod(len(grouped[i]) for i in range(3)))
    print(points[bridge.p1].x * points[bridge.p2].x)
