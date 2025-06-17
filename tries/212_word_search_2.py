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


class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_word: bool = False

    def add_word(self, word: str) -> None:
        current_node = self
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()

            current_node = current_node.children[char]

        current_node.is_word = True


def find_words_trie_hash_set(board: list[list[str]], words: list[str]) -> list[str]:
    """
    Time complexity: O(m * n * 4 * 3^(k-1) + s)
    Space complexity: O(s)
    """
    def depth_first_search(
        row_index: int, column_index: int, node: TrieNode, word: str
    ):
        if (
            row_index < 0
            or column_index < 0
            or (row_index, column_index) in visited_cells
        ):
            return

        try:
            cell: str = board[row_index][column_index]  # Character in the board
            if cell not in node.children:
                return
        except IndexError:
            return

        visited_cells.add((row_index, column_index))
        node = node.children[cell]
        word += cell
        if node.is_word:
            found_words.add(word)

        depth_first_search(row_index + 1, column_index, node, word)
        depth_first_search(row_index - 1, column_index, node, word)
        depth_first_search(row_index, column_index + 1, node, word)
        depth_first_search(row_index, column_index - 1, node, word)
        visited_cells.remove((row_index, column_index))

    root_node = TrieNode()
    for word in words:
        root_node.add_word(word)

    height, width = len(board), len(board[0])
    found_words: set[str] = set()
    visited_cells: set[tuple[int, int]] = set()

    for row_idx in range(height):
        for column_idx in range(width):
            depth_first_search(row_idx, column_idx, root_node, word='')

    return list(found_words)


def test_find_words():
    solutions = [
        find_words_backtracking,
        find_words_trie_hash_set,
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