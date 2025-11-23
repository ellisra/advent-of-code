from dataclasses import dataclass


@dataclass
class Instruction:
    wire: str
    lhs: int | str | None = None
    operator: str | None = None
    rhs: int | str | None = None


test = [
    '123 -> x',
    '456 -> y',
    'x AND y -> d',
    'x OR y -> e',
    'x LSHIFT 2 -> f',
    'y RSHIFT 2 -> g',
    'NOT x -> h',
    'NOT y -> i',
]

parts = [c.split(' -> ') for c in test]

def handle_cases(wire: str, instruction: list[str]) -> Instruction:
    if len(instruction) == 1:
        return Instruction(
            wire=wire,
            rhs=int(instruction[0]) if instruction[0].isdigit() else instruction[0]
        )
    elif len(instruction) == 2:
        return Instruction(
            wire=wire,
            operator=instruction[0],
            rhs=int(instruction[1]) if instruction[1].isdigit() else instruction[1]
        )
    else:
        return Instruction(
            wire=wire,
            lhs=int(instruction[0]) if instruction[0].isdigit() else instruction[0],
            operator=instruction[1],
            rhs=int(instruction[2]) if instruction[2].isdigit() else instruction[2],
        )


instructions: list[Instruction] = []
for instruction, wire in parts:
    instructions.append(handle_cases(wire, instruction.split(' ')))

print(instructions)
