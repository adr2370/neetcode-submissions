# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        ans = head
        n_later = head
        for i in range(n):
            n_later = n_later.next
        prev = head
        if n_later:
            n_later = n_later.next
            head = head.next
        else:
            return ans.next
        while n_later:
            n_later = n_later.next
            prev = head
            head = head.next
        prev.next = head.next
        return ans