"""
128. Longest Consecutive Sequence
-------------------------------
Difficulty: Medium

Given an unsorted array of integers nums, return the length of the
longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


def longest_consecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest_streak = 0

    for number in num_set:
        if number - 1 in num_set:  # Skip if number is not the start of sequence
            continue

        current_number, current_streak = number, 1
        while current_number + 1 in num_set:
            current_number += 1
            current_streak += 1

        longest_streak = max(longest_streak, current_streak)

    return longest_streak


def test_longest_consecutive():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


if __name__ == '__main__':
    test_longest_consecutive()
