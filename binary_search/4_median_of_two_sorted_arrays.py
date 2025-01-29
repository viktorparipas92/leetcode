"""
4. Median of Two Sorted Arrays
-------------------------------
Difficulty: Hard

You are given two integer arrays nums1 and nums2 of size m and n respectively,
where each is sorted in ascending order.
Return the median value among all elements of the two arrays.

Your solution must run in O(log(m+n)) time.

Example 1:
Input: nums1 = [1,2], nums2 = [3]
Output: 2.0
Explanation: Among [1, 2, 3] the median is 2.

Example 2:
Input: nums1 = [1,3], nums2 = [2,4]
Output: 2.5
Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""


def find_median_sorted_arrays_brute_force(
    numbers_1: list[int], numbers_2: list[int]
) -> float:
    """
    Time complexity: O((n + m) log(n + m))
    Space complexity: O(n + m)
    """
    merged = numbers_1 + numbers_2
    merged.sort()

    total_length = len(merged)
    if not total_length % 2:  # even length
        return (merged[total_length // 2 - 1] + merged[total_length // 2]) / 2.0
    else:
        return merged[total_length // 2]


def test_find_median_sorted_arrays():
    solutions = [
        find_median_sorted_arrays_brute_force,
    ]

    test_cases = [
        ([1, 2], [3], 2.0),
        ([1, 3], [2, 4], 2.5),
    ]

    for find_median_sorted_arrays in solutions:
        for numbers_1, numbers_2, expected_median in test_cases:
            assert find_median_sorted_arrays(numbers_1, numbers_2) == expected_median

        print(f'All tests passed for {find_median_sorted_arrays.__name__}!')


if __name__ == '__main__':
    test_find_median_sorted_arrays()