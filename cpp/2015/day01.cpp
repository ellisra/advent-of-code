#include "../utils.h"
#include <algorithm>
#include <iostream>
#include <vector>

int num_steps_into_basement(std::vector<char>& input);

int main() {
    std::vector<char> input = read_file_to_char_vector("../inputs/2015/day01.txt");

    std::cout << "Part 1: "
        << static_cast<int>(input.size()) - 2 * static_cast<int>(std::ranges::count(input, ')'))
        << "\n";
    std::cout << "Part 2: "
        << num_steps_into_basement(input);
}

int num_steps_into_basement(std::vector<char>& input) {
    int floor_num = 0;
    for (int i = 0; i < static_cast<int>(input.size()); i++) {
        if (floor_num < 0) {
            return i;
        }

        floor_num += (input[i] == '(') ? 1 : -1;
    }

    return -1;
}
