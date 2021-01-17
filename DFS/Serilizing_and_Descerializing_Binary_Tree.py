
# Convert a tree to a string, and then convert string back into a tree
# A long time confusing question for me, how to describe a tree and convert a list to a tree.
# As long as there is a rule for serializing and deserializing, there is way to precisely describe a tree
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper_serialize(root, cur):
    if root is None:
        cur = cur.append('x')
        return
    cur.append(root.val)
    helper_serialize(root.left, cur)
    helper_serialize(root.right, cur)


def serialize(root):
    result = []
    helper_serialize(root, result)
    return " ".join(result)

# State is current val we are inserting into a tree
# Return the root that is built during this call


def helper_deserialize(tree_list, index_list):
    if index_list[0] >= len(tree_list):
        return None

    val = tree_list[index_list[0]]
    index_list[0] += 1
    if val == 'x':
        return None
    cur = Node(val)
    cur.left = helper_deserialize(tree_list, index_list)
    cur.right = helper_deserialize(tree_list, index_list)
    return cur


def deserialize(s):
    tree_list = s.split()
    index_list = [0]
    return helper_deserialize(tree_list, index_list)


if __name__ == "__main__":
    # driver code, do not modify
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x':
            return
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur

    def print_tree(root):
        if not root:
            print("x", end=" ")
            return
        print(root.val, end=" ")
        print_tree(root.left)
        print_tree(root.right)
    root = build_tree(iter(input().split()))
    new_root = deserialize(serialize(root))
    print_tree(new_root)
