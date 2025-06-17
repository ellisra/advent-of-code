def main():
    with open("../inputs/20_06.txt", "r") as f:
        data = f.read().rstrip()

    groups = data.split("\n\n")

    total_num1 = 0
    total_num2 = 0
    for group in groups:
        answer_sets = [set(answer) for answer in group.split("\n")]

        all_answers = set().union(*answer_sets)
        total_num1 += len(all_answers)

        common_answers = set.intersection(*answer_sets)
        total_num2 += len(common_answers)

    print(f"Part 1: {total_num1}")
    print(f"Part 2: {total_num2}")


if __name__ == "__main__":
    main()
