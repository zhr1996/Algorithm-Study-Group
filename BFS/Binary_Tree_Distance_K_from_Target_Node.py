# Given a binary tree, a target node, and a integer K, find all nodes whose depth (level) is K away from the target node's depth. Order of returned nodes does not matter.


from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_find_target_level(root, target):
    queue = deque([root])
    level = -1
    while len(queue) != 0:
        level += 1
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            if node == target:
                return level
            children = [node.left, node.right]
            for child in children:
                if child:
                    queue.append(child)
    return -1


def binary_tree_distance_k_nodes(root, target, K):
    # First BFS find target node level
    # Then BFS the second round to found level l-K and l+K
    target_level = binary_tree_find_target_level(root, target)
    result = []
    queue = deque([root])
    level = -1
    while len(queue) != 0:
        level += 1
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            if level == target_level - K or level == target_level + K:
                result.append(node)
            children = [node.left, node.right]
            for child in children:
                if child:
                    queue.append(child)
        if level >= target_level + K:
            return result
    return result


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
