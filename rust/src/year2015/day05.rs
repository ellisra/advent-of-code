use crate::utils::read_lines;

pub fn run() {
    let input = read_lines("../inputs/2015/day05.txt");

    println!("Part 1: {}", input.iter().filter(|s| part1(s)).count());
    println!("Part 2: {}", input.iter().filter(|s| part2(s)).count());
}

fn part1(s: &str) -> bool {
    s.as_bytes().windows(2).any(|w| w[0] == w[1])
        && s.chars().filter(|c| "aeiou".contains(*c)).count() >= 3
        && !["ab", "cd", "pq", "xy"].iter().any(|&forbidden| s.contains(forbidden))
}

fn part2(s: &str) -> bool {
    s.as_bytes().windows(3).any(|w| w[0] == w[2])
        && has_repeating_pair(s)
}

fn has_repeating_pair(s: &str) -> bool {
    let bytes = s.as_bytes();
    for i in 0..bytes.len().saturating_sub(1) {
        let pair = &bytes[i..i+2];
        if bytes[i+2..].windows(2).any(|w| w == pair) {
            return true;
        }
    }
    false
}
