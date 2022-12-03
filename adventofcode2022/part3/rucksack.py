from itertools import islice
from string import ascii_lowercase, ascii_uppercase


def split_rucksack(contents: str) -> tuple[set[str], set[str]]:
    left, right = contents[:len(contents)//2], contents[len(contents)//2:]

    return set(left), set(right)


def priority(item: str) -> int:
    if item in ascii_lowercase:
        return ord(item) - 96
    elif item in ascii_uppercase:
        return ord(item) - 38


def parse1(lines: list[str]) -> int:
    sacks = []

    for line in lines:
        left, right = split_rucksack(line.strip())
        duplicate = list(left.intersection(right))[0]
        priority_value = priority(duplicate)
        sacks.append(priority_value)

    total = sum(sacks)

    return total


def parse2(lines: list[str]) -> int:
    badges = []

    line_groups = [
        islice(lines, None, None, 3),
        islice(lines, 1, None, 3),
        islice(lines, 2, None, 3)
    ]
    for groups in zip(*line_groups):
        first, second, third = set(groups[0].strip(),), set(groups[1].strip()), set(groups[2].strip())
        badge = list(first.intersection(second).intersection(third))[0]
        priority_value = priority(badge)
        badges.append(priority_value)

    total = sum(badges)

    return total
