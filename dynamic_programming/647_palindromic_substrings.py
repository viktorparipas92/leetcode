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
    for first_idx in range(len(word)):
        for second_idx in range(first_idx, len(word)):
            left_idx, right_idx = first_idx, second_idx
            while left_idx < right_idx and word[left_idx] == word[right_idx]:
                left_idx += 1
                right_idx -= 1

            substring_count += (left_idx >= right_idx)

    return substring_count


def test_count_substrings():
    solutions = [
        count_substrings_brute_force,
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

