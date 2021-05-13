# Serialize and deserialize a tree
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    def helper(result_list, root):
        if root is None:
            result_list.append('X')
            return

        result_list.append(root.val)

        helper(result_list, root.left)
        helper(result_list, root.right)
        return
    result_list = []
    helper(result_list, root)
    return ",".join(result_list)


def deserialize(s):
    # Given a string, construct a list
    s_list = s.split(",")
    s_iter = iter(s_list)

    # return the current constructed node
    def helper():
        node_val = next(s_iter)
        if node_val == "X":
            return None

        cur_node = Node(node_val)

        cur_node.left = helper()
        cur_node.right = helper()

        return cur_node

    return helper()


print(serialize(deserialize("1,2,3,X,X,X,2,X,X")))
