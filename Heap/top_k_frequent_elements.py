'''
Problem
-------------------
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Constraints
-------------------
* 1 <= nums.length <= 105
* k is in the range [1, the number of unique elements in the array].
* It is guaranteed that the answer is unique.

Thinking
-------------------
* go through the array and build a dictionary of key -> freq(key)_

* go through the dictionary and put tuple (freq, key) in a size-k heap

* since we are trying to find the top k frequent one, we need a min-heap (Keeping the highest k frequent leement)

* Time complexity:
    * Build dictionary: O(N)
    * build the min-heap: O(Nlogk)
'''
from typing import List
from collections import Counter
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    heap = []
    for key in counter:
        if len(heap) < k:
            heapq.heappush(heap, (counter[key], key))
        else:
            if counter[key] > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (counter[key], key))
    ret = []
    for freq, num in heap:
        ret.append(num)
    return ret


if __name__ == "__main__":
    print(topKFrequent([1, 1, 2, 2, 2, 3, 3, 4], 3))
