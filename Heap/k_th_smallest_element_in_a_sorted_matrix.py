'''
Problem
-------------------
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Constraints
-------------------
* n == matrix.length == matrix[i].length
* 1 <= n <= 300
* -10^9 <= matrix[i][j] <= 10^9
* All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
* 1 <= k <= n^2

Thinking
-------------------
* maintain a priority queue of size n.

* push all first elements in each row into the priority queue.
    * element in pq: (num, row_index, col_index)

* pop the smallest one out, counter += 1

* continue this process until counter reaches k
    * return the element that pops out

* every time pops an element, push in next num until reaches the end

* Time complexity
    * O(n) to heapify the first elements
    * O(logn) each time to push and pop elements
    * In summary: O(n + klogn)

* Space complexity:
    * O(n), priority queue to store the elements
'''
from typing import List
import heapq


def kthSmallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    heap = []
    for i in range(n):
        heapq.heappush(heap, (matrix[i][0], i, 0))

    num = -1
    for i in range(k):
        num, row_index, col_index = heapq.heappop(heap)
        if col_index + 1 < n:
            heapq.heappush(
                heap, (matrix[row_index][col_index+1], row_index, col_index+1))
    return num


if __name__ == "__main__":
    print(kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 2))
