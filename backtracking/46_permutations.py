"""
46. Permutations
----------------
Difficulty: Medium

Given an array nums of unique integers, return all the possible permutations.
You may return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [7]
Output: [[7]]
Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
"""


def permute_recursive(numbers: list[int]) -> list[list[int]]:
    """
    Time complexity: O(n! * n^2)
    Space complexity: O(n! * n) for the output list
    """
    if not numbers:
        return [[]]

    permutations = permute_recursive(numbers[1:])
    total_permutations = []
    for permutation in permutations:
        for i in range(len(permutation) + 1):
            permutation_copy = permutation.copy()
            permutation_copy.insert(i, numbers[0])
            total_permutations.append(permutation_copy)

    return total_permutations


def permute_iterative(numbers: list[int]) -> list[list[int]]:
    """
    Time complexity: O(n! * n^2)
    Space complexity: O(n! * n) for the output list
    """
    permutations = [[]]
    for number in numbers:
        new_permutations = []
        for permutation in permutations:
            for i in range(len(permutation) + 1):
                permutation_copy = permutation.copy()
                permutation_copy.insert(i, number)
                new_permutations.append(permutation_copy)

        permutations = new_permutations

    return permutations


def permute_backtracking(numbers: list[int]) -> list[list[int]]:
    """
    Time complexity: O(n! * n)
    Space complexity: O(n! * n)
    """

    def backtrack(permutation: list[int], picked: list[bool]):
        if len(permutation) == len(numbers):
            permutations.append(permutation[:])
            return

        for i, number in enumerate(numbers):
            if not picked[i]:
                permutation.append(number)
                picked[i] = True

                backtrack(permutation, picked)

                permutation.pop()
                picked[i] = False

    permutations: list[list[int]] = []
    initial_picked: list[bool] = [False] * len(numbers)
    backtrack(permutation=[], picked=initial_picked)
    return permutations


def permute_backtracking_bit_mask(numbers: list[int]) -> list[list[int]]:
    """
    Time complexity: O(n! * n)
    Space complexity: O(n! * n)
    """
    def backtrack(permutation: list[int], mask: int):
        if len(permutation) == len(numbers):
            permutations.append(permutation[:])
            return

        for i, number in enumerate(numbers):
            if not (mask & (1 << i)):  # Check if the number is not picked
                permutation.append(number)

                mask_with_current_number = mask | (1 << i)
                backtrack(permutation, mask_with_current_number)

                permutation.pop()

    permutations: list[list[int]] = []
    backtrack(permutation=[], mask=0)
    return permutations


def test_permute():
    solutions = [
        permute_recursive,
        permute_iterative,
        permute_backtracking,
        permute_backtracking_bit_mask,
    ]

    test_cases = [
        ([1, 2, 3], [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]),
        ([7], [[7]]),
    ]

    for solution in solutions:
        for numbers, expected_permutations in test_cases:
            # Act
            permutations = solution(numbers)

            # Assert
            assert sorted(permutations) == sorted(expected_permutations)

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_permute()