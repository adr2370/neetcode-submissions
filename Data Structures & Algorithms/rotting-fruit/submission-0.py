class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        maxTime = 0
        visited = {}
        while q:
            (x, y, time) = q.popleft()
            if x < 0 or x >= n or y < 0 or y >= m or (x, y) in visited or grid[x][y] == 0:
                continue
            visited[(x, y)] = True
            maxTime = max(maxTime, time)
            q.append((x + 1, y, time + 1))
            q.append((x - 1, y, time + 1))
            q.append((x, y + 1, time + 1))
            q.append((x, y - 1, time + 1))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    return -1
        return maxTime