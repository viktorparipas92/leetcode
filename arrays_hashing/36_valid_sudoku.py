'''
36. Valid Sudoku
----------------
Difficulty: Medium

Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:
- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily
solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''


def flatten(i: int, j: int) -> int:
    return (i // 3) * 3 + j // 3


def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == '.':
                continue
            elif (
                cell in rows[i]
                or cell in cols[j]
                or cell in boxes[flatten(i, j)]
            ):
                return False

            rows[i].add(cell)
            cols[j].add(cell)
            boxes[flatten(i, j)].add(cell)

    return True


def test_is_valid_sudoku():
    valid_board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]
    assert is_valid_sudoku(valid_board) is True

    invalid_board = [
        ['8', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]
    assert is_valid_sudoku(invalid_board) is False


if __name__ == '__main__':
    test_is_valid_sudoku()
