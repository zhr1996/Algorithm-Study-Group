'''
Problem
-------------------
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


Constraints
-------------------
* 0 <= nums.length <= 100
* 0 <= nums[i] <= 50
* 0 <= val <= 100

Thinking
-------------------
* Two pointers
    * one point at the start
    * one point at the end

* seeing occurence of the target number, we move the number to the end
'''
from typing import List


def removeElement(nums: List[int], val: int) -> int:
    start = 0
    end = len(nums) - 1

    k = 0
    while start <= end:
        if nums[end] == val:
            end -= 1
            continue

        if nums[start] == val:
            temp = nums[end]
            nums[end] = nums[start]
            nums[start] = temp
            start += 1
            k += 1
        else:
            start += 1
            k += 1
    return k


if __name__ == "__main__":
    input = [3, 3, 3, 3, 3]
    print(removeElement(input, 3))
    print(input)
