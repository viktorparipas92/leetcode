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
from collections import namedtuple


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
    Uses recursion with memoization
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # Cache to store results of previously computed sub-problems
    size = len(numbers)
    max_sum_from: list[tuple[int | None, int | None]] = [
        (None, None) for _ in range(size + 1)
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


SubarraySums = namedtuple('SubarraySums', ['best_overall_sum', 'best_contiguous_sum'])


def max_subarray_dynamic_bottom_up(numbers: list[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    max_sum_from = [SubarraySums(0, 0) for _ in numbers]

    # Base case: The last element is the best contiguous sum and overall sum on its own
    max_sum_from[-1] = SubarraySums(numbers[-1], numbers[-1])

    # Start from the second-to-last element
    # because each element's value depends on the next element.
    for j in range(len(numbers) - 2, -1, -1):
        number = numbers[j]

        # Either starting a new subarray or extending the previous one
        best_contiguous_sum = max(
            number, number + max_sum_from[j + 1].best_contiguous_sum
        )

        # Either skipping or extending the current subarray
        best_overall_sum = max(
            max_sum_from[j + 1].best_overall_sum, best_contiguous_sum
        )

        max_sum_from[j] = SubarraySums(best_overall_sum, best_contiguous_sum)

    # The best overall sum is at index 0
    return max_sum_from[0].best_overall_sum


def max_subarray_dynamic_bottom_up_optimized(numbers: list[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    max_sum_at_index = numbers.copy()
    for i, number in enumerate(numbers[1:], start=1):
        previous_sum = max_sum_at_index[i - 1]
        if previous_sum > 0:
            max_sum_at_index[i] += previous_sum

    return max(max_sum_at_index)


def test_max_subarray():
    solutions = [
        max_subarray_brute_force,
        max_subarray_recursion,
        max_subarray_dynamic_top_down,
        max_subarray_dynamic_bottom_up,
        max_subarray_dynamic_bottom_up_optimized,
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