'''
Problem
-------------------
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100

Thinking
-------------------
* Seems this is very suitable for recursive methods

* This is the same with finding the depth of nodes: for example, leave has depth 0, so arr[0] has those leaves, and so on..

* Construct a dictionary containing depth as key and node as values. Then according to the max key, construct an array and store the node v \
  vale accordingly 

Summary
-------------------
* Interesting problem! Think about tree depth next time encountered with tree problems

'''
from typing import List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findLeaves(root: TreeNode) -> List[List[int]]:
    depth_dict = defaultdict(list)

    def dfs(node):
        if node.left is None and node.right is None:
            depth_dict[0].append(node.val)
            return 1

        left_depth = -1
        right_depth = -1

        if node.left:
            left_depth = dfs(node.left)

        if node.right:
            right_depth = dfs(node.right)

        cur_depth = max(left_depth, right_depth)
        depth_dict[cur_depth].append(node.val)

        return cur_depth + 1

    dfs(root)

    max_depth = max(depth_dict.keys())
    leave_arr = [[] for x in range(max_depth)]
    for key in depth_dict:
        leave_arr[key] = depth_dict[key]

    return leave_arr

# if __name__ == "__main__":
#     print(function)
