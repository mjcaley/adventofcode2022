from dataclasses import dataclass
from enum import Enum, auto
import re
from typing import Callable, Iterator


class Operation(Enum):
    Mul = lambda left, right: left * right
    Add = lambda left, right: left + right


class Operand(Enum):
    Constant = auto()
    Old = auto()


@dataclass
class Monkey:
    items: list[int]
    operation_parameters: tuple[Operand, int | None, Operation]
    test_parameter: int
    test_true: int
    test_false: int
    inspected: int = 0

    def operation(self, value: int) -> int:
        if self.operation_parameters[0] == Operand.Constant:
            return self.operation_parameters[2](value, self.operation_parameters[1])
        else:
            return self.operation_parameters[2](value, value)

    def test(self, value: int) -> int:
        result = value % self.test_parameter
        if result:
            return self.test_false
        else:
            return self.test_true



class Monkeys:
    def __init__(self, monkeys: list[Monkey], worry_level: int = 1):
        self.monkeys = monkeys
        self.worry_level = worry_level

    def round(self):
        for monkey in self.monkeys:
            for item in monkey.items:
                monkey.inspected += 1
                item = monkey.operation(item)   # I get worried
                item //= 3   # Monkey gets bored
                test = monkey.test(item)
                self.monkeys[test].items.append(item)
            monkey.items = []



def parse_item_ids(line: str) -> list[int]:
    if items_line := re.search(r"Starting items: (?P<item_ids>\d+(, \d+)*)", line.strip()):
        return [int(item_id) for item_id in items_line["item_ids"].split(", ")]
    else:
        raise IOError("Expected item IDs")


def parse_operation(line: str) -> tuple[Operand, int | None, Operation]:
    if not line.strip().startswith(r"Operation:"):
        raise IOError("Cannot parse operation")

    ops = line.strip().removeprefix("Operation: ").split()
    operator, second_op = ops[3:]

    parsed_operator = Operation.Add if operator == "+" else Operation.Mul
    parsed_operand, parsed_value = (Operand.Old,None) if second_op == "old" else (Operand.Constant,int(second_op))

    return parsed_operand, parsed_value, parsed_operator


def parse_test(line: str) -> int:
    if divisor := re.search(r"Test: divisible by (?P<divisor>\d+)", line.strip()):
        return int(divisor["divisor"])
    else:
        raise IOError("Unable to parse test")


def parse_test_result(line: str) -> int:
    if to_monkey := re.search(r"If (true|false): throw to monkey (?P<monkey>\d+)", line.strip()):
        return int(to_monkey["monkey"])
    else:
        raise IOError("Unabel to parse test result")


def parse_monkey(lines: Iterator[str]) -> Monkey:
    line = next(lines)
    item_ids = parse_item_ids(line)
    
    line = next(lines)
    operation = parse_operation(line)

    line = next(lines)
    test = parse_test(line)

    line = next(lines)
    test_true = parse_test_result(line)
    line = next(lines)
    test_false = parse_test_result(line)

    return Monkey(item_ids, operation, test, test_true, test_false)


def parse(lines: list[str]) -> list[Monkey]:
    lines_iter = iter(lines)
    monkeys = []

    for line in lines_iter:
        if not line:
            continue
        if line.startswith("Monkey "):
            monkeys.append(parse_monkey(lines_iter))

    return monkeys


def parse1(lines: list[str]) -> int:
    monkeys = Monkeys(parse(lines), worry_level=3)

    for _ in range(20):
        monkeys.round()

    monkey1, monkey2 = sorted(monkeys.monkeys, key=lambda m: m.inspected, reverse=True)[:2]

    return monkey1.inspected * monkey2.inspected


def parse2(lines: list[str]) -> int:
    monkeys = Monkeys(parse(lines))

    for _ in range(10000):
        monkeys.round()

    monkey1, monkey2 = sorted(monkeys.monkeys, key=lambda m: m.inspected, reverse=True)[:2]

    return monkey1.inspected * monkey2.inspected
