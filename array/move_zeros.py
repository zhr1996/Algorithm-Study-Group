'''
Problem
-------------------
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Constraints
-------------------
* 1 <= nums.length <= 10^4
* -2^31 <= nums[i] <= 2^31 - 1

Thinking
-------------------
* if we are allowed to use extra space, we can make a new array of all non-zero numbers in original array and fill the rest of array with zero

* Back to the original question, 
    * two pointers
    * we can keep a index of last non-zero number, if we find a new non-zero element, we add one to the index and make it the new non-zero number
    * after we are done with keeping all non-zero numbers to the right, we add zeros to rest of the array

'''
from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    # array could be all zeros
    non_zero_index = -1
    for j in range(len(nums)):
        if nums[j] != 0:
            non_zero_index += 1
            nums[non_zero_index] = nums[j]
    # non_zero_index is index of non-zero number
    for j in range(non_zero_index + 1, n):
        nums[j] = 0
    return


if __name__ == "__main__":
    input = [1, 0, 0, 2, 3, 0]
    print(moveZeroes(input))
    print(input)
