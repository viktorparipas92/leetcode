"""
1929. Concatenation of Array
---------------------------
Difficulty: Easy
Given an integer array nums of length n, you want to create an array ans
of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i]
for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.
Return the array ans.
"""


def get_concatenation(nums: list[int]) -> list[int]:
    return nums + nums


def test_get_concatenation():
    assert get_concatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert get_concatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]


if __name__ == '__main__':
    test_get_concatenation()