"""
45. Jump Game II
----------------
Difficulty: Medium

You are given an array of integers nums, where nums[i] represents the maximum length
of a jump towards the right from index i. For example, if you are at nums[i],
you can jump to any index i + j where:
j <= nums[i]
i + j < nums.length

You are initially positioned at nums[0].
Return the minimum number of jumps to reach the last position in the array
(index nums.length - 1). You may assume there is always a valid answer.

Example 1:
Input: nums = [2,4,1,1,1,1]
Output: 2
Explanation: Jump from index 0 to index 1, then jump from index 1 to the last index.

Example 2:
Input: nums = [2,1,2,1,0]
Output: 2

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 100
"""


def jump_recursive(numbers: list[int]) -> int:
    """
    Time complexity: O(n!)
    Space complexity: O(n)
    """
    def depth_first_search(i: int):
        length = len(numbers)
        if i == length - 1:
            return 0

        number = numbers[i]
        if number == 0:
            return float('inf')

        end = min(length - 1, i + number)
        min_num_jumps = float('inf')
        for j in range(i + 1, end + 1):
            min_num_jumps = min(min_num_jumps, 1 + depth_first_search(j))

        return min_num_jumps

    return depth_first_search(0)


def jump_dynamic_bottom_up(numbers: list[int]) -> int:
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    length = len(numbers)
    num_counts: list[int] = [1000000] * length
    num_counts[-1] = 0

    for i in range(length - 2, -1, -1):
        end = min(length, i + numbers[i] + 1)
        for j in range(i + 1, end):
            num_counts[i] = min(num_counts[i], 1 + num_counts[j])

    return num_counts[0]


def jump_greedy_bfs(numbers: list[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    min_num_jumps = 0
    left_idx = right_idx = 0

    while right_idx < len(numbers) - 1:
        farthest = 0
        for i in range(left_idx, right_idx + 1):
            farthest = max(farthest, i + numbers[i])

        left_idx = right_idx + 1
        right_idx = farthest
        min_num_jumps += 1

    return min_num_jumps


def test_jump():
    solutions = [
        jump_recursive,
        jump_dynamic_bottom_up,
        jump_greedy_bfs,
    ]

    test_cases = [
        ([2, 4, 1, 1, 1, 1], 2),
        ([2, 1, 2, 1, 0], 2),
    ]

    for solution in solutions:
        for numbers, expected_num_jumps in test_cases:
            # Act
            num_jumps = solution(numbers)

            # Assert
            assert num_jumps == expected_num_jumps

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_jump()
