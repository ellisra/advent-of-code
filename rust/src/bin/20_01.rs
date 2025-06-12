use std::{collections::HashSet, fs::read_to_string};

fn part1(nums: &Vec<i32>) -> i32 {
    let mut seen = HashSet::<&i32>::new();

    for num in nums {
        let complement = 2020 - num;

        if seen.contains(&complement) {
            return num * complement;
        }

        seen.insert(num);
    }

    return 0;
}

fn part2(nums: &Vec<i32>) -> i32 {
    for num1 in nums {
        let complement1 = 2020 - num1;

        for num2 in nums {
            let complement2 = complement1 - num2;

            if nums.contains(&complement2) {
                return num1 * num2 * complement2;
            }
        }
    }

    return 0;
}

fn main() {
    let mut nums = Vec::<i32>::new();
    for line in read_to_string("../inputs/20_01.txt").unwrap().lines() {
        nums.push(line.parse::<i32>().unwrap());
    }
    println!("{}", part1(&nums));
    println!("{}", part2(&nums));
}
