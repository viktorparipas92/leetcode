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


def find_median_sorted_arrays_two_pointers(
    numbers_1: list[int], numbers_2: list[int]
) -> float:
    """
    Time complexity: O(n + m)
    Space complexity: O(1)
    """
    length_1, length_2 = len(numbers_1), len(numbers_2)
    i = j = 0
    median_1 = median_2 = 0

    for count in range((length_1 + length_2) // 2 + 1):
        median_2 = median_1
        if i < length_1 and j < length_2:
            if numbers_1[i] > numbers_2[j]:
                median_1 = numbers_2[j]
                j += 1
            else:
                median_1 = numbers_1[i]
                i += 1

        elif i < length_1:
            median_1 = numbers_1[i]
            i += 1
        else:
            median_1 = numbers_2[j]
            j += 1

    if (length_1 + length_2) % 2 == 1:
        return float(median_1)
    else:
        return (median_1 + median_2) / 2.0


def find_median_sorted_arrays_binary_search_optimal(
    numbers_1: list[int], numbers_2: list[int]
) -> float:
    """
    Time complexity: O(log(min(n, m)))
    Space complexity: O(1)
    """
    length_1, length_2 = len(numbers_1), len(numbers_2)
    total_length = length_1 + length_2
    half_length = total_length // 2

    if length_2 < length_1:
        numbers_1, numbers_2 = numbers_2, numbers_1
        length_1, length_2 = length_2, length_1

    left_idx, right_idx = 0, len(numbers_1) - 1
    while True:
        i = (left_idx + right_idx) // 2
        j = half_length - i - 2

        left_1 = numbers_1[i] if i >= 0 else float('-infinity')
        right_1 = numbers_1[i + 1] if (i + 1) < length_1 else float('infinity')

        left_2 = numbers_2[j] if j >= 0 else float('-infinity')
        right_2 = numbers_2[j + 1] if (j + 1) < length_2 else float('infinity')

        if left_1 <= right_2 and left_2 <= right_1:
            if total_length % 2:
                return min(right_1, right_2)
            else:
                return (max(left_1, left_2) + min(right_1, right_2)) / 2

        elif left_1 > right_2:
            right_idx = i - 1
        else:  # left_2 > right_1
            left_idx = i + 1


def test_find_median_sorted_arrays():
    solutions = [
        find_median_sorted_arrays_brute_force,
        find_median_sorted_arrays_two_pointers,
        find_median_sorted_arrays_binary_search_optimal,
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