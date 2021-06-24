''' The Problem
-------------------
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

1 <= n <= 104
0 <= edges.length <= 104
edges.length == 2
0 <= ai, bi <= n - 1
0 <= source <= n - 1
0 <= destination <= n - 1
The given graph may have self-loops and parallel edges.

Thinking
--------------------
* no circles on the road, any circle will create an infinite long path

* One destination (only one node with out degree 0)

* DFS, detect circle

* The question is actually asking if ALL paths from SOURCE ends on DESTINATION

Tag: moderate, has to know dfs and avoid some triky cases (loop or parallel path), use set to store nodes
'''


from typing import List
from collections import defaultdict


def leadsToDestination(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    out_edge_map = defaultdict(set)
    for edge in edges:
        out_edge_map[edge[0]].add(edge[1])

    if len(out_edge_map[destination]) > 0:
        return False

    exists_path_to_dest = False
    all_path_to_dest = True
    finite_paths = True

    node_from_source = out_edge_map[source]

    def dfs(node, cur_visited):
        nonlocal exists_path_to_dest, all_path_to_dest, finite_paths

        if not (all_path_to_dest and finite_paths):
            return

        if node == destination:
            exists_path_to_dest = True
            return

        node_next = out_edge_map[node]
        if len(node_next) == 0:
            all_path_to_dest = False
            return

        for next in node_next:
            if next in cur_visited:
                finite_paths = False
                return
            cur_visited.add(next)
            dfs(next, cur_visited)
            cur_visited.remove(next)
        return
    dfs(source, set([source]))

    return exists_path_to_dest and all_path_to_dest and finite_paths


print(leadsToDestination(3, [[0, 1], [1, 2]], 0, 2))
