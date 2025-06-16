def main():
    with open("../inputs/20_03.txt") as file:
        grid = file.read().splitlines()

    print(count_trees(grid, 3, 1))
    print(check_all_slopes(grid, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))


def count_trees(grid: list[str], right: int, down: int) -> int:
    num_trees = 0
    w = len(grid[0])

    for i in range(0, len(grid) // down):
        if grid[i * down][i * right % w] == "#":
            num_trees += 1

    return num_trees


def check_all_slopes(grid: list[str], slopes: list[tuple[int, int]]) -> int:
    total_num_trees = 1
    for slope in slopes:
        total_num_trees *= count_trees(grid, slope[0], slope[1])

    return total_num_trees


if __name__ == "__main__":
    main()
