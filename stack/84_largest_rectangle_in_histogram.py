"""
84. Largest Rectangle in Histogram
-----------------------------------
Difficulty: Hard

You are given an array of integers heights where heights[i] represents the height of a
bar. The width of each bar is 1.
Return the area of the largest rectangle that can be formed among the bars.
Note: This chart is known as a histogram.

Example 1:
Input: heights = [7,1,7,2,2,4]
Output: 8

Example 2:
Input: heights = [1,3,7]
Output: 7

Constraints:
1 <= heights.length <= 1000.
0 <= heights[i] <= 1000

"""


def largest_rectangle_area_brute_force(heights: list[int]) -> int:
    """
    Time complexity: O(n^2), space complexity: O(1)
    """
    length = len(heights)
    max_area = 0
    for i, height in enumerate(heights):
        rightmost = i + 1
        while rightmost < length and heights[rightmost] >= height:
            rightmost += 1

        leftmost = i
        while leftmost >= 0 and heights[leftmost] >= height:
            leftmost -= 1

        rightmost -= 1
        leftmost += 1
        max_area = max(max_area, height * (rightmost - leftmost + 1))

    return max_area


def largest_rectangle_area_stack(heights: list[int]) -> int:
    length = len(heights)
    leftmost = [-1] * length

    stack = []
    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] >= height:
            stack.pop()

        if stack:
            leftmost[i] = stack[-1]

        stack.append(i)

    stack = []
    rightmost = [length] * length
    for i, height in reversed(list(enumerate(heights))):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()

        if stack:
            rightmost[i] = stack[-1]

        stack.append(i)

    max_area = 0
    for left, right, height in zip(leftmost, rightmost, heights):
        left += 1
        right -= 1
        max_area = max(max_area, height * (right - left + 1))

    return max_area


def test_largest_rectangle_area():
    # Arrange
    solutions = [
        largest_rectangle_area_brute_force,
        largest_rectangle_area_stack,
    ]
    test_cases = [
        ([7, 1, 7, 2, 2, 4], 8),
        ([1, 3, 7], 7),
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
    ]
    for solution in solutions:
        for heights, expected_max_area in test_cases:
            # Act
            max_area = solution(heights)

            # Assert
            assert max_area == expected_max_area

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_largest_rectangle_area()