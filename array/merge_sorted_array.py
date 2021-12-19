'''
Problem
-------------------
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Constraints
-------------------
* nums1.length == m + n
* nums2.length == n
* 0 <= m, n <= 200
* 1 <= m + n <= 200
* -10^9 <= nums1[i], nums2[j] <= 10^9

Thinking
-------------------
* do the merge in O(m+n) time in-place
'''
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i_1 = m - 1
    i_2 = n - 1

    end = len(nums1) - 1

    while end >= 0:
        # if i_2 < 0, all numbers in the second array have been visited
        # enough to break
        if i_2 < 0:
            break
        if i_1 >= 0 and nums1[i_1] >= nums2[i_2]:
            nums1[end] = nums1[i_1]
            i_1 -= 1
        else:
            nums1[end] = nums2[i_2]
            i_2 -= 1

        end -= 1
    return


if __name__ == "__main__":
    input = [1, 2, 3, 0, 0, 0]
    print(merge(input, 3, [2, 5, 6], 3))
    print(input)
