"""
Minimum Interval to Include Each Query
--------------------------------------
Difficulty: Hard

You are given a 2D integer array intervals,
where intervals[i] = [left_i, right_i] represents the ith interval
starting at left_i and ending at right_i (inclusive).

You are also given an integer array of query points queries.
The result of query[j] is the length of the shortest interval i such that
left_i <= queries[j] <= right_i. If no such interval exists,
the result of this query is -1.

Return an array output where output[j] is the result of query[j].
Note: The length of an interval is calculated as right_i - left_i + 1.

Example 1:
Input: intervals = [[1,3],[2,3],[3,7],[6,6]], queries = [2,3,1,7,6,8]
Output: [2,2,3,5,1,-1]
Explanation:

Query = 2: The interval [2,3] is the smallest one containing 2, it's length is 2.
Query = 3: The interval [2,3] is the smallest one containing 3, it's length is 2.
Query = 1: The interval [1,3] is the smallest one containing 1, it's length is 3.
Query = 7: The interval [3,7] is the smallest one containing 7, it's length is 5.
Query = 6: The interval [6,6] is the smallest one containing 6, it's length is 1.
Query = 8: There is no interval containing 8.
Constraints:

1 <= intervals.length <= 1000
1 <= queries.length <= 1000
1 <= left_i <= right_i <= 10000
1 <= queries[j] <= 10000
"""
from intervals.shared import Interval


def min_interval_brute_force(
    intervals: list[Interval], queries: list[int]
) -> list[int]:
    """
    Time cpmplexity: O(n * m)
    Space complexity: O(1)
    where n is the number of intervals and m is the number of queries.
    """
    output: list[int] = []
    for query in queries:
        current = -1
        for interval in intervals:
            if interval.start <= query <= interval.end:
                interval_length = interval.end - interval.start + 1
                if current == -1 or interval_length < current:
                    current = interval_length

        output.append(current)

    return output


def test_min_interval():
    solutions = [
        min_interval_brute_force,
    ]

    intervals_1 = [
        Interval(1, 3),
        Interval(2, 3),
        Interval(3, 7),
        Interval(6, 6),
    ]
    test_cases = [
        (intervals_1, [2, 3, 1, 7, 6, 8], [2, 2, 3, 5, 1, -1]),
    ]

    for solution in solutions:
        for intervals, queries, expected_output in test_cases:
            # Act
            output = solution(intervals, queries)

            # Assert
            assert output == expected_output

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_min_interval()