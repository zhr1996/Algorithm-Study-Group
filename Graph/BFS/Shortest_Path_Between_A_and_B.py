from typing import Dict, List
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val


def get_length_of_shortest_path(graph: Dict[Node, List[Node]], A: Node, B: Node) -> int:
    # Use BFS to find the level and return the level
    level = 0
    queue = deque([A])
    visited = set()
    # Do a level traversal, remember to traverse every node that already in the list
    while len(queue) != 0:
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            if node == B:
                return level
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    queue.append(child)
        level += 1
    return -1


if __name__ == "__main__":
    n = int(input())
    nodes = {i:  Node(i) for i in range(n)}
    graph = {nodes[i]: [] for i in range(n)}
    for i in range(n):
        graph[nodes[i]] = [nodes[int(j)] for j in input().split()]
    A = nodes[int(input())]
    B = nodes[int(input())]
    print(get_length_of_shortest_path(graph, A, B))
