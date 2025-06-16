from typing import NamedTuple


class Expression(NamedTuple):
    min_num: int
    max_num: int
    key: str
    password: str


def main():
    lines = [line for line in open("../inputs/20_02.txt")]
    expressions = [parse_expression(ex) for ex in lines]
    print(part1(expressions))
    print(part2(expressions))


def parse_expression(ex: str) -> Expression:
    range_part, key_part, password = ex.split(" ")
    min_num, max_num = range_part.split("-")
    key_letter = key_part.rstrip(":")

    return Expression(int(min_num), int(max_num), key_letter, password.rstrip())


def part1(expressions: list[Expression]) -> int:
    return sum(
        [ex.min_num <= ex.password.count(ex.key) <= ex.max_num for ex in expressions]
    )


def part2(expressions: list[Expression]) -> int:
    return sum(
        [
            (ex.password[ex.min_num - 1] == ex.key)
            != (ex.password[ex.max_num - 1] == ex.key)
            for ex in expressions
        ]
    )


if __name__ == "__main__":
    main()
