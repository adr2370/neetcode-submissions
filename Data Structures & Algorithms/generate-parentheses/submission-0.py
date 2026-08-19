class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a = []
        def dfs(so_far, open_p):
            if len(so_far) == n * 2:
                a.append(so_far)
                return
            if open_p > 0:
                so_far += ")"
                dfs(so_far, open_p - 1)
                so_far = so_far[:-1]
            if 0 <= 2 * n - len(so_far) - 2 - open_p:
                so_far += "("
                dfs(so_far, open_p + 1)
                so_far = so_far[:-1]
        dfs("", 0)
        return a