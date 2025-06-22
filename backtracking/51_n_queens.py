"""
51. N-Queens
-----------
Difficulty: Hard

The n-queens puzzle is the problem of placing n queens on an n x n chessboard
so that no two queens can attack each other.
A queen in a chessboard can attack horizontally, vertically, and diagonally.
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a unique board layout where the queen pieces are placed.
'Q' indicates a queen and '.' indicates an empty space.
You may return the answer in any order.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There are two different solutions to the 4-queens puzzle.

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 8
"""
EMPTY = '.'
QUEEN = 'Q'


def solve_n_queens_backtracking(n: int) -> list[list[str]]:
    """
    Time complexity: O(n!)
    Space complexity: O(n^2)
    """
    layouts = []
    board = [[EMPTY] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            board_copy = [''.join(row) for row in board]
            layouts.append(board_copy)
            return

        for c in range(n):
            if is_safe(r, c, board):
                board[r][c] = QUEEN
                backtrack(r + 1)
                board[r][c] = EMPTY
    backtrack(r=0)
    return layouts


def solve_n_queens_backtracking_hash_set(n: int) -> list[list[str]]:
    pass


def is_safe(row_idx: int, column_idx: int, board: list[list[str]]) -> bool:
    _row_idx = row_idx - 1
    while _row_idx >= 0:
        if board[_row_idx][column_idx] == QUEEN:
            return False

        _row_idx -= 1

    _row_idx, _column_idx = row_idx - 1, column_idx - 1
    while _row_idx >= 0 and _column_idx >= 0:
        if board[_row_idx][_column_idx] == QUEEN:
            return False

        _row_idx -= 1
        _column_idx -= 1

    _row_idx, _column_idx = row_idx - 1, column_idx + 1
    while _row_idx >= 0 and _column_idx < len(board):
        if board[_row_idx][_column_idx] == QUEEN:
            return False

        _row_idx -= 1
        _column_idx += 1

    return True


def test_solve_n_queens():
    solutions = [
        solve_n_queens_backtracking,
    ]

    boards = [
        ['.Q..', '...Q', 'Q...', '..Q.'],
        ['..Q.', 'Q...', '...Q', '.Q..'],
    ]

    test_cases = [
        (4, boards),
        (1, [['Q']]),
    ]

    for solution in solutions:
        for n, expected_result in test_cases:
            # Act
            result = solution(n)

            # Assert
            assert result == expected_result

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_solve_n_queens()
