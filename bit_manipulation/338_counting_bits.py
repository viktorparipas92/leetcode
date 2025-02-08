"""
338. Counting Bits
------------------
Difficulty: Easy

Given an integer n, count the number of 1's in the binary representation of every
number in the range [0, n].

Return an array output where output[i] is the number of 1's in the binary
representation of i.

Example 1:
Input: n = 4
Output: [0,1,1,2,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100

Constraints:
0 <= n <= 1000
"""


def count_bits_bit_manipulation(n: int) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    one_counts: list[int] = []
    for number in range(n + 1):
        one_count = 0
        for i in range(32):  # 32-bit integer
            # (1 << i) creates a mask with only the i-th bit set to 1
            # Performing bitwise AND with 'number' isolates this bit.
            if number & (1 << i):
                one_count += 1

        one_counts.append(one_count)

    return one_counts


def count_bits_bit_manipulation_2(n: int) -> list[int]:
    """
    Time complexity: O(n) (?)
    Space complexity: O(1) (?)
    """
    bit_counts = [0] * (n + 1)
    for _number in range(1, n + 1):
        number = _number
        while number != 0:
            bit_counts[_number] += 1
            # Remove the rightmost 1 bit in number
            # eg. 5 & 4 = 101 & 100 = 100, 4 & 3 = 100 & 011 = 0
            number &= (number - 1)

    return bit_counts


def count_bits_builtin(n: int) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    return [bin(i).count('1') for i in range(n + 1)]


def count_bits_dynamic_programming(n: int) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    bit_counts = [0] * (n + 1)
    power_of_two = 1

    for number in range(1, n + 1):
        if power_of_two * 2 == number:
            power_of_two = number

        bit_counts[number] = 1 + bit_counts[number - power_of_two]

    return bit_counts


def count_bits_bit_manipulation_optimal(n: int) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    bit_counts = [0] * (n + 1)
    for number in range(n + 1):
        # number >> 1 shifts the bits to the right by 1 (equivalent to number // 2)
        # number & 1 isolates the rightmost bit (since it is lost in the right shift)
        bit_counts[number] = bit_counts[number >> 1] + (number & 1)

    return bit_counts


def test_count_bits():
    # Arrange
    solutions = [
        count_bits_bit_manipulation,
        count_bits_bit_manipulation_2,
        count_bits_builtin,
        count_bits_dynamic_programming,
        count_bits_bit_manipulation_optimal,
    ]
    test_cases = [
        (4, [0, 1, 1, 2, 1]),
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
        (0, [0]),
    ]

    # Act
    for solution in solutions:
        for n, expected_bit_count in test_cases:
            # Act
            bit_count = solution(n)

            # Assert
            assert bit_count == expected_bit_count

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_count_bits()
