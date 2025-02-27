"""
53. Maximum Subarray
---------------------
Difficulty: Medium

Given an array of integers nums, find the subarray with the largest sum and
return the sum.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [2,-3,4,-2,2,1,-1,4]
Output: 8
Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

Example 2:
Input: nums = [-1]
Output: -1

Constraints:
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
"""


def max_subarray_brute_force(numbers: list[int]) -> int:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    length, maximum_sum = len(numbers), numbers[0]
    for i in range(length):
        current_sum = 0
        for j, number in enumerate(numbers[i:], start=i):
            current_sum += number
            maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum


def test_max_subarray():
    solutions = [
        max_subarray_brute_force,
    ]

    test_cases = [
        ([2, -3, 4, -2, 2, 1, -1, 4], 8),
        ([-1], -1),
        ([1, 2, 3, 4, 5], 15),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ]

    for solution in solutions:
        for numbers, expected_maximum in test_cases:
            # Act
            maximum = solution(numbers)

            # Assert
            assert maximum == expected_maximum

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_max_subarray()