'''
Problem
-------------------
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2

Thinking
-------------------
* At first glance, I thought just k / n + k % n is enough. But columns are sorted and rows are sorted 
  doesn't mean that the matrix is sorted

* Useful constraint: the matrix is a square matrix.

* A second thought is to compare start and end of each row, but we don't have a target to compare with.

* If the columns are not sorted, can use n priority queues? Maybe not n priority queues, just one with size k

* Push all the elements into the priority queue, if the size is greater than k, pop the first element

* Time Complexity
    * O(n^2 * logn)
'''
from typing import List
import heapq


def kthSmallest(matrix: List[List[int]], k: int) -> int:
    heap = []
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if len(heap) == k:
                if -heap[0] > matrix[i][j]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, -matrix[i][j])
            else:
                heapq.heappush(heap, -matrix[i][j])

    return -heap[0]


if __name__ == "__main__":
    print(kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 2))
