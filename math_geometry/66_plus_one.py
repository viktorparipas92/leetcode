"""
66. Plus One
-------------
Difficulty: Easy

You are given an integer array digits, where each digits[i] is the ith digit of a
large integer. It is ordered from most significant to least significant digit,
and it will not contain any leading zero.

Return the digits of the given integer after incrementing it by one.

Example 1:
Input: digits = [1,2,3,4]
Output: [1,2,3,5]
Explanation 1234 + 1 = 1235.

Example 2:
Input: digits = [9,9,9]
Output: [1,0,0,0]
Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
"""


def plus_one(digits: list[int]) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    as_string = ''.join(map(str, digits))
    incremented = str(int(as_string) + 1)
    return [int(digit) for digit in incremented]


def plus_one_recursion(digits: list[int]) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if not digits:
        return [1]

    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    else:
        return plus_one_recursion(digits[:-1]) + [0]


def test_plus_one():
    solutions = [
        plus_one,
        plus_one_recursion,
    ]

    test_cases = [
        ([1, 2, 3, 4], [1, 2, 3, 5]),
        ([9, 9, 9], [1, 0, 0, 0]),
    ]

    for solution in solutions:
        for digits, expected_incremented in test_cases:
            assert solution(digits) == expected_incremented

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_plus_one()
