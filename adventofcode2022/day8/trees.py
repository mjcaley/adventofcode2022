def make_grid(lines: list[str]) -> list[list[int]]:
    return [[int(height) for height in line.strip()] for line in lines]


def is_visible(grid: list[list[int]], row: int, column: int) -> bool:
    if row == 0 or column == 0 or row == len(grid[row]) - 1 or column == len(grid) - 1:
        return True

    height = grid[row][column]
    look_at_row = grid[row]
    look_at_column = [rows[column] for rows in grid]

    tallest_left_row = max(tree for tree in look_at_row[:column])
    tallest_right_row = max(tree for tree in look_at_row[column+1:])
    tallest_left_column = max(tree for tree in look_at_column[:row])
    tallest_right_column = max(tree for tree in look_at_column[row+1:])

    return min([tallest_left_row, tallest_left_column, tallest_right_row, tallest_right_column]) < height


def until(height, iterable):
    for other_height in iterable:
        if other_height >= height:
            yield other_height
            break
        yield other_height


def tree_score(grid: list[list[int]], row: int, column: int) -> bool:
    height = grid[row][column]
    look_at_row = grid[row]
    look_at_column = [rows[column] for rows in grid]

    left_row_score = len(list(until(height, reversed(look_at_row[:column]))))
    right_row_score = len(list(until(height, look_at_row[column+1:])))
    left_column_score = len(list(until(height, reversed(look_at_column[:row]))))
    right_column_score = len(list(until(height, look_at_column[row+1:])))

    return left_row_score * right_row_score * left_column_score * right_column_score


def parse1(lines: list[str]) -> int:
    grid = make_grid(lines)

    max_row = len(grid[0])
    max_column = len(grid)

    num_visible = 0
    for row in range(max_row):
        for column in range(max_column):
            if is_visible(grid, row, column):
                num_visible += 1

    return num_visible


def parse2(lines: list[str]) -> int:
    grid = make_grid(lines)

    max_row = len(grid[0])
    max_column = len(grid)

    highest_score = 0
    for row in range(max_row):
        for column in range(max_column):
            score = tree_score(grid, row, column)
            highest_score = max(score, highest_score)

    return highest_score
