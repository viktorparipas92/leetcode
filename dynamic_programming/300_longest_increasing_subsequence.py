"""
300. Longest Increasing Subsequence
-----------------------------------
Difficulty: Medium

Given an integer array nums, return the length of the longest
strictly increasing subsequence.

A subsequence is a sequence that can be derived from the given sequence
by deleting some or no elements without changing the relative order
of the remaining characters.
For example, "cat" is a subsequence of "crabt".

Example 1:
Input: nums = [9,1,4,2,3,3,7]
Output: 4
Explanation: The longest increasing subsequence is [1,2,3,7], which has a length of 4.

Example 2:
Input: nums = [0,3,1,3,2,3]
Output: 4

Constraints:
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
"""


def length_of_lis_recursion(numbers: list[int]) -> int:
    """
    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    def depth_first_search(i: int, j: int) -> int:
        if i == len(numbers):
            return 0

        max_length: int = depth_first_search(i + 1, j)  # not include
        if j == -1 or numbers[j] < numbers[i]:
            max_length = max(max_length, 1 + depth_first_search(i + 1, i))  # include

        return max_length

    return depth_first_search(i=0, j=-1)


def length_of_lis_dynamic_top_down(numbers: list[int]) -> int:
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    def depth_first_search(i: int) -> int:
        if max_length_map[i] != -1:
            return max_length_map[i]

        max_length: int = 1
        for j in range(i + 1, length):
            if numbers[i] < numbers[j]:
                max_length = max(max_length, 1 + depth_first_search(j))

        max_length_map[i] = max_length
        return max_length

    length = len(numbers)
    max_length_map: list[int] = [-1] * length
    return max(depth_first_search(i) for i in range(length))


def length_of_lis_dynamic_bottom_up(numbers: list[int]) -> int:
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    length = len(numbers)
    max_lengths: list[int] = [1] * length
    for i in range(length - 1, -1, -1):
        for j in range(i + 1, length):
            if numbers[i] < numbers[j]:
                max_lengths[i] = max(max_lengths[i], 1 + max_lengths[j])

    return max(max_lengths)


def test_length_of_lis():
    solutions = [
        length_of_lis_recursion,
        length_of_lis_dynamic_top_down,
        length_of_lis_dynamic_bottom_up,
    ]

    test_cases = [
        ([9, 1, 4, 2, 3, 3, 7], 4),
        ([0, 3, 1, 3, 2, 3], 4),
    ]

    for solution in solutions:
        for numbers, expected_max_length in test_cases:
            # Act
            max_length = solution(numbers)

            # Assert
            assert max_length == expected_max_length

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_length_of_lis()
