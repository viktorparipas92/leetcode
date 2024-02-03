"""
125. Valid Palindrome
---------------------
Difficulty: Easy

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

import re


def is_palindrome(s: str) -> bool:
    non_alphanumeric_pattern = re.compile('[\W_]+', re.UNICODE)
    cleaned_string = non_alphanumeric_pattern.sub('', s).lower()
    return cleaned_string == cleaned_string[::-1]


def test_is_palindrome():
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('race a car') == False
    assert is_palindrome(' ') == True
    assert is_palindrome('ab_a') == True


if __name__ == '__main__':
    test_is_palindrome()