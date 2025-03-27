"""
131. Palindrome Partitioning
--------------------------------
Difficulty: Medium

Given a string s, split s into substrings where every substring is a palindrome.
Return all possible lists of palindromic substrings.
You may return the solution in any order.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
1 <= s.length <= 20
s contains only lowercase English letters.
"""


def is_palindrome(word: str, left_index: int, right_index: int):
    while left_index < right_index:
        if word[left_index] != word[right_index]:
            return False

        left_index, right_index = left_index + 1, right_index - 1

    return True


def partition_backtracking(word: str) -> list[list[str]]:
    """
    Time complexity: O(n * 2^n)
    Space complexity: O(n)
    """
    result, partitions = [], []

    def depth_first_search(j: int, i: int):
        if i >= len(word):
            if i == j:
                result.append(partitions.copy())

            return

        if is_palindrome(word, j, i):
            partitions.append(word[j: i + 1])
            depth_first_search(i + 1, i + 1)
            partitions.pop()

        depth_first_search(j, i + 1)

    depth_first_search(0, 0)
    return result


def partition_backtracking_2(word: str) -> list[list[str]]:
    result, partitions = [], []

    def depth_first_search(i: int):
        if i >= len(word):
            result.append(partitions.copy())
            return

        for j in range(i, len(word)):
            if is_palindrome(word, i, j):
                partitions.append(word[i : j + 1])
                depth_first_search(j + 1)
                partitions.pop()

    depth_first_search(i=0)
    return result


def partition_backtracking_dp(word: str) -> list[list[str]]:
    """
    Time complexity: O(n * 2^n)
    Space complexity: O(n^2)
    """
    length = len(word)

    def depth_first_search(i: int):
        if i >= length:
            result.append(partitions.copy())
            return

        for j in range(i, length):
            if _is_palindrome[i][j]:
                partitions.append(word[i: j + 1])
                depth_first_search(j + 1)
                partitions.pop()

    _is_palindrome: list[list[bool]] = [[False] * length for _ in range(length)]
    for _len in range(length):
        for i in range(length - _len):
            k = i + _len
            _is_palindrome[i][k] = (
                word[i] == word[k]
                and ((i + 1 > k - 1) or _is_palindrome[i + 1][k - 1])
            )

    result, partitions = [], []
    depth_first_search(i=0)
    return result


def test_partition():
    solutions = [
        partition_backtracking,
        partition_backtracking_2,
        partition_backtracking_dp,
    ]

    test_cases = [
        ('aab', [['a', 'a', 'b'], ['aa', 'b']]),
        ('a', [['a']]),
    ]

    for solution in solutions:
        for word, expected_partitions in test_cases:
            # Act
            partitions = solution(word)

            # Assert
            assert expected_partitions == partitions

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_partition()