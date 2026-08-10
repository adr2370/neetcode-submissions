class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1
        if nums[0] == target:
            return 0
        while s <= e:
            m = (s + e) // 2
            if nums[m] == target:
                return m
            else:
                count = 0
                if nums[0] <= nums[m]:
                    count += 1
                if nums[m] <= target:
                    count += 1
                if nums[0] <= target:
                    count += 1
                if count % 2 == 0:
                    e = m - 1
                else: 
                    s = m + 1
        return -1