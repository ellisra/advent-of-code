from common.constants import INPUT_DIR


def part2(data: list[str]) -> int:
    floor_num = 0
    for i, char in enumerate(data):
        if floor_num < 0:
            return i

        if char == '(':
            floor_num += 1
        else:
            floor_num -= 1

    return 0


if __name__ == '__main__':
    with open(INPUT_DIR + '2015/day01.txt', 'r') as file:
        data = list(file.read().strip())

    print(f"Part 1: {len(data) - 2 * data.count(')')}")
    print(f"Part 2: {part2(data)}")
