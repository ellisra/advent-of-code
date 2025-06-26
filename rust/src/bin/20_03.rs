use std::fs::read_to_string;

fn main() {
    let grid: Vec<Vec<char>> = read_to_string("../inputs/20_03.txt")
        .unwrap()
        .trim()
        .lines()
        .map(|l| l.chars().collect())
        .collect();

    println!("Part 1: {}", part1(&grid, 3, 1));
    println!(
        "Part 2: {}",
        part2(&grid, vec![(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])
    );
}

fn part1(grid: &Vec<Vec<char>>, right: i32, down: i32) -> i32 {
    let mut num_trees = 0;
    let w = grid[0].len();

    for i in 0..grid.len() as i32 / down {
        if grid[(i * down) as usize][(i * right) as usize % w] == '#' {
            num_trees += 1;
        }
    }

    num_trees
}

fn part2(grid: &Vec<Vec<char>>, slopes: Vec<(i32, i32)>) -> i32 {
    let mut total_num_trees = 1;

    for slope in slopes.iter() {
        total_num_trees *= part1(grid, slope.0, slope.1);
    }

    total_num_trees
}
