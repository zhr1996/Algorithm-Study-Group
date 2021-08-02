'''
Problem
-------------------
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Constraints
-------------------
n == grid.length\
n == grid[i].length\
1 <= n <= 500\
grid[i][j] is either 0 or 1.\

Thinking
-------------------
* Matrix problem

* No idea at first, search for article online

* Union - Find, we could form a union of one's, and store the area of islands in the parent element.
    * In this way, we can get the area of each island easily in O(1)

* Next we traverse each element and try to turn 0 to 1. Sum up the area of its four neighbors, and compare the result to current max

* Time Complexity: O(N^2)
    * Use find to re-organize union each time

* Implemention:
    * Give each island a unique number, keep island and corresponding area in a dictionary. Use a dfs to sum up the area.

* Reflect:
    * This is a tricky one, even though figured out how to do it. Thera are still quite a lot of implementaion details.
    * Next time, remember to use dfs to traverse and get the islands. Use an additional dictionary to keep track of each island's area.
'''
from typing import List


def largestIsland(grid: List[List[int]]) -> int:
    n = len(grid)
    island_index = [[-1 for y in range(n)] for x in range(n)]

    index = 0
    area = {}

    def generate_neighbors(i, j):
        moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        for move in moves:
            dx = move[0]
            dy = move[1]
            if i + dx >= 0 and i + dx < n and j + dy >= 0 and j + dy < n:
                yield(i+dx, j+dy)

    def dfs(i, j, index):
        area_sum = 1
        island_index[i][j] = index
        for neighbor in generate_neighbors(i, j):
            x = neighbor[0]
            y = neighbor[1]
            if grid[x][y] == 1 and island_index[x][y] == -1:
                area_sum += dfs(x, y, index)

        return area_sum

    for i in range(n):
        for j in range(n):
            # Not yet assigned to an island
            if grid[i][j] == 1 and island_index[i][j] == -1:

                area[index] = dfs(i, j, index)
                index += 1
    if area:
        max_area = max(area.values())
    else:
        max_area = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                # Try to change current 0 to 1
                cur_area = 1
                index_set = set()
                for x, y in generate_neighbors(i, j):
                    if grid[x][y] == 1:
                        index_set.add(island_index[x][y])
                for index in index_set:
                    cur_area += area[index]
                max_area = max(max_area, cur_area)
    return max_area


if __name__ == "__main__":
    print(largestIsland([[1, 0], [0, 1]]))
