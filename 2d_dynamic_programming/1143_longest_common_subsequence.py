"""
1143. Longest Common Subsequence
--------------------------------
Difficulty: Medium

Given two strings text1 and text2, return the length of the longest common subsequence
between the two strings if one exists, otherwise return 0.

A subsequence is a sequence that can be derived from the given sequence
by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".
A common subsequence of two strings is a subsequence that exists in both strings.

Example 1:
Input: text1 = "cat", text2 = "crabt"
Output: 3
Explanation: The longest common subsequence is "cat" which has a length of 3.

Example 2:
Input: text1 = "abcd", text2 = "abcd"
Output: 4

Example 3:
Input: text1 = "abcd", text2 = "efgh"
Output: 0

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""


def longest_common_subsequence_recursion(text1: str, text2: str) -> int:
    """
    Time complexity: O(2^(m+n))
    Space complexity: O(m+n)
    where m and n are the lengths of text1 and text2 respectively.
    """

    def depth_first_search(i: int, j: int) -> int:
        if i == len(text1) or j == len(text2):
            return 0
        elif text1[i] == text2[j]:
            return 1 + depth_first_search(i + 1, j + 1)

        return max(depth_first_search(i + 1, j), depth_first_search(i, j + 1))

    return depth_first_search(i=0, j=0)


def longest_common_subsequence_dynamic_top_down(text1: str, text2: str) -> int:
    """
    Time complexity: O(m * n)
    Space complexity: O(m * n)
    where m and n are the lengths of text1 and text2 respectively.
    """
    memory: dict[tuple[int, int], int] = {}

    def depth_first_search(i: int, j: int):
        if i == len(text1) or j == len(text2):
            return 0

        if (i, j) in memory:
            return memory[(i, j)]

        if text1[i] == text2[j]:
            memory[(i, j)] = 1 + depth_first_search(i + 1, j + 1)
        else:
            memory[(i, j)] = max(
                depth_first_search(i + 1, j),
                depth_first_search(i, j + 1),
            )

        return memory[(i, j)]

    return depth_first_search(i=0, j=0)


def longest_common_subsequence_dynamic_bottom_up(text1: str, text2: str) -> int:
    """
    Time complexity: O(m * n)
    Space complexity: O(m * n)
    where m and n are the lengths of text1 and text2 respectively.
    """
    lcs_table: list[list] = [
        [0 for j in range(len(text2) + 1)]
        for i in range(len(text1) + 1)
    ]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                lcs_table[i][j] = 1 + lcs_table[i + 1][j + 1]
            else:
                lcs_table[i][j] = max(lcs_table[i][j + 1], lcs_table[i + 1][j])

    return lcs_table[0][0]


def longest_common_subsequence_dynamic_bottom_up_optimized(
    text1: str, text2: str
) -> int:
    """
    Time complexity: O(m * n)
    Space complexity: O(min(m, n))
    where m and n are the lengths of text1 and text2 respectively.
    """
    if len(text1) < len(text2):
        text1, text2 = text2, text1  # Ensure text1 is the longer string

    previous = [0] * (len(text2) + 1)
    current = [0] * (len(text2) + 1)

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                current[j] = 1 + previous[j + 1]
            else:
                current[j] = max(current[j + 1], previous[j])

        previous, current = current, previous

    return previous[0]


def longest_common_subsequence_dynamic_bottom_up_optimal(
    text1: str, text2: str
) -> int:
    """
    Time complexity: O(m * n)
    Space complexity: O(min(m, n))
    where m and n are the lengths of text1 and text2 respectively.
    """
    if len(text1) < len(text2):
        text1, text2 = text2, text1  # Ensure text1 is the longer string

    lcs_list: list[int] = [0] * (len(text2) + 1)
    for i in range(len(text1) - 1, -1, -1):
        previous: int = 0
        for j in range(len(text2) - 1, -1, -1):
            temp: int = lcs_list[j]
            if text1[i] == text2[j]:
                lcs_list[j] = 1 + previous
            else:
                lcs_list[j] = max(lcs_list[j], lcs_list[j + 1])

            previous = temp

    return lcs_list[0]



def test_longest_common_subsequence():
    solutions = [
        longest_common_subsequence_recursion,
        longest_common_subsequence_dynamic_top_down,
        longest_common_subsequence_dynamic_bottom_up,
        longest_common_subsequence_dynamic_bottom_up_optimized,
        longest_common_subsequence_dynamic_bottom_up_optimal,
    ]

    test_cases = [
        ('cat', 'crabt', 3),
        ('abcd', 'abcd', 4),
        ('abcd', 'efgh', 0),
    ]

    for solution in solutions:
        for text1, text2, expected_lcs_length in test_cases:
            # Act
            lcs_length = solution(text1, text2)

            # Assert
            assert lcs_length == expected_lcs_length

        print(f'All test cases passed for {solution.__name__}.')


if __name__ == '__main__':
    test_longest_common_subsequence()
