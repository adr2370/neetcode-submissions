class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = {0: [[]]}
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub_str = s[i:j]
                if sub_str == sub_str[::-1]:
                    if not i in dp:
                        dp[i] = []
                    if not j in dp:
                        dp[j] = []
                    for k in range(len(dp[i])):
                        n = dp[i][k].copy()
                        n.append(sub_str)
                        dp[j].append(n)
        return dp[len(s)]