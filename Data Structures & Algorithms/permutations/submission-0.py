class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        a = []
        def dfs(so_far, used):
            if len(used) == len(nums):
                a.append(so_far.copy())
                return
            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                so_far.append(nums[i])
                dfs(so_far, used)
                used.remove(i)
                so_far.pop()
        dfs([], set())
        return a