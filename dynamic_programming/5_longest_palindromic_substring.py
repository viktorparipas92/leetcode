"""
5. Longest Palindromic Substring
----------------------------
Difficulty: Medium

Given a string s, return the longest substring of s that is a palindrome.
A palindrome is a string that reads the same forward and backward.
If there are multiple palindromic substrings that have the same length, return any one of them.

Example 1:
Input: s = "ababd"
Output: "bab"
Explanation: Both "aba" and "bab" are valid answers.

Example 2:
Input: s = "abbc"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s contains only digits and English letters.
"""


def longest_palindrome_brute_force(word: str) -> str:
    """
    Time complexity: O(n^3)
    Space complexity: O(1)
    """
    palindrome: str = ''
    palindrome_length: int = 0

    length: int = len(word)
    for i in range(length):
        for j in range(i, length):
            left_idx, right_idx = i, j
            while left_idx < right_idx and word[left_idx] == word[right_idx]:
                left_idx += 1
                right_idx -= 1

            if left_idx >= right_idx and palindrome_length < (j - i + 1):
                palindrome = word[i : j + 1]
                palindrome_length = j - i + 1

    return palindrome


def test_longest_palindrome():
    solutions = [
        longest_palindrome_brute_force,
    ]

    test_cases = [
        ('ababd', 'aba'),
        ('abbc', 'bb'),
        ('a', 'a'),
        ('ab', 'a'),
        ('abcba', 'abcba'),
        ('abccba', 'abccba'),
    ]

    for solution in solutions:
        for word, expected_longest_palindrome in test_cases:
            # Act
            longest_palindrome = solution(word)

            # Assert
            assert longest_palindrome == expected_longest_palindrome

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_longest_palindrome()
