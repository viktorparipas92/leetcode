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
import math


def climb_stairs_recursion(n: int) -> int:
    """
    Time complexity: O(2^n), space complexity: O(n)
    """
    def depth_first_search(i: int) -> int:
        if i >= n:
            return i == n

        return depth_first_search(i + 1) + depth_first_search(i + 2)

    return depth_first_search(0)


def climb_stairs_dynamic_top_down(n: int) -> int:
    """
    Time complexity: O(n), space complexity: O(n)
    """
    cache = [-1] * n

    def depth_first_search(i: int):
        if i >= n:
            return i == n

        if cache[i] != -1:
            return cache[i]

        cache[i] = depth_first_search(i + 1) + depth_first_search(i + 2)
        return cache[i]

    return depth_first_search(0)


def climb_stairs_dynamic_bottom_up(n: int) -> int:
    """
    Time complexity: O(n), space complexity: O(n)
    """
    if n <= 2:
        return n

    arr = [0] * (n + 1)
    arr[1], arr[2] = 1, 2
    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]


def climb_stairs_dynamic_space_optimized(n: int) -> int:
    """
    Time complexity: O(n), space complexity: O(1)
    :param n:
    :return:
    """
    # Initialize the number of ways to reach the first step and the second step
    # from the ground. Note that this is a simplification for the dynamic programming
    # approach.
    previous, current = 1, 1
    # Iterate from the third step to the nth step
    for _ in range(n - 1):
        temp = previous
        current += previous
        previous = temp

    return current


SQRT_5 = math.sqrt(5)


def climb_stairs_math(n: int) -> int:
    """
    Time complexity: O(log(n)), space complexity: O(1)
    """
    phi = (1 + SQRT_5) / 2
    psi = (1 - SQRT_5) / 2
    return round((phi ** (n + 1) - psi ** (n + 1)) / SQRT_5)


if __name__ == '__main__':
    assert climb_stairs_recursion(2) == 2
    assert climb_stairs_recursion(3) == 3
    print(f'All tests passed for climb_stairs_recursion()')

    assert climb_stairs_dynamic_top_down(2) == 2
    assert climb_stairs_dynamic_top_down(3) == 3
    print(f'All tests passed for climb_stairs_dynamic_top_down()')

    assert climb_stairs_dynamic_bottom_up(2) == 2
    assert climb_stairs_dynamic_bottom_up(3) == 3
    print(f'All tests passed for climb_stairs_dynamic_bottom_up()')

    assert climb_stairs_dynamic_space_optimized(2) == 2
    assert climb_stairs_dynamic_space_optimized(3) == 3
    print(f'All tests passed for climb_stairs_dynamic_space_optimized()')

    assert climb_stairs_math(2) == 2
    assert climb_stairs_math(3) == 3
    print(f'All tests passed for climb_stairs_math()')