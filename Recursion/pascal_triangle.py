'''
Problem
-------------------
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Constraints
-------------------
* 0 <= rowIndex <= 33

Thinking
-------------------
* recurssion - top down
    * triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

* base case
    * i == 0, triangle[0][j] = 1
    * j == 0 or if i == j, triangle[j][j] = 1
    * j < 0, or j > i, 0
'''
from typing import List


def getRow(rowIndex: int) -> List[int]:
    row = [[-1 for j in range(rowIndex)] for i in range(rowIndex)]

    row[0][0] = 1

    def helper(i, j):
        if i == 0:
            return 1
        if j == 0 or j == i:
            return 1
        if j < 0 or j > i:
            return 0

        if row[i][j] != -1:
            return row[i][j]

        val = helper(i-1, j-1) + helper(i-1, j)
        row[i][j] = val
        return val

    ret = [-1 for _ in range(rowIndex)]
    for j in range(rowIndex):
        ret[j] = helper(rowIndex-1, j)
    return ret


if __name__ == "__main__":
    print(getRow(4))
