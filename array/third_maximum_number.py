'''
Problem
-------------------
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Constraints
-------------------
* 1 <= nums.length <= 10^4
* -2^31 <= nums[i] <= 2^31 - 1

Thinking
-------------------
* use a min-heap

* if in the end the min-heap length is smaller than 3, return the largest by poping all other elements out
'''
from typing import List
import heapq


def thirdMax(nums: List[int]) -> int:
    min_heap = []
    num_in_heap = set()
    for num in nums:
        if num in num_in_heap:
            continue
        if len(min_heap) < 3:
            heapq.heappush(min_heap, num)
            num_in_heap.add(num)
        else:
            if num > min_heap[0]:
                num_in_heap.remove(min_heap[0])
                heapq.heappop(min_heap)
                # add in the new num
                heapq.heappush(min_heap, num)
                num_in_heap.add(num)

    ret = -1
    # if num_in_heap is smaller than 3
    if len(min_heap) < 3:
        while min_heap:
            ret = heapq.heappop(min_heap)
    else:
        ret = min_heap[0]
    return ret


if __name__ == "__main__":
    print(thirdMax([3, 2]))
