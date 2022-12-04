def parse(lines: list[str]) -> list[int]:
    elves = []
    current_total = 0
    for line in lines:
        value = line.strip()

        if not value:
            elves.append(current_total)
            current_total = 0
            continue
        
        calories = int(value)
        current_total += calories

    elves.append(current_total)

    return elves


def top1(elves: list[int]) -> int:
    return max(elves)


def top3(elves: list[int]) -> int:
    sorted_elves = list(reversed(sorted(elves)))
    total = sum(sorted_elves[0:3])

    return total