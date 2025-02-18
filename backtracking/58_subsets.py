"""
58. Subsets
-----------
Difficulty: Medium

Given an array nums of unique integers, return all possible subsets of nums.
The solution set must not contain duplicate subsets.
You may return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [7]
Output: [[],[7]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""


def subsets_backtracking(numbers: list[int]) -> list[list[int]]:
    """
    Time complexity: O(n * 2^n)
    Space complexity: O(n)
    """
    subsets: list[list[int]] = []
    subset: list[int] = []

    def depth_first_search(i: int):
        if i >= len(numbers):
            subsets.append(subset.copy())
            return

        subset.append(numbers[i])
        depth_first_search(i + 1)  # Include the current number

        subset.pop()  # Backtrack
        depth_first_search(i + 1)  # Exclude the current number

    depth_first_search(i=0)
    return subsets


def subsets_iterative(numbers: list[int]) -> list[list[int]]:
    """
    Time complexity: O(n * 2^n)
    Space complexity: O(n)
    """
    subsets: list[list[int]] = [[]]
    for number in numbers:
        subsets += [subset + [number] for subset in subsets]

    return subsets


def test_subsets():
    solutions = [
        subsets_backtracking,
        subsets_iterative,
    ]

    test_cases = [
        ([1, 2, 3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
        ([7], [[],[7]]),
    ]

    for solution in solutions:
        for numbers, expected_subsets in test_cases:
            # Act
            subsets = solution(numbers)

            # Assert
            assert sorted(subsets) == sorted(expected_subsets)

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_subsets()
