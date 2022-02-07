'''
Problem
-------------------
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Constraints
-------------------
* 1 <= n <= 2 * 10^4
* edges.length == n - 1
* 0 <= ai, bi < n
* ai != bi
* All the pairs (ai, bi) are distinct.
* The given input is guaranteed to be a tree and there will be no repeated edges.

Thinking
-------------------
* MHT (Minimum Height Tree)

* Trim the leaves until reach the centroid

* It's important to realize there are no more than 2 centroids
    * if there are three centroids, it would form a circle, or two of them need to be removed to leave the only centroid left

* Steps
    * build the graph in form of adjacent list (set)
    * count the edges each vertex have, append the vertex has only one edge to leaves queue
        * as we pop each leave, decrement edge count of its neightbors by one
        * as we decrement, again add in each vertex has edge count one (the leave vertex)
    * loop until there are less or equal to 2
'''
from typing import List
from collections import defaultdict
from collections import deque


def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    edge_count = [0] * n
    vertex_set = set([i for i in range(n)])
    for edge in edges:
        vertex1, vertex2 = edge[0], edge[1]
        graph[vertex1].append(vertex2)
        edge_count[vertex1] += 1
        graph[vertex2].append(vertex1)
        edge_count[vertex2] += 1
    leave_queue = deque()
    for vertex in range(n):
        if edge_count[vertex] == 1:
            leave_queue.appendleft(vertex)
    vertex_left = n
    while vertex_left > 2:
        # trim all leaves
        l = len(leave_queue)
        for _ in range(l):
            leave = leave_queue.pop()
            vertex_set.remove(leave)
            for neighbor in graph[leave]:
                edge_count[neighbor] -= 1
                if edge_count[neighbor] == 1:
                    leave_queue.appendleft(neighbor)

        vertex_left -= l

    return [vertex for vertex in vertex_set]


if __name__ == "__main__":
    print(findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
