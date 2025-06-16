use std::fs;

struct Expression {
    min_num: i32,
    max_num: i32,
    key: char,
    password: String,
}

fn main() {
    let input = fs::read_to_string("../inputs/20_02.txt").expect("File not found");
    let expressions: Vec<Expression> = input.lines().map(parse_expression).collect();

    println!("{}", part1(&expressions));
    println!("{}", part2(&expressions));
}

fn parse_expression(ex: &str) -> Expression {
    let parts: Vec<&str> = ex.split_whitespace().collect();

    let (min_str, max_str) = parts[0].split_once('-').expect("Invalid range");
    let min_num = min_str.parse().expect("Failed to parse min");
    let max_num = max_str.parse().expect("Failed to parse max");

    let key = parts[1]
        .trim_end_matches(":")
        .chars()
        .next()
        .expect("No key found");

    Expression {
        min_num,
        max_num,
        key,
        password: parts[2].to_string(),
    }
}

fn part1(expressions: &[Expression]) -> i32 {
    expressions
        .iter()
        .filter(|ex| {
            let count = ex.password.chars().filter(|&c| c == ex.key).count();
            count >= ex.min_num as usize && count <= ex.max_num as usize
        })
        .count() as i32
}

fn part2(expressions: &[Expression]) -> i32 {
    expressions
        .iter()
        .filter(|ex| {
            let chars: Vec<char> = ex.password.chars().collect();
            let first_match = chars.get((ex.min_num - 1) as usize) == Some(&ex.key);
            let second_match = chars.get((ex.max_num - 1) as usize) == Some(&ex.key);
            first_match != second_match
        })
        .count() as i32
}
