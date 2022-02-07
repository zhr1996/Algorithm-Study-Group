'''
Problem
-------------------
Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints
-------------------
* The number of nodes in the list is the range [0, 5000].
* -5000 <= Node.val <= 5000

Thinking
-------------------
* think on the subproblem
    * if a linked list has n_1 -> n_2 -> n_3
    * if we have list after n_2 already reversed, what should we do at n_2?
    * we should set n_2.next.(which is n_3).next = n_2, and then return the head after reversed (return value is same for all recurrsions)

* base, node.next == None, return node

* recurrence function 
    * prev_node = get_prev_node(node)
    * prev_node.next = node
    * return node
'''
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:

    def helper(node):
        if not node or not node.next:
            return node

        head_after_reverse = helper(node.next)
        node.next.next = node

        node.next = None
        return head_after_reverse

    head_after_reverse = helper(head)
    return head_after_reverse


if __name__ == "__main__":
    print(function)
