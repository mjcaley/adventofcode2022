from dataclasses import dataclass
from itertools import cycle, islice
from typing import Generator


class Noop:
    ...


@dataclass
class AddX:
    operand: int


class VideoCircuit:
    def __init__(self, instructions: list[Noop | AddX]):
        self.instructions = instructions
        self.x_register = 1
        self._ticks = 0

        self.pixel = cycle(range(240))
        self.screen = ["."] * 40 * 6

    def draw(self):
        pixel_index = next(self.pixel)
        sprite_range = [
            self.x_register - 1 + (40 * 0), self.x_register + (40 * 0), self.x_register + 1 + (40 * 0),
            self.x_register - 1 + (40 * 1), self.x_register + (40 * 1), self.x_register + 1 + (40 * 1),
            self.x_register - 1 + (40 * 2), self.x_register + (40 * 2), self.x_register + 1 + (40 * 2),
            self.x_register - 1 + (40 * 3), self.x_register + (40 * 3), self.x_register + 1 + (40 * 3),
            self.x_register - 1 + (40 * 4), self.x_register + (40 * 4), self.x_register + 1 + (40 * 4),
            self.x_register - 1 + (40 * 5), self.x_register + (40 * 5), self.x_register + 1 + (40 * 5),
        ]
        if pixel_index in sprite_range:
            self.screen[pixel_index] = "#"

    def tick(self) -> int:
        self.draw()
        self._ticks += 1
        return self._ticks * self.x_register

    def execute(self):
        for instruction in self.instructions:
            if isinstance(instruction, Noop):
                yield self.tick()
            else:
                yield self.tick()
                yield self.tick()
                self.x_register += instruction.operand


def parse(lines: list[str]) -> Generator[Noop | AddX, None, None]:
    for line in lines:
        if line.strip() == "noop":
            yield Noop()
        else:
            keyword, operand = line.strip().split()
            yield AddX(int(operand))


def parse1(lines: list[str]) -> int:
    vm = VideoCircuit(parse(lines))

    return sum(islice(vm.execute(), 19, None, 40))


def batched(iterable, n):
    "Batch data into lists of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while (batch := list(islice(it, n))):
        yield batch


def parse2(lines: list[str]) -> str:
    vm = VideoCircuit(parse(lines))

    for _ in vm.execute():
        pass

    rows = [row for row in batched(vm.screen, 40)]
    screen = "\n".join(["".join(row) for row in rows])

    return screen
