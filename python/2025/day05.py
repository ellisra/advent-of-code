#!/usr/bin/env python3


def prepare_data(data: list[str]) -> tuple[list[list[int]], list[int]]:
    delimeter = data.index('')
    intervals, ids = data[:delimeter], data[delimeter+1:]
    intervals = [list(map(int, x.split('-'))) for x in intervals]
    ids = sorted([int(x) for x in ids])

    return intervals, ids


def count_fresh(intervals: list[list[int]], ids: list[int]) -> int:
    return sum(any(start <= id_val <= end for start, end in intervals) for id_val in ids)


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    merged: list[list[int]] = []
    current = intervals[0]
    for interval in intervals:
        if interval[0] <= current[1] + 1:
            current[1] = max(interval[1], current[1])
        else:
            merged.append(current)
            current = interval

    merged.append(current)

    return merged


if __name__ == '__main__':
    with open('../inputs/2025/day05.txt') as file:
        raw_data = file.read().splitlines()

    intervals, ids = prepare_data(raw_data)
    intervals.sort(key=lambda x: x[0])

    print(f"Part 1: {count_fresh(intervals, ids)}")
    print(f"Part 2: {sum(interval[1] - interval[0] + 1 for interval in merge_intervals(intervals))}")
