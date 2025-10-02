"""
97. Interleaving String
-----------------------------
Difficulty: Medium

You are given three strings s1, s2, and s3.
Return true if s3 is formed by interleaving s1 and s2 together or false otherwise.

Interleaving two strings s and t is done by dividing s and t into
n and m substrings respectively, where the following conditions are met
- |n - m| <= 1, i.e. the difference between the number of substrings of s and t is at most 1.
- s = s1 + s2 + ... + sn
- t = t1 + t2 + ... + tm
- Interleaving s and t is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...

You may assume that s1, s2 and s3 consist of lowercase English letters.

Example 1:
Input: s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"
Output: true
Explanation: We can split s1 into ["aa", "aa"], s2 can remain as "bbbb" and s3 is formed by interleaving ["aa", "aa"] and "bbbb".

Example 2:
Input: s1 = "", s2 = "", s3 = ""
Output: true

Example 3:
Input: s1 = "abc", s2 = "xyz", s3 = "abxzcy"
Output: false
Explanation: We can't split s3 into ["ab", "xz", "cy"] as the order of characters is not maintained.

Constraints:
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
"""
from collections import defaultdict


def is_interleave_recursion(part_1: str, part_2: str, target: str) -> bool:
    """
    Time complexity: O(2^(m+n))
    Space complexity: O(m+n)
    where m and n are the lengths of part_1 and part_2 respectively.
    """
    def depth_first_search(i: int, j: int, k: int) -> bool:
        if k == len(target):
            return i == len(part_1) and j == len(part_2)

        if i < len(part_1) and part_1[i] == target[k]:
            if depth_first_search(i + 1, j, k + 1):
                return True

        if j < len(part_2) and part_2[j] == target[k]:
            if depth_first_search(i, j + 1, k + 1):
                return True

        return False

    return depth_first_search(i=0, j=0, k=0)


def is_interleave_dynamic_top_down(part_1: str, part_2: str, target: str) -> bool:
    """
    Time complexity: O(m * n)
    Space complexity: O(m * n)
    """
    def depth_first_search(i: int, j: int, k: int) -> bool:
        if k == len(target):
            return (i == len(part_1)) and (j == len(part_2))
        elif (i, j) in is_interleaving_map:
            return is_interleaving_map[(i, j)]

        is_interleaving = False
        if i < len(part_1) and part_1[i] == target[k]:
            is_interleaving = depth_first_search(i + 1, j, k + 1)

        if not is_interleaving and j < len(part_2) and part_2[j] == target[k]:
            is_interleaving = depth_first_search(i, j + 1, k + 1)

        is_interleaving_map[(i, j)] = is_interleaving
        return is_interleaving

    if len(part_1) + len(part_2) != len(target):
        return False

    is_interleaving_map: dict[tuple[int, int], bool] = {}
    return depth_first_search(i=0, j=0, k=0)


def test_is_interleave():
    solutions = [
        is_interleave_recursion,
        is_interleave_dynamic_top_down,
    ]

    test_cases = [
        ('aaaa', 'bbbb', 'aabbbbaa', True),
        ('', '', '', True),
        ('abc', 'xyz', 'abxzcy', False),
    ]

    for solution in solutions:
        for part_1, part_2, target, expected_is_interleaved in test_cases:
            # Act
            is_interleaved = solution(part_1, part_2, target)

            # Assert
            assert is_interleaved == expected_is_interleaved

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_is_interleave()
