use std::fs;

pub fn run() {
    let input: Vec<i32> = fs::read_to_string("../inputs/2025/day01.txt")
        .expect("Failed to read input")
        .lines()
        .filter_map(|line| {
            let line = line.trim();
            let number: i32 = line[1..].parse().ok()?;
            match line.chars().next()? {
                'R' => Some(number),
                'L' => Some(-number),
                _ => None
            }
        })
        .collect();

    solve(&input);
}

fn solve(lines: &[i32]) {
    let mut pos1 = 50;
    let mut pos2 = 50;
    let mut part1 = 0;
    let mut part2 = 0;

    for &step in lines {
        pos1 = (pos1 + step).rem_euclid(100);
        if pos1 == 0 {
            part1 += 1
        }

        let direction = step.signum();
        for _ in 0..step.abs() {
            pos2 = (pos2 + direction).rem_euclid(100);
            if pos2 == 0 {
                part2 += 1;
            }
        }
    }

    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}
