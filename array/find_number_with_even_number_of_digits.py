'''
Problem
-------------------
Given an array nums of integers, return how many of them contain an even number of digits.

Constraints
-------------------
* 1 <= nums.length <= 500
* 1 <= nums[i] <= 105

Thinking
-------------------
* len(str(num))
'''
from typing import List


def findNumbers(nums: List[int]) -> int:
    even_number_count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            even_number_count += 1
    return even_number_count


if __name__ == "__main__":
    print(findNumbers([12, 3456, 1, 2345]))
