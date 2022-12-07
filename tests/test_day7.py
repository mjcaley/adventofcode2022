from io import StringIO
import pytest
from adventofcode2022.day7.disk import parse1, parse2


@pytest.fixture
def test_input():
    yield StringIO("""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""").readlines()


def test_parse1(test_input):
    result = parse1(test_input)

    assert 95437 == result


def test_parse2(test_input):
    result = parse2(test_input)

    assert 24933642 == result
