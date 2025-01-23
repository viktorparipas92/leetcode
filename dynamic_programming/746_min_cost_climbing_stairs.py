"""
746. Min Cost Climbing Stairs
---------------------------------
Difficulty: Easy

You are given an array of integers cost where cost[i] is the cost of taking a step
from the ith floor of a staircase.
After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.

You may choose to start at the index 0 or the index 1 floor.

Return the minimum cost to reach the top of the staircase,
i.e. just past the last index in cost.

Example 1:
Input: cost = [1,2,3]
Output: 2
Explanation: We can start at index = 1 and pay the cost of cost[1] = 2 and take two
steps to reach the top. The total cost is 2.

Example 2:
Input: cost = [1,2,1,2,1,1,1]
Output: 4
Explanation: Start at index = 0.

Pay the cost of cost[0] = 1 and take two steps to reach index = 2.
Pay the cost of cost[2] = 1 and take two steps to reach index = 4.
Pay the cost of cost[4] = 1 and take two steps to reach index = 6.
Pay the cost of cost[6] = 1 and take one step to reach the top.
The total cost is 4.
Constraints:
2 <= cost.length <= 100
0 <= cost[i] <= 100
"""


def min_cost_climbing_stairs_recursion(cost: list[int]) -> int:
    """
    Time complexity: O(2^n), space complexity: O(n)
    """
    def min_cost(i: int) -> int:
        if i >= len(cost):
            return 0

        return cost[i] + min(min_cost(i + 1), min_cost(i + 2))

    return min(min_cost(0), min_cost(1))


def min_cost_climbing_stairs_dynamic_top_down(cost: list[int]) -> int:
    """
    Time complexity: O(n), space complexity: O(n)
    """
    memo = [-1] * len(cost)

    def min_cost(i: int) -> int:
        if i >= len(cost):
            return 0

        if memo[i] != -1:
            return memo[i]

        memo[i] = cost[i] + min(min_cost(i + 1), min_cost(i + 2))
        return memo[i]

    return min(min_cost(0), min_cost(1))


def min_cost_climbing_stairs_dynamic_bottom_up(cost: list[int]) -> int:
    """
    Time complexity: O(n), space complexity: O(n)
    """
    length = len(cost)
    min_cost = [0] * (length + 1)

    for i in range(2, length + 1):
        min_cost[i] = min(
            min_cost[i - 1] + cost[i - 1], min_cost[i - 2] + cost[i - 2]
        )

    return min_cost[length]


def min_cost_climbing_stairs_dynamic_bottom_up_space_optimized(cost: list[int]) -> int:
    """
    Time complexity: O(n), space complexity: O(1)
    """
    length = len(cost)
    # Update the cost array with the minimum cost to reach the top from each step.
    # Start from the third-to-last step because the last two steps do not need updating
    length = len(cost)
    if length == 0:
        return 0
    elif length == 1:
        return cost[0]

    for i in range(2, length):
        cost[i] += min(cost[i - 1], cost[i - 2])

    return min(cost[-1], cost[-2])



def test_min_cost_climbing_stairs():
    solutions = [
        min_cost_climbing_stairs_recursion,
        min_cost_climbing_stairs_dynamic_top_down,
        min_cost_climbing_stairs_dynamic_bottom_up,
        min_cost_climbing_stairs_dynamic_bottom_up_space_optimized,
    ]

    test_cases = [
        ([1, 2, 3], 2),
        ([1, 2, 1, 2, 1, 1, 1], 4),
    ]
    for solution in solutions:
        for cost, expected in test_cases:
            assert solution(cost) == expected
        print(f'{solution.__name__} passed all test cases')


if __name__ == '__main__':
    test_min_cost_climbing_stairs()