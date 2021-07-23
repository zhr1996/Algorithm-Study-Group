'''
Problem
-------------------
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

Constraints
-------------------
The number of nodes in the tree is in the range [1, 200].\
Node.val is either 0 or 1.\

Thinking
-------------------
* Recursively remove all subtree having 1.
    * If current node is 0
        * Recursively call on left and right node, if any of them return True, return ture, also remove the node return False
    * If current ndoe is 1,
        * Recursive call on left node and right node, if any of them return False, set the pointer to None
        * Return True
'''


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pruneTree(root: TreeNode) -> TreeNode:
    def recursive_prune_tree(root):
        if root == None:
            return False

        left_tree_have_one = recursive_prune_tree(root.left)
        right_tree_have_one = recursive_prune_tree(root.right)
        if not left_tree_have_one:
            root.left = None
        if not right_tree_have_one:
            root.right = None

        if root.val == 0:
            if left_tree_have_one or right_tree_have_one:
                return True
            else:
                return False
        else:
            return True
    if not recursive_prune_tree(root):
        return None
    return root


if __name__ == "__main__":
    print(pruneTree(None))
