"""
3. Longest Substring Without Repeating Characters
------------------------------------------------
Difficulty: Medium

Given a string s, find the length of the longest substring without repeating
characters.
"""


def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    max_length = 0
    start = 0

    for end_index, char in enumerate(s):
        if char in char_index_map:
            start_index = max(start_index, char_index_map[char] + 1)

        char_index_map[char] = end_index
        max_length = max(max_length, end_index - start_index + 1)

    return max_length


def test_length_of_longest_substring():
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3


if __name__ == '__main__':
    test_length_of_longest_substring()