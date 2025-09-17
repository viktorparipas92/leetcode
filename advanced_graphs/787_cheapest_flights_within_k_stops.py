"""
787. Cheapest Flights Within K Stops
--------------------------------
Difficulty: Medium

There are n airports, labeled from 0 to n - 1, which are connected by some flights.
You are given an array flights where flights[i] = [from_i, to_i, price_i] represents
a one-way flight from airport from_i to airport to_i with cost price_i.
You may assume there are no duplicate flights and no flights from an airport to itself.
You are also given three integers src, dst, and k where:
- src is the starting airport
- dst is the destination airport
  src != dst
- k is the maximum number of stops you can make (not including src and dst)
Return the lowest price from src to dst with at most k stops,
or return -1 if it is impossible.

Example 1:
Input: n = 4, flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]], src = 0, dst = 3, k = 1
Output: 500
Explanation:
The optimal path with at most 1 stop from airport 0 to 3 is shown in red,
with total cost 200 + 300 = 500.
Note that the path [0 -> 1 -> 2 -> 3] costs only 400, and thus is cheaper,
but it requires 2 stops, which is more than k.

Example 2:
Input: n = 3, flights = [[1,0,100],[1,2,200],[0,2,100]], src = 1, dst = 2, k = 1
Output: 200
Explanation:
The optimal path with at most 1 stop from airport 1 to 2 is shown in red
and has cost 200.

Constraints:
1 <= n <= 100
fromi != toi
1 <= pricei <= 1000
0 <= src, dst, k < n
"""
import heapq

INFINITY = float('inf')


def find_lowest_price_dijkstra(
    num_airports: int,
    flights: list[tuple[int, int, int]],
    source: int,
    destination: int,
    max_stops: int
):
    """
    Time complexity: O(n * k)
    Space complexity: O(n + m)
    where n = num_airports and k = max_stops and m = num_flights
    """
    adjacency_list: list[list[tuple[int, int]]] = [
        [(_destination, cost) for __source, _destination, cost in flights if __source == _source]
        for _source in range(num_airports)
    ]

    distances: list[list[float]] = [[INFINITY] * (max_stops + 5) for _ in range(num_airports)]  # 5 is arbitrary
    distances[source][0] = 0
    to_heap: list[tuple[int, int, int]] = [(0, source, -1)]  # cost, node, num_stops
    while to_heap:
        cost, airport, num_stops = heapq.heappop(to_heap)
        if destination == airport:
            return cost

        elif num_stops == max_stops or distances[airport][num_stops + 1] < cost:
            continue

        for neighbour, cost_to_neighbour in adjacency_list[airport]:
            next_cost = cost + cost_to_neighbour
            next_num_stops = 1 + num_stops
            if distances[neighbour][next_num_stops + 1] > next_cost:
                distances[neighbour][next_num_stops + 1] = next_cost
                heapq.heappush(to_heap, (next_cost, neighbour, next_num_stops))

    cost = -1
    return cost


def find_lowest_price_bellman_ford(
    num_airports: int,
    flights: list[tuple[int, int, int]],
    source: int,
    destination: int,
    max_stops: int
):
    prices = [INFINITY] * num_airports
    prices[source] = 0

    for i in range(max_stops + 1):
        temporary_prices = prices.copy()

        for _src, _dst, _price in flights:
            if prices[_src] == INFINITY:
                continue

            if prices[_src] + _price < temporary_prices[_dst]:
                temporary_prices[_dst] = prices[_src] + _price

        prices = temporary_prices

    return -1 if prices[destination] == INFINITY else prices[destination]


def test_find_lowest_price():
    solutions = [
        find_lowest_price_dijkstra,
        find_lowest_price_bellman_ford,
    ]

    test_cases = [
        (4, [(0, 1, 200), (1, 2, 100), (1, 3, 300), (2, 3, 100)], 0, 3, 1, 500),
        (3, [(1, 0, 100), (1, 2, 200), (0, 2, 100)], 1, 2, 1, 200),
    ]

    for solution in solutions:
        for n, flights, src, dst, k, expected_min_cost in test_cases:
            # Act
            min_cost = solution(n, flights, src, dst, k)

            # Assert
            assert min_cost == expected_min_cost

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_find_lowest_price()
