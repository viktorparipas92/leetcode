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


def test_max_sliding_window():
    solutions = [
        max_sliding_window_brute_force,
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
