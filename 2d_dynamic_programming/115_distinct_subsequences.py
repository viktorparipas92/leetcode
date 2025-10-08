"""
115. Distinct Subsequences
--------------------------
Difficulty: Hard

You are given two strings s and t, both consisting of English letters.
Return the number of distinct subsequences of s which are equal to t.

Example 1:
Input: s = "caaat", t = "cat"
Output: 3
Explanation: There are 3 ways you can generate "cat" from s.
(c)aa(at)
(c)a(a)a(t)
(ca)aa(t)

Example 2:
Input: s = "xxyxy", t = "xy"
Output: 5
Explanation: There are 5 ways you can generate "xy" from s.
(x)x(y)xy
(x)xyx(y)
x(x)(y)xy
x(x)yx(y)
xxy(x)(y)

Constraints:
1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""


def num_distinct_recursion(longer: str, shorter: str) -> int:
    """
    Time complexity: O(2^m)
    Space complexity: O(m)
    where m is the length of the string s.
    """
    def depth_first_search(i: int, j: int) -> int:
        if j == len(shorter):
            return 1

        if i == len(longer):
            return 0

        num_distinct_subsequences: int = depth_first_search(i + 1, j)
        if longer[i] == shorter[j]:
            num_distinct_subsequences += depth_first_search(i + 1, j + 1)

        return num_distinct_subsequences

    if len(shorter) > len(longer):
        return 0

    return depth_first_search(i=0, j=0)


def num_distinct_dynamic_top_down(longer: str, shorter: str) -> int:
    """
    Time complexity: O(m * n)
    Space complexity: O(m * n)
    where m is the length of the string s and n is the length of the string t.
    """
    def depth_first_search(i: int, j: int) -> int:
        if j == len(shorter):
            return 1

        if i == len(longer):
            return 0

        if (i, j) in memory:
            return memory[(i, j)]

        num_distinct_subsequences = depth_first_search(i + 1, j)
        if longer[i] == shorter[j]:
            num_distinct_subsequences += depth_first_search(i + 1, j + 1)

        memory[(i, j)] = num_distinct_subsequences
        return num_distinct_subsequences

    if len(shorter) > len(longer):
        return 0

    memory: dict[tuple[int, int], int] = {}  # (i, j) -> num_distinct_subsequences
    return depth_first_search(i=0, j=0)


def num_distinct_dynamic_bottom_up(longer: str, shorter: str) -> int:
    """
    Time complexity: O(m * n)
    Space complexity: O(m * n)
    where m is the length of the string s and n is the length of the string t.
    """
    size_longer: int = len(longer)
    size_shorter: int = len(shorter)
    num_subsequences_grid: list[list[int]] = [[0] * (size_shorter + 1) for _ in range(size_longer + 1)]

    for i in range(size_longer + 1):
        num_subsequences_grid[i][size_shorter] = 1

    for i in range(size_longer - 1, -1, -1):
        for j in range(size_shorter - 1, -1, -1):
            num_subsequences_grid[i][j] = num_subsequences_grid[i + 1][j]
            if longer[i] == shorter[j]:
                num_subsequences_grid[i][j] += num_subsequences_grid[i + 1][j + 1]

    return num_subsequences_grid[0][0]


def num_distinct_dynamic_bottom_up_optimized_space(longer: str, shorter: str) -> int:
    """
    Time complexity: O(m * n)
    Space complexity: O(n)
    where m is the length of the string s and n is the length of the string t.
    """
    size_longer: int = len(longer)
    size_shorter: int = len(shorter)
    # num_subsequences_list[j] -> ~ for longer[i:] and shorter[j:]
    num_subsequences_list: list[int] = [0] * (size_shorter + 1)
    next_num_subsequences_list: list[int] = [0] * (size_shorter + 1)

    num_subsequences_list[size_shorter] = next_num_subsequences_list[size_shorter] = 1
    for i in range(size_longer - 1, -1, -1):
        for j in range(size_shorter - 1, -1, -1):
            next_num_subsequences_list[j] = num_subsequences_list[j]
            if longer[i] == shorter[j]:
                next_num_subsequences_list[j] += num_subsequences_list[j + 1]

        num_subsequences_list = next_num_subsequences_list[:]

    return num_subsequences_list[0]


def num_distinct_dynamic_bottom_up_optimal(longer: str, shorter: str) -> int:
    """
    Time complexity: O(m * n)
    Space complexity: O(n)
    where m is the length of the string s and n is the length of the string t.
    """
    size_longer: int = len(longer)
    size_shorter: int = len(shorter)
    # num_subsequences_list[j] -> ~ for longer[i:] and shorter[j:]
    num_subsequences_list: list[int] = [0] * (size_shorter + 1)
    num_subsequences_list[size_shorter] = 1
    for i in range(size_longer - 1, -1, -1):
        previous_num_subsequences: int = 1
        for j in range(size_shorter - 1, -1, -1):
            total_num_subsequences: int = num_subsequences_list[j]
            if longer[i] == shorter[j]:
                total_num_subsequences += previous_num_subsequences

            previous_num_subsequences = num_subsequences_list[j]
            num_subsequences_list[j] = total_num_subsequences

    return num_subsequences_list[0]


def test_num_distinct():
    solutions = [
        num_distinct_recursion,
        num_distinct_dynamic_top_down,
        num_distinct_dynamic_bottom_up,
        num_distinct_dynamic_bottom_up_optimized_space,
        num_distinct_dynamic_bottom_up_optimal,
    ]

    test_cases = [
        ('caaat', 'cat', 3),
        ('xxyxy', 'xy', 5),
    ]

    for solution in solutions:
        for longer_string, shorter_string, expected_num_distinct_subsequences in test_cases:
            # Act
            num_distinct_subsequences = solution(longer_string, shorter_string)

            # Assert
            assert num_distinct_subsequences == expected_num_distinct_subsequences

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_num_distinct()
