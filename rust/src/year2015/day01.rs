use crate::utils::read_chars;

pub fn run() {
    let input = read_chars("../inputs/2015/day01.txt");
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}

fn part1(input: &[char]) -> i32 {
    input.iter().map(|&c| if c == '(' { 1 } else { -1 }).sum()
}

fn part2(input: &[char]) -> i32 {
    let mut floor = 0;
    for (i, &step) in input.iter().enumerate() {
        if floor < 0 { return i as i32 }
        floor += if step == '(' { 1 } else { -1 };
    }
    panic!("Never entered the basement")
}
