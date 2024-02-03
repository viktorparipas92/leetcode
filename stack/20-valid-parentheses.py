"""
20. Valid Parentheses
---------------------
Difficulty: Easy
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every opening bracket must have a corresponding closing bracket.
"""


def is_valid(s: str) -> bool:
    PAIRS = {
        0: None,
        '(': ')',
        '[': ']',
        '{': '}',
    }
    stack = [0]

    for char in s:
        if opening := char in PAIRS:
            stack.append(char)
        else:
            if PAIRS[stack.pop()] != char:
                return False

    return stack == [0]


def test_is_valid():
    assert is_valid('()') == True
    assert is_valid('()[]{}') == True
    assert is_valid('(]') == False
    assert is_valid('([)]') == False
    assert is_valid('{[]}') == True
    assert is_valid('') == True
    assert is_valid('[') == False
    assert is_valid(']') == False
    assert is_valid('((') == False
    assert is_valid('))') == False
    assert is_valid('(([]){})') == True
    assert is_valid('(([]){})(') == False


if __name__ == '__main__':
    test_is_valid()