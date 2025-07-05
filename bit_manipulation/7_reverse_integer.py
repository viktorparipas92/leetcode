"""
7. Reverse Integer
-----------------
Difficulty: Medium

You are given a signed 32-bit integer x.
Return x after reversing each of its digits.
After reversing, if x goes outside the signed 32-bit integer range [-2^31, 2^31 - 1],
then return 0 instead.
Solve the problem without using integers that are outside the signed 32-bit integer range.

Example 1:
Input: x = 1234
Output: 4321

Example 2:
Input: x = -1234
Output: -4321

Example 3:
Input: x = 1234236467
Output: 0

Constraints:
-2^31 <= x <= 2^31 - 1
"""
import math

MIN_VALUE = -(1 << 31)  # -2^31
MAX_VALUE = (1 << 31) - 1  # 2^31 - 1


def reverse_brute_force(x: int) -> int:
    """
    Time complexity: O(1)
    Space complexity: O(1)
    """
    absolute = abs(x)
    reverse: int = int(str(absolute)[::-1])
    if x < 0:
        reverse *= -1

    if reverse < MIN_VALUE or reverse > MAX_VALUE:
        return 0

    return reverse


def reverse_recursion(x: int) -> int:
    """
    Time complexity: O(1)
    Space complexity: O(1)
    """

    def recurse(n: int, reverse: int) -> int:
        if n == 0:
            return reverse

        reverse = reverse * 10 + n % 10
        return recurse(n // 10, reverse)

    sign = -1 if x < 0 else 1
    absolute = abs(x)
    reversed_number = recurse(n=absolute, reverse=0)
    reversed_number *= sign
    if reversed_number < MIN_VALUE or reversed_number > MAX_VALUE:
        return 0

    return reversed_number


def reverse_iterative(x: int) -> int:
    """
    Time complexity: O(1)
    Space complexity: O(1)
    """
    reverse: int = 0
    while x:
        digit = int(math.fmod(x, 10))  # Get the last digit
        x = int(x / 10)
        if (
            reverse > MAX_VALUE // 10
            or (reverse == MAX_VALUE // 10 and digit > MAX_VALUE % 10)
            or reverse < MIN_VALUE // 10
            or (reverse == MIN_VALUE // 10 and digit < MIN_VALUE % 10)
        ):
            return 0

        reverse = (reverse * 10) + digit

    return reverse


def test_reverse_integer():
    solutions = [
        reverse_brute_force,
        reverse_recursion,
        reverse_iterative,
    ]

    test_cases = [
        (1234, 4321),
        (-1234, -4321),
        (1234236467, 0),
    ]

    for solution in solutions:
        for x, expected_reverse in test_cases:
            # Act
            reversed_integer = solution(x)

            # Assert
            assert reversed_integer == expected_reverse

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_reverse_integer()
