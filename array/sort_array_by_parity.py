'''
Problem
-------------------
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Constraints
-------------------
* 1 <= nums.length <= 5000
* 0 <= nums[i] <= 5000

Thinking
-------------------
* non-inplace solution: declare a new array, go through the array once, put all even numbers in the new array
  visit array second time, insert all odd numbers

* initialize a left pointer and a right pointer
    * increase left by one until left and right point to the same number
        * if left pointer finds an odd number, stop, let right pointer go left and find an even number
            * if found, swap the two numbers
    * Time: O(N)
    * Space: O(1)
'''
from typing import List


def sortArrayByParity(nums: List[int]) -> List[int]:
    left = 0
    right = len(nums) - 1

    def swap(left, right):
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp

    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        else:
            if nums[right] % 2 == 0:
                swap(left, right)
            else:
                right -= 1
    return nums


if __name__ == "__main__":
    print(sortArrayByParity([1, 3, 5, 4]))
