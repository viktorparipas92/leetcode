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


def max_subarray_recursion(numbers: list[int]) -> int:
    """
    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    def depth_first_search(i: int, subarray_started: bool) -> int:
        try:
            number = numbers[i]
        except IndexError:
            # Prevent empty subarray from being optimal
            return 0 if subarray_started else -1e6

        # If a subarray has already started, we cannot skip numbers anymore.
        # Otherwise, we explore the option of skipping number and starting later.
        first_option = 0 if subarray_started else depth_first_search(i + 1, False)

        # Choose the best between:
        # 1. Skipping number
        # 2. Taking number and extending the subarray.
        return max(first_option, number + depth_first_search(i + 1, True))

    return depth_first_search(i=0, subarray_started=False)


def max_subarray_dynamic_top_down(numbers: list[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # Cache to store results of previously computed sub-problems
    length = len(numbers)
    max_sum_from: list[tuple[int | None, int | None]] = [
        (None, None) for _ in range(length + 1)
    ]

    def depth_first_search(i: int, subarray_started: bool) -> int:
        try:
            number = numbers[i]
        except IndexError:
            # Prevent empty subarray from being optimal
            return 0 if subarray_started else -1e6

        if best_sum := max_sum_from[i][int(subarray_started)] is not None:
            return best_sum

        first_option = 0 if subarray_started else depth_first_search(i + 1, False)
        best_sum = max(first_option, number + depth_first_search(i + 1, True))
        return best_sum

    return depth_first_search(i=0, subarray_started=False)


def test_max_subarray():
    solutions = [
        max_subarray_brute_force,
        max_subarray_recursion,
        max_subarray_dynamic_top_down,
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