class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        def dfs(index, x, y, visited):
            nonlocal ans
            if index == len(word):
                ans = True
                return
            if (x, y) in visited or x >= len(board) or y >= len(board[0]) or x < 0 or y < 0 or word[index] != board[x][y]:
                return
            visited[(x, y)] = True
            dfs(index + 1, x + 1, y, visited)
            dfs(index + 1, x - 1, y, visited)
            dfs(index + 1, x, y + 1, visited)
            dfs(index + 1, x, y - 1, visited)
            del visited[(x, y)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(0, i, j, {})
        return ans