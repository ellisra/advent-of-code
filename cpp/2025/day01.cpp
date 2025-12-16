#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

struct Results {
    int part1;
    int part2;
};

std::vector<int> read_input(std::string filepath) {
    std::vector<int> data;
    std::ifstream file(filepath);
    std::string line;

    while (std::getline(file, line)) {
        line.erase(std::remove(line.begin(), line.end(), 'R'), line.end());
        std::replace(line.begin(), line.end(), 'L', '-');
        data.push_back(std::stoi(line));
    }
    file.close();

    return data;
}

int euclidean_mod(int a) {
    return ((a % 100) + 100) % 100;
}

Results solve(std::vector<int> data) {
    int pos1 = 50;
    int pos2 = 50;
    int part1 = 0;
    int part2 = 0;

    for (int i = 0; i < data.size(); i++) {
        pos1 += data[i];
        pos1 = euclidean_mod(pos1);
        if (pos1 == 0) part1++;

        for (int j = 0; j < abs(data[i]); j++) {
            pos2 += (data[i] > 0) ? 1 : -1;
            pos2 = euclidean_mod(pos2);
            if (pos2 == 0) part2++;
        }
    }

    Results results = { part1, part2 };
    return results;
}

int main() {
    std::vector<int> data = read_input("../inputs/2025/day01.txt");
    Results results = solve(data);

    std::cout << "Part 1: " << results.part1 << "\nPart 2: " << results.part2;
}
