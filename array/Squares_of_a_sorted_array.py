'''
Problem
-------------------
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Constraints
-------------------
* 1 <= nums.length <= 10^4
* -10^4 <= nums[i] <= 10^4
* nums is sorted in non-decreasing order.

Thinking
-------------------
* follow up: O(n) solution

* the original array is already sorted in non-decreasing order

* Two pointers, 
    * since the largest square will either on left side or on the right side
    * compare absolute value
        * if right side absolute value is equal or larger, append to front (use dequeue), right -- 
        * if left side absolute value is larger, append to front and left ++ 
'''
from typing import List
from collections import deque


def sortedSquares(nums: List[int]) -> List[int]:
    queue = deque()
    left = 0
    right = len(nums) - 1

    while left <= right:
        if abs(nums[right]) >= abs(nums[left]):
            queue.appendleft(nums[right]**2)
            right -= 1
        else:
            queue.appendleft(nums[left]**2)
            left += 1
    return list(queue)


if __name__ == "__main__":
    print(sortedSquares([-7, -3, 2, 3, 11]))
