# Given a binary tree, a target node, and a integer K, find all nodes whose depth (level) is K away from the target node's depth. Order of returned nodes does not matter.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_distance_k_nodes(root, target, K):
    # WRITE YOUR BRILLIANT CODE HERE


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

    def find_node(root, target):
        if not root:
            return
        if root.val == target:
            return root
        return find_node(root.left, target) or find_node(root.right, target)
    s = input().split()
    root = build_tree(iter(s))
    target = find_node(root, int(input()))
    K = int(input())
    print(' '.join(str(x.val) for x in sorted(
        binary_tree_distance_k_nodes(root, target, K), key=lambda node: node.val)))
