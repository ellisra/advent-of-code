use std::fs;

use md5;

pub fn run() {
    let key = fs::read_to_string("../inputs/2015/day04.txt").unwrap().trim().to_string();

    let mut num = 0;
    loop {
        let digest = md5::compute(format!("{}{}", key, &num));
        if format!("{:x}", digest).starts_with("000000") {
            println!("{}", num);
            break;
        }

        num += 1;
    }
}
