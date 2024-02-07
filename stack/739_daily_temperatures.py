"""
739. Daily Temperatures
--------------------------------
Difficulty: Medium

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days
you have to wait after the ith day to get a warmer temperature.

If there is no future day for which this is possible,
keep answer[i] == 0 instead.
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    stack = []
    answer = [0] * len(temperatures)
    for i, temperature in enumerate(temperatures):
        while stack and temperature > temperatures[stack[-1]]:
            last_warm_index = stack.pop()
            answer[last_warm_index] = i - last_warm_index

        stack.append(i)

    return answer


def test_daily_temperatures():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0]


if __name__ == '__main__':
    test_daily_temperatures()