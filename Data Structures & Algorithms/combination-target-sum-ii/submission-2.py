class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        a = []
        candidates.sort()
        def dfs(candidates, index, so_far, target_remaining):
            if target_remaining == 0:
                a.append(so_far.copy())
                return
            if target_remaining < 0:
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i-1] == candidates[i]:
                    continue
                so_far.append(candidates[i])
                dfs(candidates, i + 1, so_far, target_remaining - candidates[i])
                so_far.pop()
        dfs(candidates, 0, [], target)
        return a