use std::collections::HashSet;

use crate::utils::read_chars;

pub fn run() {
    let input = read_chars("../inputs/2015/day03.txt");
    println!("Part 1: {}", count_unique(&input).len());
    println!("Part 2: {}", robo_santa(&input));
}

fn take_step(step: &char, pos: (i32, i32)) -> (i32, i32) {
    match step {
        '>' => (pos.0, pos.1 + 1),
        'v' => (pos.0 + 1, pos.1),
        '<' => (pos.0, pos.1 - 1),
        '^' => (pos.0 - 1, pos.1),
        _ => pos,
    }
}

fn count_unique(steps: &[char]) -> HashSet<(i32, i32)> {
    let mut current_pos = (0, 0);
    let mut positions = HashSet::new();
    for step in steps {
        positions.insert(current_pos);
        current_pos = take_step(step, current_pos);
    }

    positions
}

fn robo_santa(steps: &[char]) -> usize {
    let mut total_positions = HashSet::new();
    let real_steps: Vec<char> = steps.iter().step_by(2).copied().collect();
    let robo_steps: Vec<char> = steps.iter().skip(1).step_by(2).copied().collect();
    total_positions.extend(count_unique(&real_steps));
    total_positions.extend(count_unique(&robo_steps));

    total_positions.len()
}
