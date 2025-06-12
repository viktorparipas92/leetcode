"""
Meeting Rooms II
-----------------
Difficulty: Medium

Given an array of meeting time interval objects consisting of start and end times
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
find the minimum number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:
Input: intervals = [(0,40),(5,10),(15,20)]
Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:
Input: intervals = [(4,9)]
Output: 1

Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""
import heapq
from collections import defaultdict

from intervals.shared import Interval


def min_meeting_rooms_min_heap(intervals: list[Interval]) -> int:
    """
    Time complexity: O(n * log(n))
    Space complexity: O(n)
    """
    end_times: list[int] = []

    intervals.sort(key=lambda x: x.start)
    for interval in intervals:
        if end_times and end_times[0] <= interval.start:
            heapq.heappop(end_times)

        heapq.heappush(end_times, interval.end)

    return len(end_times)


def min_meeting_rooms_sweep_line(intervals: list[Interval]) -> int:
    """
    Time complexity: O(n * log(n))
    Space complexity: O(n)
    """
    meeting_time_changes: dict[int, int] = defaultdict(int)
    for interval in intervals:
        meeting_time_changes[interval.start] += 1
        meeting_time_changes[interval.end] -= 1

    current_meeting_count: int = 0
    max_meeting_count: int = 0
    for time_point in sorted(meeting_time_changes):
        current_meeting_count += meeting_time_changes[time_point]
        max_meeting_count = max(max_meeting_count, current_meeting_count)

    return max_meeting_count


def min_meeting_rooms_two_pointers(intervals: list[Interval]) -> int:
    """
    Time complexity: O(n * log(n))
    Space complexity: O(n)
    """
    start_times: list[int] = sorted([i.start for i in intervals])
    end_times: list[int] = sorted([i.end for i in intervals])

    max_rooms_needed: int = 0
    current_room_count: int = 0
    start_count = end_count = 0
    while start_count < len(intervals):
        if start_times[start_count] < end_times[end_count]:
            start_count += 1
            current_room_count += 1
        else:
            end_count += 1
            current_room_count -= 1

        max_rooms_needed = max(max_rooms_needed, current_room_count)

    return max_rooms_needed


def test_min_meeting_rooms():
    solutions = [
        min_meeting_rooms_min_heap,
        min_meeting_rooms_sweep_line,
        min_meeting_rooms_two_pointers,
    ]

    test_cases = [
        ([Interval(0, 40), Interval(5, 10), Interval(15, 20)], 2),
        ([Interval(4, 9)], 1),
    ]

    for solution in solutions:
        for intervals, expected_min_num_days in test_cases:
            # Act
            min_num_days = solution(intervals)

            # Assert
            assert min_num_days == expected_min_num_days

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_min_meeting_rooms()
