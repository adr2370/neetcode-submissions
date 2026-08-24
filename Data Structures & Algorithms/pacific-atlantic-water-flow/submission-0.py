class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        atlantic, pacific = set(), set()
        def dfs(x, y, last_value, ocean):
            if x < 0 or x >= n or y < 0 or y >= m or (x, y) in ocean or heights[x][y] < last_value:
                return
            ocean.add((x, y))
            dfs(x + 1, y, heights[x][y], ocean)
            dfs(x - 1, y, heights[x][y], ocean)
            dfs(x, y + 1, heights[x][y], ocean)
            dfs(x, y - 1, heights[x][y], ocean)
        for i in range(n):
            dfs(i, 0, 0, pacific)
        for j in range(m):
            dfs(0, j, 0, pacific)
        for i in range(n):
            dfs(i, m - 1, 0, atlantic)
        for j in range(m):
            dfs(n - 1, j, 0, atlantic)
        ans = []
        for i in range(n):
            for j in range(m):
                if (i, j) in atlantic and (i, j) in pacific:
                    ans.append([i, j])
        return ans
