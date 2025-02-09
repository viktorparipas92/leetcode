"""
268. Missing Number
-------------------
Difficulty: Easy

Given an array nums containing n integers in the range [0, n] without any duplicates,
return the single number in the range that is missing from nums.

Follow-up: Could you implement a solution using only O(1) extra space complexity
and O(n) runtime complexity?

Example 1:
Input: nums = [1,2,3]
Output: 0
Explanation: Since there are 3 numbers, the range is [0,3].
The missing number is 0 since it does not appear in nums.

Example 2:
Input: nums = [0,2]
Output: 1
Constraints:
1 <= nums.length <= 1000
"""


def get_missing_number_sorting(numbers: list[int]) -> int:
    """
    Time complexity: O(n log n)
    Space complexity: O(1)
    """
    numbers.sort()
    for i, number in enumerate(numbers):
        if number != i:
            return i

    return len(numbers)


def get_missing_number_hash_set(numbers: list[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    number_set = set(numbers)
    for i in range(len(numbers) + 1):
        if i not in number_set:
            return i


def test_missing_number():
    # Arrange
    solutions = [
        get_missing_number_sorting,
        get_missing_number_hash_set,
    ]

    test_cases = [
        ([1, 2, 3], 0),
        ([0, 2], 1),
        ([3, 0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0, 1], 2),
    ]

    for solution in solutions:
        for numbers, expected_missing_number in test_cases:
            # Act
            missing_number = solution(numbers)

            # Assert
            assert missing_number == expected_missing_number

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_missing_number()