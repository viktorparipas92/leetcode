"""
121. Best Time to Buy and Sell Stock
------------------------------------------------
Difficulty: Easy

You are given an array prices where prices[i] is the price of a given stock
on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""


def max_profit(prices: list[int]) -> int:
    minimum_price = float('inf')
    maximum_profit = 0
    for price in prices:
        if price < minimum_price:
            minimum_price = price
        elif price - minimum_price > maximum_profit:
            maximum_profit = price - minimum_price

    return maximum_profit


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0


if __name__ == '__main__':
    test_max_profit()