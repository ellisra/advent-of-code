#include <cctype>
#include <format>
#include <fstream>
#include <iterator>
#include <vector>

std::vector<char> read_file_to_char_vector(const std::string &filename) {
    std::ifstream file(filename, std::ios::binary);
    if (!file) {
        throw std::runtime_error(std::format("Failed to read file at {}", filename));
    }

    std::vector<char> chars(std::istreambuf_iterator<char>{file}, {});
    while (!chars.empty() && std::isspace(static_cast<unsigned char>(chars.back()))) {
        chars.pop_back();
    }

    return chars;
}
