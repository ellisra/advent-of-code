#include <charconv>
#include <cstddef>
#include <fstream>
#include <iostream>
#include <ranges>
#include <regex>
#include <string>
#include <string_view>
#include <utility>
#include <vector>

long part_one(const std::vector<std::pair<long, long>>& ranges) {
    long total = 0;
    for (const auto& [start, end] : ranges) {
        for (long i = start; i <= end; i++) {
            std::string i_str = std::to_string(i);
            size_t middle = i_str.size() / 2;

            if (i_str.compare(0, middle, i_str, middle, i_str.size()) == 0) {
                total += i;
            }
        }
    }

    return total;
}

long part_two(const std::vector<std::pair<long, long>>& ranges) {
    long total = 0;
    std::regex pattern("^(.+)\\1+$");
    for (const auto& [start, end] : ranges) {
        for (long i = start; i <= end; i++) {
            if (std::regex_search(std::to_string(i), pattern)) {
                total += i;
            }
        }
    }

    return total;
}

int main() {
    std::ifstream file("../inputs/2025/day02.txt");
    std::string data;
    std::getline(file, data);
    std::vector<std::pair<long, long>> input;

    for (const auto pair_view : std::ranges::views::split(data, ',')) {
        std::string_view sv(pair_view.begin(), pair_view.end());
        auto dash_pos = sv.find('-');
        long lhs, rhs;

        std::from_chars(sv.data(), sv.data() + dash_pos, lhs);
        std::from_chars(sv.data() + dash_pos + 1, sv.data() + sv.size(), rhs);
        input.emplace_back(lhs, rhs);
    }

    std::cout << "Part 1: " << part_one(input) << "\nPart 2: " << part_two(input);
}
