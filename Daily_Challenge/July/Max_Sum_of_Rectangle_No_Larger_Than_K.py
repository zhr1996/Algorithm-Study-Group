'''
Problem
-------------------
Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-105 <= k <= 105

Thinking
-------------------
* prefix sum, compute sum of square using O(1), iterate through all the sums and find the sum no larger than K

* Since the number could be negative, we can't stop iterating when finding the sum is larger than K

* The problem boils down to compute the prefix sum. 
    * Two points defines a rectangular
    * p - left top vertex, q - right bottom vertex
    * Sum((x_1, y_1) , (x_2, y_2)) = 
        * Sum((0, 0), (x_2, y_2)) 
        * - Sum((0,0), (x_1 - 1,y_2))
        * - Sum((0,0), (x_2,y_1 - 1))
        * + Sum((0,0), (x_1 - 1,y_1 - 1))

* Time limited error 10^2 * 10 ^2 * 10^2 * 10^2 = 10^8

* Refered to some blogs. This is a hard problem. Needs to use Kandane algorithm + binary search



'''
from typing import List


def maxSumSubmatrix(matrix: List[List[int]], k: int) -> int:
    m = len(matrix)
    n = len(matrix[0])
    prefix_sum = [[0 for j in range(n + 1)]
                  for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix_sum[i][j] = prefix_sum[i][j-1] + \
                prefix_sum[i-1][j] - prefix_sum[i-1][j-1] + matrix[i-1][j-1]

    max_sum_smaller_than_k = -float('inf')
    for x_1 in range(1, m+1):
        for y_1 in range(1, n+1):
            for x_2 in range(x_1, m+1):
                for y_2 in range(y_1, n+1):
                    cur_sum = prefix_sum[x_2][y_2] - prefix_sum[x_2][y_1 - 1] - \
                        prefix_sum[x_1 - 1][y_2] + prefix_sum[x_1 - 1][y_1 - 1]
                    # print(cur_sum)
                    if cur_sum <= k and cur_sum > max_sum_smaller_than_k:
                        max_sum_smaller_than_k = cur_sum
    return max_sum_smaller_than_k


if __name__ == "__main__":
    print(maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2))
