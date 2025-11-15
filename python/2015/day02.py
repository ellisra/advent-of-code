from __future__ import annotations

from dataclasses import astuple, dataclass

from common.constants import INPUT_DIR


@dataclass
class Present:
    length: int
    width: int
    height: int

    @property
    def wrapping_area(self) -> int:
        sides = [self.length * self.width, self.width * self.height, self.height * self.length]

        return 2 * sum(sides) + min(sides)

    @property
    def volume(self) -> int:
        return self.length * self.width * self.height

    @property
    def smallest_perimeter(self) -> int:
        return 2 * sum(sorted(astuple(self))[:-1])

    @classmethod
    def from_line(cls, line: str) -> Present:
        length, width, height = map(int, line.strip().split('x'))

        return cls(length, width, height)


if __name__ == '__main__':
    with open(INPUT_DIR + '2015/day02.txt', 'r') as file:
        data = [Present.from_line(line) for line in file]

    print(f"Part 1: {sum(present.wrapping_area for present in data)}")
    print(f"Part 2: {sum(present.smallest_perimeter + present.volume for present in data)}")
