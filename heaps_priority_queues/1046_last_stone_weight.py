"""
1046. Last Stone Weight
--------------------------------
Difficulty: Easy

You are given an array of integers stones where stones[i] represents the weight of the
i-th stone.

We want to run a simulation on the stones as follows:
At each step we choose the two heaviest stones, with weight x and y and smash them
together
- If x == y, both stones are destroyed
- If x < y, the stone of weight x is destroyed, and the stone of weight y has new
weight y - x.
Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

Example 1:
Input: stones = [2,3,6,2,4]
Output: 1
Explanation:
We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
We smash 2 and 2, so the array becomes [1].

Example 2:
Input: stones = [1,2]
Output: 1
Constraints:
1 <= stones.length <= 20
1 <= stones[i] <= 100

"""
import heapq


class Solution:
    def last_stone_weight_with_sorting(self, stones: list[int]) -> int:
        """Time complexity: O(n^2 * log(n))"""
        while len(stones) > 1:
            stones.sort()
            if current := (stones.pop() - stones.pop()):
                stones.append(current)

        return stones[0] if stones else 0

    def last_stone_weight_with_binary_search(self, stones: list[int]) -> int:
        """Time complexity: O(n^2)"""
        stones.sort()
        remaining = len(stones)

        while remaining > 1:
            remaining -= 2
            if current := (stones.pop() - stones.pop()) > 0:
                left_idx, right_idx = 0, remaining
                while left_idx < right_idx:
                    middle = (left_idx + right_idx) // 2
                    if stones[middle] < current:
                        left_idx = middle + 1
                    else:
                        right_idx = middle

                position = left_idx
                remaining += 1
                stones[position:position] = [current]

        return stones[0] if remaining > 0 else 0

    def last_stone_weight_with_heap(self, stones: list[int]) -> int:
        """Time complexity: O(n * log(n))"""
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])


TEST_INPUTS = [
    [2, 3, 6, 2, 4],
    [1, 2],
]
TEST_OUTPUTS = [1, 1]


def test_last_stone_weight():
    solution = Solution()
    solutions = [
        solution.last_stone_weight_with_sorting,
        solution.last_stone_weight_with_binary_search,
        solution.last_stone_weight_with_heap,
    ]

    for solution_method in solutions:
        for input_, output in zip(TEST_INPUTS, TEST_OUTPUTS):
            assert solution_method(input_) == output

        print(f'All tests passed for {solution_method.__name__}')


if __name__ == '__main__':
    test_last_stone_weight()
