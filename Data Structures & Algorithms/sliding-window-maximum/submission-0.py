from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = SortedList()
        for i in range(k):
            l.add(nums[i])
        
        ans = [l[-1]]
        for i in range(k, len(nums)):
            l.remove(nums[i-k])
            l.add(nums[i])
            ans.append(l[-1])
        return ans