from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_right_side_view(root):
    # BFS, use a queue, which is deque in python, and only add in the right most element
    # At least one element in queue to start traversing with
    result = []
    queue = deque([root])
    while len(queue) != 0:
        # How many element currently in queue(How many elements in this level)
        n = len(queue)
        # Pop left node and add in child
        for i in range(n-1):
            node = queue.popleft()
            children = [node.left, node.right]
            for child in children:
                if child:
                    queue.append(child)
        node = queue.popleft()
        result.append(node)
        children = [node.left, node.right]
        for child in children:
            if child:
                queue.append(child)
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
    root = build_tree(iter(input().split()))
    print(' '.join(str(x.val) for x in binary_tree_right_side_view(root)))
