from io import StringIO
import pytest
from adventofcode2022.day8.trees import make_grid, parse1, parse2, tree_score


@pytest.fixture
def test_input():
    yield StringIO("""30373
25512
65332
33549
35390""").readlines()


def test_parse1(test_input):
    result = parse1(test_input)

    assert 21 == result


def test_parse2(test_input):
    result = parse2(test_input)

    assert 8 == result


@pytest.mark.parametrize("row,column,score", [
    (1, 2, 4),
    (3, 2, 8)
])
def test_parse2_1_2(test_input, row, column, score):
    grid = make_grid(test_input)
    result = tree_score(grid, row, column)

    assert score == result

