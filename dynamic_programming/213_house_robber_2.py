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


def test_rob():
    solutions = [
        rob_recursion,
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
