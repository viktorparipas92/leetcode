"""
347. Top K Frequent Elements
---
Difficulty: Medium

Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.
"""
from collections import Counter, defaultdict


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    return [num for num, _ in Counter(nums).most_common(k)]


def top_k_frequent_without_counter(nums: list[int], k: int) -> list[int]:
    # Much slower
    number_frequencies = defaultdict(int)
    for number in nums:
        number_frequencies[number] += 1

    sorted_frequencies = [
        k for k, _ in
        sorted(number_frequencies.items(), key=lambda item: item[1], reverse=True)
    ]
    return sorted_frequencies[:k]


def test_top_k_frequent():
    assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_frequent([1], 1) == [1]


if __name__ == '__main__':
    test_top_k_frequent()