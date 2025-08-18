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
import heapq
from collections import defaultdict, deque


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


def network_delay_time_floyd_warshall(
    times: list[list[int]], n: int, k: int
) -> float:
    """
    Time complexity: O(V^3)
    Space complexity: O(V^2)
    where V is the number of vertices (nodes).
    """
    inf = float('inf')
    node_min_times: list[list[float]] = [[inf] * n for _ in range(n)]

    for source, target, duration in times:
        node_min_times[source - 1][target - 1] = duration

    for i in range(n):
        node_min_times[i][i] = 0

    for mid in range(n):
        for i in range(n):
            for j in range(n):
                node_min_times[i][j] = min(
                    node_min_times[i][j],
                    node_min_times[i][mid] + node_min_times[mid][j],
                )

    delay_time: float = max(node_min_times[k - 1])
    return delay_time if delay_time < inf else -1


def network_delay_time_bellman_ford(
    times: list[list[int]], n: int, k: int
) -> float:
    """
    Time complexity: O(V * E)
    Space complexity: O(V)
    where V is the number of vertices (nodes) and E is the number of edges.
    """
    min_time_to_each_node: list[float] = [float('inf')] * n
    min_time_to_each_node[k - 1] = 0
    for _ in range(n - 1):
        for source, target, duration in times:
            if min_time_to_each_node[source - 1] + duration < min_time_to_each_node[target - 1]:
                min_time_to_each_node[target - 1] = min_time_to_each_node[source - 1] + duration
    max_dist: float = max(min_time_to_each_node)
    return max_dist if max_dist < float('inf') else -1


def network_delay_time_shortest_path_faster(
    times: list[list[int]], n: int, k: int
) -> float:
    """
    Time complexity: O(V + E) in the avarege case
    Space complexity: O(V + E)
    """
    adjacency_list = defaultdict(list)
    for source, target, duration in times:
        adjacency_list[source].append((target, duration))

    node_min_time_map: dict[int, float] = {node: float('inf') for node in range(1, n + 1)}
    queue: deque[tuple[int, int]] = deque([(k, 0)])
    node_min_time_map[k] = 0

    while queue:
        node, time = queue.popleft()
        if node_min_time_map[node] < time:
            continue

        for neighbour, duration in adjacency_list[node]:
            if time + duration < node_min_time_map[neighbour]:
                new_time = time + duration
                node_min_time_map[neighbour] = new_time
                queue.append((neighbour, new_time))

    result = max(node_min_time_map.values())
    return result if result < float('inf') else -1


def network_delay_time_dijkstra(
    times: list[list[int]], n: int, k: int
) -> float:
    """
    Time complexity: O(E * log V)
    Space complexity: O(V + E)
    """
    adjacency_list = defaultdict(list)
    for source, target, duration in times:
        adjacency_list[source].append((target, duration))

    nodes_by_min_time: list[tuple[int, int]] = [(0, k)]
    visited_nodes: set[int] = set()
    max_signal_time: int = 0
    while nodes_by_min_time:
        current_time, current_node = heapq.heappop(nodes_by_min_time)
        if current_node in visited_nodes:
            continue

        visited_nodes.add(current_node)
        max_signal_time = current_time

        for neighbour_node, travel_time in adjacency_list[current_node]:
            if neighbour_node not in visited_nodes:
                heapq.heappush(
                    nodes_by_min_time, (current_time + travel_time, neighbour_node)
                )

    return max_signal_time if len(visited_nodes) == n else -1



def test_network_delay_time():
    solutions = [
        network_delay_time_depth_first_search,
        network_delay_time_floyd_warshall,
        network_delay_time_bellman_ford,
        network_delay_time_shortest_path_faster,
        network_delay_time_dijkstra,
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