use std::fs;

/// Read file contents to vector of characters, removing newlines
pub fn read_chars(path: &str) -> Vec<char> {
    fs::read_to_string(path)
        .expect("Failed to read file")
        .chars()
        .filter(|&c| c != '\n')
        .collect()
}
