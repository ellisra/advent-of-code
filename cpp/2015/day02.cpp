#include <algorithm>
#include <array>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

struct Present {
    int length, width, height;

    int wrapping_area() const {
        std::array<int, 3> sides = {length * width, width * height, height * length};
        return 2 * std::accumulate(sides.begin(), sides.end(), 0) + *std::min_element(sides.begin(), sides.end());
    }

    int volume() const {
        return length * width * height;
    }

    int smallest_perimeter() const {
        int max_dimension = std::max({length, width, height});
        return 2 * (length + width + height - max_dimension);
    }

    static Present from_line(const std::string &line) {
        int length, width, height;
        sscanf(line.c_str(), "%dx%dx%d", &length, &width, &height);
        return {length, width, height};
    }
};

int main() {
    std::vector<Present> input;
    std::ifstream file("../inputs/2015/day02.txt");
    std::string line;
    while (std::getline(file, line)) { input.push_back(Present::from_line(line)); }
    file.close();

    int total_area = 0;
    int ribbon_length = 0;
    for (const auto &present : input) {
        total_area += present.wrapping_area();
        ribbon_length += present.smallest_perimeter() + present.volume();
    }

    std::cout << "Part 1: " << total_area << "\nPart 2: " << ribbon_length;
}
