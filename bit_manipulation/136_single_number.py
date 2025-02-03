"""
136. Single Number
------------------
Difficulty: Easy

You are given a non-empty array of integers nums. Every integer appears twice except
for one. Return the integer that appears only once.

You must implement a solution with  O(n) runtime complexity and use only
O(1) extra space.

Example 1:
Input: nums = [3,2,3]
Output: 2

Example 2:
Input: nums = [7,6,6,7,8]
Output: 8

Constraints:
1 <= nums.length <= 10000
-10000 <= nums[i] <= 10000
"""


def single_number_brute_force(numbers: list[int]) -> int | None:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    for i, number_1 in enumerate(numbers):
        flag = True
        for j, number_2 in enumerate(numbers):
            if i != j and number_1 == number_2:
                flag = False
                break

        if flag:
            return number_1


def single_number_hash_set(numbers: list[int]) -> int | None:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    seen = set()
    for number in numbers:
        if number not in seen:
            seen.add(number)
        else:
            seen.remove(number)

    return seen.pop()


def single_number_sorting(numbers: list[int]) -> int:
    """
    Time complexity: O(n log n)
    Space complexity: O(1)
    """
    numbers.sort()

    for i in range(0, len(numbers) - 1, 2):
        if numbers[i] != numbers[i + 1]:
            return numbers[i]

    return numbers[-1]


def test_single_number():
    # Arrange
    solutions = [
        single_number_brute_force,
        single_number_hash_set,
        single_number_sorting,
    ]

    test_cases = [
        ([3, 2, 3], 2),
        ([7, 6, 6, 7, 8], 8),
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
    ]

    for solution in solutions:
        for numbers, expected_single_number in test_cases:
            # Act
            single_number = solution(numbers)

            # Assert
            assert single_number == expected_single_number

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_single_number()
