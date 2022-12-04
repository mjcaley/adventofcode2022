from itertools import permutations


def range_to_set(section_range: tuple[int, int]) -> set[int]:
    return {digit for digit in range(section_range[0], section_range[1] + 1)}


def is_contained(section1: set[int], section2: set[int]) -> bool:
    if section1 <= section2:
        return True
    elif section2 <= section1:
        return True

    return False


def any_overlap(section1: set[int], section2: set[int]) -> bool:
    if len(section1 & section2):
        return True
    elif len(section2 & section1):
        return True
    
    return False


def parse_section_range(section_range: str) -> tuple[int, int]:
    start, end = section_range.split("-")

    return int(start), int(end)


def parse_line(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    left, right = line.split(",")

    return parse_section_range(left), parse_section_range(right)


def parse1(lines: list[str]) -> int:
    overlaps = 0

    for line in lines:
        first, second = parse_line(line)
        if is_contained(range_to_set(first), range_to_set(second)):
            overlaps += 1

    return overlaps


def parse2(lines: list[str]) -> int:
    overlaps = 0

    for line in lines:
        first, second = parse_line(line)
        if any_overlap(range_to_set(first), range_to_set(second)):
            overlaps += 1

    return overlaps
