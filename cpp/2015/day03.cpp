#include <cstddef>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
#include "utils.h"

std::pair<int, int> take_step(char step, std::pair<int, int> position) {
    std::unordered_map<char, std::pair<int, int>> directions = {
        {'>', {0, 1}},
        {'v', {1, 0}},
        {'<', {0, -1}},
        {'^', {-1, 0}},
    };

    return {
        position.first + directions[step].first,
        position.second + directions[step].second,
    };
}

int count_unique(std::vector<char> steps) {
    std::pair<int, int> current_position = {0, 0};
    std::unordered_set<std::pair<int, int>, PairHash> positions{current_position};
    for (const auto &step : steps) {
        current_position = take_step(step, current_position);
        positions.insert(current_position);
    }

    return positions.size();
}

std::vector<char> slice_nth(const std::vector<char>& vec, int start, int step) {
    std::vector<char> result;
    for (size_t i = start; i < vec.size(); i += step) {
        result.push_back(vec[i]);
    }

    return result;
}

int main() {
    std::vector<char> input = read_file_to_char_vector("../inputs/2015/day03.txt");
    std::cout << "Part 1: "  << count_unique(input) << "\n";
}
