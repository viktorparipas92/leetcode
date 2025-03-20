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


def partition_backtracking(word: str) -> list[list[str]]:
    """
    Time complexity: O(n * 2^n)
    Space complexity: O(n)
    """
    result, partitions = [], []

    def depth_first_search(j: int, i: int):
        def is_palindrome(word: str, left_index: int, right_index: int):
            while left_index < right_index:
                if word[left_index] != word[right_index]:
                    return False

                left_index, right_index = left_index + 1, right_index - 1

            return True

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


def test_partition():
    solutions = [
        partition_backtracking,
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