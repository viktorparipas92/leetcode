"""
322. Coin Change
----------------
Difficulty: Medium

You are given an integer array coins representing coins of different denominations
(e.g. 1 dollar, 5 dollars, etc)
and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount.
If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.

Example 1:
Input: coins = [1,5,10], amount = 12
Output: 3
Explanation: 12 = 10 + 1 + 1. Note that we do not have to use every kind coin available.

Example 2:
Input: coins = [2], amount = 3
Output: -1
Explanation: The amount of 3 cannot be made up with coins of 2.

Example 3:
Input: coins = [1], amount = 0
Output: 0
Explanation: Choosing 0 coins is a valid way to make up 0.

Constraints:
1 <= coins.length <= 10
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10000
"""


def coin_change_recursion(coins: list[int], amount: int) -> int:
    """
    Time complexity: O(n * t)
    Space complexity: O(t)
    where n is the number of coins and t is the target amount.
    """

    def depth_first_search(_amount: int) -> int:
        if _amount == 0:
            return 0

        num_coins = 1e9  # Use a large number to represent infinity
        for coin in coins:
            if _amount >= coin:
                num_coins = min(num_coins, 1 + depth_first_search(_amount - coin))

        return num_coins

    min_num_coins = depth_first_search(amount)
    return -1 if min_num_coins >= 1e9 else min_num_coins


def test_coin_change():
    solutions = [
        coin_change_recursion,
    ]

    test_cases = [
        ([1, 5, 10], 12, 3),
        ([2], 3, -1),
        ([1], 0, 0),
    ]

    for solution in solutions:
        for coins, amount, expected_num_coins in test_cases:
            # Act
            num_coins = solution(coins, amount)

            # Assert
            assert num_coins == expected_num_coins

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_coin_change()
