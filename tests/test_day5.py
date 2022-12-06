from io import StringIO
import pytest
from adventofcode2022.day5.stacks import parse1, parse2


@pytest.fixture
def test_input():
    yield StringIO("""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""").readlines()


def test_parse1(test_input):
    result = parse1(test_input)

    assert "CMZ" == result


def test_parse2(test_input):
    result = parse2(test_input)

    assert "MCD" == result
