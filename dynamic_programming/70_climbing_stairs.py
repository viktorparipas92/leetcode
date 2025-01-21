"""
70. Climbing Stairs
---------------------------------
Difficulty: Easy

You are given an integer n representing the number of steps to reach the top of a
staircase. You can climb with either 1 or 2 steps at a time.
Return the number of distinct ways to climb to the top of the staircase.

Example 1:
Input: n = 2
Output: 2
Explanation:
1 + 1 = 2
2 = 2

Example 2:
Input: n = 3
Output: 3
Explanation:
1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3

Constraints:
1 <= n <= 30
"""


def climb_stairs_recursion(n: int) -> int:
    """
    Time complexity: O(2^n), space complexity: O(n)
    """
    def depth_first_search(i: int):
        if i >= n:
            return i == n

        return depth_first_search(i + 1) + depth_first_search(i + 2)

    return depth_first_search(0)


if __name__ == '__main__':
    assert climb_stairs_recursion(2) == 2
    assert climb_stairs_recursion(3) == 3