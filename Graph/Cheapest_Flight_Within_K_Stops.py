'''
Problem
-------------------
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Constraints
-------------------
* 1 <= n <= 100
* 0 <= flights.length <= (n * (n - 1) / 2)
* flights[i].length == 3
* 0 <= fromi, toi < n
* fromi != toi
* 1 <= pricei <= 104
* There will not be any multiple flights between two cities.
* 0 <= src, dst, k < n
* src != dst

Thinking
-------------------
* Dynamic Programming
    * calcualte the cheapest flight with 1 stop, 2 stops, ... etc.
    * until k stops

* Time Complexity
    * O(k * E)

* Space Complexity
    * O(N * k) - after optimize, O(N)
'''
from typing import List
from collections import defaultdict


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # build the graph as a dictionary:
    # - dest: (from, weight)
    graph = defaultdict(list)
    for f, d, weight in flights:
        graph[d].append((f, weight))

    # initialize the memory array
    prev = [float('inf') for _ in range(n)]
    prev[src] = 0
    # iterate k + 1 times
    for _ in range(k+1):
        cur = prev[:]
        for i in range(n):
            for f, weight in graph[i]:
                cost = prev[f] + weight
                if cost < cur[i]:
                    cur[i] = cost
        prev = cur

    return prev[dst] if prev[dst] < float('inf') else -1


if __name__ == "__main__":
    print(findCheapestPrice(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500], [2, 0, 1]], 0, 2, 3))
