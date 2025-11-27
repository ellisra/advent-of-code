use std::fs;

pub fn run() {
    let data: Vec<i32> = fs::read_to_string("../inputs/2015/day10.txt")
        .expect("Failed to read input")
        .trim()
        .chars()
        .map(|c| c.to_digit(10).expect("Non-numeric character in input") as i32)
        .collect();

    println!("Part 1 {}", get_result_length(&data, 40));
    println!("Part 2 {}", get_result_length(&data, 50));
}

fn look_and_say(look: &[i32]) -> Vec<i32> {
    look.chunk_by(|a, b| a == b)
        .flat_map(|group| [group.len() as i32, group[0]])
        .collect()
}

fn get_result_length(look: &[i32], n_iter: usize) -> usize {
    (0..n_iter)
        .fold(look.to_vec(), |acc, _| look_and_say(&acc))
        .len()
}
