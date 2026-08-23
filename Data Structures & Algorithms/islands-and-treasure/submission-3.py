class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        def bfs(a, b):
            q = deque([(a, b, 0)])
            visited = {}
            while q:
                (x, y, dist) = q.popleft()
                if (x, y) in visited or x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == -1 or dist > grid[x][y]:
                    continue
                visited[(x, y)] = True
                grid[x][y] = dist
                q.append((x + 1, y, dist + 1))
                q.append((x - 1, y, dist + 1))
                q.append((x, y + 1, dist + 1))
                q.append((x, y - 1, dist + 1))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    bfs(i, j)