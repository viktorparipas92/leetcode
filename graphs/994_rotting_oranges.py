"""
994. Rotting Oranges
--------------------
Difficulty: Medium

You are given a 2-D matrix grid. Each cell can have one of three possible values:
- 0 representing an empty cell
- 1 representing a fresh fruit
- 2 representing a rotten fruit

Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit,
then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits
remaining. If this state is impossible within the grid, return -1.

Example 1:
Input: grid = [[1, 1, 0], [0, 1, 1], [0, 1, 2]]
Output: 4

Example 2:
Input: grid = [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
Output: -1

Constraints:
1 <= grid.length, grid[i].length <= 10
"""
import collections

FRESH = 1
ROTTEN = 2
DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def oranges_rotting_bfs(grid: list[list[int]]) -> int:
    """
    Time complexity: O(m * n)
    Space complexity: O(m * n)
    where m is the number of rows and n is the number of columns in the grid.
    """
    queue = collections.deque()
    fresh_count: int = 0
    time: int = 0

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == FRESH:
                fresh_count += 1
            elif cell == ROTTEN:
                queue.append((r, c))

    while fresh_count > 0 and queue:
        for _ in range(len(queue)):
            r_rotten, c_rotten = queue.popleft()
            for dr, dc in DIRECTIONS:
                r, c = r_rotten + dr, c_rotten + dc
                try:
                    if grid[r][c] == FRESH and r >= 0 and c >= 0:
                        grid[r][c] = ROTTEN
                        queue.append((r, c))
                        fresh_count -= 1
                except IndexError:
                    continue

        time += 1

    return time if fresh_count == 0 else -1


def test_oranges_rotting():
    solutions = [
        oranges_rotting_bfs,
    ]

    test_cases = [
        ([[1, 1, 0], [0, 1, 1], [0, 1, 2]], 4),
        ([[1, 0, 1], [0, 2, 0], [1, 0, 1]], -1),
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
    ]

    for solution in solutions:
        for grid, expected_time_to_rot in test_cases:
            # Act
            time_to_rot = solution(grid)

            # Assert
            assert time_to_rot == expected_time_to_rot

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_oranges_rotting()
