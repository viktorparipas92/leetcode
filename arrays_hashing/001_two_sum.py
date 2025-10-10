"""
1. Two Sum
----------
Difficulty: Easy
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.
"""


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    num_to_index = {}
    for i, number in enumerate(nums):
        complement = target - number
        if complement in num_to_index:
            return num_to_index[complement], i

        num_to_index[number] = i

    return None


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([3, 2, 4], 6) == (1, 2)
    assert two_sum([3, 3], 6) == (0, 1)


if __name__ == '__main__':
    test_two_sum()