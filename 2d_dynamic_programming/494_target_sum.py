"""
494. Target Sum
----------------------------
Difficulty: Medium

You are given an array of integers nums and an integer target.
For each number in the array, you can choose to either add
or subtract it to a total sum.

For example, if nums = [1, 2], one possible sum would be "+1-2=-1".
If nums=[1,1], there are two different ways to sum the input numbers
to get a sum of 0: "+1-1" and "-1+1".

Return the number of different ways that you can build the expression
such that the total sum equals target.

Example 1:
Input: nums = [2,2,2], target = 2
Output: 3
Explanation: There are 3 different ways to sum the input numbers to get a sum of 2.
+2 +2 -2 = 2
+2 -2 +2 = 2
-2 +2 +2 = 2

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
-1000 <= target <= 1000
"""
from collections import defaultdict


def find_target_sum_ways_recursion(numbers: list[int], target: int) -> int:
    """
    Time complexity: O(2^n)
    Space complexity: O(n)
    where n is the length of numbers.
    """
    def backtrack(i: int, total: int) -> int:
        if i == len(numbers):
            return total == target

        number = numbers[i]
        return backtrack(i + 1, total + number) + backtrack(i + 1, total - number)

    return backtrack(i=0, total=0)


def find_target_sum_ways_dynamic_top_down(numbers: list[int], target: int) -> int:
    """
    Time complexity: O(n * m)
    Space complexity: O(n * m)
    where n is the length of numbers and m is the sum of all numbers in numbers.
    """
    def backtrack(i: int, total: int) -> int:
        if i == len(numbers):
            return int(total == target)
        elif (i, total) in num_ways_map:
            return num_ways_map[(i, total)]

        number = numbers[i]
        num_ways_map[(i, total)] = (
            backtrack(i + 1, total + number) + backtrack(i + 1, total - number)
        )
        return num_ways_map[(i, total)]

    num_ways_map: dict[tuple[int, int], int] = {}  # (index, total) -> # of ways
    return backtrack(i=0, total=0)


def find_target_sum_ways_dynamic_bottom_up(numbers: list[int], target: int) -> int:
    """
    Time complexity: O(n * m)
    Space complexity: O(n * m)
    where n is the length of numbers and m is the sum of all numbers in numbers.
    """
    length = len(numbers)
    num_ways_map: list[dict[int, int]] = [defaultdict(int) for _ in range(length + 1)]
    num_ways_map[0][0] = 1  # index 0, total 0 -> 1 way

    for i in range(length):
        for total, count in num_ways_map[i].items():
            num_ways_map[i + 1][total + numbers[i]] += count
            num_ways_map[i + 1][total - numbers[i]] += count

    return num_ways_map[length][target]


def find_target_sum_ways_dynamic_bottom_up_optimized(
    numbers: list[int], target: int
)-> int:
    """
    Time complexity: O(n * m)
    Space complexity: O(m)
    """
    num_ways_map: dict[int, int] = defaultdict(int)  # total -> # of ways
    num_ways_map[0] = 1

    for number in numbers:
        next_num_ways_map: dict[int, int] = defaultdict(int)
        for total, count in num_ways_map.items():
            next_num_ways_map[total + number] += count
            next_num_ways_map[total - number] += count

        num_ways_map = next_num_ways_map

    return num_ways_map[target]


def test_find_target_sum_ways():
    solutions = [
        find_target_sum_ways_recursion,
        find_target_sum_ways_dynamic_top_down,
        find_target_sum_ways_dynamic_bottom_up,
        find_target_sum_ways_dynamic_bottom_up_optimized,
    ]

    test_cases = [
        ([2, 2, 2], 2, 3),
    ]

    for solution in solutions:
        for numbers, target, expected_num_ways in test_cases:
            # Act
            num_ways = solution(numbers, target)

            # Assert
            assert num_ways == expected_num_ways

        print(f'{solution.__name__}: All test cases pass')


if __name__ == '__main__':
    test_find_target_sum_ways()
