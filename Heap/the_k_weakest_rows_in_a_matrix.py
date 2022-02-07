'''
Problem
-------------------
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Constraints
-------------------
* m == mat.length
* n == mat[i].length
* 2 <= n, m <= 100
* 1 <= k <= m
* matrix[i][j] is either 0 or 1.

Thinking
-------------------
* weakest <-> smallest, 

* maintain a min-heap of size k, put each row in as a tuple (solder_count, row)

* count can be maximized using binary search
    * find the last 1 in the array
'''
from typing import List
import heapq


def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    heap = []
    for i, row in enumerate(mat):
        soldier_count = 0
        for col in row:
            if col == 1:
                soldier_count += 1
        if len(heap) < k:
            heapq.heappush(heap, (-soldier_count, -i))
        else:
            if soldier_count < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-soldier_count, -i))
    ret = []
    # stongest to weakest
    while heap:
        ret.append(-heapq.heappop(heap)[1])
    # weakest to stongest
    return ret[::-1]


if __name__ == "__main__":
    print(kWeakestRows([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [
          1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], 3))
