def part1(report: set[int]) -> int:
    seen = set()

    for num in report:
        complement = 2020 - num

        if complement in seen:
            return num * complement

        seen.add(num)

    return 0


def part2(report: set[int]) -> int:
    # HACK: This works but has the edge case of not checking if a number is reused
    for num1 in report:
        complement1 = 2020 - num1

        for num2 in report:
            complement2 = complement1 - num2

            if complement2 in report:
                return num1 * num2 * complement2

    return 0


if __name__ == "__main__":
    report = set(map(int, [num for num in open("../../inputs/20_01.txt")]))
    print(part2(report))
