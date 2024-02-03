"""
242. Valid Anagram
------------------
Difficulty: Easy
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""


def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def test_is_anagram():
    assert is_anagram('anagram', 'nagaram') == True
    assert is_anagram('rat', 'car') == False


if __name__ == '__main__':
    test_is_anagram()
