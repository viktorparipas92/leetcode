"""
295. Find Median from Data Stream
---------------------------------
Difficulty: Hard

The median is the middle value in a sorted list of integers.
For lists of even length, there is no middle value,
so the median is the mean of the two middle values.
For example:
For arr = [1,2,3], the median is 2.
For arr = [1,2], the median is (1 + 2) / 2 = 1.5

Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far.

Example 1:
Input:
["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]
Output:
[null, null, 1.0, null, 2.0, null, 2.0]
Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.findMedian(); // return 1.0
medianFinder.addNum(3);    // arr = [1, 3]
medianFinder.findMedian(); // return 2.0
medianFinder.addNum(2);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:
-100,000 <= num <= 100,000
findMedian will only be called after adding at least one integer to the data structure.
"""


class MedianFinderSorting:
    def __init__(self):
        self.data: list[int] = []

    def add_number(self, number: int) -> None:
        """Time complexity: O(1)"""
        self.data.append(number)

    def find_median(self) -> float:
        """Time complexity: O(m * n log n) where
        - m is the number of function calls
        - and n is the number of elements in the data structure"""
        self.data.sort()
        length = len(self.data)
        if length % 2:
            return self.data[length // 2]
        else:
            return (self.data[length // 2] + self.data[length // 2 - 1]) / 2


def test_median_finder():
    solutions = [
        MedianFinderSorting(),
    ]

    for solution in solutions:
        solution.add_number(1)
        assert solution.find_median() == 1.0

        solution.add_number(3)
        assert solution.find_median() == 2.0

        solution.add_number(2)
        assert solution.find_median() == 2.0

        print(f'{solution.__class__.__name__} passed all tests!')


if __name__ == '__main__':
    test_median_finder()
