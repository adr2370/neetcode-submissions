class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a = []
        def dfs(so_far, index):
            a.append(so_far.copy())
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                so_far.append(nums[i])
                dfs(so_far, i + 1)
                so_far.pop()
        dfs([], 0)
        return a