''' 
The Problem
-------------------
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Thinking
-------------------
* Store reference to four node
    * node before left node - node_before_left (could be None)
    * left node - node_left
    * right node - node_right
    * node after right node - node_after_right (could be None)

* Reverse the list from left to right

* After reversing the list, make
    * node_before_left.next = node_right (check if node_before_left is None)
    * left_node.next = node_after_right

* Just remember consider corner cases, and use prev and cur to reverse list
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    node_before_left = None
    node_after_right = None

    # Loop till find the left node
    cur_node = head
    for i in range(left - 1):
        if i == left - 2:
            node_before_left = cur_node
        cur_node = cur_node.next
    node_left = cur_node
    # print("function " + str(node_left.val))

    for i in range(left, right):
        cur_node = cur_node.next
    node_right = cur_node
    node_after_right = node_right.next
    # print("function " + str(node_right.val))
    # Reverse node between left and right
    # Start from left node
    cur_node = node_left
    prev_node = None
    for i in range(left, right + 1):

        next_node = cur_node.next
        cur_node.next = prev_node

        # print("fucntion in loop " + str(cur_node.val))

        prev_node = cur_node
        cur_node = next_node

        # if i == right - 1:
        #     node_right = cur_node
        #     node_after_right = node_right.next

    if node_before_left:
        node_before_left.next = node_right

    node_left.next = node_after_right

    if left == 1:
        return node_right
    else:
        return head


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    cur_node = head

    def print_list(head_node):
        cur_node = head_node
        list_str = ""
        while cur_node:
            list_str += str(cur_node.val) + " "
            cur_node = cur_node.next
        print(list_str)
    print_list(head)

    head_after = reverseBetween(head, 2, 4)

    print_list(head_after)
