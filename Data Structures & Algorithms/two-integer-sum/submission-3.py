class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l):
            n = nums.pop()
            t = target - n
            if t in nums:
                return [nums.index(t), l - i - 1]