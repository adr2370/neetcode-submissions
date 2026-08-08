class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Takes a list of 9 numbers and verifies that it contians no duplicates
        def validList(l: List[str]) -> bool:
            counts = {}
            for v in l:
                if v == ".":
                    continue
                if v not in counts:
                    counts[v] = True
                else:
                    return False
            return True

        for i in range(9):
            if not validList(board[i]):
                return False
            
            column = []
            for j in range(9):
                column.append(board[j][i])
            
            if not validList(column):
                return False

        for i in range(3):
            for j in range(3):
                box = []
                for k in range(3):
                    for l in range(3):
                        box.append(board[i*3 + k][j*3 + l])
                if not validList(box):
                    return False

        return True
        
        