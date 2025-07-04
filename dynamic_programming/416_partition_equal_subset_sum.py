"""
416. Partition Equal Subset Sum
-------------------------------
Difficulty: Medium

You are given an array of positive integers nums.
Return true if you can partition the array into two subsets,
subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

Example 1:
Input: nums = [1,2,3,4]
Output: true
Explanation: The array can be partitioned as [1, 4] and [2, 3].

Example 2:
Input: nums = [1,2,3,4,5]
Output: false

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 50
"""


def can_partition_recursion(numbers: list[int]) -> bool:
    """
    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    def depth_first_search(i: int, target: int) -> bool:
        if i >= len(numbers):
            return target == 0

        if target < 0:
            return False

        return (
            depth_first_search(i + 1, target)
            or depth_first_search(i + 1, target - numbers[i])
        )

    total: int = sum(numbers)
    if total % 2:
        return False

    return depth_first_search(i=0, target=total // 2)


def test_can_partition():
    solutions = [
        can_partition_recursion,
    ]

    test_cases = [
        ([1, 2, 3, 4], True),
        ([1, 2, 3, 4, 5], False),
    ]

    for solution in solutions:
        for numbers, expected_can_partition in test_cases:
            # Act
            can_partition = solution(numbers)

            # Assert
            assert can_partition == expected_can_partition

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_can_partition()
