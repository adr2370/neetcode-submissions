class Tree:

    def __init__(self):
        self.m = {}
        self.end = False
        
    def addWord(self, w):
        curr = self
        for c in w:
            if c not in curr.m:
                curr.m[c] = Tree()
            curr = curr.m[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Tree()
        for w in words:
            t.addWord(w)
        ans = set()
        n, m = len(board), len(board[0])
        def dfs(x, y, visited, curr, a):
            if curr.end:
                ans.add(a)
            if x < 0 or x >= n or y < 0 or y >= m or (x, y) in visited:
                return
            if board[x][y] not in curr.m:
                return
            visited[(x, y)] = True
            w = curr.m[board[x][y]]
            a += board[x][y]
            dfs(x + 1, y, visited, w, a)
            dfs(x - 1, y, visited, w, a)
            dfs(x, y + 1, visited, w, a)
            dfs(x, y - 1, visited, w, a)
            del visited[(x, y)]

        for i in range(n):
            for j in range(m):
                dfs(i, j, {}, t, "")
        return list(ans)