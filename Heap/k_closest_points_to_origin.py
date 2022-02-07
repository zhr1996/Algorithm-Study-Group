'''
Problem
-------------------


Constraints
-------------------


Thinking
-------------------
* if allocating a size n min-heap
    * use O(n) to heapify the array
    * use klogn time to pop the closest points
    * in total: O(n + klogn)

* if allocating a size k max-heap
    * use O(n) to loop through the list, and use O(logk) each time to push or delete an element
    * in total: O(nlogk)
'''
from typing import List
import heapq


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    # maintain a max-heap of size k
    heap = []

    for point in points:
        distance_square = point[0]**2 + point[1]**2
        if len(heap) < k:
            heapq.heappush(heap, (-distance_square, [point[0], point[1]]))
        else:
            if distance_square < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-distance_square, [point[0], point[1]]))

    ret = []
    n = len(heap)
    for i in range(n):
        ret.append(heap[i][1])
    return ret


if __name__ == "__main__":
    print(kClosest([[3, 3], [5, -1], [-2, 4]], 2))
