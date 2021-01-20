from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_traversal(root):
    queue = deque([root])
    flag = 0
    result = []
    while len(queue) != 0:
        level = []
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            level.append(node)
            children = []
            children = [node.left, node.right]
            for child in children:
                if child:
                    queue.append(child)
        if flag == 0:
            result.append(level)
            flag = 1
        else:
            result.append(level[::-1])
            flag = 0
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
    for level in zigzag_traversal(root):
        print(' '.join(str(x.val) for x in level))
