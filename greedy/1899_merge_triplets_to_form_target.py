"""
1899. Merge Triplets to Form Target Triplet
----
Difficulty: Medium

You are given a 2D array of integers triplets,
where triplets[i] = [ai, bi, ci] represents the ith triplet.
You are also given an array of integers target = [x, y, z]
which is the triplet we want to obtain.

To obtain target, you may apply the following operation on triplets zero or more times:
Choose two different triplets (i and j) and update triplets[j] to become
[max(ai, aj), max(bi, bj), max(ci, cj)].

Return true if it is possible to obtain target as an element of triplets, or false otherwise.

Example 1:
Input: triplets = [[1,2,3],[7,1,1]], target = [7,2,3]
Output: true
Explanation:
Choose the first and second triplets, update the second triplet to be
[max(1, 7), max(2, 1), max(3, 1)] = [7, 2, 3].

Example 2:
Input: triplets = [[2,5,6],[1,4,4],[5,7,5]], target = [5,4,6]
Output: false

Constraints:
1 <= triplets.length <= 1000
1 <= ai, bi, ci, x, y, z <= 100
"""
Triplet = tuple[int, int, int]


def merge_triplets_greedy(triplets: list[Triplet], target: Triplet) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    matching_indices: set[int] = set()

    x, y, z = target
    for triplet in triplets:
        a, b, c = triplet
        if a > x or b > y or c > z:
            continue

        for i, (_triplet, _target) in enumerate(zip(triplet, target)):
            if _triplet == _target:
                matching_indices.add(i)

    return len(matching_indices) == 3


def test_merge_triplets():
    solutions = [
        merge_triplets_greedy,
    ]

    test_cases = [
        (([(1, 2, 3), (7, 1, 1)], (7, 2, 3)), True),
        (([(2, 5, 6), (1, 4, 4), (5, 7, 5)], (5, 4, 6)), False),
    ]

    for solution in solutions:
        for (triplets, target), expected_is_possible in test_cases:
            # Act
            is_possible = solution(triplets, target)

            # Assert
            assert is_possible == expected_is_possible

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_merge_triplets()
