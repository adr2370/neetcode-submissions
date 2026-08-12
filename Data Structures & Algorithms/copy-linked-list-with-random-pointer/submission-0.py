"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        orig = ans = prev = new = Node(head.val, None, head.random)
        head.random = ans
        head = head.next
        while head:
            ans = Node(head.val, None, head.random)
            prev.next = ans
            head.random = ans
            head = head.next
            prev = ans
            ans = ans.next
        while new:
            if new.random:
                new.random = new.random.random
            new = new.next
        return orig