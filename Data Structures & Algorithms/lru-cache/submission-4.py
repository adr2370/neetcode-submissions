class LinkedNode:

    def __init__(self, val: int = -1, next: LinkedNode = None, prev: LinkedNode = None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.vals = {}
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.priority_map = {}
        self.priority_len = 0

    def get(self, key: int) -> int:
        if key in self.vals:
            self.updatePriority(key)
            return self.vals[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.vals[key] = value
        self.updatePriority(key)
            
    def updatePriority(self, key: int) -> None:
        if not key in self.priority_map:
            if self.tail:
                self.tail.next = LinkedNode(key, None, self.tail)
                self.tail = self.tail.next
            else:
                self.head = LinkedNode(key, None, None)
                self.tail = self.head
            self.priority_map[key] = self.tail
            if self.priority_len >= self.capacity:
                if self.head:
                    k = self.head.val
                    self.priority_map.pop(k)
                    self.vals.pop(k)
                    self.head = self.head.next
                    self.head.prev = None
            else:
                self.priority_len += 1
        else:
            start = self.priority_map[key]
            if not start.next:
                return
            if start.prev:
                start.prev.next = start.next
            else:
                self.head = start.next
            start.next.prev = start.prev
            if self.tail:
                self.tail.next = start
            start.prev = self.tail
            start.next = None
            self.tail = start
