'''
Problem
-------------------
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Constraints
-------------------
* n == nums.length
* 1 <= n <= 10^5
* 1 <= nums[i] <= n

Thinking
-------------------
* move i in range(1, n) to nums[i-1]
'''
from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        cur = nums[i]
        while cur != nums[cur-1]:
            temp = nums[cur-1]
            nums[cur-1] = cur
            cur = temp
    disappeared_number = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            disappeared_number.append(i + 1)
    return disappeared_number


def findDisappearedNumbers_stricttwopass(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        cur = abs(nums[i])
        if nums[cur-1] > 0:
            nums[cur-1] = -nums[cur-1]
    disappeared_number = []
    for i in range(len(nums)):
        if nums[i] > 0:
            disappeared_number.append(i+1)
    return disappeared_number


if __name__ == "__main__":
    print(findDisappearedNumbers_stricttwopass([4, 3, 2, 7, 8, 2, 3, 1, 1]))
