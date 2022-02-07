'''
Problem
-------------------
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Constraints
-------------------
* 1 <= k <= 10^4
* 0 <= nums.length <= 10^4
* -10^4 <= nums[i] <= 10^4
* -10^4 <= val <= 10^4
* At most 10^4 calls will be made to add.
* It is guaranteed that there will be at least k elements in the array when you search for the kth element.

Thinking
-------------------
* use a size k min-heap, add in values

* return the element at top
'''
from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.size = k
        for num in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, num)
            else:
                if self.heap[0] < num:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        # if added num is smaller than the top element in heap
        # then we don't need to add the element because it will not be used
        # (we are not deleting any element)
        if len(self.heap) < self.size:
            heapq.heappush(self.heap, val)
        else:
            if self.heap[0] < val:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
        return self.heap[0]
        



if __name__ == "__main__":
    print(function)
