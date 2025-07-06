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
    def depth_first_search(row, col, r, c, dr, dc):
        if row == 0 or col == 0:
            return

        for i in range(col):
            r += dr
            c += dc
            output.append(matrix[r][c])

        # sub-problem
        depth_first_search(col, row - 1, r, c, dc, -dr)

    height, width = len(matrix), len(matrix[0])
    output: list[int] = []

    # start by going to the right
    depth_first_search(height, width, r=0, c=-1, dr=0, dc=1)
    return output


def spiral_order_iteration(matrix: list[list[int]]) -> list[int]:
    """
    Time complexity: O(m * n)
    Space complexity: O(m * n) for the output list, O(1) extra space
    """
    output: list[int] = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        for i in range(left, right):
            output.append(matrix[top][i])

        top += 1
        for i in range(top, bottom):
            output.append(matrix[i][right - 1])

        right -= 1
        if not (left < right and top < bottom):
            break

        for i in range(right - 1, left - 1, -1):
            output.append(matrix[bottom - 1][i])

        bottom -= 1
        for i in range(bottom - 1, top - 1, -1):
            output.append(matrix[i][left])

        left += 1

    return output


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def spiral_order_iteration_optimal(matrix: list[list[int]]) -> list[int]:
    """
    Time complexity: O(m * n)
    Space complexity: O(m * n) for the output list, O(1) extra space
    """
    output = []
    height = len(matrix)
    width = len(matrix[0])
    steps_remaining: list[int]  = [width, height - 1]

    row_idx, col_idx, direction_idx = 0, -1, 0
    # While there are steps remaining in the current direction
    while steps_remaining[direction_idx & 1]:
        # Get the current direction
        for i in range(steps_remaining[direction_idx & 1]):
            row_idx += DIRECTIONS[direction_idx][0]
            col_idx += DIRECTIONS[direction_idx][1]
            output.append(matrix[row_idx][col_idx])

        steps_remaining[direction_idx & 1] -= 1
        direction_idx += 1
        direction_idx %= 4

    return output


def test_spiral_matrix():
    solutions = [
        spiral_order_recursion,
        spiral_order_iteration,
        spiral_order_iteration_optimal,
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

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_spiral_matrix()
