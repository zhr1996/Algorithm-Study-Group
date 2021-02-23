# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Note here carry can still carry to last bits (meanning the rest of the longer list)
# Even after all the elments in the list
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode()

        carry = 0

        while l1 and l2:
            cur_sum = l1.val + l2.val + carry
            if cur_sum >= 10:
                cur.next = ListNode(cur_sum % 10)
                carry = 1
            else:
                cur.next = ListNode(cur_sum)
                carry = 0
            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        while l1:
            cur_sum = l1.val + carry
            if cur_sum >= 10:
                cur.next = ListNode(cur_sum % 10)
                carry = 1
            else:
                cur.next = ListNode(cur_sum)
                carry = 0
            l1 = l1.next
            cur = cur.next

        while l2:
            cur_sum = l2.val + carry
            if cur_sum >= 10:
                cur.next = ListNode(cur_sum % 10)
                carry = 1
            else:
                cur.next = ListNode(cur_sum)
                carry = 0
            l2 = l2.next
            cur = cur.next

        if carry > 0:
            cur.next = ListNode(1)
        return head.next
