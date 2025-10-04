"""
329. Longest Increasing Path in a Matrix
-------------------------------
Difficulty: Hard

You are given a 2-D grid of integers matrix,
where each integer is greater than or equal to 0.
Return the length of the longest strictly increasing path within matrix.

From each cell within the path, you can move either horizontally or vertically.
You may not move diagonally.

Example 1:
Input: matrix = [[5,5,3],[2,3,6],[1,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 3, 6] or [1, 2, 3, 5].

Example 2:
Input: matrix = [[1,2,3],[2,1,4],[7,6,5]]
Output: 7
Explanation: The longest increasing path is [1, 2, 3, 4, 5, 6, 7].

Constraints:
1 <= matrix.length, matrix[i].length <= 100
"""

LEFT = (-1, 0)
DIRECTIONS = [LEFT, (1, 0), (0, -1), (0, 1)]

NEGATIVE_INFINITY = float('-inf')


def longest_increasing_path_recursion(matrix: list[list[int]]) -> int:
    """
    Time complexity: O(4^(m * n))
    Space complexity: O(m * n)
    where m is the number of rows and n is the number of columns in the matrix.
    """
    def depth_first_search(row_idx: int, col_idx: int, previous_value: int | float) -> int:
        if (
            min(row_idx, col_idx) < 0
            or row_idx >= num_rows
            or col_idx >= num_columns
            or matrix[row_idx][col_idx] <= previous_value
        ):
            return 0

        _max_increasing_path_length: int = 1
        for direction in DIRECTIONS:
            _max_increasing_path_length = max(
                _max_increasing_path_length,
                1 + depth_first_search(
                    row_idx + direction[0],
                    col_idx + direction[1],
                    matrix[row_idx][col_idx],
                )
            )

        return _max_increasing_path_length

    num_rows, num_columns = len(matrix), len(matrix[0])
    max_increasing_path_length: int = 0
    for row_index in range(num_columns):
        for column_index in range(num_columns):
            max_increasing_path_length = max(
                max_increasing_path_length,
                depth_first_search(row_index, column_index, NEGATIVE_INFINITY),
            )

    return max_increasing_path_length


def test_longest_increasing_path_recursion():
    solutions = [
        longest_increasing_path_recursion,
    ]

    test_cases = [
        ([[5, 5, 3], [2, 3, 6], [1, 1, 1]], 4),
        ([[1, 2, 3], [2, 1, 4], [7, 6, 5]], 7),
    ]

    for solution in solutions:
        for matrix, expected_max_increasing_path_length in test_cases:
            # Act
            max_increasing_path_length = solution(matrix)

            # Assert
            assert max_increasing_path_length == expected_max_increasing_path_length

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_longest_increasing_path_recursion()
