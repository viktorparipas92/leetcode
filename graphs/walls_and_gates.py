"""
Walls and Gates
---------------
Difficulty: Medium

You are given a m×n 2D grid initialized with these three possible values:
- -1 - A water cell that can not be traversed.
- 0 - A treasure chest.
- INF - A land cell that can be traversed.
  We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest.
If a land cell cannot reach a treasure chest than the value should remain INF.
Assume the grid can only be traversed up, down, left, or right.
Modify the grid in-place.

Example 1:
Input: [
  [2147483647, -1, 0, 2147483647],
  [2147483647, 2147483647, 2147483647, -1],
  [2147483647, -1, 2147483647, -1],
  [0, -1, 2147483647, 2147483647]
]

Output: [
  [3, -1, 0, 1],
  [2, 2, 1, -1],
  [1, -1, 2, -1],
  [0, -1, 3, 4]
]
Example 2:

Input: [
  [0, -1],
  [2147483647, 2147483647]
]
Output: [
  [0, -1],
  [1, 2]
]

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}
"""
from collections import deque


Coordinate = tuple[int, int]


def islands_and_treasure_multi_source_bfs(grid: list[list[int]]) -> None:
    """
    Time complexity: O(m * n)
    Space complexity: O(m * n)
    where m is the number of rows and n is the number of columns in the grid.
    """
    def add_cell(row_index: int, column_index: int) -> None:
        coordinates: Coordinate = (row_index, column_index)
        if min(*coordinates) < 0 or coordinates in visited_nodes:
            return

        try:
            cell = grid[row_index][column_index]
        except IndexError:
            return

        if cell == -1:
            return

        visited_nodes.add(coordinates)
        queue.append(coordinates)

    visited_nodes: set[Coordinate] = set()
    queue: deque[Coordinate] = deque()

    for row_idx, row in enumerate(grid):
        for column_idx, cell in enumerate(row):
            coordinates = row_idx, column_idx
            if cell == 0:
                queue.append(coordinates)
                visited_nodes.add(coordinates)

    distance: int = 0
    while queue:
        for _ in range(len(queue)):
            row_idx, column_idx = queue.popleft()
            grid[row_idx][column_idx] = distance

            add_cell(row_idx + 1, column_idx)
            add_cell(row_idx - 1, column_idx)
            add_cell(row_idx, column_idx + 1)
            add_cell(row_idx, column_idx - 1)

        distance += 1


INF = 2147483647

def test_islands_and_treasure():
    solutions = [
        islands_and_treasure_multi_source_bfs,
    ]

    grid_1 = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]
    output_1 = [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]

    grid_2 = [
        [0, -1],
        [INF, INF]
    ]
    output_2 = [
        [0, -1],
        [1, 2],
    ]

    test_cases = [
        (grid_1, output_1),
        (grid_2, output_2),
    ]

    for solution in solutions:
        for grid, expected_output in test_cases:
            # Act
            solution(grid)

            # Assert
            assert grid == expected_output

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_islands_and_treasure()
