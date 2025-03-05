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

from collections import Counter


def least_interval_brute_force(tasks: list[str], n: int) -> int:
    """
    Time complexity: O(t * n)
    Space complexity: O(t),
    Where t is the time to process given tasks and n is the cooldown time.
    """
    task_counts = Counter(tasks)
    arr = [
        [count, i] for i, count in enumerate(task_counts.values())
    ]

    time = 0
    processed = []
    while arr:
        maxi = -1
        for i in range(len(arr)):
            if all(
                    processed[j] != arr[i][1] for j in
                    range(max(0, time - n), time)
            ):
                if maxi == -1 or arr[maxi][0] < arr[i][0]:
                    maxi = i

        time += 1
        cur = -1
        if maxi != -1:
            cur = arr[maxi][1]
            arr[maxi][0] -= 1
            if arr[maxi][0] == 0:
                arr.pop(maxi)
        processed.append(cur)

    return time


def test_least_interval():
    solutions = [
        least_interval_brute_force,
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
