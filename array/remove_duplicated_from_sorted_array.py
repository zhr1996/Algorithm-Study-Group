'''
Problem
-------------------
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Constraints
-------------------
* 0 <= nums.length <= 3 * 104
* -100 <= nums[i] <= 100
* nums is sorted in non-decreasing order.

Thinking
-------------------
* Keep a slow pointer and a fast pointer,
    * fast pointer check if current number is the same with cur duplicate number
    * if it's different, then makse nums[slow] = nums[fast] and increase one to slow pointer

* O(N)
'''
from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    # i is the index of last non-duplicate number
    i = 0
    # rewrite to make code concise
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


if __name__ == "__main__":
    input = [1, 2, 2, 2, 3]
    print(removeDuplicates(input))
    print(input)
