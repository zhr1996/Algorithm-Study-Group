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
* the largest square either come from rightmost number or the leftmost number

* keeps two pointer, compare the absolute value of their corresponding value

* push the larger one's square to queue (FILO), then conver the queue to list in the end
'''
from typing import List
from collections import deque


def sortedSquares(nums: List[int]) -> List[int]:
    sorted_square = deque()
    left = 0
    right = len(nums) - 1
    while left <= right:
        if abs(nums[left]) <= abs(nums[right]):
            sorted_square.appendleft(nums[right] ** 2)
            right -= 1
        else:
            sorted_square.appendleft(nums[left] ** 2)
            left += 1
    return list(sorted_square)


if __name__ == "__main__":
    print(sortedSquares([-4, -1, 0, 3, 10]))
