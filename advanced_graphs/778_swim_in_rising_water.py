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


INFINITY = float('inf')


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
    visited_nodes: list[list[int]] = [[False] * size for _ in range(size)]
    return depth_first_search(node=(0, 0), time=0)


def test_swim_in_water():
    solutions = [
        swim_in_water_brute_force,
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

        print(f'Tests passed  for {solution.__name__}!')


if __name__ == '__main__':
    test_swim_in_water()
