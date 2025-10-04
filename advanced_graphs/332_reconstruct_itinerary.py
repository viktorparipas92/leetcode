"""
332. Reconstruct Itinerary
----------------------------
Difficulty: Hard

You are given a list of flight tickets where tickets[i] = [from_i, to_i]
represent the source airport and the destination airport.
Each from_i and to_i consists of three uppercase English letters.
Reconstruct the itinerary in order and return it.

All the tickets belong to someone who originally departed from "JFK".
Your objective is to reconstruct the flight path that this person took,
assuming each ticket was used exactly once.

If there are multiple valid flight paths, return the lexicographically smallest one.
For example, the itinerary ["JFK", "SEA"] has a smaller lexical order than ["JFK", "SFO"].
You may assume all the tickets form at least one valid flight path.

Example 1:
Input: tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
Output: ["JFK","BUF","HOU","SEA"]

Example 2:
Input: tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]
Output: ["JFK","HOU","JFK","SEA","JFK"]
Explanation: Another possible reconstruction is ["JFK","SEA","JFK","HOU","JFK"]
but it is lexicographically larger.

Constraints:
1 <= tickets.length <= 300
from_i != to_i
"""
from collections import defaultdict

START_AIRPORT = 'JFK'

def find_itinerary_dfs(tickets: list[tuple[str, str]]) -> list[str]:
    """
    Time complexity: O(E * V)
    Space complexity: O(E + V)
    where E is the number of tickets (edges), and V is the number of airports (vertices).
    """
    def depth_first_search(_source: str) -> bool:
        if len(itinerary) == len(tickets) + 1:
            return True

        if _source not in adjacency_list:
            return False

        temp_next_airports = list(adjacency_list[_source])
        for _src, _dst in enumerate(temp_next_airports):
            adjacency_list[_source].pop(_src)
            itinerary.append(_dst)
            if depth_first_search(_dst):
                return True

            adjacency_list[_source].insert(_src, _dst)
            itinerary.pop()

        return False

    adjacency_list: dict[str, list[str]] = {src: [] for src, dst in tickets}

    tickets.sort()
    for source, destination in tickets:
        adjacency_list[source].append(destination)

    itinerary: list[str] = [START_AIRPORT]
    depth_first_search(START_AIRPORT)
    return itinerary


def find_itinerary_hierholzer(tickets: list[tuple[str, str]]) -> list[str]:
    """
    Time complexity: O(E log E)
    Space complexity: O(E)
    """
    def depth_first_search(_source):
        while adjacency_list[_source]:
            _destination = adjacency_list[_source].pop()
            depth_first_search(_destination)

        itinerary.append(_source)

    adjacency_list: dict[str, list] = defaultdict(list)
    for source, destination in sorted(tickets)[::-1]:
        adjacency_list[source].append(destination)

    itinerary: list[str] = []

    depth_first_search(START_AIRPORT)
    return itinerary[::-1]


def test_find_itinerary():
    solutions = [
        find_itinerary_dfs,
        find_itinerary_hierholzer,
    ]

    test_cases = [
        ([('BUF', 'HOU'), ('HOU', 'SEA'), ('JFK', 'BUF')], ['JFK', 'BUF', 'HOU', 'SEA']),
        (
            [('HOU', 'JFK'), ('SEA', 'JFK'), ('JFK', 'SEA'), ('JFK', 'HOU')],
            ['JFK', 'HOU', 'JFK', 'SEA', 'JFK'],
        ),
    ]

    for solution in solutions:
        for tickets, expected_itinerary in test_cases:
            # Act
            itinerary = solution(tickets)

            # Assert
            assert itinerary == expected_itinerary

        print(f'{solution.__name__} passed all tests')


if __name__ == '__main__':
    test_find_itinerary()
