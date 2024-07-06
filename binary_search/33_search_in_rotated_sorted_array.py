"""
33. Search in Rotated Sorted Array
-----------------------------------
Difficulty: Medium

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an
unknown pivot index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

def search(nums: list[int], target: int) -> int:
    # Find the pivot
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    pivot = left

    # Determine which half of the array to search
    if nums[pivot] <= target <= nums[-1]:
        left, right = pivot, len(nums) - 1
    else:
        left, right = 0, pivot

    # Binary search
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def test_search():
    input_1 = [3, 4, 5, 6, 1, 2]
    assert search(input_1, 4) == 1

    input_2 = [3, 5, 6, 0, 1, 2]
    assert search(input_2, 4) == -1


if __name__ == '__main__':
    test_search()