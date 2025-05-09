"""
2013. Detect Squares
--------------------
Difficulty: Medium

You are given a stream of points consisting of x-y coordinates on a 2-D plane.
Points can be added and queried as follows:
- Add
  - new points can be added to the stream into a data structure.
  - Duplicate points are allowed and should be treated as separate points.
- Query
  - Given a single query point, count the number of ways to choose three additional
    points from the data structure such that the three points and the query point
    form a square.
  - The square must have all sides parallel to the x-axis and y-axis, i.e. no diagonal
    squares are allowed. Recall that a square must have four equal sides.

Implement the CountSquares class:
- CountSquares() Initializes the object.
- void add(int[] point) Adds a new point point = [x, y].
- int count(int[] point) Counts the number of ways to form valid squares with
  point = [x, y] as described above.


Example 1:
Input:
["CountSquares", "add",
  [[1, 1]], "add", [[2, 2]], "add", [[1, 2]], "count", [[2, 1]],
   "count", [[3, 3]], "add", [[2, 2]], "count", [[2, 1]]
]
Output:
[null, null, null, null, 1, 0, null, 2]

Explanation:
CountSquares countSquares = new CountSquares();
countSquares.add([1, 1]);
countSquares.add([2, 2]);
countSquares.add([1, 2]);

countSquares.count([2, 1]);   // return 1.
countSquares.count([3, 3]);   // return 0.
countSquares.add([2, 2]);     // Duplicate points are allowed.
countSquares.count([2, 1]);   // return 2.
Constraints:

point.length == 2
0 <= x, y <= 1000
"""
from collections import defaultdict


Point = tuple[int, int]


class CountSquaresHashMap:
    """
    Space complexity: O(n)
    """
    def __init__(self):
        self.point_counts: dict[Point, int] = defaultdict(int)
        self.points: list[Point] = []

    def add(self, point: Point) -> None:
        """
        Time complexity: O(1)
        """
        self.point_counts[point] += 1
        self.points.append(point)

    def count(self, point: Point) -> int:
        """
        Count the number of squares that can be formed with the given point.
        Time complexity: O(n)
        """
        _count = 0
        px, py = point
        for x, y in self.points:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue

            _count += self.point_counts[(x, py)] * self.point_counts[(px, y)]

        return _count


def test_count_squares():
    solutions = [
        CountSquaresHashMap,
    ]

    for solution in solutions:
        # Act, Assert
        square_counter = solution()
        square_counter.add((1, 1))
        square_counter.add((2, 2))
        square_counter.add((1, 2))

        assert square_counter.count((2, 1)) == 1
        assert square_counter.count((3, 3)) == 0

        square_counter.add((2, 2))

        assert square_counter.count((2, 1)) == 2

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_count_squares()
