class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_i = nums[0]
        fast_i = nums[nums[0]]
        while slow_i != fast_i:
            slow_i = nums[slow_i]
            fast_i = nums[nums[fast_i]]
        new_slow_i = 0
        while new_slow_i != slow_i:
            slow_i = nums[slow_i]
            new_slow_i = nums[new_slow_i]
        return new_slow_i