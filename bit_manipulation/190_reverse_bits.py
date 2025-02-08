"""
190. Reverse Bits
-----------------
Difficulty: Easy

Given a 32-bit unsigned integer n,
reverse the bits of the binary representation of n and return the result.

Example 1:
Input: n = 00000000000000000000000000010101
Output:    2818572288 (10101000000000000000000000000000)
Explanation:
Reversing 00000000000000000000000000010101, which represents the unsigned integer 21,
gives us 10101000000000000000000000000000 which represents the unsigned integer
2818572288.
"""


def reverse_bits_bruce_force(n: int) -> int:
    """
    Time complexity: O(1)
    Space complexity: O(1)
    """
    binary: str = ''
    for i in range(32):
        # (1 << i) creates a mask with only the i-th bit set to 1
        # Performing bitwise AND with 'n' isolates this bit.
        binary_increment = '1' if (n & (1 << i)) else '0'
        binary += binary_increment

    reversed_number = 0
    for i, bit in enumerate(binary[::-1]):
        if bit == '1':
            # Perform bitwise OR with reversed_number to set the i-th bit
            reversed_number |= (1 << i)

    return reversed_number


def test_reverse_bits():
    # Arrange
    solutions = [
        reverse_bits_bruce_force,
    ]

    test_cases = [
        (0b00000000000000000000000000010101, 0b10101000000000000000000000000000),  # 21 -> 2818572288
        (0b00000010100101000001111010011100, 0b00111001011110000010100101000000), # 43261596 -> 964176192
        (0b11111111111111111111111111111101, 0b10111111111111111111111111111111), # 4294967293 -> 3221225471
    ]

    for solution in solutions:
        for input_number, expected_reverse in test_cases:
            # Act
            reversed_number = solution(input_number)

            # Assert
            assert reversed_number == expected_reverse

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_reverse_bits()
