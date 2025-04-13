"""
17. Letter Combinations of a Phone Number
-----------------------------------------
Difficulty: Medium

You are given a string digits made up of digits from 2 through 9 inclusive.
Each digit (not including 1) is mapped to a set of characters as shown below:
A digit could represent any one of the characters it maps to.
Return all possible letter combinations that digits could represent.
You may return the answer in any order.

Example 1:
Input: digits = "34"
Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]

Example 2:
Input: digits = ""
Output: []
Constraints:

0 <= digits.length <= 4
2 <= digits[i] <= 9
"""

DIGIT_TO_CHAR_MAPPING = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def letter_combinations_backtracking(digits: str) -> list[str]:
    """
    Time complexity: O(n * 4^n)
    Space complexity: O(n) extra space
    """
    def backtrack(i: int, current_string: str):
        if len(current_string) == len(digits):
            combinations.append(current_string)
            return

        digit = digits[i]
        for char in DIGIT_TO_CHAR_MAPPING[digit]:
            backtrack(i + 1, current_string + char)

    combinations: list[str] = []
    if digits:
        backtrack(i=0, current_string='')

    return combinations


def letter_combinations_iterative(digits: str) -> list[str]:
    """
    Time complexity: O(n * 4^n)
    Space complexity: O(n) extra space
    """
    if not digits:
        return []

    combinations: list[str] = ['']
    for digit in digits:
        temp: list[str] = []
        for combination in combinations:
            for char in DIGIT_TO_CHAR_MAPPING[digit]:
                temp.append(combination + char)

        combinations = temp

    return combinations


def test_letter_combinations():
    solutions = [
        letter_combinations_backtracking,
        letter_combinations_iterative,
    ]

    test_cases = [
        ('', []),
        ('23', ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
        ('34', ['dg', 'dh', 'di', 'eg', 'eh', 'ei', 'fg', 'fh', 'fi']),
    ]

    for solution in solutions:
        for digits, expected_combinations in test_cases:
            # Act
            combinations = solution(digits)

            # Assert
            assert sorted(combinations) == sorted(expected_combinations)

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_letter_combinations()
