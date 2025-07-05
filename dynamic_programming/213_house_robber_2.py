"""
213. House Robber II
--------------------
Difficulty: Medium

You are given an integer array nums where nums[i] represents the amount of money
the ith house has. The houses are arranged in a circle,
i.e. the first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent houses
because the security system will automatically alert the police
if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:
Input: nums = [3,4,3]
Output: 4
Explanation: You cannot rob nums[0] + nums[2] = 6
because nums[0] and nums[2] are adjacent houses. The maximum you can rob is nums[1] = 4.

Example 2:
Input: nums = [2,9,8,3,6]
Output: 15
Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16
because nums[0] and nums[4] are adjacent houses.
The maximum you can rob is nums[1] + nums[4] = 15.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""


def rob_recursion(numbers: list[int]) -> int:
    """
    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    def depth_first_search(i: int, flag: bool) -> int:
        """
        Depth-first search to find the maximum amount of money that can be robbed.
        :param i: current index in the numbers list
        :param flag: indicates whether the first house has been robbed
        :return: maximum amount of money that can be robbed
        """
        if i >= size or (flag and i == size - 1):
            return 0

        return max(
            depth_first_search(i + 1, flag),
            numbers[i] + depth_first_search(i + 2, flag or i == 0)
        )

    size = len(numbers)
    if size == 1:
        return numbers[0]

    return max(
        depth_first_search(i=0, flag=True),
        depth_first_search(i=1, flag=False),
    )


def rob_dynamic_top_down(numbers: list[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def depth_first_search(i: int, flag: bool) -> int:
        if i >= size or (flag and i == size - 1):
            return 0

        if memo[i][flag] != -1:
            return memo[i][flag]

        memo[i][flag] = max(
            depth_first_search(i + 1, flag),
            numbers[i] + depth_first_search(i + 2, flag or (i == 0))
        )
        return memo[i][flag]

    size = len(numbers)
    if size == 1:
        return numbers[0]

    # Initialize memoization table
    # Two dimensions: one for index and one for the flag (robbed first house or not)
    memo: list[list[int]] = [[-1, -1] for _ in range(size)]

    return max(
        depth_first_search(i=0, flag=True),
        depth_first_search(i=1, flag=False),
    )


def rob_dynamic_bottom_up(numbers: list[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def helper(nums: list[int]) -> int:
        if not nums:
            return 0

        remaining_size = len(nums)
        if remaining_size == 1:
            return nums[0]

        max_robbed: list[int] = [0] * remaining_size
        max_robbed[0] = nums[0]
        max_robbed[1] = max(nums[0], nums[1])
        for i in range(2, remaining_size):
            max_robbed[i] = max(max_robbed[i - 1], nums[i] + max_robbed[i - 2])

        return max_robbed[-1]

    size = len(numbers)
    if size == 1:
        return numbers[0]

    return max(helper(numbers[1:]), helper(numbers[:-1]))


def rob_dynamic_bottom_up_optimized(numbers: list[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def helper(nums):
        """
        Helper function to calculate the maximum amount of money that can be robbed
        from a linear list of houses.
        """
        rob1: int = 0
        rob2: int = 0
        for number in nums:
            new_rob = max(rob1 + number, rob2)
            rob1 = rob2
            rob2 = new_rob

        return rob2

    return max(numbers[0], helper(numbers[1:]), helper(numbers[:-1]))


def test_rob():
    solutions = [
        rob_recursion,
        rob_dynamic_top_down,
        rob_dynamic_bottom_up,
        rob_dynamic_bottom_up_optimized,
    ]

    test_cases = [
        ([3, 4, 3], 4),
        ([2, 9, 8, 3, 6], 15),
    ]

    for solution in solutions:
        for numbers, expected_maximum_robbed in test_cases:
            # Act
            maximum_robbed = solution(numbers)

            # Assert
            assert maximum_robbed == expected_maximum_robbed

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_rob()
