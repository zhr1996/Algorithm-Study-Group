

# In a binary tree, a node is considered "visible" if no node on the root-to-itself path has a greater value.
# The root is always "visible" since there are no other nodes between the root and itself. Given a binary tree,
# count the number of "visible" nodes.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(root, max_value):
    if root == None:
        return 0
    count = 0
    if root.val >= max_value:
        count = 1
    max_value = max(max_value, root.val)
    return count + helper(root.left, max_value) + helper(root.right, max_value)


def visible_tree_node(root):

    return helper(root, root.val)


if __name__ == "__main__":
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x':
            return
        cur = Node(int(val))
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    root = build_tree(iter(input().split()))
    print(visible_tree_node(root))
