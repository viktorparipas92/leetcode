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
from intervals.shared import Interval


def insert_linear_search(
    intervals: list[Interval], new_interval: Interval
) -> list[Interval]:
    """
    Time complexity: O(n)
    Space complexity: O(n) for the output + O(n) extra because of the new_interval
    """
    merged_intervals = [iv for iv in intervals if iv.end < new_interval.start]
    for iv in intervals[len(merged_intervals):]:
        if new_interval.end < iv.start:
            break

        new_interval = Interval(
            start=min(new_interval.start, iv.start),
            end=max(new_interval.end, iv.end),
        )

    merged_intervals.append(new_interval)
    merged_intervals.extend(iv for iv in intervals if new_interval.end < iv.start)
    return merged_intervals


def insert_binary_search(
    intervals: list[Interval], new_interval: Interval
) -> list[Interval]:
    """
    Time complexity: O(n) because of the insertion
    Space complexity: O(n) for the output + O(1) extra
    """
    if not intervals:
        return [new_interval]

    # Binary search to find the correct insertion point
    left_idx, right_idx = 0, len(intervals) - 1
    while left_idx <= right_idx:
        middle_idx = (left_idx + right_idx) // 2
        if intervals[middle_idx].start < new_interval.start:
            left_idx = middle_idx + 1
        else:
            right_idx = middle_idx - 1

    intervals.insert(left_idx, new_interval)

    # Merge overlapping intervals
    merged_intervals = []
    for interval in intervals:
        if not merged_intervals or merged_intervals[-1].end < interval.start:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1] = Interval(
                start=merged_intervals[-1].start,
                end=max(merged_intervals[-1].end, interval.end)
            )

    return merged_intervals


def insert_greedy(intervals: list[Interval], new_interval: Interval) -> list[Interval]:
    """
    Time complexity: O(n)
    Space complexity: O(n) for the output + O(1) extra
    """
    merged_intervals: list[Interval] = []
    for i, interval in enumerate(intervals):
        if new_interval.end < interval.start:
            merged_intervals.append(new_interval)
            return merged_intervals + intervals[i:]
        elif new_interval.start > interval.end:
            merged_intervals.append(interval)
        else:
            new_interval = Interval(
                start=min(new_interval.start, interval.start),
                end=max(new_interval.end, interval.end),
            )

    merged_intervals.append(new_interval)
    return merged_intervals


def test_insert():
    solutions = [
        insert_linear_search,
        insert_binary_search,
        insert_greedy,
    ]

    test_cases = [
        ([Interval(1, 3), Interval(4, 6)], Interval(2, 5), [Interval(1, 6)]),
        (
            [Interval(1, 2), Interval(3, 5), Interval(9, 10)],
            Interval(6, 7),
            [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(9, 10)]
        ),
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
