class Solution:
    def findMin(self, nums: List[int]) -> int:
        s, e = 1, len(nums)-1
        start_num = nums[0]
        if start_num < nums[-1]:
            return start_num
        while s <= e:
            m = (s + e) // 2
            if nums[m-1] > nums[m]:
                return nums[m]
            elif nums[m] < start_num:
                e = m - 1
            else:
                s = m + 1
        return nums[0]
