class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        keypad_map = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        def dfs(index, so_far):
            if index == len(digits):
                ans.append(so_far)
                return
            for d in keypad_map[digits[index]]:
                so_far += d
                dfs(index + 1, so_far)
                so_far = so_far[:-1]
        dfs(0, "")
        return ans
