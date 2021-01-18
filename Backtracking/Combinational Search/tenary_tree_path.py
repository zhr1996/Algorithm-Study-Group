
# Given a ternary tree (each node of the tree has ata most three children), find all root-to-left paths

# State passed to children :
# 1. current path so far, since tree can only have one path to each node,
# there is only one path needed, but after all the children traveresed, remember to pop out current node
# since in this way, parent node can continue to traverse other nodes
# 2. the result array storing paths
# 3. current node visiting
#
# return: nothing,

class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children


# Rememeber it's a tenary tree
# Loop through all children in the tree
def helper(root, cur_path, result):
    if root is None:
        return

    if all(child is None for child in root.children):
        cur_path.append(root)
        # remember to copy an entire path and add it in the result, since list is stored in heaps

        result.append('->'.join(node.val for node in cur_path))
        cur_path.pop()
        return

    cur_path.append(root)

    for child in root.children:
        helper(child, cur_path, result)

    cur_path.pop()
    return

    return


def ternary_tree_paths(root):
    # WRITE YOUR BRILLIANT CODE HERE
    result = []
    helper(root, [], result)
    return result


if __name__ == '__main__':
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x':
            return
        cur = Node(val, [])
        for _ in range(3):
            cur.children.append(build_tree(nodes))
        return cur
    root = build_tree(iter(input().split()))
    paths = ternary_tree_paths(root)
    for path in sorted(paths):
        print(path)
