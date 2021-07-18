'''
Problem
-------------------
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Constraints
-------------------
The number of nodes in the list is in the range sz.\
1 <= sz <= 5000\
0 <= Node.val <= 1000\
1 <= k <= sz\

Thinking
-------------------
* The nodes needs to be inversed in groups of k. Meaning we should at least keep two pointers in each group: the first and last nodes
    * pointer1 -> 1st and pointer2 -> kth node
    * After inverting this group, we need to start to invert on next. But the problem is we don't have pointer to last element of next group till we finish inverting.
    * So we need the pointer1_prev(this becomes the last after inverting) and after inverting the second group, have pointer1_prev.next -> pointer2_cur(which now is the first element of second group)
    * To sum up, the pointer to the last element in group is used in current iteration but the pointer to first element should be carried to next iteration.


* Inverting in each group:
    * to invert a list, set cur.next = prev, but also keeps a pointer to original cur.next as cur in next iteration. Also set perv equal to "cur", since in next iteartion, current node will be the previous node. 

* Count groups to invert
    * Traverse to get the length of the list

* This kind of problem needs patience and clear throught

* This is actually a perfect fit for a recursive algorithm. We are using the result of next group. So we can have head.next = reverseGroup(ptr, k)
'''
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    group_count = 0
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next

    group_count = length // k

    cur = head
    prev = None
    prev_first = None
    new_head = None
    for i in range(group_count):
        cur_first = cur
        for j in range(k):
            # Make prev first node.next equals the last element in next group
            if j == k - 1 and prev_first:
                prev_first.next = cur
            if j == k - 1 and i == 0:
                new_head = cur

            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        prev_first = cur_first

    # Add in any extra nodes
    prev_first.next = cur
    return new_head


def print_node(node):
    while node:
        print(node.val)
        node = node.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    print_node(reverseKGroup(head, 1))
