use crate::utils::read_lines;

pub fn run() {
    let input = read_lines("../inputs/2015/day02.txt");
    let dimensions = split_dimensions(&input);
    println!("Part 1: {}", part1(&dimensions));
    println!("Part 2: {}", part2(&dimensions));
}

fn split_dimensions(input: &[String]) -> Vec<Vec<i32>> {
    input.iter()
        .map(|line| {
            line.split('x')
                .filter_map(|num| num.parse::<i32>().ok())
                .collect()
        })
        .collect()
}

fn part1(dimensions: &[Vec<i32>]) -> i32 {
    dimensions.iter()
        .map(|dim| {
            let side_areas = vec![dim[0] * dim[1], dim[0] * dim[2], dim[2] * dim[1]];
            2 * side_areas.iter().sum::<i32>() + side_areas.iter().min().unwrap()
        })
        .sum()
}

fn part2(dimensions: &[Vec<i32>]) -> i32 {
    dimensions.iter()
        .map(|dim| {
            let mut sorted_dim = dim.clone();
            sorted_dim.sort_unstable();
            dim[0] * dim[1] * dim[2] + 2 * (sorted_dim[0] + sorted_dim[1])
        })
        .sum()
}
