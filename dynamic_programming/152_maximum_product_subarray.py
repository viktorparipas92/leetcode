"""
152. Maximum Product Subarray
-----------------------------
Difficulty: Medium

Given an integer array nums, find a subarray that has the largest product
within the array and return it.
A subarray is a contiguous non-empty sequence of elements within an array.
You can assume the output will fit into a 32-bit integer.

Example 1:
Input: nums = [1,2,-3,4]
Output: 4

Example 2:
Input: nums = [-2,-1]
Output: 2

Constraints:
1 <= nums.length <= 1000
-10 <= nums[i] <= 10
"""


def max_product_brute_force(numbers: list[int]) -> int:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    product  = numbers[0]

    for i, number in enumerate(numbers):
        current_product = number
        product = max(product, current_product)
        for j, other_number in enumerate(numbers[i + 1:], start=i + 1):
            current_product *= other_number
            product = max(product, current_product)

    return product


def max_product_kadane(numbers: list[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    product = numbers[0]
    current_minimum = current_maximum = 1

    for number in numbers:
        tmp = current_maximum * number

        current_maximum = max(
            number * current_maximum,
            number * current_minimum,
            number,
        )

        current_minimum = min(tmp, number * current_minimum, number)

        product = max(product, current_maximum)

    return product


def max_product_prefix_suffix(numbers: list[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    length = len(numbers)
    product = numbers[0]
    prefix = suffix = 0

    for i in range(length):
        prefix = numbers[i] * (prefix or 1)
        suffix = numbers[-i] * (suffix or 1)
        product = max(product, max(prefix, suffix))

    return product


def test_max_product():
    solutions = [
        max_product_brute_force,
        max_product_kadane,
        max_product_prefix_suffix,
    ]

    test_cases = [
        ([1, 2, -3, 4], 4),
        ([-2, -1], 2),
    ]

    for solution in solutions:
        for numbers, expected_product in test_cases:
            # Act
            product = solution(numbers)

            # Assert
            assert product == expected_product

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_max_product()
