"""
91. Decode Ways
---------------
Difficulty: Medium

A string consisting of uppercase english characters can be encoded to a number using
the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode a message, digits must be grouped and then mapped back into letters using
the reverse of the mapping above. There may be multiple ways to decode a message.
For example, "1012" can be mapped into:
"JAB" with the grouping (10 1 2)
"JL" with the grouping (10 12)
The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it
contains a leading zero.

Given a string s containing only digits, return the number of ways to decode it.
You can assume that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "01"
Output: 0
Explanation: "01" cannot be decoded because "01" cannot be mapped into a letter.

Constraints:
1 <= s.length <= 100
s consists of digits
"""


def num_decodings_recursion(message: str) -> int:
    """
    Time complexity: O(2^n)
    Space complexity: O(n)
    """

    def depth_first_search(i: int) -> int:
        if i == len(message):
            return 1

        if message[i] == '0':
            return 0

        num_ways_to_decode = depth_first_search(i + 1)
        if can_be_double_digit(message, i):
            num_ways_to_decode += depth_first_search(i + 2)

        return num_ways_to_decode

    return depth_first_search(0)


def num_decodings_dynamic_top_down(message: str) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def depth_first_search(i: int) -> int:
        if i in num_ways_to_decode_lookup:
            return num_ways_to_decode_lookup[i]

        if message[i] == '0':
            return 0

        num_ways_to_decode = depth_first_search(i + 1)
        if can_be_double_digit(message, i):
            num_ways_to_decode += depth_first_search(i + 2)

        num_ways_to_decode_lookup[i] = num_ways_to_decode
        return num_ways_to_decode

    num_ways_to_decode_lookup: dict[int, int] = {len(message): 1}
    return depth_first_search(0)


def num_decodings_dynamic_bottom_up(message: str) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    num_ways_to_decode_lookup: dict[int, int] = {len(message): 1}
    for i in range(len(message) - 1, -1, -1):
        if message[i] == '0':
            num_ways_to_decode_lookup[i] = 0
        else:
            num_ways_to_decode_lookup[i] = num_ways_to_decode_lookup[i + 1]

        if can_be_double_digit(message, i):
            num_ways_to_decode_lookup[i] += num_ways_to_decode_lookup[i + 2]

    return num_ways_to_decode_lookup[0]


def num_decodings_dynamic_bottom_up_optimized(message: str) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    next_ways = 1
    next_next_ways = 0
    for i in range(len(message) - 1, -1, -1):
        if message[i] == '0':
            current_ways = 0
        else:
            current_ways = next_ways

        if can_be_double_digit(message, i):
            current_ways += next_next_ways

        current_ways, next_ways, next_next_ways = 0, current_ways, next_ways

    return next_ways


def can_be_double_digit(message: str, i: int) -> bool:
    char1 = message[i]
    try:
        char2 = message[i + 1]
        return char1 == '1' or (char1 == '2' and char2 < '7')
    except IndexError:
        return False


def test_num_decodings():
    solutions = [
        num_decodings_recursion,
        num_decodings_dynamic_top_down,
        num_decodings_dynamic_bottom_up,
        num_decodings_dynamic_bottom_up_optimized,
    ]

    test_cases = [
        ('12', 2),
        ('01', 0),
        ('226', 3),
    ]

    for solution in solutions:
        for message, expected_count in test_cases:
            # Act
            count = solution(message)

            # Assert
            assert count == expected_count

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_num_decodings()
