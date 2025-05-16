"""
371. Sum of Two Integers
------------------------
Difficulty: Medium

Given two integers a and b, return the sum of the two integers
without using the + and - operators.

Example 1:
Input: a = 1, b = 1
Output: 2
Example 2:

Input: a = 4, b = 7
Output: 11

Constraints:
-1000 <= a, b <= 1000
"""


MASK: int = 0xFFFFFFFF
MAX_INT: int = 0x7FFFFFFF
NUMBER_OF_BITS: int = 32


def get_sum_bit_manipulation(*args: int) -> int:
    """
    Time complexity: O(1)
    Space complexity: O(1)
    """
    a, b = args
    carry: int = 0
    result: int = 0

    for i in range(NUMBER_OF_BITS):
        a_bit = (a >> i) & 1
        b_bit = (b >> i) & 1

        current_bit = a_bit ^ b_bit ^ carry
        carry = (a_bit + b_bit + carry) >= 2
        if current_bit:
            result |= (1 << i)

    if result > MAX_INT:  # If result is negative
        result = ~(result ^ MASK)  # Two's complement to get the negative number

    return result


def get_sum_bit_manipulation_optimal(*args: int) -> int:
    """
    Time complexity: O(1)
    Space complexity: O(1)
    """
    a, b = args
    while b != 0:
        carry = (a & b) << 1
        a = (a ^ b) & MASK
        b = carry & MASK

    result = a
    if result > MAX_INT:  # If result is negative
        result = ~(result ^ MASK)  # Two's complement to get the negative number

    return result


def test_get_sum():
    solutions = [
        get_sum_bit_manipulation,
        get_sum_bit_manipulation_optimal,
    ]

    test_cases = [
        (1, 1, 2),
        (4, 7, 11),
    ]

    for solution in solutions:
        for a, b, expected_sum in test_cases:
            # Act
            sum_result = solution(a, b)

            # Assert
            assert sum_result == expected_sum

        print(f'Tests passed for {solution.__name__}! ')

if __name__ == '__main__':
    test_get_sum()
