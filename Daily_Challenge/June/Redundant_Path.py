'''
The Problem
-------------------
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers,
return the answer that occurs last in the input.

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi

Thinking
--------------------
* Remember a algorithm that gradually build a tree by adding each path until there is a circle
* Correction: This algorithm is for finding a minimal spanning tree. This is find a minimal tree that connects every node in a connected graph.

* We can gradually build up the graph by adding each edge in the list

* Use Union-Find, we can union connected vertices and found if the adding edge will form a circle by comparing if their parents are same

Optimization
--------------------
* In each found operation, update the parent to root so next search will be faster

* Compare rank when merging the sets, the rank can be the estimate of heights or the size of the trees. Estimate height is the length of deepest tree. Since find 
  could change the length, so this is an estimate of the height.

'''

from typing import List


def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    parent = [i for i in range(len(edges) + 1)]
    size = [i for i in range(len(edges) + 1)]

    def find(vertex):
        if parent[vertex] == vertex:
            return vertex
        else:
            root = find(parent[vertex])
            parent[vertex] = root
            return root

    def union(vertex_a, vertex_b):
        # Make sure smaller one is parent
        root_a = find(vertex_a)
        root_b = find(vertex_b)

        # Find operation could change the height of a tree, so comparing size also makes sense
        # Since smaller size tree become desecdent means generally there are fewer steps in queries in the future because most nodes have a smaller height
        if size[root_a] >= size[root_b]:
            parent[root_b] = root_a
            size[root_a] += size[root_b]
        else:
            parent[root_a] = root_b
            size[root_b] += size[root_a]

        return

    for edge in edges:
        vertex_a = edge[0]
        vertex_b = edge[1]

        if find(vertex_a) == find(vertex_b):
            return edge
        else:
            union(vertex_a, vertex_b)

    return [-1, -1]


if __name__ == "__main__":
    print(findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
