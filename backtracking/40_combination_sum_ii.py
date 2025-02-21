"""
40. Combination Sum II
----------------------------------
Difficulty: Medium

You are given an array of integers candidates, which may contain duplicates,
and a target integer target.
Your task is to return a list of all unique combinations of candidates where the chosen
numbers sum to target.

Each element from candidates may be chosen at most once within a combination.
The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the numbers in each
combination can be in any order.

Example 1:
Input: candidates = [9,2,2,4,6,1,5], target = 8
Output: [
  [1,2,5],
  [2,2,4],
  [2,6]
]

Example 2:
Input: candidates = [1,2,3,4,5], target = 7
Output: [
  [1,2,4],
  [2,5],
  [3,4]
]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from collections import Counter


def combination_sum_2_brute_force(
    candidates: list[int], target: int
) -> list[list[int]]:
    """
    Time complexity: O(n 2^n)
    Space complexity: O(n 2^n)
    """
    combinations: set[tuple] = set()
    candidates.sort()

    def generate_subsets(i: int, current_combination: list, total: int):
        if total == target:
            combinations.add(tuple(current_combination))
            return
        elif total > target or i == len(candidates):
            return

        candidate = candidates[i]
        current_combination.append(candidate)
        generate_subsets(i + 1, current_combination, total + candidate)

        current_combination.pop()
        generate_subsets(i + 1, current_combination, total)

    generate_subsets(0, current_combination=[], total=0)
    return [list(combination) for combination in combinations]


def combination_sum_2_backtracking(
    candidates: list[int], target: int
) -> list[list[int]]:
    """
    Time complexity: O(n 2^n)
    Space complexity: O(n)
    """
    combinations: set[tuple] = set()
    candidates.sort()

    def generate_subsets(i: int, current_combination: list, total: int):
        if total == target:
            combinations.add(tuple(current_combination))
            return
        elif total > target or i == len(candidates):
            return

        candidate = candidates[i]
        current_combination.append(candidate)
        generate_subsets(i + 1, current_combination, total + candidate)

        current_combination.pop()

        while i + 1 < len(candidates) and candidate == candidates[i + 1]:
            i += 1

        generate_subsets(i + 1, current_combination, total)

    generate_subsets(0, current_combination=[], total=0)
    return [list(combination) for combination in combinations]


def combination_sum_2_backtracking_hash_map(
    candidates: list[int], target: int
) -> list[list[int]]:
    """
    Time complexity: O(n 2^n)
    Space complexity: O(n)
    """
    def backtrack(
        _candidates: list[int], target: int, current_combination: list[int], i: int
    ):
        if target == 0:
            combinations.append(current_combination.copy())
            return
        elif target < 0 or i >= len(_candidates):
            return

        candidate = _candidates[i]
        if candidate_counts[candidate] > 0:
            current_combination.append(candidate)
            candidate_counts[candidate] -= 1

            backtrack(_candidates, target - candidate, current_combination, i)

            candidate_counts[candidate] += 1
            current_combination.pop()

        backtrack(_candidates, target, current_combination, i + 1)

    combinations: list = []
    current_combination = []

    candidate_counts = Counter(candidates)
    unique_candidates = list(candidate_counts.keys())

    backtrack(unique_candidates, target, current_combination, 0)
    return combinations


def test_combination_sum_2():
    solutions = [
        combination_sum_2_brute_force,
        combination_sum_2_backtracking,
        combination_sum_2_backtracking_hash_map,
    ]

    test_cases = [
        ([9, 2, 2, 4, 6, 1, 5], 8, [[1, 2, 5], [2, 2, 4], [2, 6]]),
        ([1, 2, 3, 4, 5], 7, [[1, 2, 4], [2, 5], [3, 4]]),
    ]

    for solution in solutions:
        for candidates, target, expected_combinations in test_cases:
            # Act
            combinations = solution(candidates, target)

            # Assert
            assert len(combinations) == len(expected_combinations)

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_combination_sum_2()
