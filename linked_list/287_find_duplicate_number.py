"""
287. Find the Duplicate Number
--------------------------------
Difficulty: Medium

You are given an array of integers nums containing n + 1 integers.
Each integer in nums is in the range [1, n] inclusive.

Every integer appears exactly once, except for one integer which appears
two or more times. Return the integer that appears more than once.

Example 1:
Input: nums = [1,2,3,2,2]
Output: 2

Example 2:
Input: nums = [1,2,3,4,4]
Output: 4

Follow-up: Can you solve the problem without modifying the array nums and using
O(1) extra space?

Constraints:
1 <= n <= 10000
nums.length == n + 1
1 <= nums[i] <= n
"""


def find_duplicate_with_sorting(nums: list[int]) -> int:
    """Time complexity: O(n * log(n)), space complexity: O(1)"""
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]


def find_duplicate_with_hash_set(nums: list[int]) -> int:
    """Time complexity: O(n), space complexity: O(n)"""
    seen = set()
    for number in nums:
        if number in seen:
            return number
        else:
            seen.add(number)

    return -1


def find_duplicate_with_array(nums: list[int]) -> int:
    """Time complexity: O(n), space complexity: O(n)"""
    seen = [0] * len(nums)
    for number in nums:
        if seen[number - 1]:
            return number
        else:
            seen[number - 1] = 1

    return -1


def find_duplicate_with_negative_marking(nums: list[int]) -> int:
    """Time complexity: O(n), space complexity: O(1)"""
    for number in nums:
        index = abs(number) - 1
        if nums[index] < 0:
            return abs(number)
        else:
            nums[index] *= -1

    return -1


def find_duplicate_with_fast_and_slow_pointer(nums: list[int]) -> int:
    """Time complexity: O(n), space complexity: O(1)"""
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow_2 = 0
    while True:
        slow = nums[slow]
        slow_2 = nums[slow_2]
        if slow == slow_2:
            return slow


def test_solution():
    nums = [1, 2, 3, 2, 2]
    assert find_duplicate_with_sorting(nums) == 2
    assert find_duplicate_with_hash_set(nums) == 2
    assert find_duplicate_with_array(nums) == 2
    assert find_duplicate_with_negative_marking(nums) == 2
    assert find_duplicate_with_fast_and_slow_pointer(nums) == 2

    nums = [1, 2, 3, 4, 4]
    assert find_duplicate_with_sorting(nums) == 4
    assert find_duplicate_with_hash_set(nums) == 4
    assert find_duplicate_with_array(nums) == 4
    assert find_duplicate_with_negative_marking(nums) == 4
    assert find_duplicate_with_fast_and_slow_pointer(nums) == 4


if __name__ == '__main__':
    test_solution()

