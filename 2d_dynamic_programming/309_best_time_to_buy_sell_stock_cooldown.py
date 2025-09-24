"""
309. Best Time to Buy and Sell Stock with Cooldown
-----
Difficulty: Medium

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may buy and sell one NeetCoin multiple times with the following restrictions:
After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
You may only own at most one NeetCoin at a time.
You may complete as many transactions as you like.

Return the maximum profit you can achieve.

Example 1:
Input: prices = [1,3,4,0,4]
Output: 6
Explanation: Buy on day 0 (price = 1) and sell on day 1 (price = 3), profit = 3-1 = 2. Then buy on day 3 (price = 0) and sell on day 4 (price = 4), profit = 4-0 = 4. Total profit is 2 + 4 = 6.

Example 2:
Input: prices = [1]
Output: 0

Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000

"""


def max_profit_recursion(prices: list[int]) -> int:
    """
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """

    def depth_first_search(i: int, is_buying: bool) -> int:
        if i >= len(prices):
            return 0

        cooldown: int = depth_first_search(i + 1, is_buying)
        if is_buying:
            buy = depth_first_search(i + 1, not is_buying) - prices[i]
            return max(buy, cooldown)
        else:
            sell = depth_first_search(i + 2, not is_buying) + prices[i]
            return max(sell, cooldown)

    return depth_first_search(i=0, is_buying=True)


def max_profit_dynamic_top_down(prices: list[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    max_profit_map: dict[tuple[int, bool], int] = {}

    def depth_first_search(i: int, is_buying: bool) -> int:
        if i >= len(prices):
            return 0
        elif (i, is_buying) in max_profit_map:
            return max_profit_map[(i, is_buying)]

        cooldown = depth_first_search(i + 1, is_buying)
        if is_buying:
            buy = depth_first_search(i + 1, not is_buying) - prices[i]
            max_profit_map[(i, is_buying)] = max(buy, cooldown)
        else:
            sell = depth_first_search(i + 2, not is_buying) + prices[i]
            max_profit_map[(i, is_buying)] = max(sell, cooldown)

        return max_profit_map[(i, is_buying)]

    return depth_first_search(i=0, is_buying=True)


def test_max_profit():
    solutions = [
        max_profit_recursion,
        max_profit_dynamic_top_down,
    ]

    test_cases = [
        ([1, 3, 4, 0, 4], 6),
        ([1], 0),
    ]

    for solution in solutions:
        for prices, expected_max_profit in test_cases:
            # Act
            max_profit = solution(prices)

            # Assert
            assert max_profit == expected_max_profit

        print(f'Tests passed for solution {solution.__name__}')


if __name__ == '__main__':
    test_max_profit()
