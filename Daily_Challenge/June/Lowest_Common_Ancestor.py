'''
Problem
-------------------
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the tree.

Thinking
-------------------  
* Long time no see: LCA

* Use a list to store all the nodes on the path, and compare the node where the two paths first diverge

* 
'''
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def find_path_to_node(cur_node, target, path):
        if cur_node == target:
            path.append(target)
            return True

        if cur_node.left is None and cur_node.right is None:
            return False

        if cur_node.left:
            if find_path_to_node(cur_node.left, target, path):
                path.append(cur_node)
                return True

        if cur_node.right:
            if find_path_to_node(cur_node.right, target, path):
                path.append(cur_node)
                return True
        return False

    path_to_p = []
    find_path_to_node(root, p, path_to_p)
    path_to_p = path_to_p[::-1]

    path_to_q = []
    find_path_to_node(root, q, path_to_q)
    path_to_q = path_to_q[::-1]

    last_node = None
    for i in range(min(len(path_to_p), len(path_to_q))):
        if path_to_p[i] != path_to_q[i]:
            break
        last_node = path_to_p[i]

    return last_node
