# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        valid = True
        end = head
        prior_end = None
        while valid:
            start = end
            for i in range(k):
                if end:
                    end = end.next
                else:
                    valid = False
            if not valid:
                break
            beginning = start
            prev = None
            for i in range(k):
                temp = start.next
                start.next = prev
                prev = start
                start = temp
            beginning.next = end
            if not prior_end:
                head = prev
            else:
                prior_end.next = prev
            prior_end = beginning
        return head