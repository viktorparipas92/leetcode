"""
90. Subsets II
--------------
Difficulty: Medium

You are given an array nums of integers, which may contain duplicates.
Return all possible subsets.
The solution must not contain duplicate subsets.
You may return the solution in any order.

Example 1:
Input: nums = [1,2,1]
Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]

Example 2:
Input: nums = [7,7]
Output: [[],[7], [7,7]]

Constraints:
1 <= nums.length <= 11
-20 <= nums[i] <= 20
"""


def subsets_with_duplicates_brute_force(numbers: list[int]) -> list[list[int]]:
    """
    Time complexity: O(n * 2^n)
    Space complexity: O(2^n)
    """
    subsets: set[tuple] = set()

    def generate_subsets(i: int, current_subset: list[int]):
        if i == len(numbers):
            subsets.add(tuple(current_subset))
            return

        current_subset.append(numbers[i])
        generate_subsets(i + 1, current_subset)

        current_subset.pop()
        generate_subsets(i + 1, current_subset)

    numbers.sort()
    generate_subsets(i=0, current_subset=[])
    return [list(subset) for subset in subsets]


def subsets_with_duplicates_backtracking_pick_or_not(
    numbers: list[int]
) -> list[list[int]]:
    """
    Time complexity: O(n * 2^n)
    Space complexity: O(n)
    """
    subsets: list[list[int]] = []

    def generate_subsets(i: int, current_subset: list[int]):
        if i == len(numbers):
            subsets.append(current_subset[::])
            return

        current_subset.append(numbers[i])
        generate_subsets(i + 1, current_subset)

        current_subset.pop()
        while i + 1 < len(numbers) and numbers[i] == numbers[i + 1]:
            i += 1

        generate_subsets(i + 1, current_subset)

    numbers.sort()
    generate_subsets(i=0, current_subset=[])
    return subsets


def test_subsets_with_duplicates():
    solutions = [
        subsets_with_duplicates_brute_force,
        subsets_with_duplicates_backtracking_pick_or_not,
    ]

    test_cases = [
        ([1, 2, 1], [[], [1], [1, 1], [1, 1, 2], [1, 2], [2]]),
        ([7, 7], [[], [7], [7, 7]]),
    ]

    for solution in solutions:
        for numbers, expected_subsets in test_cases:
            # Act
            subsets = solution(numbers)

            # Assert
            assert sorted(subsets) == sorted(expected_subsets)

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_subsets_with_duplicates()
