"""
42. Trapping Rain Water
-----------------------
Difficulty: Hard

You are given an array non-negative integers height which represent an elevation map.
Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9
Constraints:

1 <= height.length <= 1000
0 <= height[i] <= 1000
"""


def trap_brute_force(heights: list[int]) -> int:
    """
    Time complexity: O(n^2), space complexity: O(1)
    """
    length = len(heights)
    total_water_area = 0

    for i, height in enumerate(heights):
        left_max = right_max = height
        for j in range(i):
            left_max = max(left_max, heights[j])

        for j in range(i + 1, length):
            right_max = max(right_max, heights[j])

        total_water_area += min(left_max, right_max) - height

    return total_water_area


def trap_prefix_suffix_arrays(heights: list[int]) -> int:
    """
    Time complexity: O(n), space complexity: O(n)
    """
    length = len(heights)
    if len(heights) == 0: return 0

    left_maximums = [height if i == 0 else 0 for i, height in enumerate(heights)]
    # List comprehension does not work here because we need to access the last element
    for i, height in enumerate(heights[1:], 1):
        left_maximums[i] = max(left_maximums[i - 1], height)

    right_maximums = [0] * length
    right_maximums[-1] = heights[-1]
    for i in range(length - 2, -1, -1):
        right_maximums[i] = max(right_maximums[i + 1], heights[i])

    total_water_area = sum(
        min(left_max, right_max) - height
        for left_max, right_max, height in zip(left_maximums, right_maximums, heights)
    )
    return total_water_area


def trap_stack(heights: list[int]) -> int:
    """
    Time complexity: O(n), space complexity: O(n)
    """
    indices_stack : list[int] = []
    total_water_area = 0
    for i, height in enumerate(heights):
        while indices_stack and height >= heights[indices_stack[-1]]:
            middle_height = heights[indices_stack.pop()]
            if indices_stack:
                right_height = height
                left_height = heights[indices_stack[-1]]
                water_height = min(right_height, left_height) - middle_height
                width = i - indices_stack[-1] - 1
                total_water_area += water_height * width

        indices_stack.append(i)

    return total_water_area


def test_trap_rainwater():
    # Arrange
    solutions = [
        trap_brute_force,
        trap_prefix_suffix_arrays,
        trap_stack,
    ]
    test_cases = [
        ([0, 2, 0, 3, 1, 0, 1, 3, 2, 1], 9),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
    ]

    for solution in solutions:
        for heights, expected_area in test_cases:
            # Act
            area = solution(heights)

            # Assert
            assert area == expected_area

        print(f"Passed all test cases for {solution.__name__}!")


if __name__ == "__main__":
    test_trap_rainwater()

