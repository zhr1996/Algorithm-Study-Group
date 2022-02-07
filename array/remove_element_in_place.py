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
* use a slow pointer and fast pointer
    * slow pointer points to the last index of array that doesn't have the num to be deleeted
    * fast pointer go through the array check every element
        * if it's not equal to the element to be deleted, then slow+1; nums[slow] = nums[fast]
    * return slow + 1 as the length of the array of deletion

'''
from typing import List


def removeElement(nums: List[int], val: int) -> int:
    # slow is index of last element in array that doesn't have the number to be deleted
    slow = -1
    for fast in range(0, len(nums)):
        if nums[fast] != val:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


# anther way
# if element to be removed are rare, for example: [4,1,2,3,5], 4 ->
# we can swap to element to be removed with the last element, and decrease the lenght by one
# this way, the result for the example would be: [5,1,2,3,4], and then no more change to the array
    # this works, because the problem doesn't care the order of the solution

# if the array are all 4: [4,4,4,4,5], then
def removeElement(nums: List[int], val: int) -> int:

    n = len(nums)

    i = 0
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n-1]
            n -= 1
        else:
            i += 1
    return n


if __name__ == "__main__":
    input = [3, 1, 2, 3, 2, 1, 3]
    print(removeElement(input, 3))
    print(input)
