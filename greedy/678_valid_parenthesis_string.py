"""
678. Valid Parenthesis String
-----------------------------
Difficulty: Medium

You are given a string s which contains only three types of characters: '(', ')' and '*'.
Return true if s is valid, otherwise return false.
A string is valid if it follows all the following rules:
- Every left parenthesis '(' must have a corresponding right parenthesis ')'.
- Every right parenthesis ')' must have a corresponding left parenthesis '('.
  Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(
  character, or as an empty string "".

Example 1:
Input: s = "((**)"
Output: true
Explanation: One of the '*' could be a ')' and the other could be an empty string.

Example 2:
Input: s = "(((*)"
Output: false
Explanation: The string is not valid because there is an extra '('
at the beginning, regardless of the extra '*'.

Constraints:
1 <= s.length <= 100
"""


OPENING = '('
CLOSING = ')'
STAR = '*'


def check_valid_string_recursion(string: str) -> bool:
    """
    Time complexity: O(3^n)
    Space complexity: O(n)
    """

    def depth_first_search(i: int, open_count: int) -> bool:
        if open_count < 0:
            return False

        if i == len(string):
            return open_count == 0

        if string[i] == OPENING:
            return depth_first_search(i + 1, open_count + 1)
        elif string[i] == CLOSING:
             return depth_first_search(i + 1, open_count - 1)
        else:
            return (
                depth_first_search(i + 1, open_count)
                or depth_first_search(i + 1, open_count + 1)
                or depth_first_search(i + 1, open_count - 1)
            )

    return depth_first_search(0, 0)


def check_valid_string_stack(string: str) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    opening_indices: list[int] = []
    star_indices: list[int] = []
    for i, char in enumerate(string):
        if char == OPENING:
            opening_indices.append(i)
        elif char == STAR:
            star_indices.append(i)
        else:
            if not opening_indices and not star_indices:
                return False

            if opening_indices:
                opening_indices.pop()
            else:
                star_indices.pop()

    while opening_indices and star_indices:
        if opening_indices.pop() > star_indices.pop():
            return False

    return not opening_indices


def test_check_valid_string():
    solutions = [
        check_valid_string_recursion,
        check_valid_string_stack,
    ]

    test_cases = [
        ('((**)', True),
        ('(((*)', False),
    ]

    for solution in solutions:
        for string, expected_validity in test_cases:
            # Act
            is_valid = solution(string)

            # Assert
            assert is_valid == expected_validity

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_check_valid_string()
