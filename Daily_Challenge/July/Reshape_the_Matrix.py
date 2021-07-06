'''
Problem
-------------------
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300

Thinking
-------------------
* first check if m * n == r * c
* Filling the new matrix
    * keep two state variables: i and j. every time j + 1, check if j >= c. If so, clear j and add 1 to i

'''
from typing import List


def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])

    if m * n != r * c:
        return mat

    cur_r = 0
    cur_c = 0

    new_matrix = [[0 for j in range(c)] for i in range(r)]
    for i in range(m):
        for j in range(n):
            new_matrix[cur_r][cur_c] = mat[i][j]

            cur_c += 1
            if cur_c >= c:
                cur_c = 0
                cur_r += 1
    return new_matrix


if __name__ == "__main__":
    print(matrixReshape([[1, 2], [3, 4]], 1, 4))
