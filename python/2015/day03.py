from collections import namedtuple

from common.constants import INPUT_DIR

Position = namedtuple('Position', ['y', 'x'])


def step(pos: Position, direction: str) -> Position:
    if direction == '^':
        return Position(pos.y - 1, pos.x)
    elif direction == 'V':
        return Position(pos.y + 1, pos.x)
    elif direction == '>':
        return Position(pos.y, pos.x + 1)
    else:
        return Position(pos.y, pos.x - 1)


def part1(data: list[str]) -> int:
    current_pos = Position(y=0, x=0)
    houses: set[Position] = set(current_pos)

    for move in data:
        current_pos = step(current_pos, move)
        houses.add(current_pos)

    return len(houses)


if __name__ == '__main__':
    with open(INPUT_DIR + '2015/day03.txt', 'r') as file:
        data = list(file.read().strip())

    print(f"Part 1: {part1(data)}")
