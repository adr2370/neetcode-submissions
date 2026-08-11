# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        start0 = start1 = head
        length = 1
        while head.next:
            head = head.next
            length += 1

        for i in range((length - 1) // 2):
            start1 = start1.next
        temp = start1.next
        start1.next = None
        start1 = temp

        # reverse the 2nd half
        curr = start1.next
        start1.next = None
        counter = 0
        while curr:
            temp = curr.next
            curr.next = start1
            start1 = curr
            curr = temp
        
        #zip it up
        for i in range(length // 2):
            temp0, temp1 = start0.next, start1.next
            start0.next = start1
            start1.next = temp0
            start0, start1 = temp0, temp1
