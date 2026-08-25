class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        safe = {}
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or (x, y) in safe or board[x][y] == "X":
                return
            safe[(x, y)] = True
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        for j in range(m):
            dfs(0, j)
            dfs(n - 1, j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i, j) not in safe:
                    board[i][j] = "X"
        