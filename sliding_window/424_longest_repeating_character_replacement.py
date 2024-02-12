'''
424. Longest Repeating Character Replacement
--------------------------------------------
Difficulty: Medium

You are given a string s and an integer k.
You can choose any character of the string and change it to any other
uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter
you can get after performing the above operations.
'''
from collections import defaultdict


def character_replacement(word: str, k: int) -> int:
    char_count = defaultdict(int)
    left_idx = 0
    max_count = 0
    for right_idx, char in enumerate(word):
        char_count[char] += 1
        max_count = max(max_count, char_count[char])
        characters_left_to_change = right_idx - left_idx + 1 - max_count
        if characters_left_to_change > k:
            char_count[word[left_idx]] -= 1
            left_idx += 1

    return right_idx - left_idx + 1


def test_character_replacement():
    assert character_replacement('ABAB', 2) == 4
    assert character_replacement('AABABBA', 1) == 4


if __name__ == '__main__':
    test_character_replacement()
