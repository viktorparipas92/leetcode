"""
10. Regular Expression Matching
------------------------------
Difficulty: Hard

You are given an input string s consisting of lowercase english letters,
 and a pattern p consisting of lowercase english letters,
 as well as '.', and '*' characters.

Return true if the pattern matches the entire input string, otherwise return false.
- '.' Matches any single character
- '*' Matches zero or more of the preceding element.

Example 1:
Input: s = "aa", p = ".b"
Output: false
Explanation: Regardless of which character we choose for the '.' in the pattern, we cannot match the second character in the input string.

Example 2:
Input: s = "nnn", p = "n*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'n'. We choose 'n' to repeat three times.

Example 3:
Input: s = "xyz", p = ".*z"
Output: true
Explanation: The pattern ".*" means zero or more of any character, so we choose ".." to match "xy" and "z" to match "z".

Constraints:
1 <= s.length <= 20
1 <= p.length <= 20
Each appearance of '*', will be preceded by a valid character or '.'
"""


def is_match_recursion(string: str, pattern: str) -> bool:
    """
    Time complexity: O(2^(m+n))
    Space complexity: O(m+n)
    where m is the length of the string and n is the length of the pattern.
    """
    def depth_first_search(i: int, j: int) -> bool:
        if j == pattern_size:
            return i == string_size

        match = (
            i < string_size
            and (string[i] == pattern[j] or pattern[j] == '.')
        )
        if (j + 1) < pattern_size and pattern[j + 1] == '*':
            return (
                depth_first_search(i, j + 2)  # don't use *
                or (match and depth_first_search(i + 1, j))  # use *
            )
        elif match:
            return depth_first_search(i + 1, j + 1)

        return False

    string_size = len(string)
    pattern_size = len(pattern)
    return depth_first_search(i=0, j=0)


def is_match_dynamic_top_down(string: str, pattern: str) -> bool:
    """
    Time complexity: O(m * n)
    Space complexity: O(m * n)
    """
    def depth_first_search(i: int, j: int) -> bool:
        if j == pattern_size:
            return i == string_size

        if (i, j) in cache:
            return cache[(i, j)]

        match = (
            i < string_size
            and (string[i] == pattern[j] or pattern[j] == '.')
        )
        if (j + 1) < pattern_size and pattern[j + 1] == '*':
            cache[(i, j)] = (
                depth_first_search(i, j + 2)
                or (match and depth_first_search(i + 1, j))
            )
            return cache[(i, j)]

        if match:
            cache[(i, j)] = depth_first_search(i + 1, j + 1)
            return cache[(i, j)]

        cache[(i, j)] = False
        return False

    string_size = len(string)
    pattern_size = len(pattern)
    cache: dict = {}
    return depth_first_search(i=0, j=0)


def is_match_dynamic_bottom_up_optimal(string: str, pattern: str) -> bool:
    """
    Time complexity: O(m * n)
    Space complexity: O(n)
    """
    pattern_size = len(pattern)
    is_match_map: list[bool] = [False] * (pattern_size + 1)
    is_match_map[pattern_size] = True

    string_size = len(string)
    for i in range(string_size, -1, -1):
        is_match: bool = is_match_map[pattern_size]
        is_match_map[pattern_size] = (i == string_size)

        for j in range(pattern_size - 1, -1, -1):
            match = (
                i < string_size
                and (string[i] == pattern[j] or pattern[j] == '.')
            )
            result: bool = False
            if (j + 1) < pattern_size and pattern[j + 1] == '*':
                result = is_match_map[j + 2]
                if match:
                    result |= is_match_map[j]
            elif match:
                result = is_match
            is_match_map[j], is_match = result, is_match_map[j]

    return is_match_map[0]


def test_is_match():
    solutions = [
        is_match_recursion,
        is_match_dynamic_top_down,
        is_match_dynamic_bottom_up_optimal,
    ]

    test_cases = [
        ('aa', '.b', False),
        ('nnn', 'n*', True),
        ('xyz', '.*z', True),
    ]

    for solution in solutions:
        for string, pattern, expected_is_match in test_cases:
            # Act
            is_match = solution(string, pattern)

            # Assert
            assert is_match == expected_is_match

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_is_match()
