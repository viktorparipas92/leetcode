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


def longest_palindrome_dynamic(word: str) -> str:
    """
    Time complexity: O(n^2)
    Space complexity: O(n^2)
    """
    result_start_index: int = 0
    palindrome_length: int = 0
    length: int = len(word)

    is_candidate: list[list[bool]] = [[False] * length for _ in range(length)]

    for i in range(length - 1, -1, -1):
        for j in range(i, length):
            if (
                word[i] == word[j]
                and (j - i <= 2 or is_candidate[i + 1][j - 1])
            ):
                is_candidate[i][j] = True
                if palindrome_length < (j - i + 1):
                    result_start_index = i
                    palindrome_length = j - i + 1

    return word[result_start_index: result_start_index + palindrome_length]


def longest_palindrome_two_pointers(word: str) -> str:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    result_start_index: int = 0
    palindrome_length: int = 0

    length = len(word)
    for i in range(length):
        left_idx = right_idx = i
        # Odd-length palindrome
        while (
            left_idx >= 0
            and right_idx < len(word)
            and word[left_idx] == word[right_idx]
        ):
            if (right_idx - left_idx + 1) > palindrome_length:
                result_start_index = left_idx
                palindrome_length = right_idx - left_idx + 1

            left_idx -= 1
            right_idx += 1

        # Even-length palindrome
        left_idx = i
        right_idx = i + 1
        while (
            left_idx >= 0
            and right_idx < len(word)
            and word[left_idx] == word[right_idx]
        ):
            if (right_idx - left_idx + 1) > palindrome_length:
                result_start_index = left_idx
                palindrome_length = right_idx - left_idx + 1

            left_idx -= 1
            right_idx += 1

    return word[result_start_index: result_start_index + palindrome_length]


def test_longest_palindrome():
    solutions = [
        longest_palindrome_brute_force,
        longest_palindrome_dynamic,
        longest_palindrome_two_pointers,
    ]

    test_cases = [
        ('ababd', {'aba', 'bab'}),
        ('abbc', {'bb'}),
    ]

    for solution in solutions:
        for word, expected_longest_palindromes in test_cases:
            # Act
            longest_palindrome = solution(word)

            # Assert
            assert longest_palindrome in expected_longest_palindromes

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_longest_palindrome()
