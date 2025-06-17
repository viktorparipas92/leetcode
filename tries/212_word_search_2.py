"""
212. Word Search II
-------------------
Difficulty: Hard

Given a 2-D grid of characters board and a list of strings words,
return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board
with horizontally or vertically neighboring cells.
The same cell may not be used more than once in a word.

Example 1:
Input:
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
],
words = ["bat","cat","back","backend","stack"]
Output: ["cat","back","backend"]

Example 2:
Input:
board = [
  ["x","o"],
  ["x","o"]
],
words = ["xoxo"]
Output: []

Constraints:
1 <= board.length, board[i].length <= 10
board[i] consists only of lowercase English letter.
1 <= words.length <= 100
1 <= words[i].length <= 10
words[i] consists only of lowercase English letters.
All strings within words are distinct.
"""


def find_words_backtracking(board: list[list[str]], words: list[str]) -> list[str]:
    """
    Time complexity: O(m * n * 4^k + s)
    Space complexity: O(k)
    where
    - m is the number of rows,
    - n is the number of columns in the board,
    - k is the maximum length of a word in words,
    - s is the total number of characters in words.
    """
    def backtrack(row_idx: int, col_idx: int, i: int) -> bool:
        """
        Backtracking function to search for the word in the board.
        """
        if i == len(word):
            return True

        if (
            row_idx < 0
            or col_idx < 0
            or row_idx >= height
            or col_idx >= width
            or board[row_idx][col_idx] != word[i]
        ):
            return False

        board[row_idx][col_idx] = '*'
        result = (
            backtrack(row_idx + 1, col_idx, i + 1)
            or backtrack(row_idx - 1, col_idx, i + 1)
            or backtrack(row_idx, col_idx + 1, i + 1)
            or backtrack(row_idx, col_idx - 1, i + 1)
        )
        board[row_idx][col_idx] = word[i]
        return result

    height, width = len(board), len(board[0])
    found_words: list[str] = []
    for word in words:
        flag = False
        for row_index in range(height):
            if flag:
                break

            for column_index in range(width):
                if board[row_index][column_index] != word[0]:
                    continue

                if backtrack(row_index, column_index, 0):
                    found_words.append(word)
                    flag = True
                    break

    return found_words


def test_find_words():
    solutions = [
        find_words_backtracking,
    ]

    board_1 = [
        ['a', 'b', 'c', 'd'],
        ['s', 'a', 'a', 't'],
        ['a', 'c', 'k', 'e'],
        ['a', 'c', 'd', 'n'],
    ]
    words_1 = ['bat', 'cat', 'back', 'backend', 'stack']
    found_words_1 = ['cat', 'back', 'backend']

    board_2 = [['x', 'o'], ['x', 'o']]
    test_cases = [
        ((board_1, words_1), found_words_1),
        ((board_2, ['xoxo']), []),
    ]

    for solution in solutions:
        for (board, words), expected_found_words in test_cases:
            # Act
            found_words = solution(board, words)

            # Assert
            assert sorted(found_words) == sorted(expected_found_words)

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_find_words()