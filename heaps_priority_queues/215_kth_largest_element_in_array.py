"""
215. Kth Largest Element in an Array
-------------------------------------
Difficulty: Medium

Given an unsorted array of integers nums and an integer k,
return the k-th largest element in the array.

By k-th largest element, we mean the kth largest element in the sorted order,
not the kth distinct element.

Follow-up: Can you solve it without sorting?

Example 1:
Input: nums = [2,3,1,5,4], k = 2
Output: 4

Example 2:
Input: nums = [2,3,1,1,5,5,4], k = 3
Output: 4
Constraints:

1 <= k <= nums.length <= 10000
-1000 <= nums[i] <= 1000
"""
import heapq


def find_kth_largest_sorting(numbers: list[int], k: int) -> int:
    """
    Time complexity: O(n * log(n))
    Space complexity: O(1)
    """
    return sorted(numbers)[-k]


def find_kth_largest_min_heap(numbers: list[int], k: int) -> int:
    """
    Time complexity: O(n * log(k))
    Space complexity: O(k)
    """
    return heapq.nlargest(k, numbers)[-1]


def find_kth_largest_quick_select(numbers: list[int], k: int) -> int:
    """
    Time complexity: O(n) in the average case, O(n^2) in the worst case
    Space complexity: O(n)
    """
    k = len(numbers) - k

    def quick_select(left_idx: int, right_idx: int) -> int:
        # Picking the last element as pivot simplifies partitioning
        pivot = numbers[right_idx]
        partition_idx = left_idx  # Keeps track of where smaller elements should go
        for i in range(left_idx, right_idx):
            if numbers[i] <= pivot:
                # Swap smaller elements to the left
                numbers[partition_idx], numbers[i] = numbers[i], numbers[partition_idx]
                partition_idx += 1  # Move boundary to the right

        # Move pivot to its final place
        numbers[partition_idx], numbers[right_idx] = (
            numbers[right_idx], numbers[partition_idx]
        )

        if partition_idx > k:  # k-th largest element is on the left
            return quick_select(left_idx, partition_idx - 1)
        elif partition_idx < k:  # k-th largest element is on the right
            return quick_select(partition_idx + 1, right_idx)
        else:  # k-th largest element is found
            return numbers[partition_idx]

    return quick_select(left_idx=0, right_idx=len(numbers) - 1)


def test_find_kth_largest():
    solutions = [
        find_kth_largest_sorting,
        find_kth_largest_min_heap,
        find_kth_largest_quick_select,
    ]

    test_cases = [
        ([2, 3, 1, 5, 4], 2, 4),
        ([2, 3, 1, 1, 5, 5, 4], 3, 4),
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ]

    for solution in solutions:
        for numbers, k, expected_kth_largest in test_cases:
            # Act
            kth_largest = solution(numbers, k)

            # Assert
            assert kth_largest == expected_kth_largest

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_find_kth_largest()
