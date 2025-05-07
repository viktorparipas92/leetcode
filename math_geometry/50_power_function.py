"""
50. Power Function
------------------
Difficulty: Medium

Pow(x, n) is a mathematical function to
calculate the value of x raised to the power of n (i.e., x^n).
Given a floating-point value x and an integer value n,
implement the myPow(x, n) function, which calculates x raised to the power n.
You may not use any built-in library functions.

Example 1:
Input: x = 2.00000, n = 5
Output: 32.00000

Example 2:
Input: x = 1.10000, n = 10
Output: 2.59374

Example 3:
Input: x = 2.00000, n = -3
Output: 0.12500

Constraints:
-100.0 < x < 100.0
-1000 <= n <= 1000
n is an integer.
If x = 0, then n will be positive.
"""


def my_pow_brute_force(x: float, n: int) -> float:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if x == 0:
        return 0
    elif n == 0:
        return 1

    result = 1
    for _ in range(abs(n)):
        result *= x

    return result if n >= 0 else 1 / result


def my_pow_recursive_binary_exponentiation(x: float, n: int) -> float:
    """
    Time complexity: O(log n)
    Space complexity: O(1)
    """

    def helper(x: float, n: int) -> float:
        if x == 0:
            return 0
        elif n == 0:
            return 1

        _result = helper(x * x, n // 2)
        return x * _result if n % 2 else _result

    result = helper(x, abs(n))
    return result if n >= 0 else 1 / result


def my_pow_iterative_binary_exponentiation(x: float, n: int) -> float:
    """
    Time complexity: O(log n)
    Space complexity: O(1)
    """
    if x == 0:
        return 0
    elif n == 0:
        return 1

    result = 1
    power = abs(n)
    while power:
        if power & 1:  # Check if the last bit is 1
            result *= x

        x *= x
        power >>= 1  # Right shift to divide by 2

    return result if n >= 0 else 1 / result


def test_my_pow():
    solutions = [
        my_pow_brute_force,
        my_pow_recursive_binary_exponentiation,
        my_pow_iterative_binary_exponentiation,
    ]

    test_cases = [
        (2.00000, 5, 32.00000),
        (1.10000, 10, 2.59374),
        (2.00000, -3, 0.12500),
    ]

    for solution in solutions:
        for base, exponent, expected_result in test_cases:
            # Act
            result = solution(base, exponent)

            # Assert
            assert abs(result - expected_result) < 1e-5

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_my_pow()
