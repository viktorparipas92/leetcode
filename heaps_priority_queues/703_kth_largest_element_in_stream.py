"""
703. Kth Largest Element in a Stream
-------------------------------------
Difficulty: Easy

You are part of a university admissions office and need to keep track of the kth
highest test score from applicants in real-time. This helps to determine cut-off marks
for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of
test scores and continuously returns the kth highest test score after a new score has
been submitted. More specifically, we are looking for the kth highest score in the 'sorted list of all scores.

Implement the KthLargest class:
KthLargest(int k, int[] nums)
Initializes the object with the integer k and the stream of test scores nums.

int add(int val) Adds a new test score val to the stream and returns the element
representing the kth largest element in the pool of test scores so far.


Example 1:
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output: [null, 4, 5, 5, 8, 8]

Explanation:
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3); // return 4
kthLargest.add(5); // return 5
kthLargest.add(10); // return 5
kthLargest.add(9); // return 8
kthLargest.add(4); // return 8

Example 2:

Input:
["KthLargest", "add", "add", "add", "add"]
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]
Output: [null, 7, 7, 7, 8]

Explanation:
KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
kthLargest.add(2); // return 7
kthLargest.add(10); // return 7
kthLargest.add(9); // return 7
kthLargest.add(9); // return 8


Constraints:
0 <= nums.length <= 104
1 <= k <= nums.length + 1
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
"""
import heapq


# With sorting
class KthLargest:
    def __init__(self, k: int, numbers: list[int]):
        self.k = k
        self.numbers = numbers

    def add(self, value: int) -> int:
        self.numbers.append(value)
        self.numbers.sort()
        return self.numbers[-self.k]


class KthLargestMinHeap:
    def __init__(self, k: int, numbers: list[int]):
        self.min_heap, self.k = numbers, k
        heapq.heapify(self.min_heap)

        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, value: int) -> int:
        heapq.heappush(self.min_heap, value)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]


def test_case_1(kth_largest_class):
    kth_largest = kth_largest_class(3, [4, 5, 8, 2])

    assert kth_largest.add(3) == 4
    assert kth_largest.add(5) == 5
    assert kth_largest.add(10) == 5
    assert kth_largest.add(9) == 8
    assert kth_largest.add(4) == 8


def test_case_2(kth_largest_class):
    kth_largest = kth_largest_class(4, [7, 7, 7, 7, 8, 3])
    assert kth_largest.add(2) == 7
    assert kth_largest.add(10) == 7
    assert kth_largest.add(9) == 7
    assert kth_largest.add(9) == 8


if __name__ == '__main__':
    classes_to_test = [KthLargest, KthLargestMinHeap]
    test_cases = [test_case_1, test_case_2]
    for kth_largest_class in classes_to_test:
        for test_case in test_cases:
            test_case(kth_largest_class)

        print(f"{kth_largest_class.__name__} passed")


