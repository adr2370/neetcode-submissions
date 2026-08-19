class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def help(nums, index, so_far, target):
            if target == 0:
                output.append(so_far.copy())
                return
            if target < 0:
                return
            for i in range(index, len(nums)):
                so_far.append(nums[i])
                help(nums, i, so_far, target - nums[i])
                so_far.pop()
        help(nums, 0, [], target)
        return output