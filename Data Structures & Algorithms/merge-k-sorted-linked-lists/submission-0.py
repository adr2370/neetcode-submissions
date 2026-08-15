# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from sortedcontainers import SortedList
import random

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        starts = SortedList()

        for list_start in lists:
            if list_start:
                starts.add((list_start.val, random.random(), list_start))
        ans = point = ListNode()
        while starts:
            (_, _, smallest) = starts.pop(0)
            point.next = smallest
            point = point.next
            if smallest.next:
                starts.add((smallest.next.val, random.random(), smallest.next))
        return ans.next
