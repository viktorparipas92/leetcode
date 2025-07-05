"""
48. Rotate Image
----------------
Difficulty: Medium

Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.
You must rotate the matrix in-place.
Do not allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [
  [1,2],
  [3,4]
]
Output: [
  [3,1],
  [4,2]
]

Example 2:
Input: matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
Output: [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""


def rotate_brute_force(matrix: list[list[int]]) -> None:
    """
    Time complexity: O(n^2)
    Space complexity: O(n^2)
    """
    size = len(matrix)
    rotated: list[list[int]] = [[0] * size for _ in range(size)]

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            rotated[j][size - 1 - i] = cell

    for i, row in enumerate(rotated):
        for j, rotated_cell in enumerate(row):
            matrix[i][j] = rotated_cell


def rotate_by_four_cells(matrix: list[list[int]]) -> None:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    left_idx = 0
    right_idx = len(matrix) - 1
    while left_idx < right_idx:
        for i in range(right_idx - left_idx):
            top_idx = left_idx
            bottom_idx = right_idx

            top_left = matrix[top_idx][left_idx + i]
            matrix[top_idx][left_idx + i] = matrix[bottom_idx - i][left_idx]
            matrix[bottom_idx - i][left_idx] = matrix[bottom_idx][right_idx - i]
            matrix[bottom_idx][right_idx - i] = matrix[top_idx + i][right_idx]
            matrix[top_idx + i][right_idx] = top_left

        right_idx -= 1
        left_idx += 1


def test_rotate():
    solutions = [
        rotate_brute_force,
        rotate_by_four_cells,
    ]

    original_matrix = [
        [1, 2],
        [3, 4],
    ]
    expected_matrix = [
        [3, 1],
        [4, 2],
    ]

    original_matrix_2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    expected_matrix_2 = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]
    test_cases = [
        (original_matrix, expected_matrix),
        (original_matrix_2, expected_matrix_2),
    ]

    for solution in solutions:
        for original_matrix, expected_rotated_matrix in test_cases:
            # Arrange
            copy_matrix = [row[:] for row in original_matrix]

            # Act
            solution(copy_matrix)

            # Assert
            assert copy_matrix == expected_rotated_matrix

        print(f'Tests passed  for {solution.__name__}!')


if __name__ == '__main__':
    test_rotate()
