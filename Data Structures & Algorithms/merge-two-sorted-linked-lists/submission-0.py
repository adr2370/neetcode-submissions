# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        p1 = list1
        p2 = list2
        if p1.val < p2.val:
            ans = p1
            p1 = p1.next
        else:
            ans = p2
            p2 = p2.next
        orig_ans = ans
        while p1 or p2:
            if not p1:
                ans.next = p2
                p2 = p2.next
            elif not p2:
                ans.next = p1
                p1 = p1.next
            else:
                if p1.val < p2.val:
                    ans.next = p1
                    p1 = p1.next
                else:
                    ans.next = p2
                    p2 = p2.next
            ans = ans.next
        return orig_ans
