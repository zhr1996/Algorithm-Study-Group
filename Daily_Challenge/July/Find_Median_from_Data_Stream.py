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
-105 <= num <= 105\
There will be at least one element in the data structure before calling findMedian.\
At most 5 * 104 calls will be made to addNum and findMedian.\

Thinking
-------------------
* Two requirements
    * Dynamically update the array
    * Find median in at most nlogn time (input is 5 * 10^4), each call at most logn time

* Maintain two heaps, one is min heap and the other is max heap. Always split the larger array in min heap, smaller array in max heap
    * If the array is not even, put the extra num in min array (larger one)

* In this way, the median will always be 
    * the first element in min array (the smallest element), if the array is odd
    * the median of first element in both heaps, if the array is even

* Time complexity
    * O(nlogm), m is the length of the final array, which can be approximated by n
* Space complexity
    * O(m), m is the length of the final array

* Note:
    * Put negative num in the second heap so that it is converted into a max-heap
    * One point is very easily confusing here:
        * min-heap stores the larger part, max-heap stores the smaller part
        * That's not quite intuitive, besides python doesn't have a max heap, so number stores in it has to be negative

* Follow up:
    * If the number are all in 0 to 100
        * Use bucket sort, keep an array of size 100 to store count of each number and store the length of current array
        * find median: loop throught the array to find the half length point. O(100) = O(1)
    * If the number are 99% in 100
        * Besides storing 0 to 100, we also need to store the number smaller than 0 and larger than one hundred
        * Since we know the median must be in 0-100, we only need the count to find the median
    * [Follow-up reference](https://www.junhaow.com/lc/problems/heap/295_find-median-from-data-stream)
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
        if len(self.min_heap) == len(self.max_heap) == 0:
            heapq.heappush(self.min_heap, num)
        elif len(self.min_heap) == len(self.max_heap):
            if num < -self.max_heap[0]:
                max_first = -heapq.heappop(self.max_heap)
                heapq.heappush(self.max_heap, -num)
                heapq.heappush(self.min_heap, max_first)
            else:
                heapq.heappush(self.min_heap, num)
        else:
            if num > self.min_heap[0]:
                min_first = heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, num)
                heapq.heappush(self.max_heap, -min_first)
            else:
                heapq.heappush(self.max_heap, -num)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + (-self.max_heap[0])) / 2
        else:
            return self.min_heap[0]

    # Debug\
    def print_heap(self):
        print(self.min_heap)
        print(self.max_heap)


if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.print_heap()
    obj.addNum(3)
    print(obj.findMedian())
    obj.print_heap()
