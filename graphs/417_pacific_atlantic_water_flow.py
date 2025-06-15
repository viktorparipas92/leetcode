"""
417. Pacific Atlantic Water Flow
--------------------------------
Difficulty: Medium

You are given a rectangular island heights
where heights[r][c] represents the height above sea level of the cell
at coordinate (r, c).

The island borders the Pacific Ocean from the top and left sides,
and borders the Atlantic Ocean from the bottom and right sides.

Water can flow in four directions (up, down, left, or right)
from a cell to a neighboring cell with height equal or lower.
Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell
to both the Pacific and Atlantic oceans.
Return it as a 2D list where each element is a list [r, c]
representing the row and column of the cell. You may return the answer in any order.

Example 1:
Input: heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]
Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

Example 2:
Input: heights = [[1],[1]]
Output: [[0,0],[0,1]]

Constraints:
1 <= heights.length, heights[r].length <= 100
0 <= heights[r][c] <= 1000
"""

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def pacific_atlantic_brute_force(heights: list) -> list:
    """
    Time complexity: O(m * n * 4^(m * n))
    Space complexity: O(m * n)
    """
    num_rows, num_columns = len(heights), len(heights[0])
    is_pacific = is_atlantic = False

    def depth_first_search(row_index: int, column_index: int, previous_value: int):
        nonlocal is_pacific, is_atlantic
        if row_index < 0 or column_index < 0:
            is_pacific = True
            return
        elif row_index >= num_rows or column_index >= num_columns:
            is_atlantic = True
            return
        elif heights[row_index][column_index] > previous_value:
            return

        tmp = heights[row_index][column_index]
        heights[row_index][column_index] = float('inf')
        for dx, dy in DIRECTIONS:
            depth_first_search(row_index + dx, column_index + dy, tmp)
            if is_pacific and is_atlantic:
                break

        heights[row_index][column_index] = tmp

    result = []
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            is_pacific = is_atlantic = False
            depth_first_search(row_index, column_index, float('inf'))
            if is_pacific and is_atlantic:
                result.append((row_index, column_index))

    return result


def pacific_atlantic_dfs(heights: list) -> list:
    num_rows, nuw_columns = len(heights), len(heights[0])
    pacific: set = set()
    atlantic: set = set()

    def depth_first_search(
        row_index: int, column_index: int, visited: set[tuple], previous_height: int
    ):
        if (
            (row_index, column_index) in visited
            or row_index < 0
            or column_index < 0
            or row_index == num_rows
            or column_index == nuw_columns
            or heights[row_index][column_index] < previous_height
        ):
            return

        visited.add((row_index, column_index))

        depth_first_search(row_index + 1, column_index, visited, heights[row_index][column_index])
        depth_first_search(row_index - 1, column_index, visited, heights[row_index][column_index])
        depth_first_search(row_index, column_index + 1, visited, heights[row_index][column_index])
        depth_first_search(row_index, column_index - 1, visited, heights[row_index][column_index])

    for c in range(nuw_columns):
        depth_first_search(0, c, pacific, heights[0][c])
        depth_first_search(num_rows - 1, c, atlantic, heights[num_rows - 1][c])

    for r in range(num_rows):
        depth_first_search(r, 0, pacific, heights[r][0])
        depth_first_search(r, nuw_columns - 1, atlantic, heights[r][nuw_columns - 1])

    result = []
    for r in range(num_rows):
        for c in range(nuw_columns):
            if (r, c) in pacific and (r, c) in atlantic:
                result.append((r, c))

    return result


def test_pacific_atlantic():
    solutions = [
        pacific_atlantic_brute_force,
        pacific_atlantic_dfs,
    ]

    heights_1 = [
        [4, 2, 7, 3, 4],
        [7, 4, 6, 4, 7],
        [6, 3, 5, 3, 6],
    ]
    output_1 = [
        (0, 2), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0),
    ]
    test_cases = [
        (heights_1, output_1),
        ([[1], [1]], [(0, 0), (1, 0)]),
    ]

    for solution in solutions:
        for heights, expected_output in test_cases:
            # Act
            output = solution(heights)

            # Assert
            assert output == expected_output

        print(f'Tests passed for {solution.__name__}')


if __name__ == '__main__':
    test_pacific_atlantic()
