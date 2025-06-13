"""
763. Partition Labels
---------------------
Difficulty: Medium

You are given a string s consisting of lowercase english letters.
We want to split the string into as many substrings as possible,
while ensuring that each letter appears in at most one substring.

Return a list of integers representing the size of these substrings in the order they appear in the string.

Example 1:
Input: s = "xyxxyzbzbbisl"
Output: [5, 5, 1, 1, 1]
Explanation: The string can be split into ["xyxxy", "zbzbb", "i", "s", "l"].

Example 2:
Input: s = "abcabc"
Output: [6]

Constraints:
1 <= s.length <= 100
"""


def partition_labels_two_pointers_greedy(word: str) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(m)
    where n is the length of the string and m is the number of unique characters.
    """
    last_index: dict[str, int] = {char: idx for idx, char in enumerate(word)}

    partitions: list[int] = []
    partition_size: int = 0
    end_index: int = 0
    for idx, char in enumerate(word):
        partition_size += 1
        end_index = max(end_index, last_index[char])

        if idx == end_index:
            partitions.append(partition_size)
            partition_size = 0

    return partitions


def test_partition_labels():
    solutions = [
        partition_labels_two_pointers_greedy,
    ]

    test_cases = [
        ('xyxxyzbzbbisl', [5, 5, 1, 1, 1]),
        ('abcabc', [6]),
    ]

    for solution in solutions:
        for word, expected_partition_sizes in test_cases:
            # Act
            partition_sizes = solution(word)

            # Assert
            assert partition_sizes == expected_partition_sizes

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_partition_labels()
