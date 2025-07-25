"""
210. Course Schedule II
-----------------------
Difficulty: Medium

You are given an array prerequisites where prerequisites[i] = [a, b] indicates that
you must take course b first if you want to take course a.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return a valid ordering of courses you can take to finish all courses.
If there are many valid answers, return any of them.
If it's not possible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 3, prerequisites = [[1,0]]
Output: [0,1,2]
Explanation: We must ensure that course 0 is taken before course 1.

Example 2:
Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
Output: []
Explanation: It's impossible to finish all courses.

Constraints:
1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
All prerequisite pairs are unique.
"""
from collections import deque


def find_order_cycle_detection_dfs(num_courses: int, prerequisites: list[tuple[int, int]]) -> list[int]:
    """
    Time complexity: O(V + E)
    Space complexity: O(V + E)
    where
    - V is the number of courses (vertices),
    - E is the number of prerequisite pairs (edges).
    """
    def depth_first_search(_course: int):
        if _course in cycle:
            return False

        if _course in courses_visited:
            return True

        cycle.add(_course)
        if any_false := any(
            not depth_first_search(_prerequisite)
            for _prerequisite in prerequisites_per_course[_course]
        ):
            return False

        cycle.remove(_course)
        courses_visited.add(_course)
        schedule.append(_course)
        return True

    prerequisites_per_course: dict[int, list[int]] = {c: [] for c in range(num_courses)}
    for course, prerequisite in prerequisites:
        prerequisites_per_course[course].append(prerequisite)

    schedule: list[int] = []
    courses_visited: set[int] = set()
    cycle: set[int] = set()
    return (
        []
        if any(not depth_first_search(course) for course in range(num_courses))
        else schedule
    )


def find_order_topological_sort_kahn(num_courses: int, prerequisites: list[tuple[int, int]]) -> list[int]:
    """
    Time complexity: O(V + E)
    Space complexity: O(V + E)
    where
    - V is the number of courses (vertices),
    - E is the number of prerequisite pairs (edges).
    """
    num_following_courses: list[int] = [0] * num_courses
    # Adjacency list to store prerequisites for each course
    prerequisites_by_course: list[list[int]] = [[] for i in range(num_courses)]

    for course, prerequisite in prerequisites:
        num_following_courses[prerequisite] += 1
        prerequisites_by_course[course].append(prerequisite)

    courses_not_required: deque = deque(
        [p for p in range(num_courses) if num_following_courses[p] == 0]
    )

    num_courses_processed: int = 0
    schedule = []
    while courses_not_required:
        cnr = courses_not_required.popleft()
        schedule.append(cnr)

        num_courses_processed += 1

        for _prerequisite in prerequisites_by_course[cnr]:
            num_following_courses[_prerequisite] -= 1
            if num_following_courses[_prerequisite] == 0:
                courses_not_required.append(_prerequisite)

    if num_courses_processed != num_courses:
        return []

    return schedule[::-1]


def find_order_topological_sort_dfs(num_courses: int, prerequisites: list[tuple[int, int]]) -> list[int]:
    """
    Time complexity: O(V + E)
    Space complexity: O(V + E)
    """
    def depth_first_search(_course):
        schedule.append(_course)
        num_following_courses[_course] -= 1
        for _prerequisite in prerequisites_by_course[_course]:
            num_following_courses[_prerequisite] -= 1
            if num_following_courses[_prerequisite] == 0:
                depth_first_search(_prerequisite)

    prerequisites_by_course: list[list[int]] = [[] for i in range(num_courses)]
    num_following_courses: list[int] = [0] * num_courses
    for next_course, prerequisite in prerequisites:
        num_following_courses[next_course] += 1
        prerequisites_by_course[prerequisite].append(next_course)

    schedule = []
    for course in range(num_courses):
        if num_following_courses[course] == 0:
            depth_first_search(course)

    return schedule if len(schedule) == num_courses else []


def test_find_order():
    solutions = [
        find_order_cycle_detection_dfs,
        find_order_topological_sort_kahn,
        find_order_topological_sort_dfs,
    ]

    possible_solutions = [[0, 1, 2], [0, 2, 1], [2, 0, 1]]
    test_cases = [
        ((3, [(1, 0)]), possible_solutions),
        ((3, [(0, 1), (1, 2), (2, 0)]), [[]]),
    ]

    for solution in solutions:
        for (num_courses, prerequisites), expected_schedules in test_cases:
            # Act
            schedule = solution(num_courses, prerequisites)

            # Assert
            assert schedule in expected_schedules

        print(f'{solution.__name__} passed all tests!')


if __name__ == '__main__':
    test_find_order()
