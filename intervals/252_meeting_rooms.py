"""
252. Meeting Rooms
--------------------------------
Difficulty: Easy

Given an array of meeting time interval objects consisting of start and end times
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could
add all meetings to their schedule without any conflicts.

Example 1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:
(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]
Output: true

Note:
(0,8),(8,10) is not considered a conflict at 8
Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    @staticmethod
    def can_attend_meetings_brute_force(intervals: list[Interval]) -> bool:
        """Time complexity: O(n^2)"""
        for i, first_interval in enumerate(intervals):
            for j, second_interval in enumerate(intervals[i+1:]):
                if (
                    min(first_interval.end, second_interval.end)
                    > max(first_interval.start, second_interval.start)
                ):
                    return False

        return True

    @staticmethod
    def can_attend_meetings_sorting(intervals: list[Interval]) -> bool:
        """Time complexity: O(n * log(n))"""
        intervals.sort(key=lambda i: i.start)
        for i, interval in enumerate(intervals[1:], 1):
            interval_1 = intervals[i - 1]
            if interval_1.end > interval.start:
                return False

        return True


def test_can_attend_meetings():
    solution = Solution()
    solution_methods = [
        solution.can_attend_meetings_brute_force,
        solution.can_attend_meetings_sorting,
    ]
    intervals_1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    test_cases = [
        {'input': intervals_1, 'expected': False},
        {'input': [Interval(5, 8), Interval(9, 15)], 'expected': True},
    ]

    for solution_method in solution_methods:
        for test_case in test_cases:
            assert solution_method(test_case['input']) == test_case['expected']

        print(f'Tests passed for {solution_method.__name__}')


if __name__ == '__main__':
    test_can_attend_meetings()
