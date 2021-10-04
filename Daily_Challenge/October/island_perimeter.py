'''
Problem
-------------------
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Constraints
-------------------
* row == grid.length
* col == grid[i].length
* 1 <= row, col <= 100
* grid[i][j] is 0 or 1.
* There is exactly one island in grid.

Thinking
-------------------
* First think clear about what the problem wants, the problem wants us to calculate the perimeter

* In usual case, a cubic would have perimeter 4, but when it has a neighbor, then one side is not considered as perimeter, since it's shared with a neighbor

* so in total going through cubic one by one, add 4 first, if find a neighbor, minus 1 from total.
'''
from typing import List


def islandPerimeter(grid: List[List[int]]) -> int:
    perimeter = 0
    m = len(grid)
    n = len(grid[0])

    def get_neighbor(i, j):
        x = [0, -1, 0, 1]
        y = [-1, 0, 1, 0]
        for k in range(4):
            neighbor_x = i + x[k]
            neighbor_y = j + y[k]
            if 0 <= neighbor_x < m and 0 <= neighbor_y < n:
                yield grid[neighbor_x][neighbor_y]
            else:
                yield 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                perimeter += 4
                for neighbor in get_neighbor(i, j):
                    if neighbor == 1:
                        # current line doesn't count as border, so both minus 1
                        perimeter -= 1
    return perimeter


if __name__ == "__main__":
    print(islandPerimeter([[1, 0], [1, 0]]))
