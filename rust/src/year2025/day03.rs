use std::fs;

pub fn run() {
    let input: Vec<Vec<i32>> = fs::read_to_string("../inputs/2025/day03.txt")
        .expect("Failed to read input file")
        .lines()
        .map(|line| {
            line.trim()
                .chars()
                .map(|c| c.to_digit(10).expect("Non-numeric character in input") as i32)
                .collect()
        })
        .collect();

    println!("Part 1: {}", highest_pairs(&input));
    println!("Part 2: {}", highest_twelves(&input));
}

fn highest_pairs(banks: &Vec<Vec<i32>>) -> i32 {
    let mut total = 0;
    for bank in banks {
        let (i, &n1) = bank[..bank.len()-1]
            .iter()
            .enumerate()
            .max_by(|(i1, a), (i2, b)| a.cmp(b).then(i2.cmp(i1)))
            .unwrap();
        let &n2 = bank[i+1..]
            .iter()
            .max()
            .unwrap();
        total += 10 * n1 + n2;
    }

    total
}

fn highest_twelves(banks: &Vec<Vec<i32>>) -> i64 {
    let mut total = 0i64;
    for bank in banks {
        let mut bank_slice = &bank[..];
        let mut digits: Vec<i32> = vec![];
        for i in (0..=11).rev() {
            let (j, &n) = bank_slice[..bank_slice.len()-i]
                .iter()
                .enumerate()
                .max_by(|(j1, a), (j2, b)| a.cmp(b).then(j2.cmp(j1)))
                .unwrap();
            digits.push(n);
            bank_slice = &bank_slice[j+1..];
        }
        total += digits.iter().fold(0i64, |acc, elem| acc * 10 + *elem as i64);
    }

    total
}
