from io import StringIO
import pytest
from adventofcode2022.day11.monkeys import parse1, parse2


@pytest.fixture
def test_input():
    return StringIO("""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""").readlines()


def test_parse1(test_input):
    result = parse1(test_input)

    assert 10605 == result


@pytest.mark.long
def test_parse2(test_input):
    result = parse2(test_input)

    assert 2713310158 == result
