use std::fs;

use regex::Regex;

pub fn run() {
    let input: Vec<(usize, usize)> = fs::read_to_string("../inputs/2025/day02.txt")
        .expect("Failed to read input")
        .trim_end()
        .split(',')
        .map(|x| {
            let (a, b) = x.split_once('-').unwrap();
            (a.parse().unwrap(), b.parse().unwrap())
        })
        .collect();

    println!("Part 1: {}", part_one(&input));
    println!("Part 2: {}", part_two(&input));
}

fn part_one(ranges: &[(usize, usize)]) -> usize {
    ranges
        .iter()
        .flat_map(|&(start, end)| start..=end)
        .filter(|&i| {
            let s = i.to_string();
            let mid = s.len() / 2;
            s[..mid] == s[mid..]
        })
        .sum()
}

fn part_two(ranges: &[(usize, usize)]) -> usize {
    let re = Regex::new(r"^(.+)\1+$").expect("Invalid regex");
    ranges
        .iter()
        .flat_map(|&(start, end)| start..=end)
        .filter(|&i| re.is_match(&i.to_string()))
        .sum()
}
