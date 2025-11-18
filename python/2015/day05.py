import re

from common.constants import INPUT_DIR

VOWELS = { 'a', 'e', 'i', 'o', 'u' }
BANNED_STRINGS = { 'ab', 'cd', 'pq', 'xy' }


def part_one(lines: list[str]) -> int:
    num_nice = 0
    for line in lines:
        vowel_count = 0
        has_double_letter = False

        if any(banned_string in line for banned_string in BANNED_STRINGS):
            continue

        for i in range(len(line)):
            vowel_count += 1 if line[i] in VOWELS else 0

            if i != len(line) - 1 and line[i] == line[i+1]:
                has_double_letter = True

        if vowel_count >= 3 and has_double_letter:
            num_nice += 1

    return num_nice


def part_two(lines: list[str]) -> int:
    def _rule_one(line: str) -> bool:
        for i in range(len(line) - 2):
            pair = line[i:i+2]
            if pair in line[i+2:]:
                return True
        return False

    def _rule_two(line: str) -> bool:
        for i in range(len(line) - 2):
            if line[i] == line[i+2]:
                return True
        return False

    num_nice = 0
    for line in lines:
        if _rule_one(line) and _rule_two(line):
            num_nice += 1

    return num_nice


if __name__ == '__main__':
    with open(INPUT_DIR + '2015/day05.txt', 'r') as file:
        text = file.read()

    print(f"Part 1: {len(re.findall(r"^(?=\w*([a-z])\1\w*)(?!.*(?:ab|cd|pq|xy))(?:.*[aeiou]){3}.*$", text, re.MULTILINE))}")
    print(f"Part 2: {len(re.findall(r"^(?=.*([a-z]{2}).*\1)(?=.*([a-z]).\2).*$", text, re.MULTILINE))}")
