'''
Problem
-------------------
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Constraints
-------------------
* 1 <= n <= 8

Thinking
-------------------
* print all so use recurrsion instead of dynamic programming

* recurssion: 
    * get_bst(start, end)

* recurrence relation:
    * for i in range(start, end):
        * i.left = left_tree
        * i.right = right_tree
    * left_tree_list is generated by calling recurrence functions get_bst(start,i-1)
    * right_tree_list is generated by calling recurrence functions get_bst(i+1, end)

* base case
    * if start > end: return None
'''
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generateTrees(n: int) -> List[Optional[TreeNode]]:
    def helper(start: int, end: int) -> List[Optional[TreeNode]]:
        # base case
        if start > end:
            return [None]

        all_trees = []
        # choose each number as root
        # [start, end]
        for i in range(start, end + 1):

            left_trees = helper(start, i - 1)
            right_trees = helper(i + 1, end)

            for left_tree in left_trees:
                for right_tree in right_trees:
                    cur_node = TreeNode(i)
                    cur_node.left = left_tree
                    cur_node.right = right_tree
                    all_trees.append(cur_node)
        return all_trees
    return helper(1, n)


if __name__ == "__main__":
    print(generateTrees(3))
