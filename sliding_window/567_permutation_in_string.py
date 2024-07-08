"""
567. Permutation in String
---------------------------
Difficulty: Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1,
or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""

from collections import Counter


def check_inclusion(substring: str, container: str) -> bool:
    len_substring = len(substring)
    len_container = len(container)
    if len_substring > len_container:
        return False

    substring_count = Counter(substring)
    container_count = Counter(container[:len_substring])
    if substring_count == container_count:
        return True

    for i in range(len_substring, len_container):
        container_count[container[i]] += 1
        container_count[container[i - len_substring]] -= 1
        if container_count[container[i - len_substring]] == 0:
            del container_count[container[i - len_substring]]

        if substring_count == container_count:
            return True

    return False


def test_check_inclusion():
    assert check_inclusion('ab', 'eidbaooo') is True
    assert check_inclusion('ab', 'eidboaoo') is False
    assert check_inclusion('abc', 'lecaabee') is False


if __name__ == '__main__':
    test_check_inclusion()