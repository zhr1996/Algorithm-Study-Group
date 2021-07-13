'''
Problem
-------------------
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.



Constraints
-------------------
1 <= nums.length <= 1000\
-2^31 <= nums[i] <= 2^31 - 1\
nums[i] != nums[i + 1] for all valid i.\

Thinking
-------------------
* First thought just iterate throught the array and compare the number with its neightbors
    * Time Complexity: O(n)

* The problem asks for a log(n) solution:
    * Binary Search: a naive thought, just search the half where the neightbor is larger then mid
    * That's right. There are two occassions, if nums[i+1] > nums[i], then we continue to search the right half
      There should be at least a peak element in the larger half
    * We can draw line on paper to see it. It's pretty obvious once drawn on paper, that the larger half will always have a peak element
    * Time Complexity: O(logn)
'''
from typing import List


def findPeakElement(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if mid == 0:
            if nums[mid] > nums[mid + 1]:
                return mid
            else:
                left = mid + 1
        # elif mid == len(nums) - 1:
        #     if nums[mid] > nums[mid - 1]:
        #         return mid
        #     else:
        #         right -= 1
        elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid] < nums[mid-1]:
            right = mid - 1
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    print(findPeakElement([1, 2, 5, 4]))
