'''
Problem
-------------------
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Constraints
-------------------
1 <= nums.length <= 10^4\
-10^4 <= nums[i] <= 10^4\
nums is sorted in a strictly increasing order.\

Thinking
-------------------
* Like binary search, always cut it in half and use the mid point as the root
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> TreeNode:

    def helper(left, right):
        if left > right:
            return None
        if left == right:
            return TreeNode(nums[left])

        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root
    return helper(0, len(nums) - 1)


if __name__ == "__main__":
    print(sortedArrayToBST([-10, -3, 0, 5, 9]))
