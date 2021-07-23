'''
Problem
-------------------
Given an array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.\
left and right are non-empty.\
left has the smallest possible size.\
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.\

Constraints
-------------------
2 <= nums.length <= 30000\
0 <= nums[i] <= 106\
It is guaranteed there is at least one way to partition nums as described.\
 

Thinking
-------------------
* The important states are the largest of left partition and smallest of right partition
    * If largest of left is smaller than smallest of right, then this is the partition length

* We can first iterate through the array and for each index, find the max value to the left

* And then iterate through the array again to find the mininum value to the right (not including itself cause we are comparing to array to the right)

* Then iterate to find the rightmost index where left_max[index] >= right_min[index]

* Note, return the smallest left size
'''
from typing import List


def partitionDisjoint(nums: List[int]) -> int:
    left_largest = [0 for i in range(len(nums))]
    right_smallest = [0 for i in range(len(nums))]

    left_largest[0] = nums[0]
    right_smallest[-1] = nums[-1]

    cur_largest = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > cur_largest:
            cur_largest = nums[i]
            left_largest[i] = nums[i]
        else:
            left_largest[i] = cur_largest

    cur_smallest = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        right_smallest[i] = cur_smallest
        if nums[i] < cur_smallest:
            cur_smallest = nums[i]

    left_length = 1
    # print(left_largest)
    # print(right_smallest)
    for i in range(len(nums) - 1):
        if left_largest[i] <= right_smallest[i]:
            left_length = i + 1
            break
    return left_length


if __name__ == "__main__":
    print(partitionDisjoint([5, 0, 3, 8, 6]))
