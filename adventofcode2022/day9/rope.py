from __future__ import annotations
from copy import copy
from dataclasses import dataclass, field
from enum import Enum
from itertools import pairwise
from math import sqrt
from typing import Generator


def clamp(value) -> int:
    return max(-1, min(value, 1))


@dataclass
class Point:
    x: int = 0
    y: int = 0

    def chessboard_distance_to(self, other: Point) -> int:
        return max(abs(other.x - self.x), abs(other.y - self.y))

    def normalize(self) -> Point:
        return Point(clamp(self.x), clamp(self.y))

    def direction_to(self, other: Point) -> Point:
        return other - self

    def move_toward(self, head: Point) -> Point:
        if self.chessboard_distance_to(head) > 1:
            direction = self.direction_to(head)
            normalized = direction.normalize()
            self += normalized

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other: Point) -> Point:
        x = self.x + other.x
        y = self.y + other.y

        return Point(x, y)

    def __iadd__(self, other: Point) -> Point:
        self.x += other.x
        self.y += other.y
        
        return self

    def __sub__(self, other: Point) -> Point:
        x = self.x - other.x
        y = self.y - other.y

        return Point(x, y)

    def __isub__(self, other: Point) -> Point:
        self.x -= other.x
        self.y -= other.y

        return self


class Direction(Enum):
    Right = Point(x=1, y=0)
    Left = Point(x=-1, y=0)
    Up = Point(x=0, y=1)
    Down = Point(x=0, y=-1)


@dataclass
class Instruction:
    direction: Direction
    steps: int


def parse(lines: list[str]) -> Generator[Instruction, None, None]:
    for line in lines:
        if line[0] == "R":
            direction = Direction.Right
        elif line[0] == "L":
            direction = Direction.Left
        elif line[0] == "U":
            direction = Direction.Up
        else:
            direction = Direction.Down

        steps = int(line[2:])

        yield Instruction(direction, steps)


def parse1(lines: list[str]) -> int:
    head = Point()
    tail = Point()
    visited = {tail}
    
    instructions = parse(lines)
    for instruction in instructions:
        for _ in range(instruction.steps):
            head += instruction.direction.value
            tail.move_toward(head)
            visited.add(copy(tail))
            
            try:
                assert abs(head.x - tail.x) <= 1
                assert abs(head.y - tail.y) <= 1
            except AssertionError:
                breakpoint()

    return len(visited)


def parse2(lines: list[str]) -> int:
    knots = [Point() for _ in range(10)]
    visited = {knots[-1]}
    instructions = parse(lines)

    for instruction in instructions:
        for _ in range(instruction.steps):
            knots[0] += instruction.direction.value
            for head, tail in pairwise(knots):
                tail.move_toward(head)

            visited.add(copy(knots[-1]))

    return len(visited)
