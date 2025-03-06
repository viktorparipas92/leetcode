"""
621. Task Scheduler
-------------------
Difficulty: Medium

You are given an array of CPU tasks tasks, where tasks[i] is an uppercase English
character from A to Z. You are also given an integer n.
Each CPU cycle allows the completion of a single task, and tasks may be completed in
any order. The only constraint is that identical tasks must be separated by at least
n CPU cycles, to cool down the CPU.
Return the minimum number of CPU cycles required to complete all tasks.

Example 1:
Input: tasks = ["X","X","Y","Y"], n = 2
Output: 5
Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

Example 2:
Input: tasks = ["A","A","A","B","C"], n = 3
Output: 9
Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

Constraints:
1 <= tasks.length <= 1000
0 <= n <= 100
"""
import heapq
from collections import Counter, deque


def least_interval_max_heap(tasks: list[str], n: int) -> int:
    """
    Time complexity: O(m) where m is the number of tasks
    Space complexity: O(1)
    """
    task_counts = Counter(tasks)
    max_heap = [-count for count in task_counts.values()]
    heapq.heapify(max_heap)

    time = 0
    queue: deque[tuple[int, int]] = deque()  # (count, time)
    while max_heap or queue:  # While there are tasks to process
        time += 1
        if not max_heap:
            time = queue[0][1]  # Idle
        else:
            if count := 1 + heapq.heappop(max_heap):  # Process task
                queue.append((count, time + n))  # Add to cooldown queue

        if queue and queue[0][1] == time:  # Cooldown is over
            heapq.heappush(max_heap, queue.popleft()[0])  # Add back to max heap

    return time


def test_least_interval():
    solutions = [
        least_interval_max_heap,
    ]

    test_cases = [
        (['X', 'X', 'Y', 'Y'], 2, 5),
        (['A', 'A', 'A', 'B', 'C'], 3, 9),
    ]

    for solution in solutions:
        for tasks, n, expected_cycles in test_cases:
            # Act
            cycles = solution(tasks, n)

            # Assert
            assert cycles == expected_cycles

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_least_interval()
