# Given a binary tree, find the depth of the shallowest leaf node.

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The nearest leaf node is the height limit height of tree
# If find leaf node, then stop iterating


def binary_tree_min_depth(root):
    queue = deque([root])
    level = -1
    while len(queue) != 0:
        level += 1
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            # If found a leaf, then just return current level
            if not node.left and not node.right:
                return level

            children = [node.left, node.right]
            for child in children:
                if child:
                    queue.append(child)

    return level


if __name__ == "__main__":
    # driver code, do not modify
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x':
            return
        cur = Node(int(val))
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    root = build_tree(iter(input().split()))
    print(binary_tree_min_depth(root))
