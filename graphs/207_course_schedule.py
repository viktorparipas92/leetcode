"""
207. Course Schedule
--------------------
Difficulty: Medium

You are given an array prerequisites where prerequisites[i] = [a, b]
indicates that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.
There are a total of numCourses courses you are required to take,
labeled from 0 to numCourses - 1.
Return true if it is possible to finish all courses, otherwise return false.

Example 1:
Input: numCourses = 2, prerequisites = [[0,1]]
Output: true
Explanation: First take course 1 (no prerequisites) and then take course 0.

Example 2:
Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
Output: false
Explanation: In order to take course 1 you must take course 0,
and to take course 0 you must take course 1. So it is impossible.

Constraints:
1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
All prerequisite pairs are unique.
"""


def can_finish_dfs(num_courses: int, prerequisites: list[tuple[int, int]]) -> bool:
    """
    Time complexity: O(V + E)
    Space complexity: O(V + E)
    where
    - V is the number of courses (vertices),
    - E is the number of prerequisite pairs (edges).
    """
    def depth_first_search(course: int) -> bool:
        if course in visited_courses:  # Cycle detected
            return False

        if not prerequisite_map[course]:
            return True

        visited_courses.add(course)
        prerequisites_for_course = prerequisite_map[course]
        for prerequisite in prerequisites_for_course:
            if not depth_first_search(course=prerequisite):
                return False

        visited_courses.remove(course)
        prerequisite_map[course] = []
        return True

    prerequisite_map: dict[int, list[int]] = {
        i: [prerequisite for course, prerequisite in prerequisites if course == i]
        for i in range(num_courses)
    }

    visited_courses: set[int] = set() # Store all courses along the current DFS path
    return all(
        depth_first_search(course=course) for course in range(num_courses)
    )


def test_can_finish():
    solutions = [
        can_finish_dfs,
    ]

    test_cases = [
        ((2, [(0, 1)]), True),
        ((2, [(0, 1), (1, 0)]), False),
    ]

    for solution in solutions:
        for (args, expected_can_be_finished) in test_cases:
            # Act
            can_be_finished = solution(*args)

            # Assert
            assert can_be_finished == expected_can_be_finished

        print(f'{solution.__name__} passed all tests!')


if __name__ == '__main__':
    test_can_finish()
