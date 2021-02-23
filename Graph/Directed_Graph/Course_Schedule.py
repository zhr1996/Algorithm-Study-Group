from collections import defaultdict
from enum import Enum


class State:
    TO_VISIT = 0
    VISITING = 1
    VISITED = 2


def is_valid_course_schedule(n, prerequisites):
    # WRITE YOUR BRILLIANT CODE HERE
    def build_graph():
        graph = defaultdict(list)
        for src, dest in prerequisites:
            graph[src] = dest

    def dfs(start, states):
        states[start] = State.VISITING
        for dest in graph[start]:
            if states[dest] == State.VISITED:
                continue

            if states[dest] == State.VISITING:
                return False

            dfs(dest)


if __name__ == "__main__":
    n = int(input())
    num_deps = int(input())
    deps = [[int(x) for x in input().split()] for _ in range(num_deps)]
    if is_valid_course_schedule(n, deps):
        print('true')
    else:
        print('false')
