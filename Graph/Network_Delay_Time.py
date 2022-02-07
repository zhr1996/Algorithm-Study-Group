'''
Problem
-------------------
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Constraints
-------------------
* 1 <= k <= n <= 100
* 1 <= times.length <= 6000
* times[i].length == 3
* 1 <= ui, vi <= n
* ui != vi
* 0 <= wi <= 100
* All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

Thinking
-------------------
* single source shorted path

* find the longest path amont the shortest paths

* Dikistra
    * use a heap to store all the length of path from source node

    * every time pop the shortest path
        * if has been added to dist dictionary, continue
        * if not, add the node in dist dictionary. Also add the path that pass through this node
    
* return the largest value in the dictionary

'''
from typing import List
from collections import defaultdict
import heapq


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    # find shortest path to each node
    # keep a variable to store the length of longest path

    # 1. convert to a graph represnt by dictionary (hashmap)
    graph = defaultdict(list)
    for path in times:
        node_1 = path[0]
        node_2 = path[1]
        delay = path[2]
        graph[node_1].append((node_2, delay))

    seen = set()
    dist = {node: float("inf") for node in range(1, n + 1)}
    dist[k] = 0

    # 2. greedy add in the shortest path from source to node until there are no nodes in graph
    while True:
        cand_dist = float("inf")
        cand_node = -1

        for node in range(1, n+1):
            if dist[node] < cand_dist and node not in seen:
                cand_node = node
                cand_dist = dist[node]
        if cand_node == -1:
            break

        seen.add(cand_node)
        # 3. add cand_node, update the dist dictionary accordingly, compare if the original distance is shorter, or the path has current node is shorter
        for node, delay in graph[cand_node]:
            dist[node] = min(dist[node], dist[cand_node] + delay)

    # 4. if all nodes are reachable (max distance is smaller than infinity), return max(dist.values())
    #    if the max distance is great or equal to infinite, then it means some of the nodes are not reachable, return -1
    max_distance = max(dist.values())
    return max_distance if max_distance < float('inf') else -1


def networkDelayTime_heap(times: List[List[int]], n: int, k: int) -> int:
    # 1. build the graph
    graph = defaultdict(list)
    for u, v, d in times:
        graph[u].append((v, d))

    # 2. initialize a priority queue with the start point in it
    pq = [(0, k)]

    # 3. initialize a dist dictionary to store the shortest path
    dist = {}

    # 4. continue pop from the pq until pq is empty
    #    add in the edges from the node gets poped evertime pop a node from the queue
    while pq:
        d, node = heapq.heappop(pq)

        if node in dist:
            continue

        dist[node] = d

        for next_node, d2 in graph[node]:
            if next_node not in dist:
                heapq.heappush(pq, (d + d2, next_node))

    return max(dist.values()) if len(dist) == n else -1


if __name__ == "__main__":
    print(networkDelayTime_heap(
        [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
