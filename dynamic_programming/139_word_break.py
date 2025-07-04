"""
139. Word Break
---------------
Difficulty: Medium

Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times.
You may assume all dictionary words are unique.

Example 1:
Input: s = "neetcode", wordDict = ["neet","code"]
Output: true
Explanation: Return true because "neetcode" can be split into "neet" and "code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen","ape"]
Output: true
Explanation: Return true because "applepenapple" can be split into "apple",
"pen" and "apple". Notice that we can reuse words and also not use all the words.

Example 3:
Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]
Output: false

Constraints:
1 <= s.length <= 200
1 <= wordDict.length <= 100
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
"""


def word_break_recursion(target: str, words: set[str]) -> bool:
    """
    Time complexity: O(t * m^n)
    Space complexity: O(n)
    where
    - n is the length of the target string,
    - m is the number of words in the dictionary,
    - t is the maximum length of a word in the dictionary.
    """
    def depth_first_search(i: int):
        if i == len(target):
            return True

        return any(
            (
                (i + len(word)) <= len(target)
                and target[i: i + len(word)] == word
                and depth_first_search(i + len(word))
            )
            for word in words
        )

    return depth_first_search(i=0)


def word_break_recursion_hash_set(target: str, words: set[str]) -> bool:
    """
    Time complexity: O(n * 2^n + m)
    Space complexity: O(n + t * m)
    where
    - n is the length of the target string,
    - m is the number of words in the dictionary,
    - t is the maximum length of a word in the dictionary.
    """
    def depth_first_search(i: int) -> bool:
        if i == len(target):
            return True

        return any(
            target[i: j + 1] in words and depth_first_search(j + 1)
            for j in range(i, len(target))
        )

    return depth_first_search(i=0)


def word_break_dynamic_top_down(target: str, words: set[str]) -> bool:
    """
    Time complexity: O(n * m * t)
    Space complexity: O(n)
    where
    - n is the length of the target string,
    - m is the number of words in the dictionary,
    - t is the maximum length of a word in the dictionary.
    """
    def depth_first_search(i: int) -> bool:
        if i in can_be_segmented:
            return can_be_segmented[i]

        can_be_segmented[i] = any(
            (
                (i + len(word)) <= len(target)
                and target[i: i + len(word)] == word
                and depth_first_search(i + len(word))
            )
            for word in words
        )
        return can_be_segmented[i]

    can_be_segmented: dict[int, bool] = {len(target): True}
    return depth_first_search(i=0)


def word_break_dynamic_bottom_up(target: str, words: set[str]) -> bool:
    """
    Time complexity: O(n * m * t)
    Space complexity: O(n)
    """
    length = len(target)
    can_be_segmented: list[bool] = [False] * (length + 1)
    can_be_segmented[length] = True

    for i in range(length - 1, -1, -1):
        for word in words:
            if (
                (i + len(word)) <= len(target)
                and target[i: i + len(word)] == word
            ):
                can_be_segmented[i] = can_be_segmented[i + len(word)]

            if can_be_segmented[i]:
                break

    return can_be_segmented[0]

def test_word_break():
    solutions = [
        word_break_recursion,
        word_break_recursion_hash_set,
        word_break_dynamic_top_down,
        word_break_dynamic_bottom_up,
    ]

    test_cases = [
        ('neetcode', {'neet', 'code'}, True),
        ('applepenapple', {'apple', 'pen', 'ape'}, True),
        ('catsincars', {'cats', 'cat', 'sin', 'in', 'car'}, False),
    ]

    for solution in solutions:
        for target, words, expected_can_split in test_cases:
            # Act
            can_split = solution(target, words)

            # Assert
            assert can_split == expected_can_split

        print(f'Tests passed for {solution.__name__}!')

if __name__ == '__main__':
    test_word_break()
