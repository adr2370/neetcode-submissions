class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def dfs(index, so_far):
            if index >= len(s):
                ans.append(so_far.copy())
                return
            for i in range(index, len(s)):
                sub_str = s[index:i + 1]
                if sub_str == sub_str[::-1]:
                    so_far.append(sub_str)
                    dfs(i + 1, so_far)
                    so_far.pop()
        dfs(0, [])
        return ans