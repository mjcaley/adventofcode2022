import pytest
from io import StringIO
from adventofcode2022.day9.rope import parse1, parse2


@pytest.fixture
def test_input():
    return StringIO("""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""").readlines()


@pytest.fixture
def test_input2():
    """Expected tail visits 1."""

    return StringIO("""R 1
D 1
L 2
U 2
R 2""").readlines()


@pytest.fixture
def test_input3():
    """Expected tail visits 12."""

    return StringIO("""D 2
L 2
U 4
R 4
D 4
L 2""").readlines()


@pytest.fixture
def test_input4():
    """Expected tail visits 9."""

    return StringIO("""R 5
L 10
R 10""").readlines()


def test_parse1(test_input):
    result = parse1(test_input)

    assert 13 == result


def test_parse1_circle(test_input2):
    result = parse1(test_input2)

    assert 1 == result


def test_parse1_wide_circle(test_input3):
    result = parse1(test_input3)

    assert 13 == result


def test_parse1_pacing(test_input4):
    result = parse1(test_input4)

    assert 9 == result


def test_parse2(test_input):
    result = parse2(test_input)

    assert 1 == result
