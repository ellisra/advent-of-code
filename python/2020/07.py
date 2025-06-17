import re
from collections import deque
from functools import lru_cache


def main():
    with open("../inputs/20_07.txt", "r") as f:
        data = f.read().splitlines()

    rules = parse_rules(data)

    print(f"Part 1: {part1(rules)}")
    print(f"Part 2: {part2(rules)}")


def parse_rules(rules: list[str]) -> dict[str, dict[str, int]]:
    rules_dict = {}

    for rule in rules:
        key_match = re.match(r"^([a-z ]+) bags contain (.+)\.", rule)
        if not key_match:
            continue

        key_bag = key_match.group(1)
        contents = key_match.group(2)

        rules_dict[key_bag] = {}

        if contents == "no other bags":
            continue

        contained_bags = re.findall(r"(\d+) ([a-z ]+) bags?", contents)

        for count, bag_colour in contained_bags:
            rules_dict[key_bag][bag_colour] = int(count)

    return rules_dict


def part1(rules: dict[str, dict[str, int]]) -> int:
    def find_containers(colour: str) -> list[str]:
        return [col for col in rules.keys() if colour in rules[col].keys()]

    visited = set()
    queue = deque(["shiny gold"])

    while queue:
        current = queue.popleft()
        containers = find_containers(current)

        for container in containers:
            if container not in visited:
                visited.add(container)
                queue.append(container)

    return len(visited)


def part2(rules: dict[str, dict[str, int]]) -> int:
    @lru_cache(maxsize=None)
    def num_bags_contained(colour: str) -> int:
        if not rules[colour]:
            return 0

        return sum(
            count + count * num_bags_contained(contained_colour)
            for contained_colour, count in rules[colour].items()
        )

    return num_bags_contained("shiny gold")


if __name__ == "__main__":
    main()
