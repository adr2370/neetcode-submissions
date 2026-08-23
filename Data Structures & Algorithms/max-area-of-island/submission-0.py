class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        n, m = len(grid), len(grid[0])
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            ans = 0
            ans += dfs(x + 1, y)
            ans += dfs(x, y + 1)
            ans += dfs(x - 1, y)
            ans += dfs(x, y - 1)
            return ans + 1
        for i in range(n):
            for j in range(m):
                maxArea = max(maxArea, dfs(i, j))
        return maxArea