"""
62. Unique Paths
----------------
Difficulty: Medium

There is an m x n grid where you are allowed to move
either down or to the right at any point in time.

Given the two integers m and n, return the number of possible unique paths
that can be taken from the top-left corner of the grid (grid[0][0])
to the bottom-right corner (grid[m - 1][n - 1]).

You may assume the output will fit in a 32-bit integer.

Example 1:
Input: m = 3, n = 6
Output: 21

Example 2:
Input: m = 3, n = 3
Output: 6

Constraints:
1 <= m, n <= 100
"""


def unique_paths_recursion(m: int, n: int) -> int:
    """
    Time complexity: O(2^(m + n))
    Space complexity: O(m + n)
    """

    def depth_first_search(i: int, j: int):
        if i == (m - 1) and j == (n - 1):
            return 1
        elif i >= m or j >= n:
            return 0

        return depth_first_search(i, j + 1) + depth_first_search(i + 1, j)

    return depth_first_search(i=0, j=0)


def unique_paths_dynamic_top_down(m: int, n: int) -> int:
    """
    Time complexity: O(m * n)
    Space complexity: O(m * n)
    """
    def depth_first_search(i: int, j: int) -> int:
        if i == (m - 1) and j == (n - 1):
            return 1
        elif i >= m or j >= n:
            return 0

        if num_unique_paths_map[i][j] != -1:
            return num_unique_paths_map[i][j]

        num_unique_paths_map[i][j] = (
            depth_first_search(i, j + 1)
            + depth_first_search(i + 1, j)
        )
        return num_unique_paths_map[i][j]

    num_unique_paths_map: list[list[int]] = [[-1] * n for _ in range(m)]
    return depth_first_search(i=0, j=0)


def test_unique_paths():
    solutions = [
        unique_paths_recursion,
        unique_paths_dynamic_top_down,
    ]

    test_cases = [
        ((3, 6), 21),
        ((3, 3), 6),
    ]

    for solution in solutions:
        for (m, n), expected_num_unique_paths in test_cases:
            # Act
            num_unique_paths = solution(m, n)

            # Assert
            assert num_unique_paths == expected_num_unique_paths

        print(f'Tests passed for{solution.__name__}!')


if __name__ == '__main__':
    test_unique_paths()
