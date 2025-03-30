"""
239. Sliding Window Maximum
----------------------------
Difficulty: Hard

You are given an array of integers nums and an integer k.
There is a sliding window of size k that starts at the left edge of the array.
The window slides one position to the right until it reaches the right edge of the
array.
Return a list that contains the maximum element in the window at each step.

Example 1:
Input: nums = [1,2,1,0,4,2,6], k = 3
Output: [2,2,4,4,6]
Explanation:
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6

Constraints:
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
1 <= k <= nums.length
"""

import heapq
from collections import deque
from typing import NamedTuple


def max_sliding_window_brute_force(numbers: list[int], k: int) -> list[int]:
    """
    Time complexity: O(n * k)
    Space complexity: O(1) + O(n - k + 1) for the output
    """
    maxima: list[int] = []
    length = len(numbers)
    for start_index, start_number in enumerate(numbers[:length - k + 1]):
        maximum = start_number
        for number in numbers[start_index + 1:start_index + k]:
            maximum = max(maximum, number)

        maxima.append(maximum)

    return maxima


class Number(NamedTuple):
    index: int
    value: int

    def __lt__(self, other):
        return self.value < other.value


def max_sliding_window_heap(numbers: list[int], k: int) -> list[int]:
    """
    Time complexity: O(n * log(n))
    Space complexity: O(n)
    """
    number_heap: list[Number] = []
    maxima: list[int] = []
    for i, number in enumerate(numbers):
        heapq.heappush(number_heap, Number(i, -number))
        if i >= k - 1:  # Start calculating the maximum from the kth element
            while number_heap[0].index <= i - k:
                heapq.heappop(number_heap)

            maxima.append(-number_heap[0].value)

    return maxima


def max_sliding_window_deque(numbers: list[int], k: int) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    maxima: list[int] = []
    index_queue: deque[int] = deque()
    left_index = right_index = 0

    length = len(numbers)
    while right_index < length:
        while index_queue and numbers[index_queue[-1]] < numbers[right_index]:
            index_queue.pop()

        index_queue.append(right_index)

        if left_index > index_queue[0]:
            index_queue.popleft()

        if (right_index + 1) >= k:
            maxima.append(numbers[index_queue[0]])
            left_index += 1

        right_index += 1

    return maxima


def test_max_sliding_window():
    solutions = [
        max_sliding_window_brute_force,
        max_sliding_window_heap,
        max_sliding_window_deque,
    ]

    test_cases = [
        ([1, 2, 1, 0, 4, 2, 6], 3, [2, 2, 4, 4, 6]),
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
    ]

    for solution in solutions:
        for numbers, window_size, expected_maxima in test_cases:
            # Act
            maxima = solution(numbers, window_size)

            # Assert
            assert maxima == expected_maxima

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_max_sliding_window()
