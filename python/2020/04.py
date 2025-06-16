import re


def main():
    with open("../inputs/20_04.txt", "r") as f:
        data = f.read().rstrip()

    passports = data.replace("\n", " ").split("  ")
    print(sum([part1(passport) for passport in passports]))
    print(sum([part2(passport) for passport in passports]))


def part1(passport: str) -> bool:
    key_value_pairs = passport.split(" ")
    keys = [x.split(":")[0] for x in key_value_pairs]

    return all(x in keys for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def part2(passport: str) -> bool:
    passport_dict = {x.split(":")[0]: x.split(":")[1] for x in passport.split(" ")}

    patterns = {
        "byr": r"^(19[2-9]\d|200[0-2])$",
        "iyr": r"^(201\d|2020)$",
        "eyr": r"^(202\d|2030)$",
        "hgt": r"^(1[5-8]\d|19[0-3])cm$|^(59|6\d|7[0-6])in$",
        "hcl": r"^#[0-9a-f]{6}$",
        "ecl": r"^(amb|blu|brn|gry|grn|hzl|oth)$",
        "pid": r"^\d{9}$",
    }

    if not all(
        x in passport_dict.keys()
        for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    ):
        return False

    for key, value in passport_dict.items():
        if key == "cid":
            continue

        if key in patterns:
            if not re.match(patterns[key], str(value)):
                return False
        else:
            return False

    return True


if __name__ == "__main__":
    main()
