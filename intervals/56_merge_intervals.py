"""
56. Merge Intervals
-------------------
Difficulty: Medium

Given an array of intervals where intervals[i] = [start_i, end_i],
merge all overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.
You may return the answer in any order.

Note: Intervals are non-overlapping if they have no common point.
For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

Example 1:
Input: intervals = [[1,3],[1,5],[6,7]]
Output: [[1,5],[6,7]]

Example 2:
Input: intervals = [[1,2],[2,3]]
Output: [[1,3]]

Constraints:
1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= start <= end <= 1000
"""
from collections import namedtuple, defaultdict

Interval = namedtuple('Interval', ['start', 'end'])


def merge_sorting(intervals: list[Interval]) -> list[Interval]:
    """
    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    intervals.sort(key=lambda interval: interval.start)
    merged_intervals = [intervals[0]]

    for start, end in intervals:
        last_interval = merged_intervals[-1]
        if start <= last_interval.end:
            merged_intervals[-1] = last_interval._replace(end=max(last_interval.end, end))
        else:
            merged_intervals.append(Interval(start, end))

    return merged_intervals


def merge_sweep_line(intervals: list[Interval]) -> list[Interval]:
    """
    Time complexity: O(n logn)
    Space complexity: O(n)
    """
    event_counts = defaultdict(int)
    for interval in intervals:
        event_counts[interval.start] += 1
        event_counts[interval.end] -= 1

    merged_intervals: list[Interval] = []
    start_point = None
    active_interval_count = 0
    for point in sorted(event_counts):
        if active_interval_count == 0:
            start_point = point

        active_interval_count += event_counts[point]
        if active_interval_count == 0:
            interval = Interval(start=start_point, end=point)
            merged_intervals.append(interval)
            start_point = None

    return merged_intervals


def merge_greedy(intervals: list[Interval]) -> list[Interval]:
    """
    Time complexity: O(n + m)
    Space complexity: O(n)
    """
    max_start = max(interval.start for interval in intervals)
    end_points = [0] * (max_start + 1)  # Array to store max end values
    for itv in intervals:
        end_points[itv.start] = max(itv.end + 1, end_points[itv.start])

    merged_intervals = []
    current_end = -1
    current_start = -1

    for i, end in enumerate(end_points):
        if end != 0:
            if current_start == -1:
                current_start = i

            current_end = max(end - 1, current_end)

        if current_end == i:
            merged_intervals.append(Interval(start=current_start, end=current_end))
            current_end = -1
            current_start = -1

    if current_start != -1:
        merged_intervals.append(Interval(start=current_start, end=current_end))

    return merged_intervals


def test_merge():
    solutions = [
        merge_sorting,
        merge_sweep_line,
        merge_greedy,
    ]

    test_cases = [
        ([Interval(1, 3), Interval(1, 5), Interval(6, 7)], [Interval(1, 5), Interval(6, 7)]),
        ([Interval(1, 2), Interval(2, 3)], [Interval(1, 3)]),
    ]

    for solution in solutions:
        for intervals, expected_merged_intervals in test_cases:
            # Act
            merged_intervals = solution(intervals)

            # Assert
            assert merged_intervals == expected_merged_intervals

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_merge()
