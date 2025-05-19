"""
73. Set Matrix Zeroes
---------------------
Difficulty: Medium

Given an m x n matrix of integers matrix, if an element is 0,
set its entire row and column to 0's.
You must update the matrix in-place.
Follow up: Could you solve it using O(1) space?

Example 1:
Input: matrix = [
  [0,1],
  [1,0]
]
Output: [
  [0,0],
  [0,0]
]

Example 2:
Input: matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]
Output: [
  [1,0,3],
  [0,0,0],
  [6,0,8]
]
Constraints:
1 <= matrix.length, matrix[0].length <= 100
-2^31 <= matrix[i][j] <= (2^31) - 1
"""


def set_zeroes_iteration(matrix: list[list[int]]) -> None:
    """
    Time complexity: O(m * n)
    Space complexity: O(n)
    where m is the number of rows and n is the number of columns in the matrix.
    """
    height, width = len(matrix), len(matrix[0])
    rows, columns = [False] * height, [False] * width

    for r, row in enumerate(matrix):
        for c, cell in enumerate(row):
            if cell == 0:
                rows[r] = True
                columns[c] = True

    for r, row in enumerate(rows):
        for c, column in enumerate(columns):
            if row or column:
                matrix[r][c] = 0


def test_set_zeroes():
    solutions = [
        set_zeroes_iteration,
    ]

    matrix_1 = [
        [0, 1],
        [1, 0],
    ]
    output_1 = [
        [0, 0],
        [0, 0],
    ]

    matrix_2 = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8],
    ]
    output_2 = [
        [1, 0, 3],
        [0, 0, 0],
        [6, 0, 8],
    ]

    test_cases = [
        (matrix_1, output_1),
    ]

    for solution in solutions:
        for matrix, expected_output in test_cases:
            # Act
            solution(matrix)

            # Assert
            assert matrix == expected_output

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_set_zeroes()
