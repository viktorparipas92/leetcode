"""
518. Coin Change 2
-----------------------
Difficulty: Medium

You are given an integer array coins representing coins of different denominations
(e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target
amount of money.

Return the number of distinct combinations that total up to amount.
If it's impossible to make up the amount, return 0.

You may assume that you have an unlimited number of each coin
and that each value in coins is unique.

Example 1:
Input: amount = 4, coins = [1,2,3]
Output: 4
Explanation:
1+1+1+1 = 4
1+1+2 = 4
2+2 = 4
1+3 = 4

Example 2:
Input: amount = 7, coins = [2,4]
Output: 0

Constraints:
1 <= coins.length <= 100
1 <= coins[i] <= 5000
0 <= amount <= 5000
"""


def change_recursion(amount: int, coins: list[int]) -> int:
    """
    Time complexity: O(2^(max(n, a/m)))
    Space complexity: O(max(n, a/m))
    where n is the number of coins, a is the amount, and m is the minimum coin denomination.
    """
    coins.sort()

    def depth_first_search(i, _amount: int) -> int:
        if _amount == 0:
            return 1
        elif i >= len(coins):
            return 0

        num_combinations: int = 0
        if _amount >= coins[i]:
            num_combinations = depth_first_search(i + 1, _amount)
            num_combinations += depth_first_search(i, _amount - coins[i])

        return num_combinations

    return depth_first_search(i=0, _amount=amount)


def change_dynamic_top_down(amount: int, coins: list[int]) -> int:
    """
    Time complexity: O(n * a)
    Space complexity: O(n * a)
    where n is the number of coins and a is the amount.
    """
    coins.sort()
    memory: list[list[int]] = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

    def depth_first_search(i: int, _amount: int) -> int:
        if _amount == 0:
            return 1
        elif i >= len(coins):
            return 0
        elif memory[i][_amount] != -1:
            return memory[i][_amount]

        num_combinations: int = 0
        if _amount >= coins[i]:
            num_combinations = depth_first_search(i + 1, _amount)
            num_combinations += depth_first_search(i, _amount - coins[i])

        memory[i][_amount] = num_combinations
        return num_combinations

    return depth_first_search(0, amount)


def change_dynamic_bottom_up(amount: int, coins: list[int]) -> int:
    """
    Time complexity: O(n * a)
    Space complexity: O(n * a)
    where n is the number of coins and a is the amount.
    """
    num_different_coins = len(coins)
    coins.sort()
    num_combinations: list[list[int]] = [[0] * (amount + 1) for _ in range(num_different_coins + 1)]

    for i in range(num_different_coins + 1):
        num_combinations[i][0] = 1

    for i in range(num_different_coins - 1, -1, -1):  # iterate coins in reverse order
        for _amount in range(amount + 1):
            if _amount >= coins[i]:
                num_combinations[i][_amount] = num_combinations[i + 1][_amount]
                num_combinations[i][_amount] += num_combinations[i][_amount - coins[i]]

    return num_combinations[0][amount]


def test_change():
    solutions = [
        change_recursion,
        change_dynamic_top_down,
        change_dynamic_bottom_up,
    ]

    test_cases = [
        (4, [1, 2, 3], 4),
        (7, [2, 4], 0),
    ]

    for solution in solutions:
        for amount, coins, expected_num_combinations in test_cases:
            # Act
            num_combinations = solution(amount, coins)

            # Assert
            assert num_combinations == expected_num_combinations

        print(f'Tests passed for solution {solution.__name__}')


if __name__ == '__main__':
    test_change()
