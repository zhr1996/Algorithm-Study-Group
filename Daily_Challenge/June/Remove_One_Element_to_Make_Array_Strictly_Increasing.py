'''
The Problem
-------------------
Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).

2 <= nums.length <= 1000
1 <= nums[i] <= 1000

Thinking
-------------------
* Brute Force, iterate through the array and find if any element is not strictly increasing
  If there is, then remove that element and check if the result is strictly increasing (not workable)

* The characteritic of a strictly increasing array is that each num[i+1] - num[i] is a positive number, we can maintain an array and check

* If one element is negative, we check if num[i+1] - num[i] + num[i+2] - num[i+1] is a positive number, and mark the quota has been used

* To make it easier, make the last element of the array +int, since we are considering the last element always increasing
'''
from typing import List


def canBeIncreasing(nums: List[int]) -> bool:
    # new_arr = [0 for i in range(len(nums))]
    # new_arr[-1] = float('inf')

    def check_increasing(remove_index):

        new_nums = nums[:]
        new_nums.pop(remove_index)

        for i in range(len(new_nums) - 1):

            if new_nums[i+1] - new_nums[i] <= 0:
                return False

        return True

    for i in range(len(nums) - 1):
        if nums[i+1] - nums[i] <= 0:

            # Two choices, remove nums[i+1] or nums[i]

            if check_increasing(i) or check_increasing(i+1):
                return True
            else:
                return False

    return True


if __name__ == "__main__":
    print(canBeIncreasing([1, 2]))
