class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        s, e = 0, m * n - 1
        while s <= e:
            middle = (s + e) // 2
            v = matrix[middle // n][middle % n]
            if v == target:
                return True
            elif v < target:
                s = middle + 1
            else:
                e = middle - 1
        return False