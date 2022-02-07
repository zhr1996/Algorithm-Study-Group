'''
Problem
-------------------
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Constraints
-------------------
* rows == heights.length
* columns == heights[i].length
* 1 <= rows, columns <= 100
* 1 <= heights[i][j] <= 10^6

Thinking
-------------------
* Variant of Dikistra algorithm
    * find single source shortest path
    * just instead the path weight now is the max absolute difference

* Dikistra
    * if we can find shortest path to a vertex, further shortest path will be build on this result
        * we won't choose longer path to go to the vertex
'''
from typing import List
from collections import defaultdict
import heapq


def minimumEffortPath(heights: List[List[int]]) -> int:
    graph = defaultdict(list)
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            for dx, dy in directions:
                if 0 <= i + dx < len(heights) and 0 <= j + dy < len(heights[0]):
                    graph[(i, j)].append(
                        (abs(heights[i][j] - heights[i+dx][j+dy]), i+dx, j+dy))

    pq = []

    heapq.heappush(pq, (0, 0, 0))

    efforts = {}

    while pq:
        e, x, y = heapq.heappop(pq)
        if (x, y) in efforts:
            continue

        efforts[(x, y)] = e
        # if already reached the bottom-right point, return
        if x == len(heights) - 1 and y == len(heights[0]) - 1:
            return e

        # push in efforts of neighbors of current point
        for n_e, n_x, n_y in graph[(x, y)]:
            if (n_x, n_y) in efforts:
                continue
            effort = max(n_e, e)
            heapq.heappush(pq, (effort, n_x, n_y))
    # the answer would one hundred percent returned in loop
    return -1


if __name__ == "__main__":
    print(minimumEffortPath([[1, 2], [5, 2]]))
