"""
167. Two Sum II - Input array is sorted
---------------------------------------
Difficulty: Medium

Given an array of integers numbers that is already sorted in non-decreasing
order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of
size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution.
You may not use the same element twice.

Your solution must run in O(n) time and use O(1) extra space.
"""


def two_sum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1


# Faster solution with dictionary
def two_sum_with_dictionary(numbers: list[int], target: int) -> list[int]:
    num_to_index = {}
    for i, number in enumerate(numbers):
        complement = target - number
        if complement in num_to_index:
            return [num_to_index[complement] + 1, i + 1]

        num_to_index[number] = i


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum([2, 3, 4], 6) == [1, 3]
    assert two_sum([-1, 0], -1) == [1, 2]


if __name__ == '__main__':
    test_two_sum()
