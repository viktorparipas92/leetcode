"""
435. Non-overlapping Intervals
------------------------------
Difficulty: Medium

Given an array of intervals  where intervals[i] = [start_i, end_i], return the minimum
number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note: Intervals are non-overlapping even if they have a common point.
For example, [1, 3] and [2, 4] are overlapping,
but [1, 2] and [2, 3] are non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,4],[1,4]]
Output: 1
Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[2,4]]
Output: 0

Constraints:
1 <= intervals.length <= 1000
intervals[i].length == 2
-50000 <= starti < endi <= 50000
"""
from intervals.shared import Interval


def erase_overlap_intervals_recursion(intervals: list[Interval]) -> int:
    """
    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    intervals.sort(key=lambda interval: interval.start)

    def depth_first_search(start_index: int, previous_index: int) -> int:
        if start_index == len(intervals):
            return 0

        num_intervals_to_erase = depth_first_search(start_index + 1, previous_index)
        if (
            previous_index == -1
            or intervals[previous_index].end <= intervals[start_index].start
        ):
            num_intervals_to_erase = max(
                num_intervals_to_erase,
                1 + depth_first_search(start_index + 1, start_index)
            )

        return num_intervals_to_erase

    return len(intervals) - depth_first_search(start_index=0, previous_index=-1)


def erase_overlap_intervals_dp_top_down(intervals: list[Interval]) -> int:
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    intervals.sort(key=lambda interval: interval.end)
    n = len(intervals)
    memory: dict[int, int] = {}

    def depth_first_search(i: int) -> int:
        if i in memory:
            return memory[i]

        num_intervals_to_erase = 1
        for j in range(i + 1, n):
            if intervals[i].end <= intervals[j].start:
                num_intervals_to_erase = max(
                    num_intervals_to_erase, 1 + depth_first_search(j)
                )

        memory[i] = num_intervals_to_erase
        return num_intervals_to_erase

    return n - depth_first_search(i=0)


def test_erase_overlap_intervals():
    solutions = [
        erase_overlap_intervals_recursion,
        erase_overlap_intervals_dp_top_down,
    ]

    test_cases = [
        ([Interval(1, 2), Interval(2, 4), Interval(1, 4)], 1),
        ([Interval(1, 2), Interval(2, 4)], 0),
    ]

    for solution in solutions:
        for intervals, expected_num_intervals_to_erase in test_cases:
            # Act
            num_intervals_to_erase = solution(intervals)

            # Assert
            assert num_intervals_to_erase == expected_num_intervals_to_erase

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_erase_overlap_intervals()
