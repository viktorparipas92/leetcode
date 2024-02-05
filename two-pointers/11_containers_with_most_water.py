"""
11. Container With Most Water
------------------------------
Difficulty: Medium

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line
are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


def max_area(height: list[int]) -> int:
    maximum_area = 0
    left, right = 0, len(height) - 1
    while left < right:
        minimum_height = min(height[left], height[right])
        area = (right - left) * minimum_height
        maximum_area = max(maximum_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maximum_area


def test_max_area():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1


if __name__ == '__main__':
    test_max_area()