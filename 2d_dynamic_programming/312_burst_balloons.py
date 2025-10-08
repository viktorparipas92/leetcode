"""
312. Burst Balloons
----------------------------
Difficulty: Hard

You are given an array of integers nums of size n.
The ith element represents a balloon with an integer value of nums[i].
You must burst all of the balloons.

If you burst the ith balloon, you will receive nums[i - 1] * nums[i] * nums[i + 1] coins.
If i - 1 or i + 1 goes out of bounds of the array, then assume the out-of-bounds value is 1.

Return the maximum number of coins you can receive by bursting all the balloons.

Example 1:
Input: nums = [4,2,3,7]
Output: 143

Explanation:
nums = [4,2,3,7] --> [4,3,7] --> [4,7] --> [7] --> []
coins =  4*2*3    +   4*3*7   +  1*4*7  + 1*7*1 = 143

Constraints:
n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""


def max_coins_brute_force_recursion(numbers: list[int]) -> int:
    """
    Time complexity: O(n * 2^n)
    Space complexity: O(n * 2^n)
    """
    def depth_first_search(_numbers: list[int]) -> int:
        if len(_numbers) == 2:
            return 0

        max_coins: int = 0
        for i in range(1, len(_numbers) - 1):
            coins: int = _numbers[i - 1] * _numbers[i] * _numbers[i + 1]
            coins += depth_first_search(_numbers[:i] + _numbers[i + 1:])
            max_coins = max(max_coins, coins)

        return max_coins

    padded_numbers: list[int] = [1] + numbers + [1]
    return depth_first_search(padded_numbers)


def test_max_coins():
    solutions = [
        max_coins_brute_force_recursion,
    ]

    test_cases = [
        ([4, 2, 3, 7], 143),
    ]

    for solution in solutions:
        for numbers, expected_max_coins in test_cases:
            # Act
            max_coins = solution(numbers)

            # Assert
            assert max_coins == expected_max_coins

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_max_coins()