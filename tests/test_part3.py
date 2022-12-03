from io import StringIO

import pytest

from adventofcode2022.part3.rucksack import parse1, parse2


@pytest.fixture
def test_input():
    yield StringIO("""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""").readlines()


def test_parse1(test_input):
    result = parse1(test_input)

    assert 157 == result


def test_parse2(test_input):
    result = parse2(test_input)

    assert 70 == result
