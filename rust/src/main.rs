mod utils;
mod year2015;

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 3 {
        eprintln!("Usage: cargo run <year> <day>");
        std::process::exit(1);
    }

    let year: u32 = args[1].parse().unwrap();
    let day: u32 = args[2].parse().unwrap();
    dispatch(year, day);
}

fn dispatch(year: u32, day: u32) {
    match (year, day) {
        (2015, 1) => year2015::day01::run(),
        (2015, 2) => year2015::day02::run(),
        (2015, 3) => year2015::day03::run(),
        _ => panic!("Unknown year/day combination"),
    }
}
