#!/usr/bin/env python3

import json
import re
from typing import Any

with open('../inputs/2015/day12.txt') as file:
    data = file.read().strip()

print(f"Part 1: {sum(map(int, re.findall(r"-?\d+", data)))}")


def sum_object(obj: Any) -> int:
    if isinstance(obj, int):
        return obj

    if isinstance(obj, list):
        return sum(map(sum_object, obj))

    if isinstance(obj, dict):
        vals = obj.values()
        if 'red' in vals:
            return 0

        return sum(map(sum_object, vals))

    return 0


obj = json.loads(data)
print(f"Part 2: {sum_object(obj)}")
