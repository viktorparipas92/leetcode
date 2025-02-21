"""
39. Combination Sum
----------------------------------
Difficulty: Medium

You are given an array of distinct integers nums and a target integer target.
Your task is to return a list of all unique combinations of nums where the
chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times.
Two combinations are the same if the frequency of each of the chosen numbers is the
same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each
combination can be in any order.

Example 1:
Input:
nums = [2,5,6,9]
target = 9
Output: [[2,2,5],[9]]
Explanation:
2 + 2 + 5 = 9. We use 2 twice, and 5 once.
9 = 9. We use 9 once.

Example 2:
Input:
nums = [3,4,5]
target = 16
Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

Example 3:
Input:
nums = [3]
target = 5
Output: []

Constraints:
All elements of nums are distinct.
1 <= nums.length <= 20
2 <= nums[i] <= 30
2 <= target <= 30
"""


def combination_sum_backtracking(numbers: list[int], target: int) -> list[list[int]]:
    """
    Time complexity: O(2^(t/m))
    Space complexity: O(t/m) where t is the target and m is the minimum value in numbers
    """
    combinations: list[list[int]] = []

    def depth_first_search(i: int, current: list[int], total: int):
        if total == target:
            combinations.append(current.copy())
            return

        if i >= len(numbers) or total > target:
            return

        current.append(numbers[i])

        depth_first_search(i, current, total + numbers[i])
        current.pop()
        depth_first_search(i + 1, current, total)

    depth_first_search(0, current=[], total=0)
    return combinations


def test_combination_sum():
    solutions = [
        combination_sum_backtracking,
    ]

    test_cases = [
        ([2, 5, 6, 9], 9, [[2, 2, 5], [9]]),
        ([3, 4, 5], 16, [[3, 3, 3, 3, 4], [3, 3, 5, 5], [4, 4, 4, 4], [3, 4, 4, 5]]),
        ([3], 5, []),
    ]

    for solution in solutions:
        for numbers, target, expected_combinations in test_cases:
            # Act
            combinations = solution(numbers, target)

            # Assert
            assert sorted(combinations) == sorted(expected_combinations)

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_combination_sum()
