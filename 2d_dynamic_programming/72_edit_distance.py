"""
72. Edit Distance
-----------------
Difficulty: Medium

You are given two strings word1 and word2, each consisting of lowercase English letters.
You are allowed to perform three operations on word1 an unlimited number of times:
- Insert a character at any position
- Delete a character at any position
- Replace a character at any position

Return the minimum number of operations to make word1 equal word2.

Example 1:
Input: word1 = "monkeys", word2 = "money"
Output: 2
Explanation:
monkeys -> monkey (remove s)
monkey -> money (remove k)

Example 2:
Input: word1 = "neatcdee", word2 = "neetcode"
Output: 3
Explanation:
neatcdee -> neetcdee (replace a with e)
neetcdee -> neetcde (remove last e)
neetcde -> neetcode (insert o)

Constraints:
0 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""


def min_distance_recursion(word1: str, word2: str) -> int:
    """
    Time complexity: O(3^(m+n))
    Space complexity: O(m+n)
    where m and n are the lengths of word1 and word2 respectively.
    """
    def depth_first_search(i: int, j: int) -> int:
        if i == length_1:
            return length_2 - j
        elif j == length_2:
            return length_1 - i
        elif word1[i] == word2[j]:
            return depth_first_search(i + 1, j + 1)

        distance: int = min(
            depth_first_search(i + 1, j),
            depth_first_search(i, j + 1),
            depth_first_search(i + 1, j + 1),
        )
        return distance + 1

    length_1, length_2 = len(word1), len(word2)
    return depth_first_search(0, 0)


def test_min_distance():
    solutions = [
        min_distance_recursion,
    ]

    test_cases = [
        ('monkeys', 'money', 2),
        ('neatcdee', 'neetcode', 3),
    ]

    for solution in solutions:
        for word1, word2, expected_min_distance in test_cases:
            # Act
            min_distance = solution(word1, word2)

            # Assert
            assert min_distance == expected_min_distance

        print(f'{solution.__name__} passed all tests')


if __name__ == '__main__':
    test_min_distance()
