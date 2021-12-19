'''
Problem
-------------------
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Constraints
-------------------
* 1 <= nums.length <= 105
* nums[i] is either 0 or 1.

Thinking
-------------------
* maintain a count state variable
'''
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    count = 0
    i = 0
    max_consecutive_one = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            max_consecutive_one = max(max_consecutive_one, count)
            count = 0
    return max(max_consecutive_one, count)


if __name__ == "__main__":
    print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 0]))
