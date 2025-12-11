#!/usr/bin/env python3

from collections import defaultdict


def parse_graph(lines: list[list[str]]) -> dict[str, list[str]]:
    graph = defaultdict(list)
    for line in lines:
        graph[line[0][:-1]] = line[1:]

    return graph


def depth_first_search(
    graph: dict[str, list[str]],
    start: str,
    end: str,
    path: list[str],
    all_paths: list[list[str]],
):
    path.append(start)
    if start == end:
        all_paths.append(path.copy())
    else:
        for adjacent_node in graph[start]:
            if adjacent_node not in path:
                depth_first_search(graph, adjacent_node, end, path, all_paths)

    path.pop()



def count_paths(graph: dict[str, list[str]], start: str, end: str, part: int = 1) -> int:
    all_paths = []
    path = []
    depth_first_search(graph, start, end, path, all_paths)

    if part == 2:
        return sum(['fft' in path and 'dac' in path for path in all_paths])
    else:
        return len(all_paths)


if __name__ == '__main__':
    with open('2025/example.txt') as file:
    # with open('../inputs/2025/day11.txt') as file:
        lines = file.read().splitlines()
        lines = [line.split() for line in lines]

    graph = parse_graph(lines)
    print(count_paths(graph=graph, start='svr', end='out', part=2))
