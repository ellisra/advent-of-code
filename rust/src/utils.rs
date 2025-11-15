use std::fs::{self};

/// Read file contents to vector of characters, removing newlines
pub fn read_chars(path: &str) -> Vec<char> {
    fs::read_to_string(path)
        .expect("Failed to read file")
        .chars()
        .filter(|&c| c != '\n')
        .collect()
}

/// Read file contents to vector of line strings
pub fn read_lines(path: &str) -> Vec<String> {
    fs::read_to_string(path)
        .expect("Failed to read file")
        .lines()
        .map(String::from)
        .collect()
}
