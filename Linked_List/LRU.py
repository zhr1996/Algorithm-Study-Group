# The problem here is how to achieve O(1) put and get
# using a dictionary and a double linked list would be a very efficient way

class DLinkListNode():
    def __init__(self, key=0, val=0, prev=None, next_node=None):
        self.val = val
        self.prev = prev
        self.next = next_node
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}

        # dummy head and tail
        self.head = DLinkListNode()
        self.tail = DLinkListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]

        self.moveToHead(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.capacity == 0:
                node = self.tail.prev
                self.removeNode(node)
                self.cache.pop(node.key)
            else:
                self.capacity -= 1
            node = DLinkListNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
        else:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
