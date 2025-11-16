from common.constants import INPUT_DIR


def take_step(step: str, pos: tuple[int, int]) -> tuple[int, int]:
    directions = {
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1),
        '^': (-1, 0),
    }
    delta = directions[step]

    return pos[0] + delta[0], pos[1] + delta[1]


def count_unique(steps: list[str]) -> set[tuple[int, int]]:
    current_pos = (0, 0)
    positions: set[tuple[int, int]] = set()
    positions.add(current_pos)
    for step in steps:
        current_pos = take_step(step, current_pos)
        positions.add(current_pos)

    return positions


if __name__ == '__main__':
    with open(INPUT_DIR + '2015/day03.txt', 'r') as file:
        data = list(file.read().strip())

    print(f"Part 1: {len(count_unique(data))}")
    print(f"Part 2: {len(count_unique(data[::2]) | count_unique(data[1::2]))}")
