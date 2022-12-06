from dataclasses import dataclass
import re


def parse_crates(line: str) -> list[str | None]:
    crates_strings = (line[crate:crate + 4].strip() for crate in range(0, len(line), 4))
    crates = [crate.strip("[]") if crate else None for crate in crates_strings]
    return crates


def is_stack_index_line(line: str) -> bool:
    return re.match(r"(\s+\d+\s+)+", line)


def parse_stacks(lines: list[str]) -> list[list[str]]:
    grid = []
    for line in reversed(lines):
        grid.append(parse_crates(line))

    stacks = []
    for i in range(len(grid[0])):
        stacks.append([crate[i] for crate in grid if crate[i] is not None])

    return stacks


@dataclass
class Instruction:
    From: int
    To: int
    Quantity: int


def parse_instruction(line: str) -> Instruction:
    match = re.match(r"move (?P<quantity>\d+) from (?P<from>\d+) to (?P<to>\d+)", line)
    return Instruction(
        int(match.group("from")) - 1,
        int(match.group("to")) - 1,
        int(match.group("quantity"))
        )


def execute9000(instruction: Instruction, stacks: list[list[str]]):
    for i in range(instruction.Quantity):
        crate = stacks[instruction.From].pop()
        stacks[instruction.To].append(crate)


def execute9001(instruction: Instruction, stacks: list[list[str]]):
    crates = stacks[instruction.From][-instruction.Quantity:]
    stacks[instruction.From] = stacks[instruction.From][:-instruction.Quantity]
    stacks[instruction.To].extend(crates)


def bottom_row(stacks: list[list[str]]) -> str:
    return "".join([stack[-1] for stack in stacks])


def parse1(lines: list[str]) -> str:
    line_iter = iter(lines)

    stack_lines = []
    for line in line_iter:
        if is_stack_index_line(line):
            break
        
        stack_lines.append(line)

    stacks = parse_stacks(stack_lines)

    next(line_iter)
    for line in line_iter:
        instruction = parse_instruction(line)
        execute9000(instruction, stacks)

    return bottom_row(stacks)


def parse2(lines: list[str]) -> str:
    line_iter = iter(lines)

    stack_lines = []
    for line in line_iter:
        if is_stack_index_line(line):
            break
        
        stack_lines.append(line)

    stacks = parse_stacks(stack_lines)

    next(line_iter)
    for line in line_iter:
        instruction = parse_instruction(line)
        execute9001(instruction, stacks)

    return bottom_row(stacks)
