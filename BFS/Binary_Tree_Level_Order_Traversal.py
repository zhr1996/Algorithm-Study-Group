from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root):
    queue = deque([root])
    result = []
    while len(queue) != 0:
        child_temp = []
        level = []
        while len(queue) != 0:
            node = queue.popleft()
            if node.left:
                child_temp.append(node.left)
            if node.right:
                child_temp.append(node.right)
            level.append(node)
        result.append(level)
        queue.extend(child_temp)
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
    for level in level_order_traversal(root):
        print(' '.join(str(x.val) for x in level))
