"""
202. Happy Number
-----------------
Difficulty: Easy

A non-cyclical number is an integer defined by the following algorithm:
- Given a positive integer, replace it with the sum of the squares of its digits.
- Repeat the above step until the number equals 1, or it loops infinitely in a cycle
  which does not include 1.
- If it stops at 1, then the number is a non-cyclical number.

Given a positive integer n, return true if it is a non-cyclical number,
otherwise return false.

Example 1:

Input: n = 100
Output: true
Explanation: 1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 101
Output: false
Explanation:
1^2 + 0^2 + 1^2 = 2
2^2 = 4
4^2 = 16
1^2 + 6^2 = 37
3^2 + 7^2 = 58
5^2 + 8^2 = 89
8^2 + 9^2 = 145
1^2 + 4^2 + 5^2 = 42
4^2 + 2^2 = 20
2^2 + 0^2 = 4 (This number has already been seen)

Constraints:
1 <= n <= 1000
"""


def sum_of_squares(n: int) -> int:
    return sum(int(digit) ** 2 for digit in str(n))


def is_happy_number_hash_set(n: int) -> bool:
    """
    Time complexity: O(log n)
    Space complexity: O(log n)
    """
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squares(n)

    return n == 1


def is_happy_number_two_pointers(n: int) -> bool:
    """
    Time complexity: O(log n)
    Space complexity: O(1)
    """
    slow, fast = n, sum_of_squares(n)
    while slow != fast:
        fast = sum_of_squares(fast)
        fast = sum_of_squares(fast)
        slow = sum_of_squares(slow)

    return fast == 1


def test_is_happy_number():
    # Arrange
    solutions = [
        is_happy_number_hash_set,
        is_happy_number_two_pointers,
    ]

    test_cases = [
        (100, True),
        (101, False),
        (19, True),
        (2, False),
    ]

    for solution in solutions:
        for n, expected_is_happy in test_cases:
            # Act
            is_happy = solution(n)
            # Assert
            assert is_happy == expected_is_happy

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_is_happy_number()