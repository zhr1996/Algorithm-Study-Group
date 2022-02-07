'''
Problem
-------------------
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Constraints
-------------------
* The number of nodes in the list is in the range [0, 100].
* 0 <= Node.val <= 100

Thinking
-------------------
* take the first two nodes for example, how do we know what should be the next node of first node
    * we need to cal a recursive function on the third node, and make it return what that next node should be

* base case, if this node is None or node.next is None, return current node
'''


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

    def helper(node: ListNode) -> ListNode:
        if not node or not node.next:
            return node

        # get the pair node
        node1 = node
        node2 = node.next

        # get the next node after pair
        next_node_after_pair = helper(node2.next)

        node2.next = node1
        node1.next = next_node_after_pair

        return node2
    return helper(head)


if __name__ == "__main__":
    print(function)
