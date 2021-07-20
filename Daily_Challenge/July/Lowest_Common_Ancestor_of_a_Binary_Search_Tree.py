'''
Problem
-------------------
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Constraints
-------------------
The number of nodes in the tree is in the range [2, 105].\
-109 <= Node.val <= 109\
All Node.val are unique.\
p != q\
p and q will exist in the BST.\

Thinking
-------------------
* Make use of the property of Binary Search Tree
    * All smaller nodes are on left, all larger nodes are on the right
    * If current node is in between two targets, then it's the lowest common ancestor
        * To prove it, suppose it is not. So the two nodes have a same parent lower the current node. The same parent is either smaller or larger than current node, 
          , which breaks the assumption that the the current node is in between the targets.
    * If current node is smaller than the two targets: search right
    * If current node is larger, then search left

* Anytime if the current node value is the same with any of the target, then it is the lowest common ancestor

* Time Complexity:
    * Best Olog(n), worst O(n), depends on the structure of the tree.
'''


from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if p.val > q.val:
        temp = p
        p = q
        q = temp

    def find_lca(cur_node, p, q):
        if cur_node == p or cur_node == q:
            return cur_node

        if cur_node.val > p.val and cur_node.val < q.val:
            return cur_node

        if cur_node.val > q.val:
            return find_lca(cur_node.left, p, q)

        if cur_node.val < p.val:
            return find_lca(cur_node.right, p, q)

        return None

    return find_lca(root, p, q)


if __name__ == "__main__":
    print(lowestCommonAncestor())
