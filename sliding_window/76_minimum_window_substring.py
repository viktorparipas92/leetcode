"""
76. Minimum Window Substring
----------------------------
Difficulty: Hard

Given two strings s and t, return the shortest substring of s such that every
character in t, including duplicates, is present in the substring.
If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:
Input: s = "OUZODYXAZV", t = "XYZ"
Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes
"X", "Y", and "Z" from string t.

Example 2:
Input: s = "xyz", t = "xyz"
Output: "xyz"

Example 3:
Input: s = "x", t = "xy"
Output: ""

Constraints:
1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.
"""
from collections import Counter


def min_window_brute_force(text: str, target: str) -> str:
    """
    Time complexity: O(n^2) where n = len(s)
    Space complexity: O(m) where m = len(t)
    """
    if not target:
        return ''

    target_char_counts = Counter(target)

    min_substring_bounds, min_length = [-1, -1], float('infinity')

    for start, start_char in enumerate(text):
        text_char_counts = Counter()
        for end, end_char in enumerate(text[start:], start=start):
            text_char_counts[end_char] += 1

            is_valid = all(
                text_char_counts[char] >= count
                for char, count in target_char_counts.items()
            )
            length = end - start + 1
            if is_valid and length < min_length:
                min_length = length
                min_substring_bounds = [start, end]

    left, right = min_substring_bounds
    return text[left: right + 1] if min_length != float('infinity') else ''


def test_min_window():
    solutions = [
        min_window_brute_force,
    ]

    test_cases = [
        ('OUZODYXAZV', 'XYZ', 'YXAZ'),
        ('xyz', 'xyz', 'xyz'),
        ('x', 'xy', ''),
    ]

    for solution in solutions:
        for s, t, expected_result in test_cases:
            # Act
            result = solution(s, t)

            # Assert
            assert result == expected_result

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_min_window()
