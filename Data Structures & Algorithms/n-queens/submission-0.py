class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        base_string = ""
        for i in range(n):
            base_string += "."
        def dfs(row, board):
            if row == n:
                ans.append(board.copy())
                return
            for i in range(n):
                valid = True
                for j in range(row):
                    if board[j][i] == "Q":
                        valid = False
                        break
                    offset = row - j
                    up = i - offset
                    down = i + offset
                    if up >= 0 and up < n and board[j][up] == "Q":
                        valid = False
                        break
                    if down >= 0 and down < n and board[j][down] == "Q":
                        valid = False
                        break
                if valid:
                    board[row] = base_string[:i] + "Q" + base_string[i+1:]
                    dfs(row + 1, board)
                    board[row] = base_string
        dfs(0, [base_string]*n)
        return ans