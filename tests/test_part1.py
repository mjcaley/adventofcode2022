from io import StringIO

import pytest

from adventofcode2022.part1.calorie_parser import parse, top1, top3


@pytest.fixture
def test_input():
    data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
    yield StringIO(data).readlines()


def test_parse(test_input):
    elves = parse(test_input)

    assert 6000 == elves[0]
    assert 4000 == elves[1]
    assert 11000 == elves[2]
    assert 24000 == elves[3]
    assert 10000 == elves[4]


def test_top1(test_input):
    result = top1(parse(test_input))

    assert 24000 == result


def test_top3(test_input):
    result = top3(parse(test_input))

    assert 45000 == result
