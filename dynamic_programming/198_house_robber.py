"""
198. House Robber
-----------------
Difficulty: Medium

You are given an integer array nums where nums[i] represents the amount of money the
ith house has. The houses are arranged in a straight line,
i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses
because the security system will automatically alert the police if two adjacent houses
were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:
Input: nums = [1,1,3,3]
Output: 4
Explanation: nums[0] + nums[2] = 1 + 3 = 4.

Example 2:
Input: nums = [2,9,8,3,6]
Output: 16
Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""


def rob_recursive(houses: list[int]) -> int:
    """
    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    def depth_first_search(i: int) -> int:
        if i >= len(houses):
            return 0

        return max(
            depth_first_search(i + 1),
            houses[i] + depth_first_search(i + 2),
        )

    return depth_first_search(i=0)


def rob_dynamic_top_down(houses: list[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def depth_first_search(i: int) -> int:
        if i >= len(houses):
            return 0

        if haul[i] != -1:
            return haul[i]

        haul[i] = max(
            depth_first_search(i + 1),
            houses[i] + depth_first_search(i + 2),
        )
        return haul[i]

    haul: list[int] = [-1] * len(houses)
    return depth_first_search(i=0)


def rob_dynamic_bottom_up(houses: list[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if not houses:
        return 0
    elif len(houses) == 1:
        return houses[0]

    haul: list[int] = [0] * len(houses)
    haul[0] = houses[0]
    haul[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        haul[i] = max(haul[i - 1], houses[i] + haul[i - 2])

    return haul[-1]


def rob_dynamic_bottom_up_optimized(houses: list[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    haul_1 = haul_2 = 0
    for house in houses:
        temp = max(house + haul_1, haul_2)
        haul_1 = haul_2
        haul_2 = temp

    return haul_2


def test_rob():
    solutions = [
        rob_recursive,
        rob_dynamic_top_down,
        rob_dynamic_bottom_up,
        rob_dynamic_bottom_up_optimized,
    ]

    test_cases = [
        ([1, 1, 3, 3], 4),
        ([2, 9, 8, 3, 6], 16),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
        ([1], 1),
        ([0], 0),
        ([100], 100),
    ]

    for solution in solutions:
        for houses, expected_haul in test_cases:
            # Act
            haul = solution(houses)

            # Assert
            assert haul == expected_haul

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_rob()
