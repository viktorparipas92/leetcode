"""
778. Swim in Rising Water
-----------------------------
Difficulty: Hard

You are given a square 2-D matrix of distinct integers grid where each integer
grid[i][j] represents the elevation at position (i, j).

Rain starts to fall at time = 0, which causes the water level to rise.
At time t, the water level across the entire grid is t.

You may swim either horizontally or vertically in the grid between two adjacent
squares if the original elevation of both squares is
less than or equal to the water level at time t.

Starting from the top left square (0, 0),
return the minimum amount of time it will take until
it is possible to reach the bottom right square (n - 1, n - 1).

Example 1:
Input: grid = [[0,1],[2,3]]
Output: 3
Explanation: For a path to exist to the bottom right square grid[1][1] the water elevation must be at least 3. At time t = 3, the water level is 3.

Example 2:
Input: grid = [
  [0,1,2,10],
  [9,14,4,13],
  [12,3,8,15],
  [11,5,7,6]
]
Output: 8
Explanation: The water level must be at least 8 to reach the bottom right square. The path is [0, 1, 2, 4, 8, 7, 6].

Constraints:
grid.length == grid[i].length
1 <= grid.length <= 50
0 <= grid[i][j] < n^2
"""
import heapq

INFINITY = float('inf')
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def swim_in_water_brute_force(grid: list[list[int]]) -> int:
    """
    Time complexity: O(4^(n^2))
    Space complexity: O(n^2)
    where n is the number of rows or columns in the grid.
    """
    def depth_first_search(node: tuple[int, int], time: int) -> int | float:
        i, j = node
        if min(i, j) < 0 or max(i, j) >= size or visited_nodes[i][j]:
            return INFINITY

        if i == j == size - 1:
            return max(time, grid[i][j])

        visited_nodes[i][j] = True
        time = max(time, grid[i][j])
        min_time: int = min(
            depth_first_search((i + 1, j), time),
            depth_first_search((i - 1, j), time),
            depth_first_search((i, j + 1), time),
            depth_first_search((i, j - 1), time),
        )
        visited_nodes[i][j] = False
        return min_time

    size: int = len(grid)
    visited_nodes: list[list[bool]] = [[False] * size for _ in range(size)]
    return depth_first_search(node=(0, 0), time=0)


def swim_in_water_dfs(grid: list[list[int]]) -> int:
    """
    Time complexity: O(n^4)
    Space complexity: O(n^2)
    """
    def depth_first_search(node: tuple[int, int], time: int) -> int:
        i, j = node
        if (
            min(i, j) < 0
            or max(i, j) >= size
            or visited_nodes[i][j]
            or grid[i][j] > time
        ):
            return False

        if i == j == (size - 1):
            return True

        visited_nodes[i][j] = True
        return (
            depth_first_search((i + 1, j), time)
            or depth_first_search((i - 1, j), time)
            or depth_first_search((i, j + 1), time)
            or depth_first_search((i, j - 1), time)
        )

    size: int = len(grid)
    visited_nodes: list[list[bool]] = [[False] * size for _ in range(size)]
    min_height = max_height = grid[0][0]
    for row_idx in range(size):
        max_height = max(max_height, max(grid[row_idx]))
        min_height = min(min_height, min(grid[row_idx]))

    for _time in range(min_height, max_height):
        if depth_first_search(node=(0, 0), time=_time):
            return _time

        for row_idx in range(size):
            for col_idx in range(size):
                visited_nodes[row_idx][col_idx] = False

    return max_height


def swim_in_water_binary_and_dfs(grid: list[list[int]]) -> int:
    """
    Time complexity: O(n^2 * log(n))
    Space complexity: O(n^2)
    """
    def depth_first_search(node: tuple[int, int], time: int) -> bool:
        i, j = node
        if (
            min(i, j) <
            0 or max(i, j) >= size
            or visited_nodes[i][j]
            or grid[i][j] > time
        ):
            return False

        if i == (size - 1) and j == (size - 1):
            return True

        visited_nodes[i][j] = True
        return (
            depth_first_search((i + 1, j), time)
            or depth_first_search((i - 1, j), time)
            or depth_first_search((i, j + 1), time)
            or depth_first_search((i, j - 1), time)
        )

    size: int = len(grid)
    visited_nodes: list[list[bool]] = [[False] * size for _ in range(size)]
    min_height = max_height = grid[0][0]
    for row in grid:
        max_height = max(max_height, max(row))
        min_height = min(min_height, min(row))

    left_idx, right_idx = min_height, max_height
    while left_idx < right_idx:
        mid_idx = (left_idx + right_idx) >> 1  # mid_idx = (left_idx + right_idx) // 2
        if depth_first_search((0, 0), mid_idx):
            right_idx = mid_idx
        else:
            left_idx = mid_idx + 1

        for row_idx in range(size):
            for col in range(size):
                visited_nodes[row_idx][col] = False

    return right_idx


def swim_in_water_dijkstra(grid: list[list[int]]) -> int | None:
    """
    Time complexity: O(n^2 * log(n))
    Space complexity: O(n^2)
    """
    visited_nodes: set[tuple[int, int]] = set()
    visited_nodes.add((0, 0))

    size: int = len(grid)

    min_height: list[list[int]] = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)
    while min_height:
        time, row_idx, column_idx = heapq.heappop(min_height)
        if row_idx == size - 1 and column_idx == size - 1:
            return time

        for dr, dc in DIRECTIONS:
            i, j = row_idx + dr, column_idx + dc
            if (
                i < 0 or j < 0
                or i == size or j == size
                or (i, j) in visited_nodes
            ):
                continue

            visited_nodes.add((i, j))
            heapq.heappush(min_height, [max(time, grid[i][j]), i, j])

    return None


def test_swim_in_water():
    solutions = [
        swim_in_water_brute_force,
        swim_in_water_dfs,
        swim_in_water_binary_and_dfs,
        swim_in_water_dijkstra,
    ]

    test_cases = [
        ([[0, 1], [2, 3]], 3),
        (
            [
                [0, 1, 2, 10],
                [9, 14, 4, 13],
                [12, 3, 8, 15],
                [11, 5, 7, 6],
            ],
            8,
        ),
    ]

    for solution in solutions:
        for grid, expected_min_time in test_cases:
            # Act
            min_time = solution(grid)

            # Assert
            assert min_time == expected_min_time

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_swim_in_water()
