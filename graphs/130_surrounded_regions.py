"""
130. Surrounded Regions
-----------------------
Difficulty: Medium

You are given a 2-D matrix board containing 'X' and 'O' characters.
If a continuous, four-directionally connected group of 'O's is surrounded by 'X's,
it is considered to be surrounded.
Change all surrounded regions of 'O's to 'X's
and do so in-place by modifying the input board.

Example 1:
Input: board = [
  ['X','X','X','X'],
  ['X','O','O','X'],
  ['X','O','O','X'],
  ['X','X','X','O']
]

Output: [
  ['X','X','X','X'],
  ['X','X','X','X'],
  ['X','X','X','X'],
  ['X','X','X','O']
]
Explanation: Note that regions that are on the border
are not considered surrounded regions.

Constraints:
1 <= board.length, board[i].length <= 200
board[i][j] is 'X' or 'O'.
"""

LAND = 'O'
SEA = 'X'
TEMP = 'T'


def solve_depth_first_search(board: list[list[str]]) -> None:
    """
    Time complexity: O(m * n)
    Space complexity: O(m * n)
    where m is the number of rows and n is the number of columns in the board.
    """
    def capture(row_idx: int, column_idx: int) -> None:
        if row_idx < 0 or column_idx < 0 :
            return

        try:
            cell = board[row_idx][column_idx]
        except IndexError:
            return

        if cell != LAND:
            return

        board[row_idx][column_idx] = TEMP

        capture(row_idx + 1, column_idx)
        capture(row_idx - 1, column_idx)
        capture(row_idx, column_idx + 1)
        capture(row_idx, column_idx - 1)

    height = len(board)
    width = len(board[0])
    for r, row in enumerate(board):
        if row[0] == LAND:
            capture(r, column_idx=0)

        if row[-1] == LAND:
            capture(r, column_idx=width - 1)

    for c in range(width):
        if board[0][c] == LAND:
            capture(row_idx=0, column_idx=c)

        if board[-1][c] == LAND:
            capture(row_idx=height - 1, column_idx=c)

    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell == LAND:
                board[r][c] = SEA
            elif cell == TEMP:
                board[r][c] = LAND


def test_solve():
    solutions = [
        solve_depth_first_search,
    ]

    input_board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'O'],
    ]
    output_board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'O'],
    ]
    test_cases = [
        (input_board, output_board),
    ]

    for solution in solutions:
        for input_board, output_board in test_cases:
            # Act
            solution(input_board)

            # Assert
            assert input_board == output_board

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_solve()

