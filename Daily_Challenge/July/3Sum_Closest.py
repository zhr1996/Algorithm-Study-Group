'''
Problem
-------------------
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Constraints
-------------------
3 <= nums.length <= 10^3\
-10^3 <= nums[i] <= 10^3\
-10^4 <= target <= 10^4\

Thinking
-------------------

'''
from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    closest_sum = 2**31-1
    for i in range(len(nums)):
        j, k = i+1, len(nums)-1
        while j < k:
            curr_sum = nums[i] + nums[j] + nums[k]
            if curr_sum == target:
                return curr_sum
            if abs(curr_sum-target) < abs(closest_sum-target):
                closest_sum = curr_sum
            if curr_sum < target:
                j = j+1
            else:
                k = k-1
    return closest_sum


if __name__ == "__main__":
    print(threeSumClosest([-1, 2, 1, -4], 1))
