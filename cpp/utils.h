#pragma once

#include <cstddef>
#include <functional>
#include <string>
#include <utility>
#include <vector>

struct PairHash {
    template <typename T, typename U>
    std::size_t operator()(const std::pair<T, U>& p) const {
        auto h1 = std::hash<T>{}(p.first);
        auto h2 = std::hash<U>{}(p.second);
        return h1 ^ (h2 << 1);
    }
};

std::vector<char> read_file_to_char_vector(const std::string& filename);
