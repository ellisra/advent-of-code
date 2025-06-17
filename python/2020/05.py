def main():
    with open("../inputs/20_05.txt", "r") as f:
        data = f.read().splitlines()

    all_ids = set([get_pos(line[:7]) * 8 + get_pos(line[-3:]) for line in data])
    print(max(all_ids))
    print(find_my_id(all_ids))


def get_pos(code: str) -> int:
    remaining = list(range(pow(2, len(code))))

    for char in code:
        if char == "F" or char == "L":
            remaining = remaining[: len(remaining) // 2]
        else:
            remaining = remaining[len(remaining) // 2 :]

    return remaining[0]


def find_my_id(all_ids: set[int]) -> int:
    candidates = [num for num in range(1024) if num not in all_ids]

    for i in range(1, len(candidates) - 1):
        if candidates[i] + 1 in all_ids and candidates[i] - 1 in all_ids:
            return candidates[i]

    return 0


if __name__ == "__main__":
    main()
