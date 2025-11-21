use crate::utils::read_lines;

enum Direction {
    On,
    Off,
    Toggle,
}

struct Instruction {
    direction: Direction,
    start_coords: (usize, usize),
    end_coords: (usize, usize),
}

pub fn run() {
    let input = read_lines("../inputs/2015/day06.txt");
    let instructions = parse_instructions(&input);

    println!("Part 1: {}", part1(&instructions));
    println!("Part 2: {}", part2(&instructions));
}

fn part1(instructions: &[Instruction]) -> i32 {
    let mut grid = vec![vec![0; 1000]; 1000];
    for i in instructions {
        let (start_col, start_row) = i.start_coords;
        let (end_col, end_row) = i.end_coords;

        for row in start_row..=end_row {
            let slice = &mut grid[row][start_col..=end_col];
            match i.direction {
                Direction::On => slice.fill(1),
                Direction::Off => slice.fill(0),
                Direction::Toggle => slice.iter_mut().for_each(|light| *light = 1 - *light),
            }
        }
    }

    grid.iter().flatten().sum()
}

fn part2(instructions: &[Instruction]) -> u32 {
    let mut grid = vec![vec![0u32; 1000]; 1000];
    for i in instructions {
        let (start_col, start_row) = i.start_coords;
        let (end_col, end_row) = i.end_coords;

        for row in start_row..=end_row {
            let slice = &mut grid[row][start_col..=end_col];
            match i.direction {
                Direction::On => slice.iter_mut().for_each(|light| *light += 1),
                Direction::Toggle => slice.iter_mut().for_each(|light| *light += 2),
                Direction::Off => slice.iter_mut().for_each(|light| *light = light.saturating_sub(1)),
            }
        }
    }

    grid.iter().flatten().sum()
}

fn parse_instructions(lines: &[String]) -> Vec<Instruction> {
    lines.iter().map(|line| {
        let parts: Vec<&str> = line.split_whitespace().collect();
        let (direction_str, start, end) = if parts[0] == "turn" {
            (parts[1], parts[2], parts[4])
        } else {
            (parts[0], parts[1], parts[3])
        };

        let direction = match direction_str {
            "on" => Direction::On,
            "off" => Direction::Off,
            "toggle" => Direction::Toggle,
            _ => panic!("Unknown direction"),
        };

        Instruction {
            direction,
            start_coords: parse_coords(start),
            end_coords: parse_coords(end),
        }
    }).collect()
}

fn parse_coords(coord_str: &str) -> (usize, usize) {
    let (x, y) = coord_str.split_once(',').expect("Malformed coordinates");
    (x.parse().expect("Invalid coordinates"), y.parse().expect("Invalid coordinates"))
}
