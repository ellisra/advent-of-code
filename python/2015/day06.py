from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from common.constants import INPUT_DIR


@dataclass
class Instruction:
    direction: str
    start_coords: tuple[int, int]
    end_coords: tuple[int, int]


def parse_instructions(instructions: list[str]) -> list[Instruction]:
    parsed_instructions: list[Instruction] = []
    for instruction in instructions:
        instruction = instruction.split(' ')
        if instruction[0] == 'turn':
            instruction = instruction[1:]

        try:
            start_coords = tuple(map(int, instruction[1].split(',')))
            end_coords = tuple(map(int, instruction[-1].split(',')))
        except ValueError as e:
            raise ValueError(f"Failed to parse coordinates from {instruction}: {e}")

        if len(start_coords) != 2 or len(end_coords) != 2:
            print(f"Too many coordinates to unpack from {instruction}")
            raise

        parsed_instructions.append(Instruction(
            direction=instruction[0],
            start_coords=start_coords,
            end_coords=end_coords,
        ))

    return parsed_instructions


def part_one(instructions: list[Instruction]) -> int:
    grid = np.full((1000,1000), False, dtype=bool)

    for ins in instructions:
        start_col, start_row = ins.start_coords
        end_col, end_row = ins.end_coords

        if ins.direction == 'on':
            grid[start_row:end_row+1, start_col:end_col+1] = True
        elif ins.direction == 'off':
            grid[start_row:end_row+1, start_col:end_col+1] = False
        else:
            grid[start_row:end_row+1, start_col:end_col+1] = np.logical_not(
                grid[start_row:end_row+1, start_col:end_col+1]
            )

    return np.sum(grid)


@np.vectorize
def smart_dim(arr: NDArray[np.int16]) -> NDArray[np.int16]:
    if arr > 0:
        return arr - 1
    else:
        return arr


def part_two(instructions: list[Instruction]) -> int:
    grid = np.full((1000,1000), 0, dtype=int)

    for ins in instructions:
        start_col, start_row = ins.start_coords
        end_col, end_row = ins.end_coords

        if ins.direction == 'on':
            grid[start_row:end_row+1, start_col:end_col+1] += 1
        elif ins.direction == 'toggle':
            grid[start_row:end_row+1, start_col:end_col+1] += 2
        else:
            grid[start_row:end_row+1, start_col:end_col+1] = smart_dim(
                grid[start_row:end_row+1, start_col:end_col+1]
            )

    return np.sum(grid)


if __name__ == '__main__':
    with open(INPUT_DIR + '2015/day06.txt') as file:
        instructions = file.read().splitlines()

    instructions = parse_instructions(instructions)

    print(f"Part 1: {part_one(instructions)}")
    print(f"Part 2: {part_two(instructions)}")
