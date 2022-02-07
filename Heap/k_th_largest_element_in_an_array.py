'''
Problem
-------------------
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Constraints
-------------------
* 1 <= k <= nums.length <= 10^4
* -10^4 <= nums[i] <= 10^4

Thinking
-------------------
* kth largest element 

* construct a min-heap of size k. Iterate through to fill in the heap. 
    * if current num is larger than the top of the heap, then pop the top from heap, and add in current number
    * after completing looping through the array, find 

* time complexity:
    * O(NlogK), iterate takes N, and heap push and heap pop takes O(logK)
'''
from typing import List
import heapq


def findKthLargest(nums: List[int], k: int) -> int:
    heap = []
    # maintain a heap of size k
    # use a min heap, as we will want to take the largest k element in heap
    for num in nums:
        # add in num if heap length is smaller than k
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
    return heap[0]


if __name__ == "__main__":
    print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
