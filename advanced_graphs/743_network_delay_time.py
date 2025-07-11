"""
743. Network Delay Time
-----------------------
Difficulty: Medium

You are given a network of n directed nodes, labeled from 1 to n.
 You are also given times, a list of directed edges where times[i] = (ui, vi, ti).
ui is the source node (an integer from 1 to n)
vi is the target node (an integer from 1 to n)
ti is the time it takes for a signal to travel from the source to the target node
(an integer greater than or equal to 0).
You are also given an integer k, representing the node that we will send a signal from.

Return the minimum time it takes for all the n nodes to receive the signal.
If it is impossible for all the nodes to receive the signal, return -1 instead.

Example 1:
Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1
Output: 3

Example 2:
Input: times = [[1,2,1],[2,3,1]], n = 3, k = 2
Output: -1

Constraints:
1 <= k <= n <= 100
1 <= times.length <= 1000
"""
from collections import defaultdict


def network_delay_time_depth_first_search(
    times: list[list[int]], n: int, k: int
) -> int:
    """
    Time complexity: O(V * E)
    Space complexity: O(V + E)
    where V is the number of vertices (nodes) and E is the number of edges.
    """
    def depth_first_search(node: int, time: int) -> None:
        if time >= node_min_time_map[node]:
            return

        node_min_time_map[node] = time
        for neighbour, duration in adjacency_list[node]:
            depth_first_search(neighbour, time + duration)

    adjacency_list = defaultdict(list)
    for source, target, duration in times:
        adjacency_list[source].append((target, duration))

    node_min_time_map: dict[int, float] = {
        node: float('inf') for node in range(1, n + 1)
    }

    depth_first_search(node=k, time=0)
    delay_time = max(node_min_time_map.values())
    return delay_time if delay_time < float('inf') else -1


def test_network_delay_time():
    solutions = [
        network_delay_time_depth_first_search,
    ]

    test_cases = [
        ([(1, 2, 1), (2, 3, 1), (1, 4, 4), (3, 4, 1)], 4, 1, 3),
        ([(1, 2, 1), (2, 3, 1)], 3, 2, -1),
    ]

    for solution in solutions:
        for times, n, k, expected_delay_time in test_cases:
            # Act
            delay_time = solution(times, n, k)

            # Assert
            assert delay_time == expected_delay_time

        print(f'{solution.__name__} passed all tests!')


if __name__ == '__main__':
    test_network_delay_time()