"""
200. Number of Islands
--------------------------------
Difficulty: Medium

Given a 2D grid grid where '1' represents land and '0' represents water,
count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically
and is surrounded by water.
You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1:
Input: grid = [
    ['0','1','1','1','0'],
    ['0','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
  ]
Output: 1

Example 2:
Input: grid = [
    ['1','1','0','0','1'],
    ['1','1','0','0','1'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
  ]
Output: 4
Constraints:

1 <= grid.length, grid[i].length <= 100
grid[i][j] is '0' or '1'.
"""


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
WATER = '0'
LAND = '1'


def num_islands_dfs(grid: list[list[str]]) -> int:
    """
    Time complexity: O(m * n)
    Space complexity: O(m * n)
    where m is the number of rows and n is the number of columns in the grid.
    """
    def depth_first_search(row_idx: int, column_idx: int):
        if row_idx < 0 or column_idx < 0:
            return

        try:
            is_water = grid[row_idx][column_idx] == WATER
        except IndexError:
            return

        if is_water:
            return

        grid[row_idx][column_idx] = WATER
        for x, y in DIRECTIONS:
            depth_first_search(row_idx + x, column_idx + y)

    num_islands = 0
    for row_idx, row in enumerate(grid):
        for column_idx, cell in enumerate(row):
            if cell == LAND:
                depth_first_search(row_idx, column_idx)
                num_islands += 1

    return num_islands


def test_num_islands():
    solutions = [
        num_islands_dfs,
    ]

    grid_1 = [
        ['0', '1', '1', '1', '0'],
        ['0', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ]
    grid_2 = [
        ['1', '1', '0', '0', '1'],
        ['1', '1', '0', '0', '1'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]
    test_cases = [
        (grid_1, 1),
        (grid_2, 4),
    ]

    for solution in solutions:
        for grid, expected_num_islands in test_cases:
            # Act
            num_islands = solution(grid)

            # Assert
            assert num_islands == expected_num_islands

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_num_islands()
