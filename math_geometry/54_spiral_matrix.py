"""
54. Spiral Matrix
-----------------
Difficulty: Medium

Given an m x n matrix of integers matrix,
return a list of all elements within the matrix in spiral order.

Example 1:
Input: matrix = [[1,2],[3,4]]
Output: [1,2,4,3]

Example 2:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 3:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
1 <= matrix.length, matrix[i].length <= 10
-100 <= matrix[i][j] <= 100
"""


def spiral_order_recursion(matrix: list[list[int]]) -> list[int]:
    """
    Time complexity: O(m * n)
    Space complexity: O(min(m, n)) for recursion stack, O(m * n) for the output list
    """
    # append all the elements in the given direction
    def dfs(row, col, r, c, dr, dc):
        if row == 0 or col == 0:
            return

        for i in range(col):
            r += dr
            c += dc
            res.append(matrix[r][c])

        # sub-problem
        dfs(col, row - 1, r, c, dc, -dr)

    height, width = len(matrix), len(matrix[0])
    res = []

    # start by going to the right
    dfs(height, width, 0, -1, 0, 1)
    return res


def test_spiral_matrix():
    solutions = [
        spiral_order_recursion,
    ]

    test_cases = [
        ([[1, 2,], [3, 4]], [1, 2, 4, 3]),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        )
    ]

    for solution in solutions:
        for input, expected_output in test_cases:
            # Act
            output = solution(input)

            # Assert
            assert output == expected_output

        print(f'Tests passed!')


if __name__ == '__main__':
    test_spiral_matrix()
