"""
57. Insert Interval
------------------------------
Difficulty: Medium

You are given an array of non-overlapping intervals where
intervals[i] = [start_i, end_i] represents the start and end time of the ith interval.
intervals is initially sorted in ascending order by start_i.
You are given another interval newInterval = [start, end].

Insert newInterval into intervals such that intervals is still sorted in ascending
order by start_i and also intervals still does not have any overlapping intervals.
You may merge the overlapping intervals if needed.

Return intervals after adding newInterval.

Note: Intervals are non-overlapping if they have no common point.
For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

Example 1:
Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
Output: [[1,6]]

Example 2:
Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
Output: [[1,2],[3,5],[6,7],[9,10]]

Constraints:
0 <= intervals.length <= 1000
newInterval.length == intervals[i].length == 2
0 <= start <= end <= 1000
"""


def insert_linear_search(
    intervals: list[tuple[int, int]], new_interval: list[int]
) -> list[tuple[int, int]]:
    """
    Time complexity: O(n)
    Space complexity: O(n) for the output + O(1) extra
    """
    merged_intervals = [iv for iv in intervals if iv[1] < new_interval[0]]
    for iv in intervals[len(merged_intervals):]:
        if new_interval[1] < iv[0]:
            break

        new_interval[0] = min(new_interval[0], iv[0])
        new_interval[1] = max(new_interval[1], iv[1])

    merged_intervals.append(tuple(new_interval))
    merged_intervals.extend(iv for iv in intervals if iv[0] > new_interval[1])
    return merged_intervals


def test_insert():
    solutions = [
        insert_linear_search,
    ]

    test_cases = [
        ([(1, 3), (4, 6)], [2, 5], [(1, 6)]),
        ([(1, 2), (3, 5), (9, 10)], [6, 7], [(1, 2), (3, 5), (6, 7), (9, 10)]),
    ]

    for solution in solutions:
        for intervals, new_interval, expected_merged_intervals in test_cases:
            # Act
            merged_intervals = solution(intervals, new_interval)

            # Assert
            assert merged_intervals == expected_merged_intervals

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_insert()
