# Max depth
# Tree length, divide and conquer to find the deepest length of child tree

def maxDepth(self, root: TreeNode) -> int:
    # State child needs to run, current root node
    # Return the max child tree depth
    def helper(root):
        if root is None:
            return 0
        left_length = helper(root.left)
        right_length = helper(root.right)
        return max(left_length, right_length) + 1

    return helper(root)
