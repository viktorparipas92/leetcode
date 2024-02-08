"""
74. Search a 2D Matrix
--------------------------------
Difficulty: Medium

You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the
  previous row.

Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
"""


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    left = 0

    num_rows = len(matrix)
    num_columns = len(matrix[0])
    right = num_rows * num_columns - 1

    while left <= right:
        middle_index = left + (right - left) // 2
        middle_row = middle_index // num_columns
        middle_column = middle_index % num_columns
        middle_element = matrix[middle_row][middle_column]
        if middle_element == target:
            return True
        if middle_element < target:
            left = middle_index + 1
        else:
            right = middle_index - 1

    return False


def test_search_matrix():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ]
    assert search_matrix(matrix, 3) is True
    assert search_matrix(matrix, 13) is False


if __name__ == '__main__':
    test_search_matrix()
