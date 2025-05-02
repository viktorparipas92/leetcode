"""
647. Palindromic Substrings
---------------------------
Difficulty: Medium

Given a string s, return the number of substrings within s that are palindromes.
A palindrome is a string that reads the same forward and backward.

Example 1:
Input: s = "abc"
Output: 3
Explanation: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings
are counted as different palindromes even if the string contents are the same.

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""


def count_substrings_brute_force(word: str) -> int:
    """
    Time complexity: O(n^3)
    Space complexity: O(1)
    """
    substring_count: int = 0
    length = len(word)
    for first_idx in range(length):
        for second_idx in range(first_idx, length):
            left_idx, right_idx = first_idx, second_idx
            while left_idx < right_idx and word[left_idx] == word[right_idx]:
                left_idx += 1
                right_idx -= 1

            substring_count += (left_idx >= right_idx)

    return substring_count


def count_substrings_dynamic(word: str) -> int:
    """
    Time complexity: O(n^2)
    Space complexity: O(n^2)
    """
    substring_count: int = 0
    length = len(word)
    is_palindrome: list[list[bool]] = [[False] * length for _ in range(length)]

    for _, first_char in enumerate(reversed(word)):
        first_idx = length - 1 - _
        for second_idx, second_char in enumerate(word[first_idx:], start=first_idx):
            if (
                first_char == second_char and
                (
                    second_idx - first_idx <= 2
                    or is_palindrome[first_idx + 1][second_idx - 1]
                )
            ):
                is_palindrome[first_idx][second_idx] = True
                substring_count += 1

    return substring_count


def count_substrings_two_pointers_optimized(word: str) -> int:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    def count_palindromes(left_idx: int, right_idx: int) -> int:
        count = 0
        while (
            left_idx >= 0
            and right_idx < length
            and word[left_idx] == word[right_idx]
        ):
            count += 1
            left_idx -= 1
            right_idx += 1

        return count

    substring_count: int = 0
    length: int = len(word)
    for idx in range(length):
        substring_count += count_palindromes(left_idx=idx, right_idx=idx)
        substring_count += count_palindromes(left_idx=idx, right_idx=idx + 1)

    return substring_count


def test_count_substrings():
    solutions = [
        count_substrings_brute_force,
        count_substrings_dynamic,
        count_substrings_two_pointers_optimized,
    ]
    test_cases = [
        ('abc', 3),
        ('aaa', 6),
    ]

    for solution in solutions:
        for word, expected_substring_count in test_cases:
            # Act
            substring_count = solution(word)

            # Assert
            assert substring_count == expected_substring_count

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_count_substrings()
