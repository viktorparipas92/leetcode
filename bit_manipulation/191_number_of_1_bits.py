"""
191. Number of 1 Bits
----------------------
Difficulty: Easy

You are given an unsigned integer n.
Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.

Example 1:
Input: n = 00000000000000000000000000010111
Output: 4

Example 2:
Input: n = 01111111111111111111111111111101
Output: 30
"""


def hamming_weight_bit_mask(n: int) -> int:
    """
    Time complexity: O(1)
    Space complexity: O(1)
    """
    result = 0
    for i in range(32):
        if (1 << i) & n:
            result += 1

    return result


def test_hamming_weight():
    # Arrange
    solutions = [
        hamming_weight_bit_mask,
    ]

    test_cases = [
        (0b00000000000000000000000000010111, 4),
        (0b01111111111111111111111111111101, 30),
    ]

    for solution in solutions:
        for input_number, expected_hamming_weight in test_cases:
            # Act
            hamming_weight = solution(input_number)

            # Assert
            assert hamming_weight == expected_hamming_weight

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_hamming_weight()
