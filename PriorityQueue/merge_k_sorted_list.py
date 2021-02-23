# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Use heap to implement priority queue

# heapq.heappush(), heapq.heappop()

class Solution:
    # heapq.heappush(), heapq.heappop()
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # lists: list of linkedlist head node

        pq = []

        result_head = cur = ListNode()

        index = 0

        # since right now python3 will compare the element in each tuple element, so
        # another value index needs to be added into it
        for node in lists:
            if node:
                heapq.heappush(pq, (node.val, index, node))
            index += 1

        while pq:
            _, _, node = heappop(pq)

            # result list
            cur.next = ListNode(node.val)
            cur = cur.next

            # cur list
            if node.next:
                node = node.next
                heapq.heappush(pq, (node.val, index, node))
                index += 1

        return result_head.next
