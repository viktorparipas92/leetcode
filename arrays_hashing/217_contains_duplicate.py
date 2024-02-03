"""
217. Contains Duplicate
-----------------------
Difficulty: Easy
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.
"""


def contains_duplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


def test_contains_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) == True
    assert contains_duplicate([1, 2, 3, 4]) == False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True


if __name__ == "__main__":
    test_contains_duplicate()