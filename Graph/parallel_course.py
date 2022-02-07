'''
Problem
-------------------
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.

Constraints
-------------------
* 1 <= n <= 5000
* 1 <= relations.length <= 5000
* relations[i].length == 2
* 1 <= prevCoursei, nextCoursei <= n
* prevCoursei != nextCoursei
* All the pairs [prevCoursei, nextCoursei] are unique.

Thinking
-------------------
* topological sort

* kind of like BFS, each iteration take out all zero indegree course in the queue. count how many iteration needed to finish all the course

* build the graph: O(E)

* topological sorting O(E)
    * O(E) to decrement indegree of neighbor nodes

* Time complexity: O(E)
'''
from typing import List
from collections import defaultdict, deque


def minimumSemesters(n: int, relations: List[List[int]]) -> int:
    graph = defaultdict(list)
    in_degree_count = [0] * (n + 1)

    zero_degree_queue = deque()

    for edge in relations:
        node0, node1, = edge[0], edge[1]
        graph[node0].append(node1)
        in_degree_count[node1] += 1

    for i in range(1, n + 1):
        if in_degree_count[i] == 0:
            zero_degree_queue.appendleft(i)

    iterations = 0
    course_taken = 0
    while zero_degree_queue:
        iterations += 1
        m = len(zero_degree_queue)
        for _ in range(m):
            course = zero_degree_queue.pop()
            course_taken += 1
            for next_course in graph[course]:
                in_degree_count[next_course] -= 1
                if in_degree_count[next_course] == 0:
                    zero_degree_queue.appendleft(next_course)
    if course_taken < n:
        return -1
    return iterations


if __name__ == "__main__":
    print(minimumSemesters(4, [[1, 3]]))
