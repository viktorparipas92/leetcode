"""
973. K Closest Points to Origin
-------------------------------
Difficulty: Medium

You are given an 2-D array points where points[i] = [x_i, y_i] represents the
coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance
(sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.

Example 1:
Input: points = [[0,2],[2,2]], k = 1
Output: [[0,2]]

Example 2:
Input: points = [[0,2],[2,0],[2,2]], k = 2
Output: [[0,2],[2,0]]
Explanation: The output [2,0],[0,2] would also be accepted.

Constraints:
1 <= k <= points.length <= 1000
-100 <= points[i][0], points[i][1] <= 100
"""

import heapq


POINT = tuple[int, int]


def euclidean_distance(point: POINT) -> int:
    return point[0] ** 2 + point[1] ** 2


def k_closest_sorting(points: list[POINT], k: int) -> list[POINT]:
    """
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    points.sort(key=euclidean_distance)
    return points[:k]


def k_closest_min_heap(points: list[POINT], k: int) -> list[POINT]:
    """
    Time complexity: O(k log n)
    Space complexity: O(n)
    """
    minimum_heap: list[tuple[int, POINT]] = []
    for point in points:
        distance = euclidean_distance(point)
        minimum_heap.append((distance, point))

    heapq.heapify(minimum_heap)
    closest_points = []
    while k > 0:
        distance, point = heapq.heappop(minimum_heap)
        closest_points.append(point)
        k -= 1

    return closest_points


def test_k_closest_points():
    solutions = [
        k_closest_sorting,
        k_closest_min_heap,
    ]

    test_cases = [
        ([(0, 2), (2, 2)], 1, [(0, 2)]),
        ([(0, 2), (2, 0), (2, 2)], 2, [(0, 2), (2, 0)]),
        ([(1, 3), (-2, 2)], 1, [(-2, 2)]),
        ([(3, 3), (5, -1), (-2, 4)], 2, [(3, 3), (-2, 4)]),
    ]

    for solution in solutions:
        for points, k, expected_k_closest in test_cases:
            # Act
            k_closest = solution(points, k)

            # Assert
            assert k_closest == expected_k_closest

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_k_closest_points()


