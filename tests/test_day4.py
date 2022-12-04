from io import StringIO
import pytest
from adventofcode2022.day4.sections import parse1, parse2


@pytest.fixture
def test_input():
    yield StringIO("""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""").readlines()


def test_parse1(test_input):
    result = parse1(test_input)

    assert 2 == result


def test_parse2(test_input):
    result = parse2(test_input)

    assert 4 == result
