"""
55. Jump Game
------------------
Difficulty: Medium

You are given an integer array nums where each element indicates your maximum jump
length at that position.
Return true if you can reach the last index starting from index 0, or false otherwise.

Example 1:
Input: nums = [1,2,0,1,0]
Output: true
Explanation: First jump from index 0 to 1, then from index 1 to 3,
and lastly from index 3 to 4.

Example 2:
Input: nums = [1,2,1,0,1]
Output: false

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""


def can_jump_recursive(numbers: list[int]) -> bool:
    """
    Time complexity: O(n!)
    Space complexity: O(n)
    """

    def depth_first_search(i: int) -> bool:
        if i == len(numbers) - 1:
            return True

        end = min(len(numbers) - 1, i + numbers[i])
        return any(depth_first_search(j) for j in range(i + 1, end + 1))

    return depth_first_search(i=0)


def can_jump_greedy(numbers: list[int]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    goal = len(numbers) - 1
    # Start from the second last number and check if we can reach the goal from there.
    for i, number in enumerate(reversed(numbers[:-1])):
        # The index of the number in the original list.
        index = len(numbers) - 2 - i
        if index + number >= goal:
            goal = index

    return goal == 0


def test_can_jump_recursive():
    solutions = [
        can_jump_recursive,
        can_jump_greedy,
    ]

    test_cases = [
        ([1, 2, 0, 1, 0], True),
        ([1, 2, 1, 0, 1], False),
    ]

    for solution in solutions:
        for numbers, expected_can_jump in test_cases:
            # Act
            can_jump = solution(numbers)

            # Assert
            assert can_jump == expected_can_jump

        print(f'{solution.__name__} is correct')


if __name__ == '__main__':
    test_can_jump_recursive()
