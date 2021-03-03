class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def convert_leaf_node_to_ddl(root):
    head = Node(-1)
    cur = head
    if root is None:
        return None

    def helper(root):
        if root.left == None and root.right == None:
            nonlocal cur  # !!
            cur.right = root
            root.left = cur
            cur = root
            return None

        if root.left:
            root.left = helper(root.left)

        if root.right:
            root.right = helper(root.right)

        return root

    helper(root)

    return head.right

# Utility function for printing tree in InOrder


def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)


def print_list(head):
    """Function to print the given
       doubly linked list"""
    if head is None:
        return
    while head:
        print(head.val, end=" ")
        head = head.right


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    printInorder(root)
    head = convert_leaf_node_to_ddl(root)
    # print_list(head)
    printInorder(root)
