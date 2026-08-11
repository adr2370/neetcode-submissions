# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = head
        curr = head.next
        if not curr:
            return prev
        prev.next = None
        n = curr.next
        curr.next = prev
        while True:
            if not n:
                return curr
            prev = curr
            curr = n
            n = curr.next
            curr.next = prev
