'''
Problem
-------------------
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Constraints
-------------------
* -10^5 <= num <= 10^5
* There will be at least one element in the data structure before calling findMedian.
* At most 5 * 104 calls will be made to addNum and findMedian.

* If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
* If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

Thinking
-------------------
* median is calculated by only the median numbers

* use two heaps,
    * one min heap, one max heap
    * max-heap stores the small half
    * min-heap stores the larger haf

* first choose to add to the max-heap, which is the smaller half

* when a new number comes
    * if two heaps have the same size
        * compare current number with the top in min-heap
            * if smaller, add current number to max-heap
            * if larger, pop the top element and push curent number in min heap
            * time: O(logn)
    * if smaller half has more numbers than the larger half
        * compare current number with the top in max-heap
            * if larger, add the min-heap
            * if smaller, pop one out from max-heap and push current number in
            * time: O(logn)

* when asking for median
    * O(logn)
    * if smaller half has more numbers than the larger half
        * return the top of smaller half
    * if they have same amount of numbers   
        * return the median of the top of two heaps
'''
from typing import List
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap and not self.max_heap:
            heapq.heappush(self.max_heap, -num)
        elif len(self.min_heap) == len(self.max_heap):
            if num <= self.min_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                pop_num = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -pop_num)
                heapq.heappush(self.min_heap, num)
        else:
            if num >= -self.max_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                pop_num = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, pop_num)
                heapq.heappush(self.max_heap, -num)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) // 2

        return -self.max_heap[0]


if __name__ == "__main__":
    print(function)
