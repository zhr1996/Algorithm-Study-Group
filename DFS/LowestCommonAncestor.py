# A very simply presented but can get very complex problem. To find the lowest common ancestor, one
# best think of tree composed of different paths, the first point the two paths differ is where
# the lowest common ancestor is


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def look_for_path(root, node, path):
        if root is None:
            return False

        if root.val == node.val:
            path.append(node)
            return True

        # Backtracking, tentatively adding in the current node
        # Divide and conquer, if the node is not in the left tree, left tree path will remove automatically
        path.append(root)
        if look_for_path(root.left, node, path):
            return True

        if look_for_path(root.right, node, path):
            return True

        path.pop()
        return False

    path1 = []
    path2 = []
    if not look_for_path(root, p, path1) or not look_for_path(root, q, path2):
        return None

    n1 = len(path1)
    n2 = len(path2)

    prev = root

    for i in range(0, min(n1, n2)):
        if path1[i].val != path2[i].val:
            return prev

        prev = path1[i]

    return prev
