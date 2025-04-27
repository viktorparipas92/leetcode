WATER = 0


def max_area_of_island(grid: list[list[int]]) -> int:
    """
    Time complexity: O(m * n)
    Space complexity: O(m * n)
    where m is the number of rows and n is the number of columns in the grid.
    """
    visited: set[tuple[int, int]] = set()

    def depth_first_search(row_idx: int, column_idx: int) -> int:
        if row_idx < 0 or col_idx < 0 or (row_idx, column_idx) in visited:
            return 0

        try:
            is_water = grid[row_idx][column_idx] == WATER
        except IndexError:
            return 0

        if is_water:
            return 0

        visited.add((row_idx, column_idx))
        return (
            1
            + depth_first_search(row_idx + 1, column_idx)
            + depth_first_search(row_idx - 1, column_idx)
            + depth_first_search(row_idx, column_idx + 1)
            + depth_first_search(row_idx, column_idx - 1)
        )

    area = 0
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            area = max(area, depth_first_search(row_idx, col_idx))

    return area


def test_max_area_of_island():
    solutions = [
        max_area_of_island,
    ]

    grid_1 = [
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1],
    ]
    test_cases = [
        (grid_1, 6),
    ]

    for solution in solutions:
        for grid, expected_max_area in test_cases:
            # Act
            max_area = solution(grid)

            # Assert
            assert max_area == expected_max_area

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_max_area_of_island()
