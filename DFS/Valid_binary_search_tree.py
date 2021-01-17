
# A very classic example of using recursion and divide and conquer
# To tell if the tree under current node is a valid binary search tree,
# we need to know the max from the left tree, and the min from right tree,
# and compare it with root.
# It's not enough to just test whether left child tree is a valid binary search tree
# and right child tree is a valid binary search tree


def isValidBST(self, root: TreeNode) -> bool:

    def helper(root):
        if root.left is None and root.right is None:
            return (root.val, root.val, True)

        cur_min = root.val
        cur_max = root.val

        if root.left is not None:
            (left_min, left_max, left_valid) = helper(root.left)
            if not left_valid:
                return (-1, -1, False)

            if root.val <= left_max:
                return (-1, -1, False)

            cur_min = left_min

        if root.right is not None:
            (right_min, right_max, right_valid) = helper(root.right)

            if not right_valid:
                return (-1, -1, False)

            if root.val >= right_min:
                return (-1, -1, False)

            cur_max = right_max

        return (cur_min, cur_max, True)

    _, _, isValid = helper(root)
    return isValid
