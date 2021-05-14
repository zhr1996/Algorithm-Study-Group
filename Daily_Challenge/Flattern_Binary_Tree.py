# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Flattern a tree, result in a linked-list, with root.right point to the next node

# It's not hard to flattern a sub-tree, but the difficulty is how to make the last node of this sub-tree
# point to the right flatterned tree

# Solution: Return the last node every time when flatterning the tree
class Solution:
    def flattern_tree_and_return_last(self, root):
        if root is None:
            return None

        left_last = self.flattern_tree_and_return_last(root.left)
        right_last = self.flattern_tree_and_return_last(root.right)

        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None

        return right_last or left_last or root

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattern_tree_and_return_last(root)
