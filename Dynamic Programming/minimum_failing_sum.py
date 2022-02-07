'''
Problem
-------------------
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Constraints
-------------------
* n == matrix.length == matrix[i].length
* 1 <= n <= 100
* 100 <= matrix[i][j] <= 100

Thinking
-------------------
* brute force
    * iterate through all possible sums
    * first row n possibilities, next row 3 possibilities, next 3 more 
    * 3^n 

* must be some repetitive work here

* the solution is acutually based on optimal solution of sub-problems
    * for cell in each row, we will always choose the minimal path that falls into it
        * we won't choose larger falling path
    * we can use bottom up approach in this way
'''
from typing import List


def minFallingPathSum(matrix: List[List[int]]) -> int:
    n = len(matrix)
    prev_row = [0] * n

    d_y = [-1, 0, 1]
    for cur_row in matrix:
        new_row = [0] * n
        for j in range(n):
            min_falling_path = float("inf")
            for d in d_y:
                if 0 <= j + d < n:
                    min_falling_path = min(
                        min_falling_path, prev_row[j+d] + cur_row[j])
            new_row[j] = min_falling_path
        prev_row = new_row
    return min(prev_row)


if __name__ == "__main__":
    print(minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
