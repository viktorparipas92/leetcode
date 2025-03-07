"""
79. Word Search
---------------
Difficulty: Medium

Given a 2-D grid of characters board and a string word, return true if the word is
present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with
horizontally or vertically neighboring cells.
The same cell may not be used more than once in a word.

Example 1:
Input: board = [
['A','B','C','E'],
['S','F','C','S'],
['A','D','E','E'],
], word = 'ABCCED'
Output: true

Example 2:
word = 'SEE'
Output: true

Example 3:
word = 'ABCB'
Output: false
"""


def exist_backtracking_hash_set(board: list[list[str]], word: str) -> bool:
    """
    Time complexity: O(m*4^n)
    where m is the number of cells in the board and n is the length of the word
    Space complexity: O(n)
    """
    num_rows, num_columns = len(board), len(board[0])
    path: set[tuple[int, int]] = set()

    def depth_first_search(row_index: int, column_index: int, i: int) -> bool:
        try:
            word_character = word[i]
        except IndexError:
            return True

        try:
            board_character = board[row_index][column_index]
        except IndexError:
            return False

        if word_character != board_character or (row_index, column_index) in path:
            return False

        path.add((row_index, column_index))
        result = (
            depth_first_search(row_index + 1, column_index, i + 1)
            or depth_first_search(row_index - 1, column_index, i + 1)
            or depth_first_search(row_index, column_index + 1, i + 1)
            or depth_first_search(row_index, column_index - 1, i + 1)
        )
        path.remove((row_index, column_index))
        return result

    for row_idx in range(num_rows):
        for column_idx in range(num_columns):
            if depth_first_search(row_idx, column_idx, i=0):
                return True

    return False


def exist_backtracking_visited_array(board: list[list[str]], word: str) -> bool:
    """
    Time complexity: O(m*4^n)
    where m is the number of cells in the board and n is the length of the word
    Space complexity: O(n)
    """
    num_rows, num_columns = len(board), len(board[0])
    visited: list[list[bool]] = [[False for _ in row] for row in board]

    def depth_first_search(row_index: int, column_index: int, i: int) -> bool:
        try:
            word_character = word[i]
        except IndexError:
            return True

        try:
            board_character = board[row_index][column_index]
        except IndexError:
            return False

        if word_character != board_character or visited[row_index][column_index]:
            return False

        visited[row_index][column_index] = True
        is_word_found = (
            depth_first_search(row_index + 1, column_index, i + 1)
            or depth_first_search(row_index - 1, column_index, i + 1)
            or depth_first_search(row_index, column_index + 1, i + 1)
            or depth_first_search(row_index, column_index - 1, i + 1)
        )
        visited[row_index][column_index] = False
        return is_word_found

    for row_idx in range(num_rows):
        for column_idx in range(num_columns):
            if depth_first_search(row_idx, column_idx, i=0):
                return True

    return False


def test_exist():
    solutions = [
        exist_backtracking_hash_set,
        exist_backtracking_visited_array,
    ]

    character_grid = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E'],
    ]
    test_cases = [
        (character_grid, 'ABCCED', True),
        (character_grid, 'SEE', True),
        (character_grid, 'ABCB', False),
    ]

    for solution in solutions:
        for board, word, expected_is_word_found in test_cases:
            # Act
            is_word_found = solution(board, word)

            # Assert
            assert is_word_found == expected_is_word_found

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_exist()
