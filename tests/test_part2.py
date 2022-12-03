from io import StringIO
import pytest

from adventofcode2022.part2.game import parse, parse2


@pytest.fixture
def test_input():
    data = """A Y
B X
C Z
"""

    yield StringIO(data).readlines()


def test_calculate_game_score(test_input):
    result = parse(test_input)

    assert 15 == result


def test_calculate_game_score2(test_input):
    result = parse2(test_input)

    assert 12 == result
